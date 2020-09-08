from code_delivery.ext.db import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    email = db.Column("email", db.Unicode, unique=True)
    password = db.Column("password", db.Unicode)

class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column("id", db.Integer, primary_key=True)
    zip_code = db.Column("zip_code", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)

class Partner(db.Model):
    __tablename__ = "partners"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    email = db.Column("email", db.Unicode, unique=True)
    password = db.Column("password", db.Unicode)
    zip_code = db.Column("zip_code", db.Unicode)
    address = db.Column("address", db.Unicode)
    category_id = db.Column("category_id", db.Integer, db.ForeignKey("categories.id"))
    is_open = db.Column("is_open", db.Boolean)

class Driver(db.Model):
    __tablename__ = "drivers"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    email = db.Column("email", db.Unicode, unique=True)
    password = db.Column("password", db.Unicode)
    is_available = db.Column("is_available", db.Boolean)

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    image = db.Column("image", db.Unicode)
    price = db.Column("price", db.Numeric)
    partner_id = db.Column("partner_id", db.Integer, db.ForeignKey("partners.id"))
    available = db.Column("is_available", db.Boolean)

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    is_completed = db.Column("is_completed", db.Boolean)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
    partner_id = db.Column("partner_id", db.Integer, db.ForeignKey("partners.id"))

class OrderItem(db.Model):
    __tablename__ = "order_items"
    id = db.Column("id", db.Integer, primary_key=True)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("orders.id"))
    item_id = db.Column("item_id", db.Integer, db.ForeignKey("items.id"))
    quantity = db.Column("quantity", db.Numeric)

class Checkout(db.Model):
    __tablename__ = "checkouts"
    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Unicode)
    total = db.Column("total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    is_completed = db.Column("is_completed", db.Boolean)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("orders.id"))

class Delivery(db.Model):
    __tablename__ = "deliveries"
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    is_completed = db.Column("is_completed", db.Boolean)
    driver_id = db.Column("driver_id", db.Integer, db.ForeignKey("drivers.id"))
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("users.id"))
    partner_id = db.Column("partner_id", db.Integer, db.ForeignKey("partners.id"))
    address_id = db.Column("address_id", db.Integer, db.ForeignKey("addresses.id"))
