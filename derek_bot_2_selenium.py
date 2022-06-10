import pandas as pd
import multiprocessing
from bs4 import BeautifulSoup
import requests
import time
from multiprocessing import Pool
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




start_time = int(time.time())

url = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273?ll=43.653226%2C-79.383184&parking-included=1&address=Toronto%2C+ON&radius=1.0"

def ilan_linklerini_topla(url):
    chrome_options = Options()

    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="./chromedriver" ,options = chrome_options)
    driver.get(url)
    tüm_ilanlar = list()
    time.sleep(1)
    try:
        ilan_1 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[4]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_1)
    except:
        ilan_1 = None
    try:
        ilan_2 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[5]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_2)
    except:
        ilan_2 = None
    try:
        ilan_3 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[6]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_3)
    except:
        ilan_3 = None
    try:
        ilan_4 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[7]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_4)
    except:
        ilan_4 = None
    try:
        ilan_5 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[8]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_5)
    except:
        ilan_5 = None
    try:
        ilan_6 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[10]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_6)
    except:
        ilan_6 = None
    try:
        ilan_7 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[11]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_7)
    except:
        ilan_7 = None
    try:
        ilan_8 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[12]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_8)
    except:
        ilan_8 = None
    try:
        ilan_9 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[13]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_9)
    except:
        ilan_9 = None
    try:
        ilan_10 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[15]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_10)
    except:
        ilan_10 = None
    try:
        ilan_11 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[16]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_11)
    except:
        ilan_11 = None
    try:
        ilan_12 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[17]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_12)
    except:
        ilan_12 = None
    try:
        ilan_13 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[18]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_13)
    except:
        ilan_13 = None
    try:
        ilan_14 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[20]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_14)
    except:
        ilan_14 = None
    try:
        ilan_15 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[21]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_15)
    except:
        ilan_15 = None
    try:
        ilan_16 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[22]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_16)
    except:
        ilan_16 = None
    try:
        ilan_17 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[23]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_17)
    except:
        ilan_17 = None
    try:
        ilan_18 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[24]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_18)
    except:
        ilan_18 = None
    try:
        ilan_19 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[25]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_19)
    except:
        ilan_19 = None
    try:
        ilan_20 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[26]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_20)
    except:
        ilan_20 = None
    try:
        ilan_21 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[27]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_21)
    except:
        ilan_21 = None
    try:
        ilan_22 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[29]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_22)
    except:
        ilan_22 = None
    try:
        ilan_23 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[30]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_23)
    except:
        ilan_23 = None
    try:
        ilan_24 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[31]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_24)
    except:
        ilan_24 = None
    try:
        ilan_25 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[32]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_25)
    except:
        ilan_25 = None
    try:
        ilan_26 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[33]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_26)
    except:
        ilan_26 = None
    try:
        ilan_27 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[34]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_27)
    except:
        ilan_27 = None
    try:
        ilan_28 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[35]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_28)
    except:
        ilan_28 = None
    try:
        ilan_29 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[36]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_29)
    except:
        ilan_29 = None
    try:
        ilan_30 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[38]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_30)
    except:
        ilan_30 = None
    try:
        ilan_31 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[39]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_31)
    except:
        ilan_31 = None
    try:
        ilan_32 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[40]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_32)
    except:
        ilan_32 = None
    try:
        ilan_33 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[41]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_33)
    except:
        ilan_33 = None
    try:
        ilan_34 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[42]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_34)
    except:
        ilan_34 = None
    try:
        ilan_35 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[43]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_35)
    except:
        ilan_35 = None
    try:
        ilan_36 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[44]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_36)
    except:
        ilan_36 = None
    try:
        ilan_37 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[45]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_37)
    except:
        ilan_37 = None
    try:
        ilan_38 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[47]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_38)
    except:
        ilan_38 = None
    try:
        ilan_39 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[48]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_39)
    except:
        ilan_39 = None
    try:
        ilan_40 = driver.find_element_by_xpath('//*[@id="mainPageContent"]/div[3]/div[3]/main/div[2]/div[49]/div/div[2]/div/div[2]/a').get_attribute('href')
        tüm_ilanlar.append(ilan_40)
    except:
        ilan_40 = None
    #driver.close()
    
    return tüm_ilanlar


def get_next_page(url):

    response = requests.get(url)
    
    soup = BeautifulSoup(response.content,'html.parser')
    
    find_next = soup.find('a',{'title':'Next'})['href']
    next_page_url = "https://www.kijiji.ca" + find_next
    house_number = soup.find('span',class_ = 'resultsShowingCount-1707762110').text
    house_number = house_number.split(' ')
    
    do_math = (int(house_number[5]) / 40) + 1 
    do_math = int(do_math)
    all_links = list()
    all_links.append(url)
    all_links.append(next_page_url)
    for item in range(do_math):
        try:
            print("######################")
            print(next_page_url)
            response = requests.get(next_page_url)
            soup = BeautifulSoup(response.content,'html.parser')
            
            find_next = soup.find('a',{'title':'Next'})['href']
            next_page_url = "https://www.kijiji.ca" + find_next
            all_links.append(next_page_url)
            print("#################3####\n\n")
        except:
            print("Patladı")
            break
    return all_links


def getHouseFeatures(urlList):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(urlList)
    # time.sleep(1)
    title,price,upload_date,house_type = None,None,None,None
    bedroom,bathroom,wifi_item_1,wifi_item_2 = None,None,None,None
    parking_number,agreement_info,move_data,pet_data = None,None,None,None
    size_data,furnished_data,app_1,app_2,app_3,app_4 = None,None,None,None,None,None
    air_info,personal_1,personal_2,smoking_info = None,None,None,None
    amen_1,amen_2,amen_3,amen_4,amen_5,amen_6,amen_7 = None,None,None,None,None,None,None

    dict_1 = dict()
    
    try:
        title = driver.find_element_by_xpath('//*[@id="vip-body"]/div[2]/div[1]/h1').text
    except:
        title = "None"
    try:
        price = driver.find_element_by_xpath('//*[@id="vip-body"]/div[2]/div[1]/div/span[1]').text
    except:
        price = "None"
    try:    
        upload_date = driver.find_element_by_xpath('//*[@id="vip-body"]/div[2]/div[2]/div[2]/time').text
    except:
        upload_date = "None"
    try:
        house_type = driver.find_element_by_xpath('//*[@id="vip-body"]/div[2]/div[3]/div[1]/li[1]/span').text
    except:
        house_type = "None"
    try:    
        bedroom = driver.find_element_by_xpath('//*[@id="vip-body"]/div[2]/div[3]/div[1]/li[2]/span').text
    except:
        bedroom = "None"
    try:
        bathroom = driver.find_element_by_xpath('//*[@id="vip-body"]/div[2]/div[3]/div[1]/li[3]/span').text
    except:
        bathroom = "None"
    try:
        wifi_items = list()
        wifi_item_1 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[2]/div/ul/li[1]')
        wifi_item_2 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[2]/div/ul/li[2]')
        if bool(wifi_item_1.text) == True:
            wifi_items.append(wifi_item_1.text)
        if bool(wifi_item_2.text) == True:
            wifi_items.append(wifi_item_2.text)
        print("Wi-Fi",wifi_items)
    except:
        pass
    try:
        parking = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[3]/dl/dt')
        if parking.text == "Parking Included":
            parking_item = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[3]/dl/dd')
            parking_number = parking_item.text
        else:
            parking_number = "None"
    except:
        pass
    try:
        agreement_type = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[4]/dl/dt')
        if agreement_type.text == "Agreement Type":
            agreement_item = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[4]/dl/dd')
            agreement_info = agreement_item.text
        else:
            agreement_info = "None"
    except:
        pass
    try:
        move_date = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[5]/dl/dt')
        if move_date.text == "Move-In Date":
            move_info = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[5]/dl/dd/span')
            move_data = move_info.text
        else:
            move_data = "None"
    except:
        pass
    try:
        pet_name = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[6]/dl/dt')
        if pet_name.text == "Pet Friendly":
            pet_info = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[1]/ul/li[6]/dl/dd')
            pet_data = pet_info.text
        else:
            pet_data = "None"
    except:
        pass
    try:
        size = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[1]/dl/dt')
        if size.text == "Size (sqft)":
            size_info = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[1]/dl/dd')
            size_data = size_info.text  
        else:
            size_data = "None"
    except:
        pass
    try:
        furnished = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[2]/dl/dt')
        if furnished.text == "Furnished":
            furnished_info = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[2]/dl/dd')
            furnished_data = furnished_info.text 
        else:
            furnished_data = "None"
    except:
        pass
    try:
        appliances_items = list()
        appliances = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[3]/div/h4')
        if appliances.text == 'Appliances':
            app_1 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[3]/div/ul/li[1]')
            if bool(app_1.text) == True:
                appliances_items.append(app_1.text)
            else:
                app_1 = ""
            app_2 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[3]/div/ul/li[2]')
            if bool(app_2.text) == True:
                appliances_items.append(app_2.text)
            else:
                app_2 = ""
            app_3 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[3]/div/ul/li[3]')
            if bool(app_3.text) == True:
                appliances_items.append(app_3.text)
            else:
                app_3 = ""
            app_4 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[3]/div/ul/li[4]')
            if bool(app_4.text) == True:
                appliances_items.append(app_4.text)
            else:
                app_4 = ""
    except:
        pass
    try:
        air_conditioning = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[4]/dl/dt')
        if air_conditioning.text == "Air Conditioning":
            air_data = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[4]/dl/dd')
            air_info = air_data.text
        else:
            air_info = "None"
    except:
        pass
    try:
        personal_item = list()
        personal = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[5]/div/h4')
        if personal.text == "Personal Outdoor Space":
            personal_1 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[5]/div/ul/li[1]')
            if bool(personal_1.text) == True:
                personal_item.append(personal_1.text)
            else:
                personal_1 = ""
            personal_2 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[5]/div/ul/li[2]')
            if bool(personal_2.text) == True:
                personal_item.append(personal_2.text)
            else:
                personal_2 = "None"
    except:
        pass
    try:
        smoking = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[6]/dl/dt')
        if smoking.text == "Smoking Permitted":
            smoking_data = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[2]/ul/li[6]/dl/dd')
            smoking_info = smoking_data.text
        else:
            smoking_info = "None"
    except:
        pass 
    try:
        the_building = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/h3')
    
        
        if bool(the_building.text) == True:
            amen_list = list()
            amenities = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/h4')
            if amenities.text == "Amenities":
                amen_1 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/ul/li[1]')
                if bool(amen_1.text) == True:    
                    amen_list.append(amen_1.text)
                amen_2 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/ul/li[2]')
                if bool(amen_2.text) == True:
                    amen_list.append(amen_2.text)
                amen_3 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/ul/li[3]')
                if bool(amen_3.text) == True:
                    amen_list.append(amen_3.text)
                amen_4 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/ul/li[4]')
                if bool(amen_4.text) == True:
                    amen_list.append(amen_4.text)
                amen_5 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/ul/li[5]')
                if bool(amen_5.text) == True:
                    amen_list.append(amen_5.text)
                amen_6 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/ul/li[6]')
                if bool(amen_6.text) == True:
                    amen_list.append(amen_6.text)
                amen_7 = driver.find_element_by_xpath('//*[@id="vip-body"]/div[3]/div[2]/div/div/div[3]/ul/li/div/ul/li[7]')
                if bool(amen_7.text) == True:
                    amen_list.append(amen_7.text)
            
            else:
                pass
    except:
        pass

    dict_1 = {'Title URL':urlList,'Title':title,'Price':price,'Upload Date':upload_date,'House Type':house_type,
          'Bedroom':bedroom,'Bathroom':bathroom,"Parking Included":parking_number,
          "Agreement Type":agreement_info,'Move-In Date':move_data,"Pet Friendly":pet_data,
          "Size":size_data,"Furnished":furnished_data,"Appliances":appliances_items,
          "Air Conditioning":air_info,"Personal Outdoor Space":personal_item,
          "Smoking":smoking_info,'Amentities':amen_list}
    return dict_1



def main_function(i,flatten_list,storage,geoHouseFeatures):
    print("hey!")
    data = []
    count = 0
    for link in flatten_list:
        # try:
        run_3 = getHouseFeatures(link)
        data.append(run_3)
        print(f"Link {count} bitti.")
        count+=1

    storage[i] = data




if __name__ == "__main__":
    run = get_next_page(url)
    all_link = list()
    for count,i in enumerate(run):
        print(f"{count}/{len(run)} collected!")
        run_2 = ilan_linklerini_topla(i)
        all_link.append(run_2)

    flatten_list = sum(all_link,[])
    uz = len(flatten_list)
    info = list()
    print(f"Tüm ilanların sayısı {uz}")


    # <----------------- Multiprocessing Section  --------------------------->

    # if you want to work with multiprocessing,
    # you need to use if __name__ == "__main__": its necessary!
    manager = multiprocessing.Manager()
    storage = manager.dict()
    p1 = multiprocessing.Process(target=main_function, args=(1,flatten_list[:(int(len(flatten_list) / 6))] ,storage,getHouseFeatures ))
    p2 = multiprocessing.Process(target=main_function, args=(2,flatten_list[(int(len(flatten_list) / 6)):(2*int(len(flatten_list) / 6))],storage,getHouseFeatures ))
    p3 = multiprocessing.Process(target=main_function, args=(3,flatten_list[(2*int(len(flatten_list) / 6)):(3*int(len(flatten_list) / 6))],storage,getHouseFeatures ))
    p4 = multiprocessing.Process(target=main_function, args=(4,flatten_list[(3*int(len(flatten_list) / 6)):(4*int(len(flatten_list) / 6))],storage,getHouseFeatures ))
    p5 = multiprocessing.Process(target=main_function, args=(5,flatten_list[(4*int(len(flatten_list) / 6)):(5*int(len(flatten_list) / 6))],storage,getHouseFeatures ))
    p6 = multiprocessing.Process(target=main_function, args=(6,flatten_list[(5*int(len(flatten_list) / 6)):],storage,getHouseFeatures ))
    #------------
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    #------------
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    #------------

    info = storage.values()
    info = sum(info,[])

    df = pd.DataFrame(info)
    df.to_excel("house_info.xlsx")



    #----------- Time Section ------------
    end_time = int(time.time())

    # ----------- Print Storage  ------------
    print(f"Return Dict : {storage}")
    process_time = end_time - start_time

