Well, we have to authenticate. We already had this problem in web-server/verb tampering.
Let's use the same technique, and use a OPTIONS request instead of GET.

```
curl -X OPTIONS http://challenge01.root-me.org/realiste/ch3/admin/
```

We now have the flag !
