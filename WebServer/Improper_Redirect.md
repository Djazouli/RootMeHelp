After reading the documentation given in the challenge, we see that sometimes, the redirection is made after the execution of a php page.

For developers, Location(...) should always be put at the beginning of your php file, and use exit() after it. Here we can just use curl:

```
curl http://challenge01.root-me.org/web-serveur/ch32/index.php
```

You have the following response :

```
<html>
<body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'></iframe>
<h1>Welcome !</h1>

<p>Yeah ! The redirection is OK, but without exit() after the header('Location: ...'), PHP just continue the execution and send the page content !...</p>
<p><a href="http://cwe.mitre.org/data/definitions/698.html">CWE-698: Execution After Redirect (EAR)</a></p>
<p>The flag is : FLAG</p>
</body>
</html>
```
