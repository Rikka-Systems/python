# Code here is always executed

if __name__ == '__main__':
	# Code here Executed when invoked directly (Not a module)
	from selenium import webdriver
	from selenium.webdriver.chrome.service import Service
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.common.action_chains import ActionChains
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as condition
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

	# Setup browser
	options = Options()
	options.add_argument('start-maximized')
	chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
	action = ActionChains(chrome)
	wait = WebDriverWait(chrome, 300)

	# Aaaaand go!
	chrome.get('https://www.warframe.com/promocode')
	wait.until(condition.presence_of_element_located((By.ID, 'btnLogin'))).click()
	wait.until(condition.presence_of_element_located((By.CLASS_NAME, 'logged-in')))

	# Reset results file
	with open('Results.txt', 'w') as _:
		pass

	# Code Input
	try:
		codes_file = open('WarframeCodes.txt', 'r')
	except FileNotFoundError:
		exit('Could not find "WarframeCodes.txt"')
	else:
		with codes_file:
			code_list = [line.strip() for line in codes_file.readlines()]

	for code in code_list:
		chrome.get('https://www.warframe.com/promocode')
		wait.until(condition.presence_of_element_located((By.CLASS_NAME, 'logged-in')))
		try:
			code_input = wait.until(condition.presence_of_element_located((By.ID, 'promocode_input')))
		except:
			exit('Could not find code input field')
		code_input.clear()
		code_input.send_keys(code)
		wait.until(condition.element_to_be_clickable((By.ID, 'btnSubmit'))).click()
		wait.until(condition.presence_of_element_located((By.CLASS_NAME, 'submitted')))
		time.sleep(1)
		update_results(code, check_result())

else:
	# Code here executed when imported (As a module)
	pass
