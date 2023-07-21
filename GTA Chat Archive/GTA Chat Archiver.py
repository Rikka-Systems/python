# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	import re
	from datetime import date

	def create_archive():
		log_path = 'C:\\Users\\Loki\\AppData\\Roaming\\Stand'

		with open(f'{log_path}\\chat-today.txt', mode='w', encoding='utf-8') as _:
			pass

		with open(f'{log_path}\\chat.txt', encoding='utf-8') as chat_file:
			while message := chat_file.readline():
				get_date = re.search(r'(\d{1,2}/\d{1,2}/\d{4})', message.rstrip())
				try:
					mes_date = get_date.group().split('/')
				except AttributeError:
					continue

				mes_year = mes_date[2]
				mes_month = mes_date[0]
				if len(mes_month) == 1:
					mes_month = f'0{mes_month}'
				mes_day = mes_date[1]
				if len(mes_day) == 1:
					mes_day = f'0{mes_day}'

				mes_date = "-".join((mes_year, mes_month, mes_day))
				if mes_date == str(date.today()):
					with open(f'{log_path}\\chat-today.txt', mode='a', encoding='utf-8') as chat_today:
						chat_today.write(message)


	create_archive()

else:
	# Code here executed when imported (As a module)
	pass
