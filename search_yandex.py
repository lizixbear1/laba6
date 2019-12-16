import time # Подключение модуля для работы со временем

from selenium import webdriver # Подключение webdriver для управления браузером

# Инициализируется драйвер браузера. После этой команды должно открыться новое окно браузера:
driver = webdriver.Chrome()

# Пауза в 3 секунд, чтобы успеть увидеть, что происходит в браузере:
time.sleep(3)

# Метод get сообщает браузеру, что нужно открыть сайт поиска Яндекс:
driver.get("https://yandex.ru/")

time.sleep(3) # пауза 3 секунд

# Ищем поисковую строку для ввода в нее "АлтГУ":
textinput = driver.find_element_by_id("text")

# Пишем в область поиска "АлтГУ" для поиска его сайта:
textinput.send_keys("АлтГУ")
time.sleep(5)

# Нашли кнопку, которая отправит введенный текст:
submit_button = driver.find_element_by_css_selector(".button_theme_websearch")

# Нажатие на кнопку поиска: 
submit_button.click()

time.sleep(5) # Пауза после выполненного поиска

# Закрытие окна браузера:
driver.quit()
