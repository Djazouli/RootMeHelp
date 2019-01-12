Well apparently the site contains only a webpage of connection, where you can input a password, and click on "Connect".

The statement of the challenge is "It seems that the developper often leaves backup files around...". Well, we already searched for backup files in another challenge, and I put in note a program to bruteforce backup extensions. Let's use this on index.php.

We see that we can download a index.php.bak. We read through the file and we see this line:

```php
if (( isset ($password) && $password!="" && auth($password,$hidden_password)==1) || (is_array($_SESSION) && $_SESSION["logged"]==1 ) ){
    $aff=display("well done, you can validate with the password : $hidden_password");
```

So we can use the fact that register globals is on, and put $_SESSION["logged"]==1 to true, and it's won !

Just go to http://challenge01.root-me.org//web-serveur/ch17/?_SESSION%5Blogged%5D=1, and enjoy your flag !
