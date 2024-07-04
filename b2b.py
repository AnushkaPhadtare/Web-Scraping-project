from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.b2bmarketingexpo.us/"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')

#print("Event Name:")
event_name=soup.find("h1",class_="panel__header__title")
#print(event_name.text)

#print("Event Date: ")
event_date=soup.find("h3",class_="ck-strapline ck-strapline--colour-white")
#print(event_date.text)

#print("Website URL")
#print(url)

#print("Description:")
description=soup.find("p",class_="ck-intro-text")
#print(description.text)

#print("speaker:")
speaker_tag="https://www.b2bmarketingexpo.us/welcome-la/speakers"
page2=requests.get(speaker_tag)
soup2=BeautifulSoup(page2.text,'html.parser')
speaker=soup2.find("a",class_="m-speakers-list__items__item__header__title__link js-librarylink-entry")
#print(speaker.text)

#print("schedule:")
agenda=soup.find("h3",class_="ck-strapline ck-strapline--colour-white")
agenda2=soup.find("h3",class_="ck-strapline ck-strapline--colour-white")
p_tags=soup.find_all("p",style="text-align: center;")
#print(agenda.text)
#print(agenda2.text)
for idx, p in enumerate(p_tags):
    text = p.text.strip()
    #print(f"Paragraph {idx + 1}: {text}")
    
scraped_data={
    "Event Name":event_name.text,
    "Event Date":event_date.text,
    "Website URL":url,
    "Description":description.text,
    "Speaker":speaker.text,
    "Agenda/Time":agenda.text
}

df=pd.DataFrame([scraped_data])
sheet="scraped.xlsx"
df.to_excel(sheet,index=False)
print("Done")    
    
    
    
    

