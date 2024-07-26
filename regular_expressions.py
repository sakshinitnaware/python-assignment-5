import re
import string
import random
 
def email(mail):
    if not isinstance(mail, str):
        return False
    else :
    # Basic email pattern 
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # returning using regrex function 
    return re.match(pattern, mail) is not None



#function to Validate a Bangladesh phone number and  function variable number 
def bangla_moblile_number(number):
    # Regex pattern for Bangladesh mobile number matching 
    mobile_pattern = r'^01[3-9]\d{8}$'
    # returning using regrex function 
    return re.match(mobile_pattern, number) is not None


#function to Validate a U.S. telephone number 
def usa_telephone(telephone_number):
    # Regex pattern for US telephone numbers
    telephone_pattern = r'^(\+1\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    
    # Used re.match to check if the number matches the pattern
    return re.match(telephone_pattern, telephone_number, re.VERBOSE) is not None


def checking_password(password):
    
    # Define the regular expression patterns,Password must be exactly 16 characters,At least one uppercase letter
    # At least one uppercase letter,At least one lowercase letter,At least one digit and,At least one special character
    length_pattern = r'^.{16}$'          
    upper_pattern = r'[A-Z]'              
    lower_pattern = r'[a-z]'              
    digit_pattern = r'\d'                 
    special_pattern = r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`]' 

    # Checking length of password
    if not re.match(length_pattern, password):
        return False
    
    # Checking for at least one uppercase letter
    if not re.search(upper_pattern, password):
        return False
    
    # Checking for at least one lowercase letter
    if not re.search(lower_pattern, password):
        return False
    
    # Checking for at least one digit
    if not re.search(digit_pattern, password):
        return False
    
    # Checking for at least one special character
    if not re.search(special_pattern, password):
        return False
    
    return True


# Validating and print results for email
mail = '122wssdd'
email(mail)
print(f"{mail} is valid ?", email(mail))

# sample number for Validating and print results for Bangladesh moblile number
number = '01712345678'
print(f"{number} is valid ?", bangla_moblile_number(number))

# a sample telephone number for Validating and print results for USA telephone number
telephone_number = '143-236-7890'
print(f"{telephone_number} is valid?", usa_telephone(telephone_number))

# Validating and print results for password
password = 'WSX!a@a2112saa'
print(f"{password} is valid ? :",checking_password(password))
