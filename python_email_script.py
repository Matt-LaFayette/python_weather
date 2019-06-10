import requests
import pprint
from datetime import datetime
import smtplib


api_address='http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/30043?apikey=hrMZkaYQAAzyAKJOvSaFX67RmE0LTPAV'
url = api_address
json_data = requests.get(url).json()
pp = pprint.PrettyPrinter(indent=4)

#pp.pprint (json_data[0]['DateTime'])

def stripDate(date):
	cutDate = date[0:10]+ " " + date[11:19]
	formattedDate =  datetime.strptime(cutDate, '%Y-%m-%d %H:%M:%S').strftime("%m-%d-%y %I:%M %p")
	return formattedDate

def returnTime(time):
	timeOnly = time[9:16]
	return timeOnly

#NEED TO CLEAN THESE UP
dateArray = []
percentArray = []
combinedArray = []
todayArray = []


today = str(datetime.today())

'''
if (stripDate(json_data[x]['DateTime']) = today):
 	returnTime(stripDate(json_data[x]['DateTime']))
 	combinedArray.append(str(returnTime) + str(json_data[x]['PrecipitationProbability']) + "%")

'''




date_list_string = '\n'.join(combinedArray)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("lafayette.matt@gmail.com", "empxkcyzlxdntovz")
server.sendmail(
  "lafayette.matt@gmail.com", 
  "lafayette.matt@gmail.com", 
  "\n" + date_list_string)
server.quit()



pp.pprint(combinedArray)


#test = datetime.strptime(json_data[0]['DateTime'], '%Y-%m-%dT%H:%M:%S%z')
#print (test.strftime("%m-%d-%y %I:%M %p %Z"))


'''
EXAMPLE OUTPUT OF api_address

{   'DateTime': '2019-06-11T02:00:00+02:00',
    'EpochDateTime': 1560211200,
    'HasPrecipitation': False,
    'IconPhrase': 'Cloudy',
    'IsDaylight': False,
    'Link': 'http://www.accuweather.com/en/be/seilles/30043/hourly-weather-forecast/30043?day=2&hbhhour=2&lang=en-us',
    'MobileLink': 'http://m.accuweather.com/en/be/seilles/30043/hourly-weather-forecast/30043?day=2&hbhhour=2&lang=en-us',
    'PrecipitationProbability': 47,
    'Temperature': {'Unit': 'F', 'UnitType': 18, 'Value': 57.0},
    'WeatherIcon': 7}



put this seciont back in main code.... API only allows 50 calls per day

for x in range(10):
	dateArray.append(stripDate(json_data[x]['DateTime']))
	percentArray.append(str(json_data[x]['PrecipitationProbability']) + "%")
	combinedArray.append(str(stripDate(json_data[x]['DateTime'])) + str(json_data[x]['PrecipitationProbability']) + "%" )

'''

'''
['06-10-19 10:00 PM has a 60% chance of rain', '06-10-19 11:00 PM has a 40% chance of rain', 
'06-11-19 12:00 AM has a 34% chance of rain', '06-11-19 01:00 AM has a 37% chance of rain', 
'06-11-19 02:00 AM has a 47% chance of rain', '06-11-19 03:00 AM has a 51% chance of rain', 
'06-11-19 04:00 AM has a 43% chance of rain', '06-11-19 05:00 AM has a 51% chance of rain', 
'06-11-19 06:00 AM has a 47% chance of rain', '06-11-19 07:00 AM has a 47% chance of rain']

'''