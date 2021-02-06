import requests 
from fake_useragent import UserAgent
import os

def get_html(url,coding) :
    ua = UserAgent()
    headers = {'user-agents': f'{ua.opera}'}
    r = requests.get(url, auth=('login','pass'), headers=headers) # логин и пароль 
    r.encoding = coding 
    return r.text


def save_file(url,name):
	r = requests.get(url, stream= True)
	with open(name, 'bw') as f:
		for chunk in r.iter_content(8192):
			f.write(chunk)


def get_name(url,obj):
	
	name = url.split('/')[-1]
	folder = str(obj)
                											#создание папки
	if not os.path.exists(folder):			# os.path.exists возвращает true/folse, if сработает при true = not false 
		os.makedirs(folder)
	path = os.path.abspath(folder)
	return path + '/' + name

