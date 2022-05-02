import pyshorteners

site = input('Qual a url do site que você deseja encurtar? ')

encurta = pyshorteners.Shortener()
print(encurta.tinyurl.short(site))



# print(pyshorteners.Shortener().tinyurl.short('http://www.google.com'))
