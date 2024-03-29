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
    mars_data=mongo.db.scraped_mars.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/scrape")
def scrape():
    
    # Run the scrape function
    mars_data=mongo.db.scraped_mars
    
    headlines=scrape_mars.news_scrape()
    images=scrape_mars.image_scrape()          
    tweets=scrape_mars.tweet_scrape()
    facts=scrape_mars.table_scrape()
    hemispheres=scrape_mars.hemisphere_img_scrape()
    update_data={"headlines":headlines,"images":images,"tweets":tweets,"facts":facts,"hemispheres":hemispheres}

    mars_data.update({}, update_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run()
