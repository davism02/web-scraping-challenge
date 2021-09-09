from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
mongo = PyMongo(app)

mars_db = mongo.db.mars

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/phone_app")


@app.route("/")
def index():
    mars_dict = mars_db.find_one()
    return render_template("index.html", mars=mars_dict)


@app.route("/scrape")
def scrape():
    mars_dict = scrape_mars.scrape_all()
    mars_db.update({}, mars_dict, upsert=True)
    return redirect('/')
    
  
if __name__ == "__main__":
    app.run(debug=True)
