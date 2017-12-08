
class BloodBag(object):
	__id = 0

	def __init__(self, bloodtype, donor, collectiondate, expirydate, address)
		self.bagid = BloodBag.__id += 1
		self.type = bloodtype
		self.donor = donor
		self.collectiondate = collectiondate
		self.expirydate = expirydate
		self.address = address

	def __eq__(self, other):
		return self.name == other.name