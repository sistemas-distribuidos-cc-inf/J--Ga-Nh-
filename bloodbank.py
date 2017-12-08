import Pyro4
from bloodbag import BloodBag

class BloodBank(object):
	def __init__(self):
		self.storage = []

	def list_storage(self):
		for bag in self.storage:
			return bag.__dict__

	def retrieve(self, doctorname, bagid, patient):
		for bag in self.storage:
			if bag.bagid == bagid:
				self.storage.remove(bag)

		print('{0} retrieved a blood bag for {1}'.format(doctorname, patient))

	def store(self, bagid, bloodtype, donor, collectiondate, expirydate, address):
		bag = BloodBag(bagid, bloodtype, donor, collectiondate, expirydate, address)
		self.storage.append(bag)


def main():
	bloodbank = BloodBank()
	Pyro4.Daemon.serveSimple({bloodbank: "bloodbank"}, ns=True)

if __name__ == "__main__":
	main()