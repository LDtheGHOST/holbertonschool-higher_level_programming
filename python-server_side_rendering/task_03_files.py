from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    with open('products.json') as file:
        data = json.load(file)
    return data

def read_csv_file():
    products = []
    with open('products.csv') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source == 'json':
        products = read_json_file()
    elif source == 'csv':
        products = read_csv_file()
    else:
        return render_template('product_display.html', error="Wrong source specified.")

    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found.")
    
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)