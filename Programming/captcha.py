import urllib.request, urllib.parse
import re, base64, subprocess
import time
try:
    from PIL import Image
except ImportError:
    import Image
stop = False
def convert(path):
    im = Image.open(path)
    R, G, B = im.convert('RGB').split()
    r = R.load()
    g = G.load()
    b = B.load()
    w, h = im.size

    # Convert non-black pixels to white
    for i in range(w):
        for j in range(h):
            if(r[i, j]%255 == 0 and g[i, j]%255 == 0 and b[i, j]%255 == 0):
                r[i, j] = 255 # Just change R channel
            else:
                r[i,j] = 0

    # Merge just the R channel as all channels
    im = Image.merge('RGB', (R, R, R))
    im.save(path)
    return


req = urllib.request.build_opener()
req.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
req.addheaders.append(('Cookie', 'challenge_frame=1; spip_session=myspip_session; PHPSESSID=myPHPSESSID'))
req.addheaders.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'))
req.addheaders.append(('Accept-Language', 'en-US,en;q=0.5'))
req.addheaders.append(('DNT', '1'))
req.addheaders.append(('Connection', 'Keep-Alive'))
req.addheaders.append(('Connection', 'Keep-Alive'))
start = time.time()

contents = req.open("http://challenge01.root-me.org/programmation/ch8/").read().decode('UTF-8')
base64code = re.search(r'4,(.*)" /><br>',contents).group(0)[2:-8]
img = base64.b64decode(base64code)
filename = 'some_image.png'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(img)
convert(filename)
res = str(subprocess.Popen(['gocr -i '+filename], shell=True, stdout=subprocess.PIPE).communicate()[0])[1:]

res = res.replace('\n', '')
res = res.replace(' ', '')
res = res.replace(',', '')
res = res.replace('\'', '')
res = res.replace('_', '')
res = re.search('[a-zA-Z0-9]+', res)
if res == None:
    pass
else:
    res = res.group(0)
    print(res)
    query_args = {'cametu':res}
    encoded_args = urllib.parse.urlencode(query_args).encode('UTF-8')
    rep = req.open("http://challenge01.root-me.org/programmation/ch8/", encoded_args).read().decode('utf-8')
print(time.time() - start)
print(rep)
print('\n \n', res)
print(rep[200:230])
