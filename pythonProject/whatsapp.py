import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
import pywhatkit

import pywhatkit

# Specify the recipient's phone number in international format (including the country code)
phone_number = "+17788871963"

# Write the message you want to send
message = "Hello, this is a WhatsApp message sent using Python!"

# Specify the time when you want to send the message (optional)
# The time should be in 24-hour format: "hour:minute"
# For example, "10:30" represents 10:30 AM
scheduled_time = "16:38"

# Call the sendwhatmsg() function to send the message
pywhatkit.sendwhatmsg(phone_number, message, int(scheduled_time[:2]), int(scheduled_time[3:]))


import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

def get_amazon_ratings(asin):
    # Create the URL for the product's page on Amazon.in
    url = f"https://www.amazon.in/dp/{asin}"

    # Send a GET request to the URL and retrieve the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')



    # Find the element that contains the total number of ratings
    ratings_element = soup.find('span', {'id': 'acrCustomerReviewText'})
    if ratings_element is not None:
        ratings_text = ratings_element.text.strip()
        ratings_count = ''.join(filter(str.isdigit, ratings_text))
        print("Number of ratings:", ratings_count)

    # Find the element that contains the average number of ratings
    avg_ratings_element = soup.find('span', {'id': 'acrPopover'})
    if avg_ratings_element is not None:
        avg_ratings_text = avg_ratings_element.text.strip()
#//avg_ratings_count = ''.join(filter(str.isdigit, avg_ratings_text))
        split_string = avg_ratings_text.split()
        avgRating = split_string[0]

        print("Average number of ratings:", avgRating ,"out of 5 stars")



    # Find elements that contain individual ratings
    ratings_elements = soup.find_all('i', {'data-hook': 'review-star-rating'})
    # average_ratings_elements =soup.find_all('i', {'data-hook': 'rating-out-of-text'})
    # if average_ratings_elements is not None:
    #     average_ratings_text = average_ratings_elements.text.strip()
    #     average_ratings_count = ''.join(filter(str.isdigit, average_ratings_text))
    #     print("Average", average_ratings_count)


    # # Initialize counters for each star category
    # star_ratings = {
    #     '5-star': 0,
    #     '4-star': 0,
    #     '3-star': 0,
    #     '2-star': 0,
    #     '1-star': 0
    # }
    #
    # # Count the ratings for each star category
    # for element in ratings_elements:
    #     rating_text = element.span.text.strip()
    #     if rating_text in star_ratings:
    #         star_ratings[rating_text] += 1
    #
    # # Print the number of ratings for each star category
    # for star, count in star_ratings.items():
    #     print(star, ":", count)

    ##start
    target_elements = soup.find_all('tr', {'data-reftag': True, 'aria-label': True})

    # Extract and print the values from the aria-label attribute
    print("Rating category level report")
    for element in target_elements:
        aria_label_value = element['aria-label']

        print("", aria_label_value)
    ##end

# Specify the ASIN of the product you want to retrieve the ratings for
product_asin = "B09B6FMW8L"

# Call the function to get the ratings
get_amazon_ratings(product_asin)
