from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template('main_page.html')

@app.route('/products', methods=['GET'])
def products_page():
    return render_template('products_page.html')

@app.route('/order', methods=['GET','POST'])
def order_page():
    if request.method == 'GET':
        return render_template('order_page.html')
    elif request.method == 'POST':
        number_of_product=request.form["product_number"]
        quantity = request.form["quantity"]
        email = request.form["email"]
        with open ("orders.txt","a") as orders_file:
            orders_file.write(f"{email} si objednava {quantity}x produkt číslo: {number_of_product}\n")

        return render_template("order_finished_page.html")

if __name__ == '__main__':
    app.run(debug=True)
