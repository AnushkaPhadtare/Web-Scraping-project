from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url="https://www.salesforce.com/dreamforce/"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
print("Website 2")

print("Event Name")
event_name=soup.find('title')
#print(event_name.text)

print("Event Date:")
event_date=soup.find('section',class_='sticky bottom-20 z-40 pointer-events-none')
if event_date:
       
        text_content = event_date.get_text(separator=' ', strip=True)
        
        
        date_pattern = r'\b[A-Za-z]+\s\d{1,2}-\d{1,2},\s\d{4}\b'
        match = re.search(date_pattern, text_content)
        
        if match:
            date = match.group(0)
            print(date)
        else:
            print('Date not found in the text')
    
else:
    print('Failed to retrieve the webpage')
    
print("Website URL:")
print(url)

print("Description:")
description=soup.find("p",class_="body-md text-center leading-relaxed text-balance xl:max-w-[615px] mx-auto")
print(description.text) 

price_element = soup.find('p', class_='heading-xl text-indigo-50')
    
if price_element:
        # Find the <span> element within the <p> element that contains the cost
        span_element = price_element.find('span')
        
        if span_element:
            cost = span_element.text.strip()
            print('Cost:', cost)
        else:
            print('<span> element not found within the <p> element')

else:
    print('Failed to retrieve the webpage')   
    
print(" Key Speaker:")
speaker=soup.find('h3',class_="heading-xxs")
print(speaker.text)

scraped_data={
    "Event Name":event_name.text,
    "Date":event_date.text,
    "URL":url,
    "Cost":cost,
    "description":description.text,
    "Key Speaker":speaker.text
}

df=pd.DataFrame([scraped_data])
sheet="scraped_dreamforce.xlsx"
df.to_excel(sheet,index=False)
print("Done")    
    
    
    