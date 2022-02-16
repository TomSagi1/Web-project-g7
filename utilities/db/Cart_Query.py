from utilities.db import db_manager
from datetime import datetime

class Cart_Query:
    def __init__(self):
        self.db = db_manager.dbManager

    def getProducts(self):
        query = "SELECT * FROM products"
        ans = self.db.fetch(query=query)
        return ans;

    def getLastOrderID(self):
        query = "SELECT orderID FROM orders"
        ans = self.db.fetch(query=query)
        maxOrderID = ans[-1][0]
        return maxOrderID

    def createNewOrder(self, orderID, User):
        query = "INSERT INTO orders (orderID, order_date, total_price, customerID, approved) VALUES ('%s','%s','%s','%s','%s');" % (orderID, datetime.today(), 0, User, 0)
        self.db.commit(query = query)

    def createNewProductInOrder(self, orderID, productID, quantity):
        query = "INSERT INTO products_in_order (orderID, productID, quantity, total_price)  VALUES ('%s','%s','%s','%s');" % (orderID, productID, quantity, 0)
        self.db.commit(query=query)

    def getProductsInOrder(self, orderID):
        current = orderID
        query = "SELECT p1.orderID, p1.productID, p1.total_price, p1.quantity, p2.product_name, p2.image, p2.price FROM products_in_order as p1 join products as p2 ON (p1.productID = p2.productID) Where p1.orderID = '%s'" %current
        ans = self.db.fetch(query=query)
        return ans;

    def getTotalOrderPrice(self, orderID):
        current = orderID
        query = "Select total_price from orders where orders.orderID = '%s'" %current
        ans = self.db.fetch(query=query)
        return ans[-1][0];

    def approveOrder(self, orderID):
        current = orderID
        query = "Update orders set approved = '1' where orders.orderID = '%s' " %current
        self.db.commit(query=query)

    def cancelOrder(self, orderID):
        current = orderID
        query1 = "Delete from products_in_order where products_in_order.orderID = '%s'" % current
        self.db.commit(query=query1)
        query2 = "Delete From Orders where orders.orderID = '%s' " % current
        self.db.commit(query=query2)