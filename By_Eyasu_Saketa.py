from bs4 import BeautifulSoup
import requests
from pprint import pprint
def get_data_type1(url,file_name,message):
    url =url
    data = requests.get(url)
    my_data = []
    data_gathered=''
    html = BeautifulSoup(data.text, 'html.parser')
    articles = html.select('article')
    file=open(file_name,'w',encoding='utf-8')
    for article in articles:
        if article.find('p') is not None and article.find('a') is not None :
            title =article.find('h2').text
            link=article.find('a')['href']
            detail_data=get_detail_data(link,file_name,"Data Recording  Please Wait...............................")
            print(detail_data)
            title_to_be_saved=title+":\n"
            detail =article.find('p').text
            detail_to_be_saved="\t >"+detail
            if title in my_data:
                print(1)
            else:
                my_data.append( {title:detail} )
                data_gathered=data_gathered+"\n \n"+ title_to_be_saved + detail_to_be_saved+"\n"+detail_data
    #pprint(my_data)
    file.write(data_gathered)
    file.close()
    print(message)

def get_detail_data(url,file_name,message):
    url =url
    data = requests.get(url)
    my_data = []
    data_gathered='\t \t'
    html = BeautifulSoup(data.text, 'html.parser')
    articles = html.select('div.details')
    i=0
    for article in articles:
        i=i+1
        if article.find_all('p') is not None  :
          
            detail_to_be_saved=article.text
          
    print(detail_to_be_saved)
    print(message)
    return  detail_to_be_saved
        
def get_data_type2(url,file_name,message):
    url =url
    data = requests.get(url)
    my_data = []
    data_gathered=''
    html = BeautifulSoup(data.text, 'html.parser')
    articles = html.select('div.col-12')
    file=open(file_name,'w',encoding='utf-8')
    for article in articles:
        if article.find('p') is not None and article.find('a') is not None :
            title =article.find('h2').text
            
            title_to_be_saved=title+":\n"
            detail =article.find('p').text
            detail_to_be_saved="\t >"+detail
            if title in my_data:
                print(1)
            else:
                my_data.append( {title:detail} )
                data_gathered=data_gathered+"\n \n"+ title_to_be_saved + detail_to_be_saved+"\n\t"
    #pprint(my_data)
    file.write(data_gathered)
    file.close()
    print(message)
def get_data_type3(url,file_name,message):
    url =url
    data = requests.get(url)
    my_data = []
    data_gathered=''
    html = BeautifulSoup(data.text, 'html.parser')
    articles = html.select('div.col-6')
    file=open(file_name,'w',encoding='utf-8')
    i=0
    for article in articles:
        if article.find('h2') is not None:
            title =article.find('h2',class_='card-title').text
            link=article.find('a')['href']
            detail_data=get_detail_data(link,file_name,"Data Recording  Please Wait>..................................")
            title_to_be_saved=title+":\n"
            print(title)
            i=i+1
            if title in my_data:
                print(1)
            else:
                data_gathered=data_gathered+"\n \n"+ title_to_be_saved +"\n\t"+detail_data
    #pprint(my_data)
    file.write(data_gathered)
    file.close()
    print(message)

#for lattest news data
get_data_type1('https://am.al-ain.com/latestnews/','latest_news_data.txt',"Latest News Data is Saved Succefuly")   
#for photos news data
get_data_type1('https://am.al-ain.com/tag/photo-news/','photo_news_data.txt',"Photo News Data is Saved Succefuly") 
# for we-select-to-you
get_data_type1('https://am.al-ain.com/tag/we-select-to-you/','we_select_to_you_news_data.txt',"we-select-to-you News Data is Saved Succefuly")
#for opinion
get_data_type2('https://am.al-ain.com/opinion/','opinion_data.txt',"Opinion Data is Saved Succefuly")
#For politics data
get_data_type1('https://am.al-ain.com/section/politics/','politics_data.txt',"Politics Data is Saved Succefuly")
#For Economic data
get_data_type1('https://am.al-ain.com/section/economy/','economic_data.txt',"Economic Data is Saved Succefuly")
#For Social data
get_data_type1('https://am.al-ain.com/section/social/','Social_data.txt',"Social Data is Saved Succefuly")
#for varities news
get_data_type1('https://am.al-ain.com/section/varities/','varities_data.txt',"Varities Data is Saved Succefuly")
#Sport news Data
get_data_type1('https://am.al-ain.com/section/sports/','sport_news_data.txt',"Sport News Data is Saved Succefuly")
#info Graphics
get_data_type3('https://am.al-ain.com/infographics/','infographics_news_data.txt',"InfoGraphics News Data is Saved Succefuly")
#for Hot rumors
get_data_type3('https://am.al-ain.com/videos/','hot_rumors_data.txt',"Tot Rumors Data is Saved Succefuly")
print("Data Collection completed succesfuly")
