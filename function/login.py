import time
from selenium.common.exceptions import NoSuchElementException


class Login:

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/div[2]/button').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[4]/div/label/input') \
            .send_keys('nome') #username
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[5]/div/label/input') \
            .send_keys('password') #password
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button').click()
            time.sleep(5)
        except:
            print('Errore')
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/section/div/button').click()
            return 'accesso effettuato'
        except NoSuchElementException:
            return 'Salva informazioni non trovato'
        return 'accesso effettuato'
