import os
from bs4 import BeautifulSoup

def scrape_html(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"No file exists with the name: {file_path}")
        return

    # Open and read the content of the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract and print the title
    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else "No title found"
    print(f"Title: {title}\n")

    # Extract and print the navigation list
    navlist = soup.find('ul', class_='navlist')
    if navlist:
        nav_items = [li.get_text(strip=True) for li in navlist.find_all('li')]
        print("Navigation List Items:")
        for item in nav_items:
            print(f" - {item}")
    else:
        print("No navigation list found.\n")

    # Extract and print the paragraphs
    paragraphs = soup.find_all('p')
    if paragraphs:
        print("\nParagraphs Found:")
        for i, paragraph in enumerate(paragraphs, 1):
            print(f"Paragraph {i}: {paragraph.get_text(strip=True)}")
    else:
        print("No paragraphs found.")

# Example usage:
file_path = "index.html"  # Replace with the correct file path if necessary
scrape_html(file_path)
