import pyperclip
import webbrowser

s = pyperclip.paste()
brave_path = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe -incognito %s'
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe -incognito %s'
#firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe -private %s'
url = ("https://www.google.com/search?q=" + s)
webbrowser.get(brave_path).open(url)
#webbrowser.get(chrome_path).open(url)
#webbrowser.get(firefox_path).open(url)

"""Chrome & Brave-WebBrowser opens new private window even when there is already a normal chrome window opened; 
  firefox doesn't.

If you want to use firefox then uncomment line 7 & 11; 
  and put "#" in at the beginning of the brave-browser lines (line 5 & 9) """
