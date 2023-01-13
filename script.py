import requests

print('requests version')
print(requests.__version__)

print()
print('Homepage of Google:')
print(requests.get("http://www.google.com/").text)
print()
print('This script contains the following source code:')
print(requests.get("https://raw.githubusercontent.com/NickSNFK/cmput404-lab1/main/script.py").text)