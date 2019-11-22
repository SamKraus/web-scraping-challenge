
# Dependencies and Setup
from flask import Flask, render_template
import pymongo
import Scrape_mar
import sys


# Flask Setup
app = Flask(__name__)


# PyMongo Connection Setup
client = pymongo.MongoClient()


db = client.marsdb
facts = db.facts



# Root Route to Query MongoDB & Pass Mars Data Into HTML Template: index.html to Display Data
@app.route("/")
def index():
    
    mars = list(db.facts.find())
    print(mars)
    return render_template("index.html", mars = mars)

# Scrape Route to Import `Scrape_mar.py` Script & Call `scrape` Function
@app.route("/scrape")
def scrape():
    
    mars = Scrape_mar.scrape()
    print("\n\n\n")
    
    db.facts.insert_one(mars)
    return "Some scrapped data"

# Define Main Behavior
if __name__ == "__main__":
    app.run()