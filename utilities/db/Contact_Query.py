from utilities.db import db_manager
from datetime import datetime

class Contact_Query:

    def __init__(self):
        self.db = db_manager.dbManager

    def insert_message(self, first_name, last_name, email, message):
        query = "INSERT into contacts(first_name, last_name, email, message, contact_date) VALUES ('%s', '%s','%s', '%s', '%s');" % (first_name, last_name, email, message, datetime.today())
        self.db.commit(query=query)
