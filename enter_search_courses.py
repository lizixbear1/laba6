import time # Подключение модуля для работы со временем
from selenium.webdriver.common.keys import Keys # Подключение модуля для работы с клавиатурой
from selenium import webdriver # Подключение webdriver для управления браузером

# Инициализируется драйвер браузера. После этой команды должно открыться новое окно браузера:
driver = webdriver.Chrome()

# Пауза в 3 секунд, чтобы успеть увидеть, что происходит в браузере:
time.sleep(3)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке:
driver.get("https://portal.edu.asu.ru/")

time.sleep(3) # пауза 3 секунд

# Ищем поисковую строку на сайте портала Агу для поиска курсов О. В. Журенкова:
textinput = driver.find_element_by_css_selector(".search-box__input")

# Пишем в область поиска "О. В. Журенков" для поиска его курсов:
textinput.send_keys("О. В. Журенков")
time.sleep(5)

# Нажатие на enter для выпонения поиска
textinput.send_keys(Keys.ENTER)

time.sleep(5) # Пауза после выполненного поиска

# Закрытие окна браузера:
driver.quit()
