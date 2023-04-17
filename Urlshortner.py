import pyshortener
import pyperclip
url = print("Enter URL")
def shortenurl(url):
    s = pyshortener.Shortener()
    print(s.tinyurl.short(url))
shortenurl(url)
