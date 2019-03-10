We read the really interesting document given by root-me.org. But well, that was not enough for me, so I typed "unzipping vulnerabilities" on Google, and YES. We can zip symbolic links !

So, I create a new symbolic link to **~index.php**. Files are uploaded in web-serveur/ch51/tmp/upload/*some_hash*, so the symbolic link is created with:

```
ln -s ~/index.php link.txt
zip -y -r zippedlink.zip link.txt
```

We created a file zippedlink.zip that contains a symbolic link to **~index.php**. Once it is automatically unzipped by the website, we are going to read the index file ! Just upload the file, click on the link, then on link.txt, and it is won, you've got the Flag !


(It is in a commented line:)

```
 // Don't know if this is safe, but it works, someone told me the flag is FLAG , did not understand what it means
```
