"""Module imports for the website."""
import csv
import os
import random
from dotenv import load_dotenv # pylint: disable=import-error
from flask import Flask, render_template, redirect, request, session # pylint: disable=import-error


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('KEY')


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

# if not os.path.exists(db_filepath):
    # with open(db_filepath, mode='w', newline='', encoding='utf-8') as csvfile:
        # writer = csv.writer(csvfile)

def randomize(meal_list):
    """Randomize the meal list and store the result."""
    randomized_result.clear()  # Clear previous results
    if meal_list:
        randomized_result.extend(random.sample(meal_list, min(3, len(meal_list))))
    else:
        randomized_result.append("No meals available")


def save_to_csv():
    """Save the meal lists to a CSV file."""
    with open('db.csv', mode='w', newline='', encoding='utf-8') as csvfile_write:
        writer = csv.writer(csvfile_write)
        writer.writerow(['breakfast'] + breakfast)
        writer.writerow(['breakfast_special'] + breakfast_special)
        writer.writerow(['lunch'] + lunch)
        writer.writerow(['lunch_special'] + lunch_special)
        writer.writerow(['noon'] + noon)
        writer.writerow(['noon_special'] + noon_special)
        writer.writerow(['dinner'] + dinner)
        writer.writerow(['dinner_special'] + dinner_special)

try:
    with open("db.csv", mode='r', newline='', encoding='utf-8') as csvfile_read:
        reader = csv.reader(csvfile_read)
        for row in reader:
            if row[0] == 'breakfast':
                breakfast = row[1:]
            elif row[0] == 'breakfast_special':
                breakfast_special = row[1:]
            elif row[0] == 'lunch':
                lunch = row[1:]
            elif row[0] == 'lunch_special':
                lunch_special = row[1:]
            elif row[0] == 'noon':
                noon = row[1:]
            elif row[0] == 'noon_special':
                noon_special = row[1:]
            elif row[0] == 'dinner':
                dinner = row[1:]
            elif row[0] == 'dinner_special':
                dinner_special = row[1:]
except IndexError:
    save_to_csv()  # Create the CSV file if it doesn't exist

@app.route('/')
def index():
    """The start page"""
    return render_template("index.html")

@app.route('/meals_db', methods=['GET', 'POST'])
def meals_db():
    """The meals database page."""
    save_to_csv()  # Save the current state of the meal lists to CSV
    return render_template("meals_db.html",
                           breakfast=breakfast, breakfast_special=breakfast_special,
                           lunch=lunch, lunch_special=lunch_special,
                           noon=noon, noon_special=noon_special,
                           dinner=dinner, dinner_special=dinner_special,
                           selected_meal_type=session.get("last_meal_type"))

@app.route('/add_meal', methods=['GET', 'POST'])
def add_meal():
    """The function for adding a meal to the database."""
    meal_type = request.form.get('meal_type')
    meal_name = request.form.get('meal_name')
    session["last_meal_type"] = meal_type
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
    save_to_csv()  # Save the updated meal lists to CSV
    return redirect('/meals_db')

@app.route('/delete_meal', methods=['POST'])
def delete_meal():
    """The function for deleting a meal from the database."""
    meal_name = request.form.get('meal_name')
    for meal_list in [breakfast, breakfast_special,
                      lunch, lunch_special,
                      noon, noon_special,
                      dinner, dinner_special]:
        if meal_name in meal_list:
            meal_list.remove(meal_name)
            break
    save_to_csv()  # Save the updated meal lists to CSV
    return redirect('/meals_db')

@app.route('/random_meal', methods=['GET', 'POST'])
def random_meal():
    """Random meal generator."""
    return render_template("random_meal.html",
                           randomized_result=randomized_result,
                           selected_meal_type=session.get("last_meal_type"))

@app.route('/generate_meals', methods=['GET', 'POST'])
def generate_meals():
    """Generate three random meals."""
    meal_type = request.form.get('meal_type')
    session["last_meal_type"] = meal_type
    if meal_type == 'breakfast':
        randomize(breakfast)
    elif meal_type == 'breakfast_special':
        randomize(breakfast_special)
    elif meal_type == 'lunch':
        randomize(lunch)
    elif meal_type == 'lunch_special':
        randomize(lunch_special)
    elif meal_type == 'noon':
        randomize(noon)
    elif meal_type == 'noon_special':
        randomize(noon_special)
    elif meal_type == 'dinner':
        randomize(dinner)
    elif meal_type == 'dinner_special':
        randomize(dinner_special)

    return redirect('/random_meal')

if __name__ == "__main__":
    app.run()
