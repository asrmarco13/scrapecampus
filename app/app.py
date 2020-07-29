from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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

from core.settings import settings

keyboard = Controller()
usernameStr = settings.USERNAME
passwordStr = settings.PASSWORD
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.maximize_window()
# apertura pagina
driver.get(settings.PRIVATE_AREA)
# logIn
username = driver.find_element_by_id("username")
username.send_keys(usernameStr)
password = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.ID, "password"))
)
password.send_keys(passwordStr)
signInButton = driver.find_element_by_name(settings.SIGNIN_BUTTON_NAME)
signInButton.click()
# apertura pagina "Vai A studiare"
driver.get(settings.GO_TO_PAGE_ONE)
driver.get(settings.GO_TO_PAGE_TWO)
driver.switch_to.frame(driver.find_element_by_tag_name(settings.FRAME_NAME))
pyautogui.moveTo(1305, 1027)
pyautogui.click()


def muove_and_click_button(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click()


def closing():
    try:
        time.sleep(1)
        driver.find_element_by_id(settings.ELEMENT_NAME).click()
        time.sleep(1)
    except (ElementClickInterceptedException, UnexpectedAlertPresentException):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
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
        row_count = len(driver.find_elements_by_xpath(settings.ELEMENT_BY_X_PATH))
    except Exception:
        # capita che a volte si generi un errore in quanto la tabella ancora non è stata caricata
        # quindi aspetto 3 secondi e poi ricarico
        time.sleep(3)
        row_count = len(driver.find_elements_by_xpath(settings.ELEMENT_BY_X_PATH))
    count = 2
    while count < row_count:
        id_button = settings.FIRST_PART_OF_NAME + str(count) + settings.END_PART_OF_NAME
        try:
            driver.switch_to.frame(driver.find_element_by_tag_name(settings.FRAME_NAME))
        except NoSuchElementException:
            print("non è necessario cambiare/entrae nel iframe")
        if count > 2:
            driver.find_element_by_id(id_button).click()
            muove_and_click_button(1069, 1002)

        try:
            driver.find_element_by_id(id_button).click()
        except ElementClickInterceptedException:
            driver.find_element_by_id(settings.ERROR_BOTTOM).click()
            driver.find_element_by_id(id_button).click()
        muove_and_click_button(1007, 14)
        count += 1
    closing()
    muove_and_click_button(1069, 1002)
    closing()
