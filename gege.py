from requests import get

print("The information about your IP Address is as follows: ")

print ("IP Address: ", get('https://ipapi.co/ip/').text)

print ("City: ", get('https://ipapi.co/city/').text)

print("Region: ", get('https://ipapi.co/region/').text)

print ("Country: ", get('https://ipapi.co/country_name/').text)

print("Top level Domain: ", get('https://ipapi.co/country_tld/').text)

print("Postal Code: ", get('https://ipapi.co/postal/').text)

print ("Capital: ", get('https://ipapi.co/country_capital/').text)

print ("European union: ", get('https://ipapi.co/in_eu/').text)

print("Latitude / Longitude: ", get('https://ipapi.co/latlong/').text)

print ("Time zone: ", get('https://ipapi.co/timezone/').text)

print("Calling Code: ", get('https://ipapi.co/country_calling_code/').text)

print("Currency: ", get('https://ipapi.co/currency_name/').text)

print ("Languages: ", get('https://ipapi.co/languages/').text)

print ("Languages: ", get('https://ipapi.co/asn/').text)

print("ISP: ", get('https://ipapi.co/org/').text)
