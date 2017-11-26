from urllib2 import Request, urlopen, HTTPError, URLError, os
import shodan, socket
from colorama import init

from termcolor import cprint, colored

#here yout shodan API KEY
SHODAN_API_KEY = ""
api = shodan.Shodan(SHODAN_API_KEY)

def banner():
     cprint ("""

         888                    888                                                            888
         888                    888                                                            888
         888                    888                                                            888
.d8888b  88888b.   .d88b.   .d88888  8888b.  88888b.       .d8888b   .d88b.   8888b.   .d8888b 88888b.
88K      888 "88b d88""88b d88" 888     "88b 888 "88b      88K      d8P  Y8b     "88b d88P"    888 "88b
"Y8888b. 888  888 888  888 888  888 .d888888 888  888      "Y8888b. 88888888 .d888888 888      888  888
     X88 888  888 Y88..88P Y88b 888 888  888 888  888           X88 Y8b.     888  888 Y88b.    888  888
 88888P' 888  888  "Y88P"   "Y88888 "Y888888 888  888       88888P'  "Y8888  "Y888888  "Y8888P 888  888

                                           v1.0 by s1d

""", 'red','on_magenta')
#cprint(figlet_format('URL CLEANER!', font='small'),
       #'red', 'on_white', attrs=['bold'])
#print colored("Desarrollado por Janeth S", 'cyan',  attrs=['reverse'])
banner()

buscar = raw_input ('What do you want to look for?: ' )
#array
listaips = []
#search API shodan
results = api.search(buscar)

for result in results['matches']:
    listaips = result

    try:
        #print results

        cprint('', 'white', 'on_green')
        cprint ('IP: %s' % listaips['ip_str'], 'white', 'on_magenta')
        cprint ('Port: %s' % listaips['port'], 'blue', 'on_white' )
        cprint ('Hostname: %s' % listaips['hostnames'], 'red')
        cprint ('OS: %s' % listaips['os'], 'red')
        ip = listaips['ip_str']
        port = listaips['port']

        cprint ('http://'+str(ip) + ':' + str(port), 'red')

        print '-----' * 10

        # Show the results
    except shodan.APIError, e:
        print 'Error: %s' % e
cprint ('Results found: %s' % results['total'], 'cyan')
