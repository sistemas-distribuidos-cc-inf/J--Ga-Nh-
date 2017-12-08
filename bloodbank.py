import Pyro4

class BloodBank(object):
	def __init__(self):
		self.storage = []

	def list_storage(self):
		return self.storage

	def retrieve(self, doctorname, bloodbag, patient):
		if bloodbag:
			self.storage.remove(bloodbag)

		print('{0} retrieved a blood bag for {1}'.format(doctorname, patient))

	def store(self, bloodbag)
		self.storage.append(bloodbag)


def main():
	bloodbank = BloodBank()
	Pyro4.Daemon.serveSimple({bloodbank: "bloodbank"}, ns=True)

if __name__ == "__main__":
	main()