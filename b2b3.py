from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url="https://www.inbound.com/"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
print("Website:3")

event_name=soup.find("title")
if event_name:
        # Extract the text from the <title> element
        title_text = event_name.text.strip()
        
        # Use string manipulation to isolate "INBOUND 2024"
        start_phrase = "INBOUND 2024"
        start_index = title_text.find(start_phrase)
        
        if start_index != -1:
            # Extract "INBOUND 2024" from the title text
            inbound_text = title_text[start_index:start_index + len(start_phrase)]
            print("Event Name:")
            print(inbound_text)
        else:
            print('INBOUND 2024 not found in the title')
    
else:
    print('Failed to retrieve the webpage')
    
dates = soup.find_all('time')
if dates:
    event_date = ' - '.join([date.get_text() for date in dates])
    print("Event Date:")
    print(event_date)
else:
    print('<time> tags not found')    

description_div = soup.find('div', class_='mess-html')
if description_div:
    description_p = description_div.find('p')
    if description_p:
        event_description = description_p.get_text(strip=True)
        print("Event Description:")
        print(event_description)
    else:
        print('<p> tag not found within the description div')
else:
    print('<div class="mess-html"> tag not found')
    
print(" Key Speaker:")
speaker=soup.find("h3",class_="name")
print(speaker.text)    

cost=soup.find("h4",class_="fs-40")
print("Cost:",cost.text)

scraped_data={
    "Event Name":event_name.text,
    "Event Date":event_date,
    "Description":description_div,
    "Key Speaker":speaker,
    "cost":cost   
}

df=pd.DataFrame([scraped_data])
sheet="scraped_inbound.xlsx"
df.to_excel(sheet,index=False)
print("Done")  

    