"""
Prompt: Refine the code so it doesn't use any third-party libraries
"""

import urllib.request
import re

def get_text_from_url(url):
    # Fetch the HTML content from the web page
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')

    # Remove HTML tags using a regular expression
    text = re.sub(r'<[^>]+>', '', html)

    # Display the extracted text
    print(text)

# Example usage
url = 'https://www.example.com'
get_text_from_url(url)
