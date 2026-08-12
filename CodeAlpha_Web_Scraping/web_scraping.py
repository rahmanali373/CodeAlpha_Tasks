# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv  # Tool for creating and writing to CSV files

# STEP 1: Define the target website URL
url = "http://books.toscrape.com/"

# STEP 2: Send a request to fetch the HTML data from the website
response = requests.get(url)

# STEP 3: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# STEP 4: Find all product containers (books) on the page
products = soup.find_all('article', class_='product_pod')

# STEP 5: Create and open a new CSV file
# 'w' stands for write mode, and encoding='utf-8' ensures proper text formatting
with open('books_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the column headers first
    writer.writerow(['Product Name', 'Price', 'Stock Status'])
    
    print("Data scraping and saving to file has started...\n")
    
    # STEP 6: Loop through each product to extract data and write it to the file
    for product in products:
        
        # 1. Extract the Product Name
        title = product.h3.a['title']
        
        # 2. Extract and clean the Product Price
        raw_price = product.find('p', class_='price_color').text
        clean_price = raw_price.replace('Â£', '') # Remove 'Â£' to keep only the numeric value
        
        # 3. Extract the Stock Status
        stock = product.find('p', class_='instock availability').text.strip()
        
        # Save the extracted data into a new row in the CSV file
        writer.writerow([title, clean_price, stock])

print("✅ Success! All data has been successfully saved to the 'books_data.csv' file!")