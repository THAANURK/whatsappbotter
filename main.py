
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 17:47:26 2018

@author: prasunsarkar
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pymysql
import itertools
import csv
    
# DB Connect & fetch

db = pymysql.connect("mmdev.c1s42kjfhzox.ap-south-1.rds.amazonaws.com","root","milmila123","mm_scarpe_data")

cursor = db.cursor()

cursor.execute("SELECT customerName FROM mm_scarpe_data.b2b_whatsappCustomer ")

data = cursor.fetchall()

myList = list(itertools.chain.from_iterable(data))

print(myList)

driver = webdriver.Chrome('/Users/prasunsarkar/Downloads/chromedrivers')

driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

colors = ['Daddy','Bright']
  
# Fetch from CSVFile

ifile  = open('/Users/prasunsarkar/Desktop/make.csv', "r")

read = csv.reader(ifile)

for row in read : 
    print(row)
    for line in row:
        try:
            name = (line.rstrip('\n'))
            text = """Dear Partner/Retailer/Wholesaler, 
Special promotion for limited period- Absolutely Free Online Offers on select products at Milmila (B2B Ecommerce Company). Just Pay Rs. 49 for shipping charges and have it delivered to you at no extra cost 
Make your business, a happy business @ https://goo.gl/8LWZ9Y
         """.format(name)
            inp_xpath_search = "//input[@title='Search or start new chat']"
            input_box_search = wait.until(EC.presence_of_element_located((
                By.XPATH, inp_xpath_search)))
            input_box_search.send_keys(name + Keys.ENTER)
            string = "https://s3.ap-south-1.amazonaws.com/mmimage/products/antitheft/antitheft-backpack.jpg"

            message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

            message.send_keys(text)

            sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/button')[0]
            sendbutton.click()
            time.sleep(5)
            print("send")
        except:
            print("error")
