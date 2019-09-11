# Web_Scraping Database

In this project, information from three websites were scraped using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter. 
A file called mission_to_mars.ipnynb in Jypyter Notebook where all scraping and analysis is done on collection data on latest news, images, weather tweets, and facts.

![]Images/headline

•	NASA Mars news website (headline title and paragraph text)	
•	Feature image (full size .jpg image) from JPL Mars Space Images website
•	Mars Weather tweet (via twitter account) 
•	Mars Facts containig facts about planet Mars (Pandas used to convert the data to a HTML table string.
•	Mars Hemispheres via the USGS Astrogeology site obtaining high resolution images for each of Mar's hemispheres (4). A dictionary of hi resolution mage url strings is created. 

# MongoDB and Flask Application
The scraped data is stored using MongoDB via a Flask app and data is displayed in a new HTML page. 
First the Jupyter notebook is converted into a Python script called scrape_mars.py. A funciton called scrape executes all scraping code and returns one Python dictionalry contating all of the scraped data.

![](images/scrape_mars.py code

Next, a Flask app called app.py with a route called /scrape is created that imports the scrape_mars.py script and calls the scrape function.

![](images/app.py_flask1

In the Flask app a root route / is created to query the Mongo database and pass the mars data into an HTML template to display the data.

![](images/app.py_flask_app_route

The HTML template called index.html is created that takes the mars data dictionary and displays all of the data in the appropriate HTML elements. 

![](images/html_code

Images of webpage are below:

![](images/scraped_page1

![](images/HiRes_images
