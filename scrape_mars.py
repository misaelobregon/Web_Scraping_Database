import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def news_scrape():
    browser=init_browser()
    url_news="https://mars.nasa.gov/news"
    browser.visit(url_news)
    time.sleep(1)
    html=browser.html
    soup=BeautifulSoup(html, "html.parser")
    article_list=[]
    
    headline=soup.find_all("li", class_="slide")
    news_title=headline[0].find('h3').text
    news_p=headline[0].a.text
    news_results={"headline":news_title, "text":news_p}
    # Close the browser after scraping
    browser.quit()
    return news_results

headline=news_scrape()

headline

def image_scrape():
    browser=init_browser()
    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    time.sleep(1)
    html=browser.html
    soup=BeautifulSoup(html, "html.parser")

    results=soup.find_all("article", class_="carousel_item")
    image_url=results[0].find("a")["data-fancybox-href"]
    # Assigning url string; variable called featured_image_url
    featured_image_url="https://www.jpl.nasa.gov"+ image_url
    # Close the browser after scraping
    browser.quit()
    return featured_image_url

image=image_scrape()

image

def tweet_scrape():
    browser=init_browser()
    url="https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(1)
    html=browser.html
    soup=BeautifulSoup(html, "html.parser")
   
    results=soup.find_all(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather=results[0].text
    # Close the browser after scraping
    browser.quit()
    return mars_weather

tweet=tweet_scrape()

tweet

def table_scrape():
    browser=init_browser()
    url="https://space-facts.com/mars/"
    browser.visit(url)
    time.sleep(1)
    html=browser.html
    soup=BeautifulSoup(html, "html.parser")

    results=soup.find_all("table", class_="tablepress tablepress-id-p-mars")
    result=str(results[0])
    with open("mars_table_facts.html", "w") as file:
        file.write(result)
    #Close the browser after scraping
    browser.quit()
    return result

mars_facts=table_scrape()

mars_facts

def hemisphere_img_scrape():
    browser = init_browser()
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    time.sleep(1)
    html=browser.html
    soup=BeautifulSoup(html, "html.parser")
    results=soup.find_all("h3")
    hemisphere_image_urls=[]
    
    # Create a sub-scrape function for hi-res images
    for result in results:
        img_title=result.text
        url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        time.sleep(1)
        
        browser.click_link_by_partial_text(img_title)
        html=browser.html
        soup=BeautifulSoup(html, "html.parser")
        
        img_link=soup.find("img", class_="wide-image")
        # html root route and image link
        img_url="https://astrogeology.usgs.gov" + img_link["src"]
        img_dict={"img_title":img_title,"img_url":img_url}
        hemisphere_image_urls.append(img_dict)
        
    #Close the browser after scraping
    browser.quit()
    return hemisphere_image_urls

hem_img=hemisphere_img_scrape()

hem_img
