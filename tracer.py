import requests
import json

print('''
▄▄▄█████▓ ██▀███   ▄▄▄       ▄████▄  ▓█████  ██▀███  
▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒    ░ ░  ░  ░▒ ░ ▒░
  ░        ░░   ░   ░   ▒   ░           ░     ░░   ░ 
            ░           ░  ░░ ░         ░  ░   ░  
             
               Created By Skitz#5674 ''')



ip_adress = input("Enter Target Ip: ")

response = requests.get(f'http://ip-api.com/json/{ip_adress}').content

data = json.loads(response)

print(f'''      
IP: {data['query']}
country: {data['country']}
City: {data['city']}
ZIP: {data['zip']}
Isp: {data['isp']}
Lon: {data['lon']}
Lat: {data['lat']}
Timezone: {data['timezone']}

''')

  