# Week 10: Web Scraping and Introduction to Web Development
# Introduction to Web Scraping
# What is Web Scraping?
# Web scraping is the process of extracting data from websites automatically using code. It is commonly used for
# data collection, price monitoring, research, and automation.
#
# Ethics and Legality of Web Scraping
# Before scraping a website, it is important to:
#
# Check the Terms of Service – Some websites explicitly forbid scraping.
#
# Respect robots.txt – Websites have a robots.txt file that defines which pages can or cannot be crawled.
#
# Avoid Overloading Servers – Sending too many requests in a short time can slow down or crash a website.
#
# Do Not Scrape Private or Personal Data – Always ensure you have the legal right to collect and use the data.

# Tools for Web Scraping
# 1️⃣ BeautifulSoup
# A Python library used to parse HTML and extract information easily.
#
# Installation:

# pip install beautifulsoup4 requests
# Basic Example:


import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# # Extract all links
for link in soup.find_all("a"):
    print(link.get("href"))

# 2️⃣ Requests
# A library to send HTTP requests and retrieve web pages.
#
# Example:

import requests

response = requests.get("https://example.com")
print(response.status_code)  # 200 means success
print(response.text)  # HTML content of the page

# 3️⃣ Scrapy
# A powerful web scraping framework for large-scale projects.
#
# Installation:

# pip install scrapy
# Basic Scrapy Spider:


import scrapy

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://example.com"]

    def parse(self, response):
        for link in response.css("a::attr(href)").getall():
            yield {"link": link}

# Run with:

# scrapy runspider example_spider.py
# Extracting Data
# Parsing HTML
# Web scraping requires understanding HTML structure.
# Example: Extracting data from an HTML page:

# <div class="product">
#     <h2>Product Name</h2>
#     <span class="price">$100</span>
# </div>
# Scraping the product name and price:

soup = BeautifulSoup(html_content, "html.parser")

product_name = soup.find("h2").text
price = soup.find("span", class_="price").text

print(f"Product: {product_name}, Price: {price}")

# Handling Dynamic Content
# Some websites use JavaScript to load content dynamically.
# For these cases, use Selenium:
#
# pip install selenium
# Example:

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
html = driver.page_source
driver.quit()

# Introduction to Web Development
# Basics of HTML
# HTML (HyperText Markup Language) structures web pages.

# Example:

# <!DOCTYPE html>
# <html>
# <head>
#     <title>My First Web Page</title>
# </head>
# <body>
#     <h1>Welcome to Web Development</h1>
#     <p>This is an introductory lesson.</p>
# </body>
# </html>

# Basics of CSS
# CSS (Cascading Style Sheets) styles web pages.
#
# Example:

# h1 {
#     color: blue;
#     font-size: 24px;
# }

# Applying CSS to HTML:
# <head>
#     <style>
#         body { background-color: lightgrey; }
#         h1 { color: blue; }
#     </style>
# </head>


# Practice Questions
# What are the ethical considerations of web scraping?
#
# Write a Python script to extract all headings (h1, h2, h3) from a webpage.
#
# Explain the difference between BeautifulSoup and Scrapy.
#
# Create a simple HTML page with a heading and a paragraph.
#
# Apply CSS to change the background color of a webpage.
#


# _____________HTML AND CSS________________________

# 1️⃣ Introduction to Web Development
# How the Web Works
# Whenever you visit a website (e.g., www.google.com), your web browser (Chrome, Firefox, etc.)
# sends a request to a server. The server then responds with an HTML page, which is displayed on your browser.
# IP ADDRESSES

# 💡 Think of a website as a building:
#
# HTML is the structure (walls, doors, and windows).
#
# CSS is the design (paint, colors, decorations).
#
# JavaScript (which we won’t cover in this lesson) makes it interactive (like doors that open automatically).
#
# 2️⃣ Understanding HTML (HyperText Markup Language)
# HTML is the foundation of every website. It provides the structure of a web page using elements enclosed in <tags>.
#
# Basic Structure of an HTML Page

# <!DOCTYPE html>
# <html>
# <head>
#     <title>My First Web Page</title>
# </head>
# <body>
#     <h1>Welcome to Web Development</h1>
#     <p>This is an introduction to HTML.</p>
# </body>
# </html>


# Breaking It Down:
# <!DOCTYPE html> → Declares that this is an HTML5 document.
#
# <html> → The root of the document.
#
# <head> → Contains metadata (title, styles, etc.).
#
# <title> → Sets the title of the page (seen on the browser tab).
#
# <body> → Contains all the visible content.
#
# <h1> → A heading.
#
# <p> → A paragraph.

# Common HTML Elements
# Element	Description	Example
# <h1> - <h6>	Headings	<h1>Biggest Heading</h1>
# <p>	Paragraph	<p>This is a paragraph.</p>
# <a>	Links	<a href="https://google.com">Google</a>
# <img>	Images	<img src="image.jpg" alt="My Image">
# <ul> & <li>	Unordered list	<ul><li>Item 1</li></ul>
# <ol> & <li>	Ordered list	<ol><li>Item 1</li></ol>
# <table>	Tables	<table><tr><td>Cell</td></tr></table>
# <input>	Forms (input field)	<input type="text">

# 3️⃣ Introduction to CSS (Cascading Style Sheets)
# CSS is used to style HTML pages. It controls colors, fonts, spacing, and layout.

# How to Use CSS
# CSS can be applied in three ways: 1️⃣ Inline CSS (inside HTML elements)

# html
# Copy
# Edit
# <p style="color: blue;">This text is blue.</p>
# 2️⃣ Internal CSS (inside <style> in the head section)
#
# html
# Copy
# Edit
# <head>
#     <style>
#         p { color: green; }
#     </style>
# </head>
# 3️⃣ External CSS (separate CSS file, recommended)
# style.css
#
# css
# Copy
# Edit
# p {
#     color: red;
#     font-size: 18px;
# }
# Linking it in HTML:
#
# html
# Copy
# Edit
# <head>
#     <link rel="stylesheet" href="style.css">
# </head>
# Common CSS Properties
# Property	Description	Example
# color	Text color	color: blue;
# background-color	Background color	background-color: yellow;
# font-size	Text size	font-size: 20px;
# text-align	Text alignment	text-align: center;
# margin	Space outside an element	margin: 10px;
# padding	Space inside an element	padding: 10px;
# border	Adds a border	border: 1px solid black;


# <!DOCTYPE html>
# <html>
# <head>
#     <style>
#         body {
#             background-color: lightgray;
#             font-family: Arial, sans-serif;
#         }
#         h1 {
#             color: blue;
#             text-align: center;
#         }
#         p {
#             color: black;
#             font-size: 18px;
#         }
#     </style>
# </head>
# <body>
#     <h1>My Styled Page</h1>
#     <p>This page is styled with CSS.</p>
# </body>
# </html>
