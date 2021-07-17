from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods=['GET'])
def main_page():
    return "<h1>sanity test</h1><p> checked </p>"

@app.route('/products', methods=['GET'])
def products_page():
    return "<h1>ZDENCINA NABIDKA</h1><p> produkt 1 </p>"


if __name__ == '__main__':
    app.run(debug=True)
