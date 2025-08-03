import csv
import os
from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'secret'

db_filepath = os.getenv('PATH')

breakfast = []
breakfast_special = []
lunch = []
lunch_special = []
noon = []
noon_special = []
dinner = []
dinner_special = []



@app.route('/')
def index():
    """The start page"""
    return "index.html"

if __name__ == "__main__":
    app.run(debug=True)
