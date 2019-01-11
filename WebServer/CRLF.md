The goal is to inject some false data in the log.

If you enter login:password in the form, you will see a new line appearing in the Authentication Log:

```
login failed to authenticate
```
And we see that we are redirected to http://challenge01.root-me.org/web-serveur/ch14/?username=login&password=password

Well, we can try to inject a line jump in the logs. For this, we need to now the equivalent of CRLF in hex code (to put it in the address). This %0d%0a. Well, let's go to http://challenge01.root-me.org/web-serveur/ch14/?username=login%0d%0anewline&password=password

We know see this two lines in the log:

```
login
newline failed to authenticate.

```
It worked !
Now, let's inject "admin authenticated". By following the same procedure, we can go to: [http://challenge01.root-me.org/web-serveur/ch14/?username=admin authenticated.%0D%0Anewline&password=password](http://challenge01.root-me.org/web-serveur/ch14/?username=admin authenticated.%0D%0Anewline&password=password)

At the bottom of the page, we can see:

```
Well done, you can validate challenge with this password : FLAG

```
