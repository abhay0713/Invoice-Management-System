class mycon:
	def __init__(self):
		import mysql.connector

		self.mydb=mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="invoice"
			)
		self.mycursor=self.mydb.cursor()


	def __del__(self):
		self.mydb.close()