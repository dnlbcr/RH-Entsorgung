import argparse

from .RHEntsorgung import RHEntsorgung
from .GarbageCollection import GarbageCollection


def main():
	parser = argparse.ArgumentParser(description='Get garbage collection dates for Rhein-Hunsrück Entsorgung.')

	parser.add_argument('city')
	parser.add_argument('street')
	parser.add_argument('number')

	# Prüfen, ob das hier überhaupt relevant ist für die RH Entsorgung
	#parser.add_argument("--asid", help="use asid instead of street", action="store_true")
	#parser.add_argument("--hnid", help="use hnid instead of street number", action="store_true")

	args = parser.parse_args()

	print ("--> Einstieg rh_entsorgung.py")
	print (args.city)
	print (args.street)
	print (args.number)

	rhe = RHEntsorgung()
	collections = rhe.getGarbageCollections(args.city, args.street, args.number)

	if (len(collections) > 0):
		print("Next garbage collections: ")
		for c in collections:
			print (c.container + " on " + c.date)