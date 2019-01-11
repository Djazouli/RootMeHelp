There are links that link to Facebook, Twitter and Slack. The goal is to find a way to make a redirection to a domain other than those showed on the web page.
If you open the source code, you can see that the links are looking like this:

```bash
<a href='?url=https://facebook.com&h=a023cfbf5f1c39bdf8407f28b60cd134'>facebook</a>
```

If we change this to:

```bash
<a href='?url=https://google.com&h=a023cfbf5f1c39bdf8407f28b60cd134'>facebook</a>
```

and then click the link, we see the following error: Incorrect hash!

It seems that we have to modify h=...

By using [http://www.fileformat.info/tool/hash.htm](http://www.fileformat.info/tool/hash.htm), we can see that the hash of https://facebook.com is a MD5 hash.
We compute the hash of https://google.com. We find

```bash
99999ebcfdb78df077ad2727fd00969f
```

Then we replace the link by:
```bash
<a href='?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f'>facebook</a>
```
or go directly to [http://challenge01.root-me.org/web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f](http://challenge01.root-me.org/web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f). You can see the flag, but you are instantly redirected. To get the flag, press escape to cancel the redirection, or use curl to get the page.

```bash
curl http://challenge01.root-me.org/web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f
```

You now have the flag !
