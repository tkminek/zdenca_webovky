from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return render_template('main_page.html')

@app.route('/products', methods=['GET'])
def products_page():
    return render_template('products_page.html')

@app.route('/contact', methods=['GET'])
def contact_page():
    return render_template('contact_page.html')

if __name__ == '__main__':
    app.run(debug=True)
