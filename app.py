from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from process_data import Crypto
# from forms import AddForm


app = Flask(__name__)

app.config['SECRET_KEY']='a46666e55ba726609e4265d39b5edef1'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Money,Wallet


crypto = Crypto()




@app.route('/', methods=['GET'])

def accueil():


    results=crypto.get_crypto()
  

    return render_template('accueil.html', **locals())


@app.route('/add', methods=['GET','POST'])

def add():

    if request.method =='POST':
        crypto_name =request.form['crypto_name']
        crypto_quantity =request.form['crypto_quantity']
        crypto_price_total =request.form['crypto_price_total']
        crypto_price =request.form['crypto_price']

        # my_data = Money(crypto_name,crypto_quantity,crypto_price_total,crypto_price)
        # db.session.add(my_data)
        # db.session.commit()
        
        
        flash('Achat effectué')
        return redirect(url_for('accueil'))
    else:
      return render_template('add.html')
    

        # if db.session.query(Wallet).filter(Wallet.crypto_name == crypto_name).count()==0:
        #     data = Wallet(crypto_name, crypto_quantity, crypto_price_total)
        #     db.session.add(data)
        #     db.session.commit()
        #     return render_template('accueil.html',message='Votre achat à était effectué')
        
    
@app.route('/delete', methods=('GET', 'POST'))

def delete():  
    return render_template('delete.html') 


if __name__ == '__main__':
    app.run(debug = True)
