```
python3 captcha.py
```

The idea is to request the web page, decode the image that is on it (base64), and try to read the captcha with image recognition. To make the task easier for the OCR, I suppress all the dots that makes the captcha difficult to read, and convert the image to black and white.

It does not work every time, so you will have to launch the code several times. After some time, you will obtain

```
<p>Congratz, the flag is dtePZJgVAfaU</p>
```
