from parser_modul_1 import get_html, save_file, get_name
# https://wallpaperscraft.ru/search/?order=&page=1&query=%D0%BF%D1%80%D0%B8%D1%80%D0%BE%D0%B4%D0%B0&size=
from bs4 import BeautifulSoup as BS
from datetime import datetime

E_SITE = 'UTF-8'
i_count = 0 # счётчик скаченных 

def get_pages(html):

	soup = BS(html, 'lxml')
#	soup = BS( html, 'html.parser' ) парсер №2 

	try:
		img_count = str(soup.find('div', class_='pager').find_all('a', class_='pager__link')[-1])
		r = int((img_count.split('=')[4]).split('&')[0]) 
		return int(r)
	except AttributeError:
		return 0 


def parsing(html,obj,win_size_w, win_size_h):
	global i_count
	soup = BS(html, 'lxml')
	r = soup.find('div', class_='wallpapers wallpapers_zoom wallpapers_main').find_all('a', class_='wallpapers__link')
	for inc, a in enumerate(r, start=1):
		#link = 'https://wallpaperscraft.ru' + str(a.get('href'))
		soup = BS(get_html('https://wallpaperscraft.ru' + str(a.get('href')),E_SITE), 'lxml')
		req = soup.find('div', class_='gui-toggler__content JS-Toggler-Content').find_all('a')
		for aa in req:
			# /download/priroda_makro_ptica_84216/1920x1080
			
			size_w = int(aa.get('href').split('/')[-1].split('x')[0])
			size_h = int(aa.get('href').split('/')[-1].split('x')[1])

#						==================<Проверка разрешения экрана>==================

			if win_size_w == size_w and win_size_h == size_h:
				url_size = 'https://wallpaperscraft.ru' + str(aa.get('href'))
			else:
				continue
				
		soup2 = BS(get_html(url_size, E_SITE),'lxml')
		img_url = soup2.find('div', class_='wallpaper__placeholder').find('a').get('href')
		#name = f'img/{obj}-{img_url1.split("/")[-1] }'
		name = get_name(img_url,obj)
		save_file(img_url, name)
		print(f'|{inc:^{4}}|{name.split("/")[-1]:^{33}}|{"Загружен":^{10}}|')
		i_count += 1
	return i_count


#		link = 'https://wallpaperscraft.ru' + str(a.get('href'))


def main(list_obj): 

	start_time = datetime.now()
	win_width = int(input('1920 >>')) 
	win_height = int(input('1080 >>'))

	for obj in list_obj :
		url = f'https://wallpaperscraft.ru/search/?order=&page=1&query={obj}&size=' 
		pages = get_pages(get_html(url, E_SITE))

		for page in range(2, 3): # 2 = page +1

			base_url = f'https://wallpaperscraft.ru/search/?order=&page={page}&query={obj}&size='
			print(f'Страниц:{page}-{pages}')
			print('-'*50)
			print(f'|{"№":^{4}}|{"Категория - имя файла":^{33}}|{"Статус":^{10}}|')
			print('-'*50)
			inc = parsing(get_html(base_url, E_SITE), obj, win_width, win_height)
			print('-'*50, end='\n')
			print(f'Скачено :{inc}')
	end_time = datetime.now()
	print(f' Затрачено времени:{str(end_time-start_time):{50}}')
	print('-'*50)

#		print( 'Страничек найдено:', pages )




if __name__ == '__main__':
	main(input(':_>').split(','))

