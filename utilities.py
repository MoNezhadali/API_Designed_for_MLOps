from dateutil.parser import parse as dateparser
import re

def process_input_data(input_data):
    processed_data = input_data
    processed_data['age_category'] = calculate_age_category(input_data['BirthDate'], input_data['RequestDateTime'])
    processed_data['consecutive_digits_username'] = count_consecutive_digits(input_data['Email'])
    # Add other necessary processing steps here
    return processed_data

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
    except

def count_consecutive_digits(email):
    if not email or "@" not in email:
        return 0
    try:
        username = email.split('@')[0]
        return max([len(match) for match in re.findall(r'\d+', username)] + [0])
    except Exception as e:
        return str(e)
        # raise UnexpectedError(str(f"Unexpected error in counting consecutive digits in Email: {e}"))
