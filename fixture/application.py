from selenium import webdriver
from fixture.session import SessionHelper


# Класс-менеджер, который инициализирует всех помощников
class Application:

    # создание фикстуры, инициализация драйвера
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(capabilities={"marionette": False})
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie
#            self.wd.implicitly_wait(60)
        else:
            raise ValueError("Unrecognized browser %s", browser)
        # конструирование помощников, передаем ссылку на саму фикстуру
        self.session = SessionHelper(self)# помощник сесссий получает ссылку на объект класса Application
        self.base_url = base_url

    def open_home_page(self): # метод навигации, кандидат на перенос в соответ.помощник
        wd = self.wd
        wd.get(self.base_url)

    # метод разрушает фикстуру, останавливает браузер
    def destroy(self):
        self.wd.quit()

    # метод проверяет валидность фикстуры
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


