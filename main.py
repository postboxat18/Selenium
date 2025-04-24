import threading
import time
from flask import Flask
import json
import codecs

from flask.logging import create_logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
import os
import shutil
import win32api
import os
from flask import Flask, request, jsonify, url_for, redirect
import asyncio
import sys
from subprocess import Popen
import shutil
import os
import os.path
import time

from selenium.webdriver.support.select import Select


def LogFileRemove():
    if os.path.exists("log.txt"):
        os.remove("log.txt")
    else:
        pass


def TestLogin(url):
    global driver
    chromeOptions = webdriver.ChromeOptions()
    # PATH TO DOWNLOAD THE FILES
    paths = ""
    prefs = {"download.default_directory": paths}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=chromeOptions)
    driver.maximize_window()
    try:
        driver.get(url)
        print("webdriver Open")

        return True
    except Exception as e:
        print(e)
        return False


def Login():
    action = 1

    # ACTION -> INPUT
    if (action == 1):
        try:
            fileName = "Trial Balance"
            driver.find_element("xpath", xpath).click()
            driver.find_element("xpath", xpath).send_keys(fileName)
            #select = Select(driver.find_element("xpath", ""))
            #select.select_by_visible_print()
            time.sleep(2)


        except Exception as e:
            print(e)
            return

    # ACTION -> DROP DOWN TO CLEAR INPUT
    elif (action == 6):
        try:

            time.sleep(2)
            driver.find_element("xpath", "").clear()
            driver.find_element("xpath", "").send_keys()
        except Exception as e:
            print(e)
            return


    # ACTION -> CLICK
    elif (action == 2):

        try:
            driver.find_element("xpath", "").click()
        except Exception as e:
            print(e)
            return

    # ACTION -> SELECT THE CHEKBOX 1-SELECT AND 2-UNSELECT
    elif (action == 3):
        try:

            value = 1
            element = driver.find_element("xpath", "")

            if (value == "1"):
                if (element.is_selected() == True):
                    print("true")

                elif (element.is_selected() == False):
                    print("false")
                    driver.find_element("xpath", "").click()

            else:
                if (element.is_selected() == True):
                    print(" true")
                    driver.find_element("xpath", "").click()
                elif (element.is_selected() == False):
                    print("false")

        except Exception as e:
            print(e)
            return

    # ACTION -> WINDOWS HANDER FOR NEXT CHILD TAB
    elif (action == 4):
        try:
            n = len(driver.window_handles)
            n -= 1
            time.sleep(5)
            window1 = driver.window_handles[n]
            driver.switch_to.window(window1)

        except Exception as e:
            print(e)
            return

    # ACTION -> SWITCH THE FRAME
    elif (action == 5):
        try:
            driver.switch_to.frame(driver.find_element("xpath", ""))
            time.sleep(3)

        except Exception as e:
            print(e)
            return

    # ACTION -> ALERT THE BOX
    elif (action == 8):
        try:

            # WINDOWS HANDLER FOR NEXT CHILD TAB
            n = len(driver.window_handles)
            n -= 1
            window1 = driver.window_handles[n]
            driver.switch_to.window(window1)

            # ALERT BOX
            alert = Alert(driver)
            print(alert.text)
            alert.accept()
            time.sleep(3)
        except Exception as e:
            print(e)
            return

    # ACTION -> WAIT FOR THE XPATH IS PROCEED
    elif (action == 9):
        try:
            driver.maximize_window()

        except Exception as e:
            print(e)

    # WINDOWS HANDLER TO CLOSE NEXT CHILD TAB
    elif (action == 12):
        try:
            driver.close()
            n = len(driver.window_handles)
            n -= 1
            window1 = driver.window_handles[n]
            driver.switch_to.window(window1)
        except Exception as e:
            print(e)
            return

    else:
        pass

    print(" FOR LOOP end end ------->>>")


app = Flask(__name__)
app.config["csv_files"] = 'files\\'
# logging.basicConfig(filename="mylog.txt",
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S')
logger = create_logger(app)


@app.route('/', methods=['POST'])
def hello_world():
    LogFileRemove()
    global headerId
    headerId = request.form['headerId']
    threading.Thread(target=home_page, args=(headerId)).start()
    return "headerId:" + headerId


# KILL THE PROCESS USING LOG COMMAND
@app.route('/kill', methods=['POST'])
def KillProcess():
    global driver
    driver.quit()
    return "Kill Process"


# TO READ TEXT FILE IN LOG COMMAND
@app.route('/log', methods=['POST', 'GET'])
def LogPath():
    global logFile
    global numFile
    global filedir
    # read file
    if os.path.exists(logFile):
        if request.method == 'GET':
            listdir = os.listdir(logFile)

            return listdir
        elif request.method == 'POST':
            fileName = request.form['fileName']
            numFile = os.path.join(logFile, fileName)

            filedir = os.listdir(numFile)
            textFile = request.form['textFile']
            if (textFile == ""):
                return filedir
            else:
                return redirect(url_for('LogFile', textFile=str(textFile)))
    else:
        return "Empty File"


def home_page(headerId):
    # PASS THE URL AT INDEX 0
    i = 0
    URL = ""
    if i == 0:
        TestLogin(URL)
    else:
        # PASS THE ACTION
        Login(headerId)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
