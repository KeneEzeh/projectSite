from project import db, app, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text,unique = True, nullable= False)
    password = db.Column(db.String(20), nullable= False)
    name = db.Column(db.String(20), nullable= False)
    address = db.Column(db.Text, nullable= False)
    product_id = db.relationship('Products', backref = 'author', lazy='joined')

    def __repr__ (self):
        return f"Users('self.email')"

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable= False, unique =False)
    price = db.Column(db.Integer, nullable =False)
    description = db.Column(db.Text, nullable =True)
    image = db.Column(db.Text, default= "default.png")
    stock = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    cat_id = db.relationship('Categories', backref= 'goods', lazy='joined')


    def __repr__ (self):
        return f"Products('self.name')"

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    product_id = db.Column(db.Integer,db.ForeignKey('products.id'))

    def __repr__ (self):
        return f"Categories('self.name')"