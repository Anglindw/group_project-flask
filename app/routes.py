from app import app
from flask import redirect, render_template, url_for, flash
from flask_login import current_user, login_required
from app.models import Cart
import json

@app.route('/')
@app.route('/home')
def home():
    if current_user.is_authenticated:
        cart = Cart.query.get(current_user.id)
        if cart:
            full_cart = json.loads(cart.items)
            total_items = 0
            for key in full_cart.items():
                total_items += 1
            
            return render_template('index.html', items=total_items)
        else:
            return render_template('index.html', items=0)
    else:
        return render_template('index.html')