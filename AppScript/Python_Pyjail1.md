```
 	ssh -p 2222 app-script-ch8@challenge02.root-me.org
```

A python script is automatically launched, and the goal is to escape it by typing **exit(flag)**.
Let's play around a bit.

```
>>> a = 3
>>> a
>>> print(a)
3
>>> a = "hey"
Denied
```
 We can define some interger variables and call print, but we cannot define strings. Can we call dir, that will give us a lots of information about exit ?

 ```
 >>> dir(exit)
NameError : name 'dir' is not defined
 ```

dir has been removed. But maybe we can call some properties of the exit function.
For example:

```
print(exit.func_code.co_consts)
(None, 'flag-WQ0dSFrab3LGADS1ypA1', -1, 'cat .passwd', 'You cannot escape !')
```
We have what we need to escape the pyjail.
But exit('flag-WQ0dSFrab3LGADS1ypA1') is not working, because we cannot define a string.

```
exit(exit.func_code.co_consts[1])
Well done flag : FLAG
Connection to challenge02.root-me.org closed.
```
