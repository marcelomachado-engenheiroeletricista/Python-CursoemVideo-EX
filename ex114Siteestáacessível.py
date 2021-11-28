import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.getmodal.com.br/tracking/de9de5f263d4397f74f22e08411bf1eb')
except:
    print('Deu ERRO')
else:
    print('Tudo OK')
    #print(site.read())
    '''if site.read() in "PORTO ALEGRE":
        print('OK')'''
n = str(site.read())
print(n)
o = (n.count('ENTREGUE'))
print(o)
if o > 0:
    print('Entregue')