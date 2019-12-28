from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime

from .GarbageCollection import GarbageCollection

class RHEntsorgung:
	def getGarbageCollections(self, city, street, number):

		print ("--> getGarbageCollections()")

		city = city.lower()
		city = city.replace (u"ä", u"ae")
		city = city.replace (u"ö", u"oe")
		city = city.replace (u"ü", u"ue")
		city = city.replace (u"ß", u"ss")

		street = street.lower()
		street = street.replace (u"ä", u"ae")
		street = street.replace (u"ö", u"oe")
		street = street.replace (u"ü", u"ue")
		street = street.replace (u"ß", u"ss")

		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--window-size=1024x1400")

		chrome_driver = os.path.join(os.getcwd(), "chromedriver")

		driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

		driver.get('https://extdienste01.koblenz.de/WasteManagementRheinhunsrueck/WasteManagementServlet?SubmitAction=wasteDisposalServices&InFrameMode=TRUE')

    	# Ort
		ort = driver.find_element_by_name("Ort")
		ort.send_keys(city)

    	# Straße
		strasse = driver.find_element_by_name("Strasse")
		strasse.send_keys(street)

    	# Hausnummer
		hnr = driver.find_element_by_name("Hausnummer")
		hnr.send_keys(number)

    	# Seite abschicken
		hnr.send_keys(Keys.RETURN)

		driver.get_screenshot_as_file("Rhe-script.png")

		collections = []

		# Später
		# check for errors 
		#possible_err = r.html.find('td.info.listcolumn')
		#if (len(possible_err) > 0):
		#	print(possible_err[0].text)

		# Garbage Collection dates (only first one)
		elements = driver.find_elements_by_xpath("//*[contains(@name,'WasteDisposalServicesDialogComponent.Date')]")
		merkType = ""
		for e in elements:
			typeName = e.get_attribute("name")
			find = typeName.find('.Date')
			type = typeName[(find+5):]
			date = e.text[:10]
			if merkType != type:
				collection = GarbageCollection(date, type)
				merkType = type
				collections.append(collection)

		return collections



class CityNotFoundException(Exception):
	pass

class StreetNotFoundException(Exception):
	pass

class StreetNumberNotFoundException(Exception):
	pass