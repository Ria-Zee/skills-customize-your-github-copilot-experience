"""
Starter code for Web Scraping & HTTP Requests

This file contains the basic structure to get started with the assignment.
Add your implementation below each function definition.
"""

import requests
from bs4 import BeautifulSoup
import time
import csv

# Task 1: Making HTTP Requests
def fetch_webpage(url):
    """
    Fetch a webpage and examine the response
    
    Args:
        url (str): The URL to fetch
        
    Returns:
        requests.Response: The response object
    """
    # TODO: Make an HTTP GET request to the URL
    # TODO: Check the status code
    # TODO: Print the headers
    # TODO: Return the response
    pass

def examine_response(response):
    """
    Examine the HTTP response
    
    Args:
        response (requests.Response): The response object
    """
    # TODO: Print the status code
    # TODO: Print key headers (Content-Type, Content-Length, Server)
    # TODO: Print the first 500 characters of content
    pass

# Task 2: Parsing HTML and Extracting Data
def parse_html(html_content):
    """
    Parse HTML content using BeautifulSoup
    
    Args:
        html_content (str): The HTML content to parse
        
    Returns:
        BeautifulSoup: The parsed HTML object
    """
    # TODO: Create a BeautifulSoup object from the HTML content
    # TODO: Return the parsed object
    pass

def extract_data(soup, selector):
    """
    Extract data from parsed HTML using CSS selectors
    
    Args:
        soup (BeautifulSoup): The parsed HTML object
        selector (str): CSS selector for elements to extract
        
    Returns:
        list: List of extracted data
    """
    # TODO: Use the selector to find elements
    # TODO: Extract text from each element
    # TODO: Return the list of extracted data
    pass

# Task 3: Building a Complete Web Scraper
def scrape_website(url, selectors, output_file="scraped_data.csv"):
    """
    Scrape a website and save data to a CSV file
    
    Args:
        url (str): The URL to scrape
        selectors (dict): Dictionary of {field_name: css_selector}
        output_file (str): Output CSV filename
    """
    try:
        # TODO: Fetch the webpage
        # TODO: Parse the HTML
        # TODO: Extract data using the provided selectors
        # TODO: Save the data to a CSV file
        # TODO: Print a summary of scraped data
        pass
    except requests.RequestException as e:
        # TODO: Handle network errors
        print(f"Error fetching {url}: {e}")
    except Exception as e:
        # TODO: Handle parsing errors
        print(f"Error parsing data: {e}")

def add_delay(seconds=1):
    """
    Add a delay between requests to be respectful to servers
    
    Args:
        seconds (int): Number of seconds to wait
    """
    # TODO: Implement a respectful delay
    time.sleep(seconds)

if __name__ == "__main__":
    # Example usage
    # TODO: Modify these with a real website and selectors
    
    # example_url = "https://example.com"
    # example_selectors = {
    #     "title": "h1",
    #     "links": "a",
    #     "paragraphs": "p"
    # }
    
    # scrape_website(example_url, example_selectors)
    pass
