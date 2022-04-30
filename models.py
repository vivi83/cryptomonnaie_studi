
from app import db
from datetime import datetime

class Money(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)
    crypto_name=db.Column(db.String(50), nullable=False)
    crypto_quantity=db.Column(db.String(20), nullable=False)
    crypto_price=db.Column(db.String(20), nullable=False)
    crypto_price_total=db.Column(db.String(50), nullable=False)
    date_purchase=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f"Money('{self.crypto_name}','{self.crypto_quantity}','{self.crypto_price}','{self.crypto_price_total}','{self.date_purchase}')"


class Wallet(db.Model):
    
    id=db.Column(db.Integer, primary_key=True)
    crypto_price_total=db.Column(db.String(50), nullable=False)
    date_purchase=db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f"Wallet('{self.crypto_price_total}','{self.date_purchase}')"   

