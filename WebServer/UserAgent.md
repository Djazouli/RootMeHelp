If you go to the webpage with your browser, you will see:
```
 Wrong user-agent: you are not the "admin" browser!
```

We can think that the headers sent by our browser are not the good one.

Let's give curl a try.

```bash
curl -v http://challenge01.root-me.org/web-serveur/ch2/
```
We have the same result (Obviously)

Let's add a header user-agent:

```bash
curl -v -H "User-Agent:admin" http://challenge01.root-me.org/web-serveur/ch2/
```

Just look at the response:

```
<h3>Welcome master!<br/>Password: ...</h3>
```
