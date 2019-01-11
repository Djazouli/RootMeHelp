from bs4 import BeautifulSoup
with open('web-server','r')  as f:
    soup = BeautifulSoup(f, 'html.parser')
tbody = soup.find_all('tbody')[0]
list_entry = tbody.find_all('tr')
with open('readme.md','a+') as readme:
    for entry in list_entry:
        tds = entry.find_all('td')
        if tds[0].img.attrs['alt'] == 'pas_valide':
            status = 'Not Done'
        else:
            status = 'Done'
        td = tds[1]
        c = td.find_all(text=True)[1]
        readme.write(c + ' : ' + status + '\n')
