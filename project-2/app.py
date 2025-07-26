from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

MONGO_URI = os.environ.get("MONGO_URI")
MONGO_DB = os.environ.get("MONGO_DB", "mydb")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "users")

try:
    client = MongoClient(MONGO_URI)

    client.admin.command('ping')
    print("Successfully connected to MongoDB Atlas!")
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
except Exception as e:
    print(f"MongoDB connection error: {e}")
    client = None
    db = None
    collection = None

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if collection is None:
            flash("Database connection failed. Please check your MongoDB Atlas configuration.")
            return render_template('form.html')
        
        name = request.form.get('name')
        try:
            collection.insert_one({'name': name})
            return redirect(url_for('success'))
        except Exception as e:
            flash(f"Error: {e}")
            return render_template('form.html')
    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True) 