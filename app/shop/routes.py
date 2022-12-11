from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import Items, Cart
from .forms import AddToCart
from json

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
    product = Items.query.get(id) 
    cart = Cart.query.get(current_user.id)
    if product:
        if cart:
            cart_item = json.loads(cart.item)
            # If there is a cart
            del cart_item[name]
            cart.item = json.dumps(cart_item)
            cart.update_db()
            pass
        else:
            # if not cart, return no cart (backdoor)
            return redirect(url_for('cart.create_cart'))
            pass
    else:
        flash('That product was not found')
        return redirect(url_for('shop.view_shop'))

@shop.route('/shop/cart/add', methods =['GET','POST'])
@login_required
def add_to_cart(id):
    product = Items.query.get(id)
    cart = Cart.query.get(current_user.id)
    if product:
        if cart:
            form=AddToCart()
            if request.method =="POST":
                if form.validate():
                    first_item = form.name.data
                    current_list = json.loads(Cart.items)

            # If there is a cart 
            pass 
        else:
            # if not create, create dict
            pass
    else:
        flash('That product was not found')
        return redirect(url_for('shop.view_shop'))
        
    
@shop.route('/shop/cart/')
def view_cart():
    products = Items.query.all() # Fetch all items
    # Create a DICT to itterate through in Jinja
        
    return render_template('checkout.html', products=products)
    
