from utilities.db import db_manager
from datetime import datetime

class Customer_Query:

    def __init__(self):
        self.db = db_manager.dbManager

    def get_customers(self):
        query = "select * from customers"
        ans = self.db.fetch(query=query)
        return ans

    def insert_user(self, customerID, phone, email, first_name, last_name, password):
        query = "INSERT into customers(customerID, phone, email, first_name, last_name, password) VALUES ('%s', '%s','%s', '%s','%s','%s');" % (customerID, phone, email, first_name, last_name, password)
        self.db.commit(query=query)

    def getLastUserId(self):
        query = "select customerID from customers"
        ans = self.db.fetch(query=query)
        maxId = ans[-1][0]
        return maxId

    def getCustomerInfo(self, customerID):
        query = "select * from customers where customers.customerID = '%s'" %customerID
        ans = self.db.fetch(query=query)
        return ans

    def updateCustomerInfo(self, customerID, first_name, last_name, phone, email, psw):
        query = "Update customers set first_name = '%s', last_name = '%s', phone = '%s', email = '%s', password = '%s' where customers.customerID = '%s' " %(first_name, last_name, phone, email, psw, customerID)
        self.db.commit(query=query)
