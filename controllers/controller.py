from flask import render_template
from app import app
from models.order_list import orders

@app.route('/')
def show_order_names():
    return render_template("index.html", order_list = orders)


@app.route('/order/<index>')
def show_order_details(index):
    return render_template("order.html", order_list = orders[int(index)])

