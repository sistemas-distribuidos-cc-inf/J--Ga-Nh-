import sys
import Pyro4
import Pyro4.util
from person import Person
from doctor import Doctor

sys.excepthook = Pyro4.util.excepthook

bloodbank = Pyro4.Proxy("PYRONAME:bloodbank")

p1 = Person("John", "O-", "555-1234", "221B Baker Street")
p2 = Person("Sherlock", "AB+", "555-1234", "221B Baker Street")
d = Doctor("Mary", "Hematology", "The Best Hospital Ever")

p1.donate(bloodbank)
d.retrieve_bloodbag(p2, bloodbank)