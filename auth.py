import MySQLdb
import hashlib
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

DBHOST = 'localhost'
DBUSER = 'jaganho'
DBPASS = 'JaGaNho'
DBNAME = 'jaganho'

class AuthenticationError(Exception): pass

class RegisterError(Exception): pass

class AuthenticationServer:
	"""docstring for AuthenticationServer"""
	def __init__(self):
		self.db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
		self.cur = self.db.cursor()

	def authenticate(self, username, password):
		error = None

		try:
			# 1 if the username is found on the database, 0 otherwise
			self.cur.execute("SELECT COUNT(1) FROM user WHERE username = %s", [username])
			if not self.cur.fetchone()[0]:
				raise AuthenticationError('Incorrect password or username')

			# retrieves the password hash
			self.cur.execute("SELECT password FROM user WHERE username = %s", [username])

			for row in self.cur.fetchall():
				if hashlib.md5(password).hexdigest() == row[0]:
					return True, error

			raise AuthenticationError('Incorrect password or username')

		except AuthenticationError as e:
			error = str(e)

		return False, error

	def register(self, username, password):
		error = None

		try:
			self.cur.execute("SELECT username FROM user")

			if username in self.cur.fetchall():
				raise RegisterError('Username already in use')

			else:
				self.cur.execute("INSERT INTO user(username, password) VALUES(%s, %s)", (username, hashlib.md5(password).hexdigest()))
				self.db.commit()
				return True, error

		except RegisterError as e:
			error = str(e)

		return False, error


server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(AuthenticationServer())
server.register_introspection_functions()
server.serve_forever()