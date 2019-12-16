import time # Подключение модуля для работы со временем

from selenium import webdriver # Подключение webdriver для управления браузером

# Инициализируется драйвер браузера. После этой команды должно открыться новое окно браузера:
driver = webdriver.Chrome()

# Пауза в 3 секунд, чтобы успеть увидеть, что происходит в браузере:
time.sleep(3)

# Метод get сообщает браузеру, что нужно открыть сайт поиска Гугл:
driver.get("https://www.google.ru/")

time.sleep(3) # пауза 3 секунд

# Ищем поисковую строку для ввода в нее "АлтГУ":
textinput = driver.find_element_by_css_selector(".gLFyf")

# Пишем в область поиска "АлтГУ" для поиска его сайта:
textinput.send_keys("АлтГУ")
time.sleep(5)

# Нашли кнопку, которая отправит введенный текст:
submit_button = driver.find_element_by_css_selector(".gNO89b")

# Нажатие на кнопку поиска: 
submit_button.click()

time.sleep(5) # Пауза после выполненного поиска

# Закрытие окна браузера:
driver.quit()
