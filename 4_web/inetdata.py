import urllib.request

url = 'https://github.com/avlye'
request = urllib.request.urlopen(url)
data = request.read()

print(data)