We are going to use a GBK vulnerability for this.
We cannot use the previous injection, because the PHP is calling the mysql_real_escape_string() function. It means that if we try to ' in our data, it will be replaced by a \'.

But, if we add a GBK character such as 呵, we can escape this, and use

```
呵' or 1=1 #
```

which allows us to obtain the password.
