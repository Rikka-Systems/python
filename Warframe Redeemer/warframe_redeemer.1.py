# Code here is always executed
from rich.traceback import install

install()

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	from selenium import webdriver
	from selenium.webdriver.chrome.service import Service
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.common.action_chains import ActionChains
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions
	from webdriver_manager.chrome import ChromeDriverManager
	import time

	def check_result():
		success = chrome.find_element(By.ID, 'basicTextContain').text.strip()
		if success == 'Thanks for redeeming your code!':
			return True
		else:
			return False

	def update_results(*args):
		with open('Results.txt', 'a') as results_file:
			results_file.write(f'{args[0]}={args[1]}\n')
		return

	options = Options()
	options.add_argument('start-maximized')
	chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	action = ActionChains(chrome)

	chrome.get('https://www.warframe.com/promocode')
	wait = WebDriverWait(chrome, 300)

	# Login
	wait.until(expected_conditions.presence_of_element_located((By.ID, 'btnLogin'))).click()
	wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'logged-in')))

	# Code Input
	with open('WarframeCodes.txt', 'r') as codes_file:
		code_list = [line.strip() for line in codes_file.readlines()]
		for code in code_list:
			code_input = chrome.find_element(By.ID, 'promocode_input')
			code_input.clear()
			code_input.send_keys(code)
			action.click(chrome.find_element(By.ID, 'btnSubmit')).perform()
			time.sleep(1)
			# Check code result then update results
			update_results(code, check_result())
			chrome.get('https://www.warframe.com/promocode')
			time.sleep(1)
			wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'logged-in')))
			wait.until(expected_conditions.presence_of_element_located((By.ID, 'promocode_input')))
			wait.until(expected_conditions.presence_of_element_located((By.ID, 'btnSubmit')))

else:
	# Code here executed when imported (As a module)
	pass
