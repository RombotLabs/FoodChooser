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
    return render_template("index.html")

@app.route('/meals_db', methods=['GET', 'POST'])
def meals_db():
    """The meals database page."""
    return render_template("meals_db.html", breakfast=breakfast, breakfast_special=breakfast_special,
                           lunch=lunch, lunch_special=lunch_special,
                           noon=noon, noon_special=noon_special,
                           dinner=dinner, dinner_special=dinner_special)

@app.route('/add_meal', methods=['POST'])
def add_meal():
    """The function for adding a meal to the database."""
    meal_type = request.form.get('meal_type')
    meal_name = request.form.get('meal_name')
    
    if meal_type == 'breakfast':
        breakfast.append(meal_name)
    elif meal_type == 'breakfast_special':
        breakfast_special.append(meal_name)
    elif meal_type == 'lunch':
        lunch.append(meal_name)
    elif meal_type == 'lunch_special':
        lunch_special.append(meal_name)
    elif meal_type == 'noon':
        noon.append(meal_name)
    elif meal_type == 'noon_special':
        noon_special.append(meal_name)
    elif meal_type == 'dinner':
        dinner.append(meal_name)
    elif meal_type == 'dinner_special':
        dinner_special.append(meal_name)

    return redirect('/meals_db')

@app.route('/random_meal', methods=['POST'])
def random_meal():
    """Random meal generator."""
    pass

if __name__ == "__main__":
    app.run(debug=True)
