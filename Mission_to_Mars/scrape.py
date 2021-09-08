# Dependencies
# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict ={}

    