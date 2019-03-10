The goal is again to compromise the gallery by uploading some malicious php code.

If we try to upload our previous **hack.php.png**, we got a "wrong file name" error.

We are going to use the Null Byte exploit to solve this. Null Byte %00 signals the end of a string.

Let's create a new file called **hack.php%00.png**. We can now upload this file, because we are tricking the security system. The file has been uploaded to http://challenge01.root-me.org/web-serveur/ch22/galerie/upload/kgpjpm6ab3ktbud01bgh6gp680/hack.php%00.png

But we know that %00 is ending a string, so we can find our file in http://challenge01.root-me.org/web-serveur/ch22/galerie/upload/kgpjpm6ab3ktbud01bgh6gp680/hack.php

You now have the flag !

Congratz !
