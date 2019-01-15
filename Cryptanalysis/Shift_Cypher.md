You can bruteforce the 256 possible shift.
But let's be smarter. If you hexdump it:
```
hexdump -C ch7.bin
00000000  4c 7c 6b 80 79 2b 2a 5e  7f 2a 7a 6f 7f 82 2a 80  |L|k.y+*^.*zo..*.|
00000010  6b 76 73 6e 6f 7c 2a 6b  80 6f 6d 2a 76 6f 2a 7a  |kvsno|*k.om*vo*z|
00000020  6b 7d 7d 2a 63 79 76 6b  73 72 7f 14 0a           |k}}*cyvksr...|
0000002d
```

If we suppose that the password is a string, then it should end with the famous %00 (0x00). The shift between 0a and 0x00 is 10.

We apply -10 to this code, and the response is :

```
Bravo! Tu peux valider avec le pass Yolaihu
```
