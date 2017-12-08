
class Person(object):
	def __init__(self, name, bloodtype, phonenumber, address):
		self.name = name
		self.bloodtype = bloodtype
		self.phonenumber = phonenumber
		self.address = address

	def donate(self, bloodbank, bloodbag):
		if bloodbag:
			bloodbank.store(bloodbag)