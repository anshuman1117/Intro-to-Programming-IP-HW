# ANSHUMAN SINGH
# 2017025

import urllib.request
import datetime
# function to get weather response
def weather_response(Location,API_key):

	x = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s" %(Location, API_key))#Storing the URL return in a variable
	s = x.read()#Reading the return of the variable x 
	s = s.decode()#Decoding the read JSON to a string. 
	
	return s


# function to check for valid response 
def has_error(Location,json):
	#json=json.decode()
	x = json.index("city")# finding the index of city
	y = json.index("name",x+1)# finding the index of name of the city
	a = json.index('"',y+5)#finding the index of the start of the city name
	b = json.index('"',a+1)#finding the end of the string of the city name

	st = json[a+1:b]#Slicing the required name
	st = st.replace(" ","")#Removing any space in the name
	Location = Location.lower()#COnverting to lowercase to compare
	st = st.lower()#Converting to lower case to compare

	if(Location == st):
		return False
	else:#comparision done
		return True

	

# function to get attributes on nth day
def get_temperature (json, t,n=0):
	#json=json.decode()
	y = datetime.date.today() + datetime.timedelta(days=n)
	x = str(y) + " " + str(t)
	#^ Converted the date to the required date and stored the value in a string with the reqquired time as a continuous string
	a = json.find(x)#Locate the required date and time in the string
	b = json.find("temp",a-345,a)#Going back to the starting of the info of the particular date to find required parameter
	c = json[b+6:b+12]#Slicing the required parameter

	c = float(c)#Converting to float to return in the required format
	return(c)
   

def get_humidity(json, t, n=0):
	#json=json.decode()
	y = datetime.date.today() + datetime.timedelta(days=n)
	x = str(y) + " " + str(t)
	#^ Converted the date to the required date and stored the value in a string with the reqquired time as a continuous string
	a = json.find(x)#Locate the required date and time in the string
	b = json.find("humidity",a-345,a)#Going back to the starting of the info of the particular date to find required parameter
	c = json[b+10:b+12]#Slicing the required parameter

	c = float(c)#Converting to float to return in the required format

	return(c)

def get_pressure(json, t, n=0):
	#json=json.decode()
	y = datetime.date.today() + datetime.timedelta(days=n)
	x = str(y) + " " + str(t)
	#^ Converted the date to the required date and stored the value in a string with the reqquired time as a continuous string
	a = json.find(x)#Locate the required date and time in the string
	b = json.find("pressure",a-345,a)#Going back to the starting of the info of the particular date to find required parameter
	
	c = json[b+10:b+16]#Slicing the required parameter

	c = float(c)#Converting to float to return in the required format

	return(c)


def get_wind(json, t, n=0):
	#json=json.decode()
	y = datetime.date.today() + datetime.timedelta(days=n)
	x = str(y) + " " + str(t)
	#^ Converted the date to the required date and stored the value in a string with the reqquired time as a continuous string
	a = json.find(x)#Locate the required date and time in the string
	b = json.find("wind",a-345,a)#Going back to the starting of the info of the particular date to find required parameter
	
	c = json[b+15:b+19]#Slicing the required parameter
	c = float(c)#Converting to float to return in the required format

	return(c) 

def get_sealevel(json,t, n=0):

	#json=json.decode()
	y = datetime.date.today() + datetime.timedelta(days=n)
	x = str(y) + " " + str(t)
	#^ Converted the date to the required date and stored the value in a string with the reqquired time as a continuous string
	a = json.find(x)#Locate the required date and time in the string
	b = json.find("sea_level",a-345,a)#Going back to the starting of the info of the particular date to find required parameter
	c = json[b+11:b+17]#Slicing the required parameter
	c = float(c)#Converting to float to return in the required format

	return(c) 

	









