"""
Prompt: Write a Python function to retrieve HTML from a web page, remove the HTML tags and display the text.
"""

import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    # Fetch the HTML content from the web page
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the text from the parsed HTML
    text = soup.get_text()

    # Display the extracted text
    print(text)

# Example usage
url = 'https://www.example.com'
get_text_from_url(url)
