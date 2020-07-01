#Need to install packages 'requests' and 'pypiwin32' using 'pip install <package-name>
import requests , json
#importing text to speech
from win32com.client import Dispatch
url = ('http://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=21ce33e07e574e7297264c1e6023e335') #API of News , Visit the below link to change links accordingly for different news.

#Reference URL for more news :  https://newsapi.org/docs/get-started
#bla bla
#function to read text
def NewsReader(mystr):
    TextToSpeak=Dispatch("SAPI.spVoice")
    TextToSpeak.Speak(mystr)

#variable to read data from  url
response = requests.get(url)
#data = response.text
data = (requests.get(url)).text
print(data) #for printing incoming data
jsonData = json.loads(data) #Parses data from JSON to variable
print(jsonData)
for i in range(0, 11):
    NewsReader(jsonData['articles'][i]['title'])
    #NewsReader(jsonData['articles'][i]['description']) #Uncomment these lines to speak out description and contents.
    #NewsReader(jsonData['articles'][i]['content'])
