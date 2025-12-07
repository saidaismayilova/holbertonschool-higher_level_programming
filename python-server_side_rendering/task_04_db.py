from flask import Flask, render_template, request
import json, csv
import sqlite3

app = Flask(__name__)

def read_json(file_path="products.json"):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv(file_path="products.csv"):
    try:
        data = []
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                data.append(row)
        return data
    except FileNotFoundError:
        return []

def read_sqlite(db_path="products.db"):
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
    except sqlite3.Error:
        return []

@app.route("/products")
def show_products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    elif source == "sql":
        data = read_sqlite()
    else:
        return render_template("product_display.html", products=[], error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p["id"] == product_id]
            if not data:
                return render_template("product_display.html", products=[], error="Product not found")
        except ValueError:
            return render_template("product_display.html", products=[], error="Invalid ID")

    return render_template("product_display.html", products=data, error=None)

if __name__ == "__main__":
    app.run(debug=True)
