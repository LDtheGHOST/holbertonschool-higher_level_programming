from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.agrs.get('source')
    product_id = request.agrs.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')
    
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')

    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error='Product not found')
        
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)