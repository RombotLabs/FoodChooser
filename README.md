# FoodChooser
A web application for randomized cooking ideas.

## Installing (Linux recommended)
- Install Python 3
```
sudo apt-get update
sudo apt-get install python3
```
- Creating and activating the virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
- Install the modules
```
pip install -r requirements.txt
```
- Launch the software
```
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

© Copyrights 2025 by Mafixdeveloping
