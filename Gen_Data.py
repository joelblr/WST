import sys
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

import Modules
import Clean_Data


# Get the serialized data (the dictionary passed from the main script)
data_json = sys.argv[1]  # First argument after the script name

# Deserialize the JSON string back into a dictionary
inputs = json.loads(data_json)

# User-Agent and Accept-Language headers
headers = {
    'User-Agent': 'Use your own user agent',
    'Accept-Language': 'en-us,en;q=0.5'
}

product_name = [inputs['product_name']]
customer_names = []
review_title = []
ratings = []
comments = []

for i in range(inputs['from_page'], inputs['to_page']+1) :

    # Construct the URL for the current page
    url = inputs['base_url'] + '&page=' + str(i)

    # Send a GET request to the page
    page = requests.get(url, headers=headers)

    # Parse the HTML content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract customer names
    # names = soup.find_all('p', class_="_2NsDsF AwS1CA")
    names = soup.find_all('p', class_=inputs['cust_name'])
    for name in names:
        cleaned_name = Clean_Data.removeEmoji(name.get_text())
        customer_names.append(cleaned_name)

    # Extract review titles
    # title = soup.find_all('p', class_='z9E0IG')
    title = soup.find_all('p', class_=inputs['review_title'])
    for t in title:
        review_title.append(t.get_text())

    # Extract ratings
    # rat = soup.find_all('div', class_='XQDdHH Ga3i8K')
    rat = soup.find_all('div', class_=inputs['rating'])
    for r in rat:
        rating = r.get_text()
        if rating:
            ratings.append(rating)
        else:
            ratings.append('1')  # Replace null ratings with 0

    # Extract comments
    # cmt = soup.find_all('div', class_='ZmyHeo')
    cmt = soup.find_all('div', class_=inputs['comment'])
    for c in cmt:
        comment_text = Clean_Data.removeBrTag(c)
        cleaned_text = Clean_Data.removeEmoji(comment_text)
        comments.append(cleaned_text)


# Ensure all lists have the same length
min_length = min(len(customer_names), len(review_title), len(ratings), len(comments))
customer_names = customer_names[:min_length]
review_title = review_title[:min_length]
ratings = ratings[:min_length]
comments = comments[:min_length]

# Create a DataFrame from the collected data
data = {
    'Customer Name': customer_names,
    'Review Title': review_title,
    'Rating': ratings,
    'Comment': comments
}

df = pd.DataFrame(data)
print(f"Total Number of Records: {len(review_title)}")

## comments
import pandas as pd
data = {
    'Product Name': product_name*min_length,
    'Customer Name': customer_names,
    'Review Title': review_title,
    'Rating': ratings,
    'Comment': comments
}


df = pd.DataFrame(data)
# df['Rating'].fillna(0, inplace=True)

# Save the DataFrame to a CSV file
Modules.save_df(df, inputs['filename'], '.csv')