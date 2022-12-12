from app import app
from flask import redirect, render_template, url_for, flash, session
from flask_login import current_user
from app.models import Cart
import json

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        cart = Cart.query.get(current_user.id)
        if cart:
            cart_data = json.loads(cart.items)
            total_items = 0
            for k in cart_data.items():
                total_items += 1
            session['items'] = total_items
        else:
            session['items'] = 0
    return render_template('index.html')