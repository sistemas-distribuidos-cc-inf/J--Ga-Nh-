from bloodbag import BloodBag

class Doctor(object):
	def __init__(self, name, speciality, hospital):
		self.name = name
		self.speciality = speciality
		self.hospital = hospital

	def retrieve_bloodbag(self, person, bloodbank):
		bag = bloodbank.list_storage()
		if bag['type'] == person.bloodtype:
			bloodbank.retrieve(self.name, bag['bagid'], person.name)
		else:
			print('No {0} blood bags in storage'.format(person.bloodtype))
