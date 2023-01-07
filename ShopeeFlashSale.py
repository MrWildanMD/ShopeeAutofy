import pyttsx3
import os
import sys
from datetime import datetime
import time
from colorama import Fore
import pyfiglet as f
from config import loginurl, email, password, pinShopeePay, producturl, jumlahQty, chromeProfilePath, specifiedTime
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import warnings


warnings.filterwarnings("ignore", category=DeprecationWarning)
currentDir = sys.path[0]
os.chdir(currentDir)
voice = pyttsx3.init()
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('--no-sandbox')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
# options.add_argument("--log-level=3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--user-data-dir='+chromeProfilePath)
browser = webdriver.Chrome(
    'webdriver/chromedriver.exe', chrome_options=options)
actions = webdriver.ActionChains(browser)


def isVariation1Displayed(a):
    try:
        time.sleep(5)
        a.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[4]/div/div[4]/div/div[1]/div').is_displayed()
    except NoSuchElementException:
        return False

    return True


def isVariation2Displayed(a):
    try:
        time.sleep(5)
        a.find_element_by_xpath(
            '//*[@id="main"]/div/div[2]/div[2]/div/div[1]/div[3]/div/div[4]/div/div[4]/div/div[2]/div').is_displayed()
    except NoSuchElementException:
        return False

    return True


def isPaymentMethodDisplayed(a):
    try:
        a.find_element_by_class_name(
            'checkout-payment-setting__payment-methods-tab')
    except NoSuchElementException:
        return False

    return True


class MenuBot():
    def menu():
        print(Fore.CYAN + "[+] WMDBot Shopee Menu \n")
        print()
        print(Fore.YELLOW + "1. Auto Checkout")
        print(Fore.YELLOW + "2. Login")
        print(Fore.YELLOW + "3. Keluar")


class LoginShopee():
    def login(self):
        options.headless = False
        try:
            browser.get(loginurl)
            inputEmail = WebDriverWait(browser, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "yReWDs")))
            inputEmail.send_keys(email)
            inputEmail.send_keys(Keys.TAB, password, Keys.ENTER)
            loginSuccess = WebDriverWait(browser, 50).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[1]/div/ul/li[3]/div/div/div/div[2]')))
            loggedin = loginSuccess.text
            if loginSuccess:
                print(Fore.GREEN + "[+] Login Sukses!")
                print(Fore.GREEN + "[+] Login Sebagai: "+loggedin)
                time.sleep(5)
                browser.quit()
                main()
        except NoSuchElementException as e:
            print(Fore.RED + "Login Gagal!" + str(e))


class AutoCheckout():
    def checkout(self):
        print(Fore.GREEN + "[+} Bot Berjalan \n")
        try:
            # # jika produk memiliki variasi maka bot akan secara otomatis(random) memilihkannya
            # if isVariation1Displayed(browser):
            #     listVariasi = WebDriverWait(browser, 50).until(
            #         EC.presence_of_all_elements_located((By.CLASS_NAME, "product-variation")))
            #     print(Fore.CYAN + "Variasi: ")
            #     for item in listVariasi:
            #         print(Fore.YELLOW + item.text)
            #         if item.is_enabled():
            #             browser.execute_script("arguments[0].click();", item)
            #             print(Fore.GREEN +
            #                   "[+] Variasi yang dipilih: " + item.text)
            # # jika produk memiliki variasi maka bot akan secara otomatis(random) memilihkannya
            # if isVariation2Displayed(browser):
            #     listVariasi2 = WebDriverWait(browser, 50).until(
            #         EC.presence_of_all_elements_located((By.CLASS_NAME, "product-variation")))
            #     print(Fore.CYAN + "Variasi: ")
            #     for item2 in listVariasi2:
            #         print(Fore.YELLOW + item2.text)
            #         if item2.is_enabled():
            #             browser.execute_script("arguments[0].click();", item2)
            #             print(Fore.GREEN +
            #                   "[+] Variasi yang dipilih: " + item2.text)

            # section qty atau jumlah barang jika bisa di tambah maka hapus tanda pagar mulai dari depan addQty
            # addQty = browser.find_element_by_class_name("icon-plus-sign")
            # for i in range(jumlahQty):
            #     addQty.click()
            # qty = browser.find_element_by_class_name(
            #     "iRO3yj").get_attribute('value')
            # print(Fore.YELLOW + "Jumlah: "+qty)
            buy = WebDriverWait(browser, 50).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div:nth-child(5) > div > div > button.btn.btn-solid-primary.btn--l._3Kiuzg')))
            buy.click()
            print(Fore.GREEN + "[+] BARANG BERHASIL DIMASUKKAN KE KERANJANG")
            co = WebDriverWait(browser, 50).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[3]/div[2]/div[7]/button[4]')))
            browser.execute_script("arguments[0].click();", co)
            print(Fore.GREEN + "[+] BARANG BERHASIL DI CHECKOUT")
            # Payment default ShopeePay
            if isPaymentMethodDisplayed(browser):
                listMethod = browser.find_elements_by_class_name(
                    "product-variation")
                print(Fore.CYAN + "Payment Methods:")
                for method in listMethod:
                    print(Fore.BLUE + "Payment Method: " + method[0])
                    method[0].click()

            pay = WebDriverWait(browser, 50).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main"]/div/div[3]/div[2]/div[4]/div[2]/div[7]/button')))
            browser.execute_script("arguments[0].click();", pay)
            print(Fore.GREEN + "[+] BARANG OTW DIBAYAR")
            time.sleep(5)
            paynow = WebDriverWait(browser, 50).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@id="pay-button"]')))
            actions.move_to_element(paynow).click().perform()
            pin = WebDriverWait(browser, 50).until(EC.element_to_be_clickable(
                (By.XPATH, '//div[@class="digit-input"]')))
            browser.execute_script("arguments[0].click();", pin)
            actions.move_to_element(pin).send_keys(str(pinShopeePay)).perform()
            # pin.send_keys(str(pinShopeePay))
            konfirmasi = WebDriverWait(browser, 50).until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="pin-popup"]/div[1]/div[4]/div[2]')))
            actions.move_to_element(konfirmasi).click().perform()
            # browser.execute_script("arguments[0].click();", konfirmasi)
            print(Fore.GREEN + "[+] MISSION SUCCESS!")
            voice.say('MISSION SUCCESS')
            time.sleep(30)
            browser.quit()
        except NoSuchElementException as e:
            print(Fore.RED + "Error: " + str(e))
            browser.quit()


class Keluar():
    def keluar(self):
        sys.exit()


def main():
    appname = f.figlet_format("WMDBOT SHOPEE")
    version = f.figlet_format("1.0")

    print(appname)
    print(version)
    MenuBot.menu()
    auto = AutoCheckout()
    loginz = LoginShopee()
    exitz = Keluar()

    select = int(input(Fore.BLUE + "[+] Pilih nomor pada menu:"))

    if select == 1:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        while specifiedTime != current_time:
            time.sleep(1)
            browser.get(producturl)
            browser.refresh()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time)
            if current_time == specifiedTime:
                auto.checkout()
                break
    elif select == 2:
        loginz.login()
    elif select == 3:
        exitz.keluar()
    else:
        print(Fore.RED + "Mohon masukkan nomor yang hanya ada di menu!")


if __name__ == "__main__":
    main()
