import os

def getAll():

	__location__ = os.path.realpath(
	    os.path.join(os.getcwd(), os.path.dirname(__file__)))

	filename="stations.json"
	f = open(os.path.join(__location__, filename), "r")

	return f.read()