# Program that validates phone numbers, ssns and zip codes using regular
# expressions.- Livia Augusto Razera, Assignment 6.

import re

# Function that validates US phone numbers.
def validate_phone_number(phone):

    pattern = re.compile(r'^(\+1\s)?(\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$')
    return bool(pattern.match(phone))

# Function that validates Social Security Numbers.
def validate_ssn(ssn):

    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

# Function that validates US Zip codes.
def validate_zip_code(zip_code):

    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

# Main function, which prompts users for their phone number, ssn, and zip code.
def main():
    phone = input('Enter a phone number: ')
    ssn = input('Enter a Social Security Number (SSN): ')
    zip_code = input('Enter a ZIP code: ')

    # Displays whether the phone number, ssn, and zip code are valid by using
    # the other functions.
    print('\nValidation Results:')
    print(f'Phone number valid? {'Yes' if validate_phone_number(phone) else 'No'}')
    print(f'SSN valid? {'Yes' if validate_ssn(ssn) else 'No'}')
    print(f'Zip code valid? {'Yes' if validate_zip_code(zip_code) else 'No'}')

# Calls out main function.
if __name__ == '__main__':
    main()