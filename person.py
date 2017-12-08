import datetime
from bloodbag import BloodBag

class Person(object):
	def __init__(self, name, bloodtype, phonenumber, address):
		self.name = name
		self.bloodtype = bloodtype
		self.phonenumber = phonenumber
		self.address = address

	def donate(self, bloodbank):
		cdate = datetime.datetime.now()
		edate = cdate + datetime.timedelta(days=42)

		bloodbank.store(1, self.bloodtype, self.name, cdate, edate, self.address)
		print('Thank you for donating')