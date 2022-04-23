from selenium import webdriver ; import json ; import time

""" Setting Main Dictionaries """
Informations = {} ; Informations['USD'] = {}
for i in range (1,6):
    Informations['USD']['Shop_%i'%i] = {}

Informations['USDT'] = {}
for i in range (1,6):
    Informations['USDT']['Shop_%i'%i] = {}

""" Setting a Browser """
Browser = webdriver.Firefox()


def Dollars_To_Dict():

    Browser.get('https://torob.com/p/80ddb310-8478-4067-afb6-97700f126d7c/%D8%AF%D9%84%D8%A7%D8%B1-%D8%A7%D9%85%D8%B1%DB%8C%DA%A9%D8%A7/')
    try:
        for i in range (1,6):  
            Description = Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[2]/a/div' %i).text
            if 'خرید' in Description:
                Informations['USD']['Shop_%i' %i]['Sell_Price'] = Informations['USD']['Shop_%i' %i]['Buy_Price'] = (
                    Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[3]/a[1]' %i).text)
            elif 'فروش' in Description:
                Informations['USD']['Shop_%i' %i]['Sell_Price'] = Informations['USD']['Shop_%i' %i]['Buy_Price'] = (
                    Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[3]/a[1]' %i).text)
            elif 'آزاد' in Description:
                Informations['USD']['Shop_%i' %i]['Sell_Price'] = Informations['USD']['Shop_%i' %i]['Buy_Price'] = (
                Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[3]/a[1]' %i).text)

            Shop_Name = Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[1]/div/div/a' %i).text
            Informations['USD']['Shop_%i' %i]['Description'] = Description
            Informations['USD']['Shop_%i' %i]['Link'] = (
                Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[3]/a[1]' %i).get_attribute('href'))
            Informations['USD']['Shop_%i' %i]['Name'] = Shop_Name
    except:
        pass

def USDT_To_Dict():
    Browser.get('https://torob.com/p/0df2ae62-d478-47cd-8916-dff99ab161be/%D8%AA%D8%AA%D8%B1/')
    try:
        for i in range (1,6):
            Description = Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[2]/a/div' %i).text
            if 'خرید' in Description:
                Informations['USDT']['Shop_%i' %i]['Sell_Price'] = Informations['USDT']['Shop_%i' %i]['Buy_Price'] = (
                    Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[3]/a[1]' %i).text)
            elif 'فروش' in Description:
                Informations['USDT']['Shop_%i' %i]['Sell_Price'] = Informations['USDT']['Shop_%i' %i]['Buy_Price'] = (
                    Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[3]/a[1]' %i).text)

            Shop_Name = Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[1]/div/div/a' %i).text
            Informations['USDT']['Shop_%i' %i]['Description'] = Description
            Informations['USDT']['Shop_%i' %i]['Link'] = (
                Browser.find_element_by_xpath('/html/body/div/div/div/div/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[%i]/div[3]/a[1]' %i).get_attribute('href'))
            Informations['USDT']['Shop_%i' %i]['Name'] = Shop_Name
    except:
        pass


#Our goal is to have new json each hour while the program in running

def Making_Json():
    USDT_To_Dict(), Dollars_To_Dict()
    json_object = json.dumps(Informations, indent = 4,ensure_ascii=False) 
    print(json_object)
    with open('json_data.json', 'w') as outfile:
        outfile.write(json_object)
    Browser.quit()

Making_Json()

"""startTime = time.time()

while True:
    if time.time()-startTime >= 6000:     #after one hour
        startTime = time.time()
        Making_Json()
        """