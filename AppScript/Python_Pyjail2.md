```
 	ssh -p 2222 app-script-ch9@challenge02.root-me.org
```

We see that we have access to the help() function, and by calling ```help(getout)

```
It seems like we are invoking an external pager (less). Then, the usual technique is to press ! to exit it, but here, we are send back to the shell immediately. We go through the documentation of the pager, and see that

```
`|Xcommand` - Pipe file between current pos & mark X to shell command.
```

So, by typing |cat .passwd in the pager, then exiting it, we are sent back in the pyjail, but the password is displayed !
