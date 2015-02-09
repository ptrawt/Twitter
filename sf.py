from urllib import urlopen
from bs4 import BeautifulSoup
import re
import time

optionsUrl = 'http://booking.sfcinemacity.com/visPrintShowTimes.aspx?visLang=1&visCinemaId=9936'
optionsPage = urlopen(optionsUrl)

soup = BeautifulSoup(optionsPage)

cname = str(soup.findAll('span',{'class':'PrintCinemaName'})[0].next)
print cname

current_date = time.strftime("%a %d %b")
print current_date
print '==========='
 
# fetch movies name and showtimes
for td in soup.find_all('td',{'class':'PrintShowTimesFilm'}):
    movie_name = re.sub('\[[^)]*\]', '', td.text).strip()
    date = td.next_element.next_element.next_element.contents[1].text
    if date != current_date : continue
    time = td.next_element.next_element.next_element.contents[2].text
    print movie_name,time