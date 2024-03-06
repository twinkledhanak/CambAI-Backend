import re

# To check and block any malicious input received in the controller
# Can include validation of all parameters use in controller

class ValidationUtil:
    def __init__(self):
        pass    

    def isParameterValid(self,key):
        # Define regular expression pattern to allow only alphanumeric characters and certain special characters
        pattern = r'^[a-zA-Z0-9\s.,!?()-]+$'
        regex = re.compile(pattern)
        match = regex.match(key)

        if match:
            return True
        else:
            return False

    def isParameterValueValid(self,value):
        return True
        # @TODO - Check what all types of values are permitted
