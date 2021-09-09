# Dependencies
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup 
import pandas as pd
import datetime as dt


def scrape_all():
    # Import Splinter and set the chrome drive path
    from webdriver_manager.chrome import ChromeDriverManager
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
# save url and visit the page
    url = 'https://www.redplanetscience.com'
    browser.visit(url)

    # create Beautifulsoup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # retrieve news title and article
    slide_elem = soup.select_one('div.list_text')
    news_title = slide_elem.find('div', class_='content_title')
    news_p = slide_elem.find('div', class_='article_teaser_body')

    # save featured image
    url = 'https://spaceimages-mars.com/'
    browser.visit(url)
    # use splinter to click featured image
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('img', class_='fancybox-image')
    featured_image_url = url + featured_image_url.get("src")

    # save the mars facts url and visit the page
    url_table = "https://galaxyfacts-mars.com"
    #browser.visit(url_table)
    table = pd.read_html(url_table)[1]
    table.columns = ["Description", "Value"]
    # put table in html format

    table_html_format = table.to_html(classes='table table-striped')

    # Mars Hemispheres
    #browser = Browser('chrome', **executable_path, headless=True)
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)

    html_hemispheres = browser.html
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    items = soup.find_all('div', class_='item')
    hemisphere_image_urls = []

    hemispheres_main_url = 'https://marshemispheres.com/'

    for item in items:
        title = item.find('h3').text
        image_url = item.find('a', class_='itemLink product-item')['href']
        browser.visit(hemispheres_main_url + image_url)
        image_html = browser.html
        soup = BeautifulSoup(image_html, 'html.parser')
        image_url = hemispheres_main_url + \
        soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"Title": title, "Image_URL": image_url})

    mars_dict = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "fact_table": str(table_html_format),
        "hemisphere_images": hemisphere_image_urls
    }
    return mars_dict
