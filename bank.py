# Importing libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse
import csv
import pandas as pd

# Initializing server app
app = Flask(__name__)
api = Api(app)


# 1. Create new account
number = 1
class Create(Resource):
	def get(self, nic, name, place, work, contact, amount):
		global number
		new = [number, "unarchive", nic, name, place, work, contact, amount]

		file = open("bank_data.csv")
		bank = csv.reader(file)
		header = next(bank)

		rows = []
		for row in bank:
			if row[2] == nic:
				return (f"Already an account registered under this NIC: {nic}")
			rows.append(row)

		rows.append(new)

		df = pd.DataFrame(rows, columns=header)
		df.to_csv('bank_data.csv', index=False)

		return (f"Successfully created an account under NIC: {nic}")


# 2. Delete an existing account
class Delete(Resource):
	def get(self, nic):
		if len(nic)  == 9:
			file = open("bank_data.csv")
			bank = csv.reader(file)
			header = next(bank)

			rows = []
			count = 0
			for row in bank:
				if row[2] == nic:
					count += 1
				else:
					rows.append(row)

			if count == 0:
				return ("No account registered under this NIC number")
			elif count == 1:
				df = pd.DataFrame(rows, columns=header)
				df.to_csv('bank_data.csv', index=False)
				return ("Particular account is deleted")
			else:
				return ("How a NIC number holds more than 1 account ?????")

		else:
			return ("NIC number must have 9 numbers")


# 3. Update an existing account
class Update(Resource):
	def get(self, nic, field, value):
		if len(nic) == 9:
			details = {"name":3, "place":4, "work":5, "contact":6, "amount":7}

			if field in details.keys():
				file = open("bank_data.csv")
				bank = csv.reader(file)
				header = next(bank)

				rows = []
				count = 0

				for row in bank:
					if row[2] == nic:
						row[details[field]] = value
					else:
						count += 1
					rows.append(row)
				if count == len(rows):
					 return ("No account exist under this NIC number")
				else:
					df = pd.DataFrame(rows, columns=header)
					df.to_csv('bank_data.csv', index=False)
					return ("Account details is updated")
			else:
				return ("Invalid field inputted to update")
		else:
			return ("NIC number must have 9 numbers")


# 4. Read an existing account
class Read(Resource):
	def get(self, nic):
		if len(nic) == 9:
			file = open("bank_data.csv")
			bank = csv.reader(file)
			header = next(bank)

			rows = []
			for row in bank:
			    if row[2] == nic:
			    	return (row)
			return ("No account exist under this NIC number")
		else:
			return ("NIC number must have 9 numbers")


# 5. Archive / Unarchive an account
class Status(Resource):
	def get(self, nic, what):
		if what in ["archive", "unarchive"]:
			file = open("bank_data.csv")
			bank = csv.reader(file)
			header = next(bank)

			rows = []
			count = 0
			for row in bank:
			    if row[2] == str(nic):
			    	if row[1] == what:
			    		if what == "archive":
			    			return ("Already account is archived")
			    		else:
			    			return ("Already account is unarchived")
			    	else:
			    		row[1] = what
			    		rows.append(row)
			    else:
			    	rows.append(row)
			    	count += 1

			if count == len(rows):
			 	return ("No account exist under this NIC number")
			else:
				df = pd.DataFrame(rows, columns=header)
				df.to_csv('bank_data.csv', index=False)
				return ("Account status is updated")
		else:
			return ("Status must be archive / unarchive to modify accounts")


# 6. List archived / unarchived accounts
class Accounts(Resource):
	def get(self, what):
		if what in ["archive", "unarchive"]:
			file = open("bank_data.csv")
			bank = csv.reader(file)
			header = next(bank)

			accounts_nic = []

			for row in bank:
				if row[1] == what:
					accounts_nic.append(row[2])
			return (accounts_nic)

		else:
			return ("Status must be archive / unarchive to list accounts")


# Adding resources
api.add_resource(Create, '/create/<string:nic>/<string:name>/<string:place>/<string:work>/<string:contact>/<string:amount>')
api.add_resource(Delete, '/delete/<string:nic>')
api.add_resource(Update, '/update/<string:nic>/<string:field>/<string:value>')
api.add_resource(Read, '/read/<string:nic>')
api.add_resource(Status , '/status/<int:nic>/<string:what>')
api.add_resource(Accounts, '/accounts/<string:what>')

# Run server app
if __name__ == '__main__':
	app.run(port=2305, debug=True)