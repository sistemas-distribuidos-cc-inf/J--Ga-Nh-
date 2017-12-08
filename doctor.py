
class Doctor(object):
	def __init__(self, name, speciality, hospital):
		self.name = name
		self.speciality = speciality
		self.hospital = hospital

	def retrieve_bloodbag(self, person, bloodbank):
		for bag in bloodbank.list_storage():
			if bag.bloodtype == person.bloodtype:
				bloodbank.retrieve(self.name, bag, person.name)
				break
			else:
				print('No {0} blood bags in storage'.format(person.bloodtype))
