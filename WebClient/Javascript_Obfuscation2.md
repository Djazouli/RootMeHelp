In the source code we find

```
var pass = unescape("unescape%28%22String.fromCharCode%2528104%252C68%252C117%252C102%252C106%252C100%252C107%252C105%252C49%252C53%252C54%2529%22%29");
```

Then you can just open the console of your browser, take off the \, unescape the string, then get the string from the charcode, and gg
