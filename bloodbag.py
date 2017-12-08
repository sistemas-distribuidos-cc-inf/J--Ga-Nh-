
class BloodBag(object):
	def __init__(self, bagid, bloodtype, donor, collectiondate, expirydate, address):
		self.bagid = bagid
		self.type = bloodtype
		self.donor = donor
		self.collectiondate = collectiondate
		self.expirydate = expirydate
		self.address = address