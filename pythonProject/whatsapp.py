import os
import sys
import requests
import time
from bs4 import BeautifulSoup
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
import pywhatkit

import pywhatkit

# Specify the recipient's phone number in international format (including the country code)
phone_number = "+1123456789"

# Write the message you want to send
message = "Hello, this is a WhatsApp message sent using Python!"

# Specify the time when you want to send the message (optional)
# The time should be in 24-hour format: "hour:minute"
# For example, "10:30" represents 10:30 AM
scheduled_time = "15:41"



def get_amazon_ratings(asins):
    # Create the URL for the product's page on Amazon.in
    for asin in asins:
        print("Asin : ",asin)
        url = f"https://www.amazon.in/dp/{asin}"
        max_retries = 5
        retry_delay = 2  # Delay in seconds between retries

        for retry in range(max_retries):
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
                response = requests.get(url,headers=headers)
                if response.status_code == 200:
                # Successful response
                    break
                else:
                    print(f"Request failed with status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Request failed with exception: {e}")
            if retry < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Max retries reached. Exiting...")

        time.sleep(20)
        # Send a GET request to the URL and retrieve the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')


        #image start
        image_element = soup.find('div', {'id': 'imgTagWrapperId'})
        image_url = image_element.find('img')['src']
        image_response = requests.get(image_url)
        image_file_name = asin
        # Save the image to a file
        with open(image_file_name, 'wb') as file:
            file.write(image_response.content)

        print(f"The image has been downloaded and saved as '{image_file_name}'.")
        #image end



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

    ##start
        target_elements = soup.find_all('tr', {'data-reftag': True, 'aria-label': True})

        if len(target_elements) >0:
        # Extract and print the values from the aria-label attribute
            print("Rating category level report")
            for element in target_elements:
                aria_label_value = element['aria-label']
                print("", aria_label_value)
        else:
            print("No rating so far")

        # Call the sendwhatmsg() function to send the message
        #pywhatkit.sendwhatmsg(phone_number, message, int(scheduled_time[:2]), int(scheduled_time[3:]))
        pywhatkit.sendwhats_image(phone_number,image_file_name, "hello",int(scheduled_time[:2]), int(scheduled_time[3:]) )
        print("-----------------")
    ##end

# Specify the ASIN of the product you want to retrieve the ratings for
#product_asin = "B09B6FMW8L"
product_asins = ["B09B6FMW8L","B09B6FMW8L", "B0BNP8M7XV"]


# Call the function to get the ratings
get_amazon_ratings(product_asins)
