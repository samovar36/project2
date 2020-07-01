from requests import get, status_codes
r = get('https://google.com')
print (r, status_codes)

print ('hello world')