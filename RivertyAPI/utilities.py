# Built-in python libraries
import logging
import re
# Side-packages
from dateutil.parser import parse as dateparser


def process_input_data(input_data):
    try:
        processed_data = input_data
        processed_data['age_category'] = calculate_age_category(input_data['BirthDate'], input_data['RequestDateTime'])
        processed_data['consecutive_digits_username'] = count_consecutive_digits(input_data['Email'])
        return processed_data
    except KeyError as e:
        logging.error(f"Key error in input data: {e}")
        if 'Email' in str(e):
            processed_data['consecutive_digits_username'] = 0
            return processed_data
        if 'BirthDate' in str(e):
            raise ValueError("No BirthDate entry in json input") from e
        raise
    except Exception as e:
        logging.error(f"Error processing input data: {e}")
        raise


def calculate_age_category(birthdate_str, request_datetime_str):
    try:
        if not birthdate_str:
            return "no_age"
        birthdate = dateparser(birthdate_str)
        request_datetime = dateparser(request_datetime_str)
        age = (request_datetime - birthdate).days // 365.25
        if age < 18:
            return "under_age"
        elif age <= 25:
            return "18-25"
        elif age <= 50:
            return "26-50"
        else:
            return "51-older"
    except Exception as e:
        logging.error(f"Error in calculate_age_category: {str(e)}")
        return "no_age"

def count_consecutive_digits(email):
    try:
        if not email or "@" not in email:
            return 0
        username = email.split('@')[0]
        return max([len(match) for match in re.findall(r'\d+', username)] + [0])
    except Exception as e:
        logging.error(f"Error in calculate_age_category: {str(e)}")
        return 0
    
def check_input_necessities(input_data):
    if input_data is None:
        raise ValueError("No JSON data provided or JSON data is invalid")
    necessities_list=[ 'BirthDate', 'GrossAmount', 'NumberOfPayments', 'EMCResult', 'Merchant']
    missing_items=[item for item in necessities_list if item not in input_data]
    if missing_items:
        raise ValueError(f"Missing necessary items: {missing_items}")
    return True
