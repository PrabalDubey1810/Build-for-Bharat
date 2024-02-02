from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
#List of websites:
l1=["https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1?crid=2JVAXZH21JCGJ&keywords=iphone+13+blue+128+gb&qid=1696326226&sprefix=%2Caps%2C699&sr=8-1","https://www.flipkart.com/apple-iphone-13-blue-128-gb/p/itm6c601e0a58b3c",'https://www.reliancedigital.in/apple-iphone-13-128-gb-blue/p/491997702?gclid=CjwKCAjw9-6oBhBaEiwAHv1QvFwV3BxH4B-9H3SAdy6urV9rOF1qlMkwEhm_m0kCceRp3Nf_-ByatBoClpwQAvD_BwE']
for i in l1:
    if(i==l1[0]):
        driver.get("https://www.amazon.in/Apple-iPhone-13-128GB-Blue/dp/B09G9BL5CP/ref=sr_1_1?crid=2JVAXZH21JCGJ&keywords=iphone+13+blue+128+gb&qid=1696326226&sprefix=%2Caps%2C699&sr=8-1")
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        product_names = soup.find_all('h1', class_='a-size-large a-spacing-none')
        product_prices = soup.find_all('span', class_='a-price-whole')
        data = []
        for name, price in zip(product_names, product_prices):
            data_dict = {}
            data_dict['name'] = name.text
            data_dict['price'] = price.text
            data.append(data_dict)
            df = pd.DataFrame(data)
            df.to_csv('data.csv', index=False, encoding='utf-8')
            print(df)
    if(i==l1[1]):
        driver.get('https://www.flipkart.com/apple-iphone-13-blue-128-gb/p/itm6c601e0a58b3c')
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        product_names = soup.find_all('span', class_="B_NuCI")
        product_prices = soup.find_all('div', class_='_30jeq3 _16Jk6d')
        data = []
        for name, price in zip(product_names, product_prices):
            data_dict = {}
            data_dict['name'] = name.text
            data_dict['price'] = price.text
            data.append(data_dict)
            df = pd.DataFrame(data)
            df.to_csv('data.csv', index=False, encoding='utf-8')
            print(df)
    if(i==l1[2]):
        driver.get('https://www.reliancedigital.in/apple-iphone-13-128-gb-blue/p/491997702?gclid=CjwKCAjw9-6oBhBaEiwAHv1QvFwV3BxH4B-9H3SAdy6urV9rOF1qlMkwEhm_m0kCceRp3Nf_-ByatBoClpwQAvD_BwE')
        page_source = driver.page_source
        
        soup = BeautifulSoup(page_source, 'html.parser')
        product_names = soup.find_all('h1', class_="dp__title")
        product_prices = soup.find_all('span', class_="TextWeb__Text-sc-1cyx778-0 kFBgPo")
        data = []
        for name, price in zip(product_names, product_prices):
            data_dict = {}
            data_dict['name'] = name.text
            data_dict['price'] = price.text
            data.append(data_dict)
            df = pd.DataFrame(data)
            df.to_csv('data.csv', index=False, encoding='utf-8')
            print(df)