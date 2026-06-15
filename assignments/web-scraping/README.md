# 📘 Assignment: Web Scraping & HTTP Requests

## 🎯 Objective

Learn how to fetch and parse real-world web data using Python. You will make HTTP requests, handle responses, parse HTML content, and extract meaningful information from websites.

## 📝 Tasks

### 🛠️ Making HTTP Requests

#### Description
Write code to fetch web pages using HTTP requests and examine the response data.

#### Requirements
Completed program should:

- Use the `requests` library to fetch content from a public website
- Handle HTTP status codes appropriately
- Extract and display the HTTP headers
- Print a sample of the response content (first 500 characters)

### 🛠️ Parsing HTML and Extracting Data

#### Description
Parse HTML content and extract specific data elements from a webpage.

#### Requirements
Completed program should:

- Use `BeautifulSoup` to parse HTML structure
- Locate and extract specific elements (e.g., titles, links, paragraphs)
- Store extracted data in a structured format (list or dictionary)
- Print the extracted data in a readable format

### 🛠️ Building a Web Scraper

#### Description
Create a complete web scraper that collects multiple data points from a website and handles errors gracefully.

#### Requirements
Completed program should:

- Scrape at least 5 data items from a website
- Implement error handling for network issues and missing elements
- Respect rate limiting (add delays between requests)
- Save the collected data to a CSV file
- Display a summary of scraped data
