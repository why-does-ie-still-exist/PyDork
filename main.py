#I haven't run this through an ide or anything so it'll probably crash
'''
Ideas from:
https://www.exploit-db.com/ghdb/4309/
https://github.com/abenassi/Google-Search-API
https://stackoverflow.com/questions/3305926/python-csv-string-to-array
https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe
https://stackoverflow.com/questions/20449427/how-can-i-read-inputs-as-integers //maybe useful as extra options
https://docs.python.org/2/library/urlparse.html
https://stackoverflow.com/questions/6838238/comparing-a-string-to-multiple-items-in-python
https://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python
https://www.dotnetperls.com/2d-python
'''

#IMPORTS GO UP HERE
from google import google
from bs4 import BeautifulSoup
form urlparse import urlparse

#Here is da google dork with escape characters :-)
dork = "intext:\"Dumping data for table \`orders\`\""

dork += "-git -hack -exploit -dork -cod -cyber" //Default ignored tags

''' STEP 1:
ask for ignored tags with comma seperated values
because google dorks often pull up a lot of exploit databases and blogs
'''
ignore = input("Enter ignored tags with csv. Default ignored tags are: -git -hack -exploit -dork -cod -cyber")
''' EXAMPLE:
>>> a = "1,2"
>>> a
'1,2'
>>> b = a.split(",")
>>> b
['1', '2']
'''
#Parse to String array:
tags = ignore.split(",")

#STEP 2: Append modifiers to google dork
for tag in tags:
  dork += "-" + tag + " "

#STEP 3: search google dork with google search api

num_page = 1 //Just does the first page in google
search_results = google.search("This is my query", num_page)

#STEP 4: scrape those pages in google with beautiful soup web scraper
pages = []
pages.append([])
pages.append([])
''' EXAMPLE:
# Add elements to empty lists.
elements[0].append(1)
elements[0].append(2)

elements[1].append(3)
elements[1].append(4)
'''
for result in search_results: //GoogleResult object
  pages[0].append(str(BeautifulSoup(result.link, ‘html.parser’)) to layer 1 of pages (adds the string-ified html))
  pages[1].append(add str(urlparse(result.link).netloc) to correspond with ^^^ (adds the homepage url))
  
'''
So in my mind it kinda looks like this:

|-------------|-------------|
|HTML OF PAGE1|HTML OF PAGE2|             <-----pages[0]
|-------------|-------------|  ETC.
|PAGE1.com    |PaGe2.net    |             <-----pages[1]
|-------------|-------------|
'''

goodchars= {"1",
"2",
"3",
"4",
"5",
"6",
"7",
"8",
"9",
"+",
"-",
".",
" ",
"(",
")"} #a bit tedious, I know:
for pagehtml in pages[0]:
  phonenums = ""
  phonelength = 0 //counts length of stored numbers
  count = 0
  while count < len(pagehtml):
    if phonelength >= 20:
      phonenums= phonenums[:phonelength-1] //THIS LINE IS VERY SKETCH IF ERROR LOOK @ HERE
      phonelength = 0
    else:
      if pagehtml[count:count+1] in goodchars:
        phonenums += pagehtml[count:count+1]
      else if "555" in phonenums:
        phonenums= phonenums[:phonelength-1] //THIS LINE IS VERY SKETCH IF ERROR LOOK @ HERE
        phonelength = 0
      else:
        if phonelength < 10
          phonenums= phonenums[:phonelength-1] //THIS LINE IS VERY SKETCH IF ERROR LOOK @ HERE
          phonelength = 0
        else:
          phonenums += ", "
  pages[0] = []
  pages[0].append(phonenums)
  
'''
AND FINALLY:
VISUALIZE
pages
'''
print(pages)
#Yay now you may have some phone numbers associated with purchases on the website.
