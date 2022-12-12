from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import Items, Cart
import json

shop = Blueprint('shop', __name__, template_folder='shop_templates')

@shop.route('/shop')
def view_shop():
    products = Items.query.all() # Fetch all items
    # Create a DICT to itterate through in Jinja
    items = {}
    for item in products:
        items[item.id] = {}
        items[item.id]['name'] = item.item_name
        items[item.id]['icon'] = item.item_icon
        items[item.id]['description'] = item.item_description
        items[item.id]['price'] = item.item_price
        
    return render_template('shop.html', prods=items)

@shop.route('/shop/cart/removeall')
@login_required
def remove_all():
    cart = Cart.query.get(current_user.id)
    if cart:
        cart.delete_from_db()
        return redirect(url_for('shop.view_shop'))
    else:
        return redirect(url_for('shop.view_cart'))

@shop.route('/shop/view/<int:id>')
def view_product(id):
    product = Items.query.get(id)
    if product:
        return render_template('product.html', name=product.item_name, icon=product.item_icon, description=product.item_description, price=product.item_price, id=product.id)
    else:
        flash('That product was not found')
        return redirect(url_for('shop.view_shop'))
    
@shop.route('/shop/cart/remove/<int:id>')
@login_required
def remove_from_cart(id):
    cart = Cart.query.get(current_user.id)
    if cart:
        cart_data = json.loads(cart.items)
        del cart_data[str(id)]
        cart.items = json.dumps(cart_data)
        cart.update_db()
        return redirect(url_for('shop.view_cart'))
    else:
        return redirect(url_for('shop.view_shop'))

@shop.route('/shop/cart/add/<int:id>', methods =['GET','POST'])
@login_required
def add_to_cart(id):
    product = Items.query.get(id)
    cart = Cart.query.get(current_user.id)
    if product:
        if cart:
            cart_data = json.loads(cart.items)
            if str(product.id) in cart_data.keys():
                cart_data[str(product.id)]['quantity'] = cart_data[str(product.id)]['quantity'] + 1
                cart.items = json.dumps(cart_data)
                cart.update_db()
                return render_template('product.html',  name=product.item_name, icon=product.item_icon, description=product.item_description, price=product.item_price, id=product.id)
            else:
                cart_data[product.id] = {}
                cart_data[product.id]['name'] = product.item_name
                cart_data[product.id]['icon'] = product.item_icon
                cart_data[product.id]['description'] = product.item_description
                cart_data[product.id]['price'] = product.item_price
                cart_data[product.id]['quantity'] = 1
                cart.items = json.dumps(cart_data)
                cart.update_db()
                return render_template('product.html',  name=product.item_name, icon=product.item_icon, description=product.item_description, price=product.item_price, id=product.id)
        else:
            cart_data = {}
            cart_data[product.id] = {}
            cart_data[product.id]["name"] = product.item_name
            cart_data[product.id]["icon"] = product.item_icon
            cart_data[product.id]["description"] = product.item_description
            cart_data[product.id]['price'] = product.item_price
            cart_data[product.id]['quantity'] = 1
            d = Cart(current_user.id, json.dumps(cart_data))
            d.save_to_db()
            return render_template('product.html',  name=product.item_name, icon=product.item_icon, description=product.item_description, price=product.item_price, id=product.id)
    else:
        flash('That product was not found')
        return redirect(url_for('shop.view_shop'))


@shop.route('/shop/cart/', methods =['GET','POST'])
@login_required
def view_cart():
    items = Cart.query.get(current_user.id) # Fetch all items
    # Create a DICT to itterate through in Jinja
    cart = json.loads(items.items)
    if items:
        total = 0 #: Float
        items = 0 #: Int
        for key, value in cart.items():
            total += value['price']
            items += 1
            
        return render_template('Checkout.html', cart=cart, total=round(total, 2), items=items)
    else:
        return redirect(url_for('shop.view_shop'))
