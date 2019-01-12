import urllib.request
import re

req = urllib.request.build_opener()
req.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
req.addheaders.append(('Cookie', 'challenge_frame=1; spip_session=myspip_session; PHPSESSID=myPHPSESSID'))
req.addheaders.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'))
req.addheaders.append(('Accept-Language', 'en-US,en;q=0.5'))
req.addheaders.append(('DNT', '1'))
req.addheaders.append(('Connection', 'Keep-Alive'))
req.addheaders.append(('Connection', 'Keep-Alive'))
contents = req.open("http://challenge01.root-me.org/programmation/ch1/").read().decode('UTF-8')
#http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result=...
relation = re.search(r'e>U<sub>n\+1</sub> = (.*)]<',contents).group(0)
u0 = re.search(r'U<sub>0</sub> = (.*)\n',contents).group(0)
goal = re.search(r' U<sub>(.*)</sub><b', contents).group(0)

#Let's clean everything
number1 = int(re.search(r'-*[0-9]+ \+', relation).group(0)[:-2])
multiplierN = int(re.search(r'\* -*[0-9]+',relation).group(0)[2:])
u0 = int(re.search(r'= -*[0-9]+',u0).group(0)[2:])
index = int(re.search(r'>[0-9]+',goal).group(0)[1:])
#Do not care about loop, my computer is so fast
for n in range(index):
    u0 = number1 + u0 + multiplierN*n
print("http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="+str(u0))
contents = req.open("http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="+str(u0)).read().decode('UTF-8')
print(contents)
#...
