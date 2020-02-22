# Includes solution for Exercise 21)

# Exercise 19
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article 
# on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

# The article is long, so it is split up between 4 pages. Your task is to print out the text to 
# the screen so that you can read the full article without having to click any buttons.

# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries 
# through the solution of the exercise posted here.)

# This will just print the full text of the article to the screen. It will not make it 
# easy to read, so next exercise we will learn how to write this text to a .txt file.

import requests
from bs4 import BeautifulSoup
import time

tic = time.perf_counter() # timer starts

url = ""
page_variable = '?page='
save_location = r'C:\Users\Fede\Desktop\practicepython'

links = []
bodies = []
cutoff = int(input('Cutoff limit: '))  # custom limit (to avoid an infinite loop)
page = 0

for i in range(1, cutoff+1):
    print("*"*50)
    url_check = "https://www.fanfiction.net/s/9357902/"+str(i)+"/All-That-Remains"
    # or url_check = url + ((url_suffix + str(i)) if i > 1 else "")
    print(f'Checking: {url_check}')
    response = requests.get(url_check)
    print(f'Response: {response.status_code}')

    if response.status_code == 200:
        soup = BeautifulSoup(response.text)

        if i == 1:
            article_title = soup.find_all('b', {'class':'xcontrast_txt'})
            for t in article_title:
                title = t.text

            article_author = soup.find_all('a', {'class':'xcontrast_txt'})
            lst = []
            for i in article_author:
                lst.append(i.text)
            author = lst[2]

        content = soup.find_all('div', {'class':'storytext xcontrast_txt nocopy'})
        for i in content:
            body = i.text
        if body in bodies:
            print("Page doesn't exist.")
            break
        else:
            bodies.append(body)
            links.append(url_check)
            print('Page downloaded')
            page += 1
            continue
    else:
        print("*"*50)
        print(f'Website response: {response.status_code}\nPage could not be loaded.')
        print('Further links will not be checked.')
        break

if links != []:        
    with open(f'{save_location}\\{title}.txt', 'w', encoding="utf-8") as file:
        file.write(title + '\n')
        file.write('by ' + author + '\n\n')
        file.write(f'Link: {links[0]}' + '\n\n')
        page_num = 1 
        for i in bodies:
            file.write(f'\n' + "*"*10 + f' Page {page_num} ' + "*"*10 + '\n\n' + i + '\n')
            page_num += 1

toc = time.perf_counter()
print(f'\nTime taken: {toc - tic:0.4} secs.')

