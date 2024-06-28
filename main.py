
import pyshorteners
link = input("paste your link = ")
shortner = pyshorteners.Shortener()
short_link = shortner.tinyurl.short(link)
print("here is your short link \n",short_link )