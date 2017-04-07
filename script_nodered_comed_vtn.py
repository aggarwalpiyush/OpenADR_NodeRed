#!/usr/bin/python
import re 
import time
import json
from mechanize import Browser
br = Browser()
br.set_handle_robots(False)
ip='127.0.0.1:7070'


from datetime import date, timedelta
date1= str((date.today()).strftime('%Y%m%d'))
date2=str((date.today() + timedelta(1)).strftime('%Y%m%d'))
watch=0
def watcher(val):
	global watch
	if watch!=val:
		vtn_update(val)
		
		print val
		watch =val

def vtn_update(val):
	try:
		# Ignore robots.txt
		#br.set_handle_robots( False )
		# some websites demands a user-agent that isn't a robot
		br.addheaders = [('User-agent', 'Firefox')]

		# Retrieve the VTN home page, saving the response
		resp=br.open( 'http://'+ip )
		time.sleep(.500)
		# Select the login form and input credentials
		br.select_form(nr=0)
		br.form[ 'session[user_name]' ] = 'admin'
		br.form[ 'session[password]' ] = 'testing'
		br.find_control('session[agree]','checkbox').items[0].selected=True



		# # Click submit button
		resp=br.submit()

		# Open page to edit signal payload
		resp = br.open('http://'+ip+'/event_signals/10')
		time.sleep(.500)
		br.select_form(nr=2)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = price
		resp=br.submit(name='commit',label='Save')

		#Open page to publish event changes
		resp = br.open('http://'+ip+'/events/7')
		time.sleep(.500)
		br.select_form(nr=0)
		resp=br.submit(name='commit',label='Publish Event')
		# Print the site
		#content = resp.get_data()
		#print resp.read()
		
	except:
		# Ignore robots.txt
		#br.set_handle_robots( False )
		# some websites demands a user-agent that isn't a robot
		br.addheaders = [('User-agent', 'Firefox')]

		# Retrieve the VTN home page, saving the response
		resp=br.open( 'http://'+ip)
		time.sleep(.500)
		# Select the login form and input credentials
		#br.select_form(nr=0)
		#br.form[ 'session[user_name]' ] = 'admin'
		#br.form[ 'session[password]' ] = 'testing'
		#br.find_control('session[agree]','checkbox').items[0].selected=True



		# Click submit button
		#resp=br.submit()

		# Open page to edit signal payload
		resp = br.open('http://'+ip+'/event_signals/10')
		time.sleep(.500)
		br.select_form(nr=2)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = price
		resp=br.submit(name='commit',label='Save')

		#Open page to publish event changes
		resp = br.open('http://'+ip+'/events/7')
		time.sleep(.500)
		br.select_form(nr=0)
		resp=br.submit(name='commit',label='Publish Event')
		
		# Print the site
		#content = resp.get_data()
		#print resp.read()

def forecast_update():
	try:
	
		resp=br.open( 'https://hourlypricing.comed.com/rrtp/ServletFeed?type=daynexttoday&date='+date1)
		a_data1=br.response().read()
		a_data1=a_data1.split()
		#a_data1=a_data1[3][0:3]
		resp=br.open( 'https://hourlypricing.comed.com/rrtp/ServletFeed?type=daynexttoday&date='+date2)
		a_data2=br.response().read()
		a_data2=a_data2.split()
		#a_data2=a_data2[3][0:3]
		localtime = time.localtime(time.time())
		if (localtime.tm_hour <18):
			array=[a_data1[3][0:3],a_data1[5][0:3],a_data1[7][0:3],a_data1[9][0:3],a_data1[11][0:3],a_data1[13][0:3],a_data1[15][0:3],a_data1[17][0:3],a_data1[19][0:3],a_data1[21][0:3],a_data1[23][0:3],a_data1[25][0:3],a_data1[27][0:3],a_data1[29][0:3],a_data1[31][0:3],a_data1[33][0:3],a_data1[35][0:3],a_data1[37][0:3],a_data1[39][0:3],a_data1[41][0:3],a_data1[43][0:3],a_data1[45][0:3],a_data1[47][0:3]]
			list_max=max(array)
			a_data=[a_data1[3][0:3],a_data1[5][0:3],a_data1[7][0:3],a_data1[9][0:3],a_data1[11][0:3],a_data1[13][0:3],a_data1[15][0:3],a_data1[17][0:3],a_data1[19][0:3],a_data1[21][0:3],a_data1[23][0:3],a_data1[25][0:3],a_data1[27][0:3],a_data1[29][0:3],a_data1[31][0:3],a_data1[33][0:3],a_data1[35][0:3],a_data1[37][0:3],a_data1[39][0:3],a_data1[41][0:3],a_data1[43][0:3],a_data1[45][0:3],a_data1[47][0:3],list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max]
		else :
			a_data=[a_data1[3][0:3],a_data1[5][0:3],a_data1[7][0:3],a_data1[9][0:3],a_data1[11][0:3],a_data1[13][0:3],a_data1[15][0:3],a_data1[17][0:3],a_data1[19][0:3],a_data1[21][0:3],a_data1[23][0:3],a_data1[25][0:3],a_data1[27][0:3],a_data1[29][0:3],a_data1[31][0:3],a_data1[33][0:3],a_data1[35][0:3],a_data1[37][0:3],a_data1[39][0:3],a_data1[41][0:3],a_data1[43][0:3],a_data1[45][0:3],a_data1[47][0:3],a_data2[1][0:3],a_data2[3][0:3],a_data2[5][0:3],a_data2[7][0:3],a_data2[9][0:3],a_data2[11][0:3],a_data2[13][0:3],a_data2[15][0:3],a_data2[17][0:3],a_data2[19][0:3],a_data2[21][0:3],a_data2[23][0:3],a_data2[25][0:3],a_data2[27][0:3],a_data2[29][0:3],a_data2[31][0:3],a_data2[33][0:3],a_data2[35][0:3],a_data2[37][0:3],a_data2[39][0:3],a_data2[41][0:3],a_data2[43][0:3],a_data2[45][0:3],a_data2[47][0:3]]
			
		a=a_data
		# Ignore robots.txt
		#br.set_handle_robots( False )
		# some websites demands a user-agent that isn't a robot
		br.addheaders = [('User-agent', 'Firefox')]

		# Retrieve the VTN home page, saving the response
		resp=br.open( 'http://'+ip )
		time.sleep(.500)
		# Select the login form and input credentials
		br.select_form(nr=0)
		br.form[ 'session[user_name]' ] = 'admin'
		br.form[ 'session[password]' ] = 'testing'
		br.find_control('session[agree]','checkbox').items[0].selected=True



		# Click submit button
		resp=br.submit()

		# Open page to edit signal payload
		resp = br.open('http://'+ip+'/event_signals/9')
		time.sleep(.500)
		br.select_form(nr=2)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[0])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=3)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[1])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=4)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[2])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=5)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[3])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=6)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[4])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=7)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[5])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=8)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[6])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=9)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[7])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=10)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[8])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=11)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[9])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=12)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[10])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=13)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[11])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=14)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[12])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=15)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[13])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=16)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[14])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=17)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[15])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=18)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[16])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=19)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[17])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=20)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[18])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=21)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[19])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=22)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[20])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=23)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[21])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=24)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[22])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=25)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[23])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=26)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[24])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=27)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[25]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=28)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[26]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=29)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[27]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=30)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[28]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=31)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[29]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=32)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[30]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=33)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[31]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=34)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[32]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=35)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[33]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=36)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[34]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=37)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[35]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=38)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[36]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=39)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[37]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=40)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[38]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=41)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[39]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=42)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[40]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=43)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[41]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=44)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[42]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=45)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[43]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=46)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[44]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=47)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[45]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=48)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[46]
		resp=br.submit(name='commit',label='Save')
		
		
		
		
		#Open page to publish event changes
		resp = br.open('http://'+ip+'/events/6')
		time.sleep(.500)
		br.select_form(nr=0)
		resp=br.submit(name='commit',label='Publish Event')
		
	except:
		resp=br.open( 'https://hourlypricing.comed.com/rrtp/ServletFeed?type=daynexttoday&date='+date1)
		a_data1=br.response().read()
		a_data1=a_data1.split()
		#a_data1=a_data1[3][0:3]
		resp=br.open( 'https://hourlypricing.comed.com/rrtp/ServletFeed?type=daynexttoday&date='+date2)
		a_data2=br.response().read()
		a_data2=a_data2.split()
		#a_data2=a_data2[3][0:3]
		localtime = time.localtime(time.time())
		if (localtime.tm_hour <18):
			array=[a_data1[3][0:3],a_data1[5][0:3],a_data1[7][0:3],a_data1[9][0:3],a_data1[11][0:3],a_data1[13][0:3],a_data1[15][0:3],a_data1[17][0:3],a_data1[19][0:3],a_data1[21][0:3],a_data1[23][0:3],a_data1[25][0:3],a_data1[27][0:3],a_data1[29][0:3],a_data1[31][0:3],a_data1[33][0:3],a_data1[35][0:3],a_data1[37][0:3],a_data1[39][0:3],a_data1[41][0:3],a_data1[43][0:3],a_data1[45][0:3],a_data1[47][0:3]]
			list_max=max(array)
			a_data=[a_data1[3][0:3],a_data1[5][0:3],a_data1[7][0:3],a_data1[9][0:3],a_data1[11][0:3],a_data1[13][0:3],a_data1[15][0:3],a_data1[17][0:3],a_data1[19][0:3],a_data1[21][0:3],a_data1[23][0:3],a_data1[25][0:3],a_data1[27][0:3],a_data1[29][0:3],a_data1[31][0:3],a_data1[33][0:3],a_data1[35][0:3],a_data1[37][0:3],a_data1[39][0:3],a_data1[41][0:3],a_data1[43][0:3],a_data1[45][0:3],a_data1[47][0:3],list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max,list_max]
		else :
			a_data=[a_data1[3][0:3],a_data1[5][0:3],a_data1[7][0:3],a_data1[9][0:3],a_data1[11][0:3],a_data1[13][0:3],a_data1[15][0:3],a_data1[17][0:3],a_data1[19][0:3],a_data1[21][0:3],a_data1[23][0:3],a_data1[25][0:3],a_data1[27][0:3],a_data1[29][0:3],a_data1[31][0:3],a_data1[33][0:3],a_data1[35][0:3],a_data1[37][0:3],a_data1[39][0:3],a_data1[41][0:3],a_data1[43][0:3],a_data1[45][0:3],a_data1[47][0:3],a_data2[1][0:3],a_data2[3][0:3],a_data2[5][0:3],a_data2[7][0:3],a_data2[9][0:3],a_data2[11][0:3],a_data2[13][0:3],a_data2[15][0:3],a_data2[17][0:3],a_data2[19][0:3],a_data2[21][0:3],a_data2[23][0:3],a_data2[25][0:3],a_data2[27][0:3],a_data2[29][0:3],a_data2[31][0:3],a_data2[33][0:3],a_data2[35][0:3],a_data2[37][0:3],a_data2[39][0:3],a_data2[41][0:3],a_data2[43][0:3],a_data2[45][0:3],a_data2[47][0:3]]
			
		a=a_data
		# Ignore robots.txt
		#br.set_handle_robots( False )
		# some websites demands a user-agent that isn't a robot
		br.addheaders = [('User-agent', 'Firefox')]

		# Retrieve the VTN home page, saving the response
		resp=br.open( 'http://'+ip )
		time.sleep(.500)
		# Select the login form and input credentials
		# br.select_form(nr=0)
		# br.form[ 'session[user_name]' ] = 'admin'
		# br.form[ 'session[password]' ] = 'testing'
		# br.find_control('session[agree]','checkbox').items[0].selected=True



		# # Click submit button
		# resp=br.submit()

		# Open page to edit signal payload
		resp = br.open('http://'+ip+'/event_signals/9')
		time.sleep(.500)
		br.select_form(nr=2)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[0])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=3)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[1])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=4)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[2])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=5)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[3])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=6)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[4])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=7)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[5])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=8)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[6])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=9)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[7])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=10)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[8])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=11)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[9])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=12)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[10])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=13)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[11])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=14)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[12])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=15)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[13])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=16)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[14])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=17)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[15])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=18)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[16])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=19)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[17])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=20)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[18])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=21)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[19])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=22)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[20])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=23)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[21])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=24)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[22])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=25)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[23])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=26)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = str(a[24])
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=27)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[25]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=28)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[26]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=29)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[27]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=30)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[28]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=31)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[29]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=32)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[30]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=33)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[31]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=34)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[32]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=35)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[33]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=36)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[34]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=37)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[35]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=38)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[36]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=39)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[37]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=40)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[38]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=41)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[39]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=42)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[40]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=43)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[41]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=44)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[42]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=45)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[43]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=46)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[44]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=47)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[45]
		resp=br.submit(name='commit',label='Save')
		br.select_form(nr=48)
		#br.find_control('event_signal_interval[payload]','text').items[0].selected='60'
		br.form['event_signal_interval[payload]'] = a[46]
		resp=br.submit(name='commit',label='Save')
		
		
		
		
		#Open page to publish event changes
		resp = br.open('http://'+ip+'/events/6')
		time.sleep(.500)
		br.select_form(nr=0)
		resp=br.submit(name='commit',label='Publish Event')
		# Print the site
		#content = resp.get_data()
		#print resp.read()
		

forecast_update()
while 1:
	try:
		# Ignore robots.txt
		br.set_handle_robots( False )
		# some websites demands a user-agent that isn't a robot
		br.addheaders = [('User-agent', 'Firefox')]

		# Retrieve the price 
		price_resp=br.open( "https://hourlypricing.comed.com/api?type=currenthouraverage" )
		data = json.load(price_resp)
		price= data[0]["price"]
		watcher(price)
		# if now = 6:00 PM then update forecast data and update vtn
		localtime = time.localtime(time.time())
		if (localtime.tm_hour ==18 and localtime.tm_min==05):
			forecast_update()
			##
		
		
		
	except:
		# Ignore robots.txt
		br.set_handle_robots( False )
		# some websites demands a user-agent that isn't a robot
		br.addheaders = [('User-agent', 'Firefox')]

		# Retrieve the price 
		price_resp=br.open( "https://hourlypricing.comed.com/api?type=currenthouraverage" )
		data = json.load(price_resp)
		price= data[0]["price"]
		watcher(price)
		# if now = 6:00 PM then update forecast data and update vtn
		localtime = time.localtime(time.time())
		if (localtime.tm_hour ==18 and localtime.tm_min==05):
			forecast_update()
		
