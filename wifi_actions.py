from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from constants import WifiACTION, RADIOS
import json
import logging
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument('--enable', action='store_true')
args = parser.parse_args()

logging.basicConfig(level=logging.INFO, filename="./logfile", filemode="a+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")


def wifi_driver(driverPath):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.binary_location = driverPath
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(60)
    return driver


def wifi_action(driver, url, password, action, radios):
    driver.get(url)
    try:
        pw_input = driver.find_element(By.ID,
                                       'http_passwd')
        pw_input.send_keys(password)
        driver.find_element(By.NAME, 'button').click()
        driver.find_element(By.LINK_TEXT, 'Wireless Network').click()
        driver.find_element(By.LINK_TEXT, 'Configuration').click()
        driver.find_element(By.LINK_TEXT, 'Wi-Fi').click()

        if (RADIOS.FIVE in radios):
            select_5 = Select(driver.find_element(By.ID, 'net_mode_5g'))
            if action == WifiACTION.DISABLE:
                select_5.select_by_value('disabled')
            else:
                select_5.select_by_value('mixed')

        if (RADIOS.TWO_POINT_FOUR in radios):
            select_2_4 = Select(driver.find_element(By.ID, 'net_mode_24g'))
            if action == WifiACTION.DISABLE:
                select_2_4.select_by_value('disabled')
            else:
                select_2_4.select_by_value('mixed')

        driver.find_element(By.ID, 'btnSave').click()
        result = driver.find_element(By.ID, "alertArea")
        logging.info(f'{action} complete')
        logging.info(result.text)
        time.sleep(20)

    except Exception as e:
        logging.error(e)
    finally:
        driver.quit()


def main():
    with open('./config.json') as j:
        envs = json.load(j)
    action = WifiACTION.ENABLE if args.enable else WifiACTION.DISABLE
    logging.info(f'Process start: {action} {envs["RADIOS"]}')
    driver = wifi_driver(envs['DRIVERPATH'])
    wifi_action(driver, envs['PATH'], envs['PASSWORD'], action, envs['RADIOS'])
    driver.quit()
    logging.info(f'Process complete')


if __name__ == '__main__':
    main()
