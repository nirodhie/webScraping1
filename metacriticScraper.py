import requests
from bs4 import BeautifulSoup
import time

def get_metascore(gamename):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = "https://www.metacritic.com/search/game/"+gamename+"/results?plats[10]=1&search_type=advanced" #10- PSX 7- PSP
    html = requests.get(page, headers=headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    fileWithScores = open("metaScores-PSX.txt","a+")
    css_location1 = "#main_content > div.fxdrow.search_results_wrapper > div.module.search_results.fxdcol.gu6 > div.body > ul > li.result.first_result > div > div.basic_stats.has_thumbnail > div > span"
    css_location2 = "#main_content > div.fxdrow.search_results_wrapper > div.module.search_results.fxdcol.gu6 > div.body > ul > li.result.first_result > div > div.basic_stats.has_thumbnail > div > h3 > a"

    try:
        metascore = soup.select(css_location1)[0].text
        link = soup.select(css_location2)[0].attrs['href']
        if metascore == "tbd":
            time.sleep(1)
        else:
            print(gamename,"has a score of",metascore,"https://metacritic.com"+link)
            print(gamename,"has a score of",metascore,"https://metacritic.com"+link,file=fileWithScores)
            fileWithScores.close()
            time.sleep(1)

    except IndexError:
        time.sleep(1)





def readFromFileIntoArray(filename):
    wordsToReplace = ['.cso', ' (USA)', ' (Europe)', ', A', ', The']


    with open(filename) as file:
        array = []
        for line in file:
            #cleanline = [line.replace(word, '') for word in wordsToReplace]
            cleanline = line.replace('.PBP', '').replace('.cso', '').replace('.iso', '').replace(' (USA)', '').replace(' (Europe)', '').replace(', A', '').replace(', The', '').replace('\n', '')
            #array.append(cleanline)

            get_metascore(cleanline)

            #cleanline = line.strip()
        #return(array[index_number])


readFromFileIntoArray("psxGames.txt")
