from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def read_csv_file(filepath):
    products = []
    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price'] = float(row['price'])  # Ensure price is a float
            products.append(row)
    return products

@app.route('/products')
def show_products():
    source = request.args.get('source', 'json')
    product_id = request.args.get('id')
    products = []
    error_message = None

    if source not in ['json', 'csv']:
        error_message = "Wrong source"
    else:
        if source == 'json':
            products = read_json_file('products.json')
        elif source == 'csv':
            products = read_csv_file('products.csv')

        if product_id:
            filtered_products = [product for product in products if str(product['id']) == product_id]
            if not filtered_products:
                error_message = "Product not found"
            else:
                products = filtered_products

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)