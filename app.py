from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app=Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"]="mongodb://localhost:27017/mission_to_mars"
mongo=PyMongo(app)

# Or set inline
# mongo=PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

@app.route("/")
def index():
    scraped_miss_mars=mongo.db.scraped_mars.find_one()
    return render_template("index.html", scraped_miss_mars=scraped_miss_mars)

@app.route("/scrape")
def scraper():
    scraped_miss_mars=mongo.db.scraped_miss_mars
    
    headlines=scrape_mars.news_scrape()
    images=scrape_mars.image_scrape()          
    tweets=scrape_mars.tweet_scrape()
    facts=scrape_mars.table_scrape()
    hemispheres=scrape_mars.hemisphere_img_scrape()
    updates={"headlines":headlines,"images":images,"tweets":tweets,"facts":facts,"hemispheres":hemispheres}

    scraped_miss_mars.update({}, updates, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
