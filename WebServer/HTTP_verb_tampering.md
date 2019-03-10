When you try to connect to the page, you are prompted for an username and a password. And admin:admin does not work this time.

By reading [this reference](http://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20HTTP%20basic%20authentication%20and%20digest%20authentication.pdf), given on the website, you can understand that some websites do have an .htpasswd that only protects POST and GET request.

Well, let's use our dear curl.

```
curl -X OPTIONS http://challenge01.root-me.org/web-serveur/ch8/
```

OPTIONS is neither a GET request, nor a POST, and is not forbidden in the .htpasswd file.
You have the password in the response !
