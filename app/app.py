from selenium import webdriver
from pynput.keyboard import Key, Controller
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    UnexpectedAlertPresentException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

keyboard = Controller()
usernameStr = ""
passwordStr = ""
driver = webdriver.Chrome(executable_path=r"")
driver.maximize_window()
# apertura pagina
driver.get("https://www.uniecampus.it/area-riservata")
# logIn
username = driver.find_element_by_id("username")
username.send_keys(usernameStr)
password = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password.send_keys(passwordStr)
signInButton = driver.find_element_by_name("_eventId_proceed")
signInButton.click()
# apertura pagina "Vai A studiare"
driver.get("https://www.uniecampus.it/area-riservata/lezioni-e-laboratori")
driver.get(
    "https://www.uniecampus.it/area-riservata/lezioni-e-laboratori/vai-a-studiare"
)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
pyautogui.moveTo(1305, 1027)
pyautogui.click()


prima_parte_del_nome = "ctl00_ContentPlaceHolder1_d_dettaglio_ctl0"
parte_finale_del_nome = "_button1"


def muove_and_click_button(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()


def chisura():
    try:
        time.sleep(1)
        driver.find_element_by_id("ctl00_ContentPlaceHolder1_b_prossima").click()
        print("premo pulsante conferma lezione volta")
        time.sleep(1)
    except (ElementClickInterceptedException, UnexpectedAlertPresentException):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("chiusura pop ok in exp")
        #    except ElementClickInterceptedException:
        # chisura pup ok
        #       keyboard.press(Key.enter)
        #       keyboard.release(Key.enter)
        #       print("chiusura pop ok prima volta in primo exp")
        #    except UnexpectedAlertPresentException:
        #        # chisura pup conferma
        #        keyboard.press(Key.enter)
        #        keyboard.release(Key.enter)
        #       print("chiusura pop ok prima volta in secondo exp")
    # popu ok
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


while 0 == 0:
    # conto quanti elementi sono presenti
    try:
        row_count = len(
            driver.find_elements_by_xpath(
                "//table[@id='ctl00_ContentPlaceHolder1_d_dettaglio']/tbody/tr"
            )
        )
    except Exception:
        # capita che a volte si generi un errore in quanto la tabella ancora non è stata caricata
        # quindi aspetto 3 secondi e poi ricarico
        time.sleep(3)
        row_count = len(
            driver.find_elements_by_xpath(
                "//table[@id='ctl00_ContentPlaceHolder1_d_dettaglio']/tbody/tr"
            )
        )
    print(row_count)
    count = 2
    while count < row_count:
        id_button = prima_parte_del_nome + str(count) + parte_finale_del_nome
        print(id_button)
        try:
            driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        except NoSuchElementException:
            print("non è necessario cambiare/entrae nel iframe")
        if count > 2:
            driver.find_element_by_id(id_button).click()
            print("chiusura pup bastardo")
            muove_and_click_button(1069, 1002)
            print("chiuso pup pup bastardo")

        try:
            print("click bottone lezione")
            driver.find_element_by_id(id_button).click()
        except ElementClickInterceptedException:
            driver.find_element_by_id("ctl00_ContentPlaceHolder1_pbOkErrScorm").click()
            print("chiusura pup bastardo")
            driver.find_element_by_id(id_button).click()
        print("chiusura pup lezione")
        muove_and_click_button(1007, 14)
        print("pup lezione chiuso")
        count += 1
    chisura()
    print("chiusura pop ok prima volta")
    print("chiusura pup conferma lezione")
    muove_and_click_button(1069, 1002)
    chisura()
    print("chiusura pop ok seconda volta")
