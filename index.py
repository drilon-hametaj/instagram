from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random
import csv
from function.login import Login
from function.utility import attesa
from function.utility import monetina

#qui ci vanno i nomi dei profili instagram su cui far lavorare il bot
profili = ['ingegneri_in_borsa','startingfinance','investirecomeimigliori','gabriele.galletta','renegade.insider.finanza','tmlplanet','trash_italiano','fedez','will_ita','pastorizianeverdiesreal','marcomontemagno', 'the_investment_boss', 'mindsettati', 'imprenditore_tips', 'psicologiavincente', 'obiettivo1milione', 'warrenbuffettitalia']
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile)
driver.set_window_size(375, 812)
login = Login(driver)
limite_like = 400
limite_follow = 150
with open('register.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    if login.login() == 'accesso effettuato':
        #mischio per creare ordini diversi tutte le volte diciamo
        random.shuffle(profili)

        #mi serve per il register log
        dati = []
        for profilo in profili:
            writer.writerow(['profilo', profilo])
            if limite_like > 0:
                time.sleep(10)
                driver.find_element_by_xpath('/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[2]/a').click()
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[1]/section/nav[1]/div/header/div/h1/div/div/div/div/label/input')\
                    .send_keys(profilo)
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/ul/li[1]/a/div').click()
                time.sleep(5)
                immagini = driver.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')
                links_hrefs = [link.find_element_by_tag_name('a').get_attribute('href') for link in immagini]
                numero_immagini = 0
                for link in links_hrefs:
                    if numero_immagini < 5:
                        driver.get(link)
                        time.sleep(5)
                        try:
                            #clicco l'immagine del profilo per leggerne i commenti
                            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/div[1]/div/div[2]/div[1]/a').click()
                            time.sleep(5)
                            #prendo lista commenti dell'immagine
                            lista_commenti = driver.find_elements_by_class_name('Mr508')
                            i = 0 #numero like per commento
                            link_profili = []
                            for commento in lista_commenti:
                                try:
                                    if i < 3 and monetina() == 1:
                                        testo = commento.find_element_by_css_selector('a.FH9sR').text

                                        #Controllo che non abbia più di 5 mi piace
                                        numero = [int(s) for s in testo.split() if s.isdigit()]

                                        #controllo che non contenga hashtag o tag di persone
                                        testo_commento = commento.find_element_by_css_selector('span').text
                                        if numero[0] < 5 and "@" not in testo_commento and "#" not in testo_commento and monetina() == 1:
                                            try:
                                                commento.find_element_by_class_name('wpO6b.ZQScA').click()
                                                i = i+1 #incremento il like per immagine
                                                limite_like = limite_like + 1
                                                nome = commento.\
                                                        find_element_by_css_selector('a.sqdOP.yWX7d._8A5w5.ZIAjV')\
                                                        .text
                                                writer.writerow(['profilo_like_commento', nome])
                                                if monetina() == 1:
                                                    link_profilo_commento = commento.\
                                                        find_element_by_css_selector('a.sqdOP.yWX7d._8A5w5.ZIAjV')\
                                                        .get_attribute('href')
                                                    link_profili.append(link_profilo_commento)
                                            except:
                                                print('Errore cuore')

                                            time.sleep(attesa())
                                        else:
                                            print('Numero >= 5')
                                except:
                                    print('Errore lista commenti o numero')

                            if len(link_profili) > 0:
                                for link_profilo in link_profili:
                                    writer.writerow(['profilo_like_immagine', link_profilo])
                                    driver.get(link_profilo)
                                    try:
                                        if monetina() == 1 and limite_follow > 0:
                                            testo_segui = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button').text
                                            if testo_segui == 'Segui':
                                                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button').click()
                                                limite_follow = limite_follow - 1
                                                time.sleep(5)
                                    except:
                                        print('Non seguito')

                                    try:
                                        immagini_profilo = driver.find_elements_by_class_name('v1Nh3.kIKUG._bz0w')
                                        imm_hrefs = [link.find_element_by_tag_name('a').get_attribute('href') for
                                                       link in immagini_profilo]
                                        conteggio_like_immagini = 0
                                        for imm in imm_hrefs:
                                            if monetina() == 1 and conteggio_like_immagini < 3:
                                                driver.get(imm)
                                                time.sleep(5)
                                                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()
                                                limite_like = limite_like - 1
                                                conteggio_like_immagini = conteggio_like_immagini + 1
                                                time.sleep(3)
                                    except:
                                        print('Profilo privato')
                            else:
                                print('Lista profili vuota')

                        except:
                            print('Non ci sono abbastanza commenti')
                        try:
                            driver.find_element_by_class_name('mXkkY.HOQT4').click()
                        except:
                            print("Errore di pagina")
                        numero_immagini = numero_immagini+1
                        time.sleep(attesa())
