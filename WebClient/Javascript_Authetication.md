We open the source code, and see that a function Login(), is called when we click the login button.
We see that we use a login.js file. You can find it at http://challenge01.root-me.org/web-client/ch9/login.js

```
/* <![CDATA[ */

function Login(){
	var pseudo=document.login.pseudo.value;
	var username=pseudo.toLowerCase();
	var password=document.login.password.value;
	password=password.toLowerCase();
	if (pseudo=="4dm1n" && password=="FLAG") {
	    alert("Password accepté, vous pouvez valider le challenge avec ce mot de passe.\nYou an validate the challenge using this password.");
	} else {
	    alert("Mauvais mot de passe / wrong password");
	}
}
/* ]]> */

```

You found the flag !
