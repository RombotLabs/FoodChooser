"""Module imports for the website."""
import csv
import os
import random
from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = 'secret'
load_dotenv()

db_filepath = os.getenv('PATH')

breakfast = []
breakfast_special = []
lunch = []
lunch_special = []
noon = []
noon_special = []
dinner = []
dinner_special = []
randomized_result = []

def randomize(meal_list):
    """The function for generating the three random meals from the lists."""
    element_double = False
    result = None
    randomized_result.clear()
    for counter in range(0,2):
        result = random.choice(meal_list)
        for i in range(0,2):
            if result == randomized_result[i]:
                element_double = True
                break
        if element_double:
            continue
        else:
            randomized_result.append(result)

@app.route('/')
def index():
    """The start page"""
    return "index.html"

if __name__ == "__main__":
    app.run(debug=True)
