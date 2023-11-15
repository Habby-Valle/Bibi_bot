from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from decouple import config
import os
import json

QUANTIDADE_COMENTARIOS = config('QUANTIDADE_COMENTARIOS')
USERNAME_INSTAGRAM = config('USERNAME_INSTAGRAM')
PASSWORD_INSTAGRAM = config('PASSWORD_INSTAGRAM')
PROFILE = config('PROFILE')

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        # coloque o caminho do seu geckodriver no seu computador
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"{C:\Users\Habby\Desktop\}geckodriver-v0.33.0-win64\geckodriver.exe")


    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        input_username = driver.find_element(By.XPATH, "//input[@name='username']")
        input_username.clear()
        input_username.send_keys(self.username)
        time.sleep(3)

        input_password = driver.find_element(By.XPATH, "//input[@name='password']")
        input_password.clear()
        input_password.send_keys(self.password)
        input_password.send_keys(Keys.RETURN)
        time.sleep(5)

        driver.get(f"https://www.instagram.com/{PROFILE}/")
        time.sleep(5)

        # publicação 
        driver.get("https://www.instagram.com/p/CzrTsMmuHOK8Igra5vXHo6tUERckrL2sQMGBIg0/")
        time.sleep(5)
        comment_times = QUANTIDADE_COMENTARIOS

        for i in range(0, int(comment_times)):
            persons = json.loads(os.environ['LIST_PERSONS'])

            first_person = random.choice(persons)
            persons.pop(persons.index(first_person))
            second_person = random.choice(persons)
            persons.pop(persons.index(second_person))
            third_person = random.choice(persons)
            persons.pop(persons.index(third_person))


            comment_formated = f'{first_person} {second_person} {third_person}'
            textarea = driver.find_element(By.CSS_SELECTOR, "textarea")
            textarea.click()
            field_comment = driver.find_element(By.CSS_SELECTOR, "textarea")
            time.sleep(random.randint(2, 5))

            self.type_like_a_person((comment_formated), field_comment)
            time.sleep(5)
            post = driver.find_element(By.CSS_SELECTOR, "div.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37")

            post.send_keys(Keys.RETURN)
            time.sleep(5)

instagram_bot = InstagramBot(USERNAME_INSTAGRAM, PASSWORD_INSTAGRAM)
instagram_bot.login()