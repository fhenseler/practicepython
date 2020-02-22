# Exercise 17
# Use the BeautifulSoup and requests Python packages to print out 
# a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests
 
base_url = 'http://www.nytimes.com/'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
 
get_titles = soup.find_all(class_="css-1qwxefa esl82me0")

for title in get_titles:
    print(title.text)
