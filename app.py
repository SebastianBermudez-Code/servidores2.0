from flask import Flask, url_for, render_template, request, redirect
import db

servidor2 = Flask(__name__)

@servidor2.route('/inicio')
def home():
    return render_template('index.html')

@servidor2.route('/productos', methods=('GET', 'POST'))
def products():
    if request.method == 'POST':
        if 'product_id' in request.form:
            # Update product
            product_id = request.form['product_id']
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            image = request.form['image']
            db.update_product(product_id, name, description, price, image)
        else:
            # Add product
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            image = request.form['image']
            db.add_product(name, description, price, image)
        return redirect(url_for('products'))
    
    products = db.get_all_products()
    return render_template('productos.html', products=products)

@servidor2.route('/delete_product/<int:product_id>', methods=('POST',))
def delete_product(product_id):
    db.delete_product(product_id)
    return redirect(url_for('products'))

if __name__ == '__main__':
    db.init_db()
    servidor2.run(debug=True)