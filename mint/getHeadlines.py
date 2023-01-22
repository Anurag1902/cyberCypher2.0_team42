# Import the necessary libraries
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
url = "https://www.livemint.com/market/stock-market-news"
driver = webdriver.Chrome()
driver.get(url)

# Initialize counter and limit variables
counter = 0
limit = 15000

# Create an empty list to store the headlines
headlines_list = []

while counter < limit:
    print(counter)
    # Scroll down the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for new content to load
    time.sleep(5)

    # Get the new HTML content
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    headlines = soup.find_all('h2',class_='headline')
    for headline in headlines:
        if counter < limit:
            cleaned_headline = headline.text.replace('\n', '')
            cleaned_headline = cleaned_headline.replace('         ', '')
            headlines_list.append(cleaned_headline)
            counter += 1
        else:
            break

# Create a DataFrame from the list of headlines
headlines_df = pd.DataFrame(headlines_list, columns=['Headlines'])


# Save the DataFrame as a CSV file
headlines_df.to_csv('headlines.csv', index=False)

driver.quit()