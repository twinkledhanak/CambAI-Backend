# For Local
# import sys
# sys.path.append("..")

# For Container
import sys
import os
file_path = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
lib_path = os.path.abspath(os.path.join(file_path, '../')).replace('\\', '/')
sys.path.append(lib_path)

import logging
from fastapi import FastAPI, HTTPException
from Services import KeyValueService
from Services.KeyValueService import KeyValueService
from ExceptionHandler import CambaiServiceException
from Util import ValidationUtil
from Util.ValidationUtil import ValidationUtil
from Constants import GENERIC_EXCEPTION_CODE,GENERIC_EXCEPTION_MSG
import asyncio

# Instantiate an object
api = FastAPI()
# Set generic message here in Controller to not give away implementation details
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

## @TODO - Implement async-await
class KeyValueController:
    def __init__(self):
        ## We may be setting initial states/values/data needed by the controller
        pass        

    #1. Retrieve all keys in the store
    @api.get("/items/")
    async def getAllKeys(self):
        try:
            service = KeyValueService()
            result = await service.getAllKeys()
            return result
        except Exception as e:
            logging.error(f"Please try again later, Error : {e}") 


    #2. Retrieve values for given key
    @api.get("/items/{item_id}")
    async def getValueForKey(self, key):
        try:
            util = ValidationUtil()
            if util.isParameterValid(key):
                service = KeyValueService()
                result = await service.getValueForKey(key)
                return result
            else:
                logging.error("Please input valid value for parameter!")           
        except Exception as e:
                logging.error(f"Please try again later. Error : {e}")


    #3. Set values for given key
    @api.post("/items/{key}/{input_data}")
    async def setValueForKey(self, key:str,  input_data: str):
        try:
            util = ValidationUtil()
            if util.isParameterValid(key) and util.isParameterValueValid(input_data):
                service = KeyValueService()
                result = await service.setValueForKey(key,input_data)
                return result
            else:
                logging.error("Please input valid values for parameter and their values!")               
        except Exception as e:
            logging.error(f"Please try again later. Error : {e}")
    

    #4. Check to see if a value exists for a given key
    @api.get("/obj-key-exists/{key}/{path}")
    async def check_obj_key_exists(key: str, path: str):
        try:
            util = ValidationUtil()
            if util.isParameterValid(key) and util.isParameterValueValid(path):
                service = KeyValueService()
                result = await service.doesKeyExists(key, path)
                return result
            else:
                logging.error("Please input valid values for key and their path!")               
        except Exception as e:
            logging.error(f"Please try again later. Error : {e}")


    #5. Delete a given key from the store
    @api.get("/items/{item_id}")
    async def deleteKeyFromStore(self, key):
        try:
            util = ValidationUtil()
            if util.isParameterValid(key):
                service = KeyValueService()
                result = await service.deleteKey(key)
                return result
            else:
                logging.error("Please input valid value for parameter!")           
        except Exception as e:
            logging.error(f"Please try again later. Error : {e}")


    async def initiateCalls(self):
        controller = KeyValueController() 
        result = await (controller.getAllKeys())
        print(result)  
        print('-------------------------------------------------------------------------------------')
        result = await (controller.setValueForKey("Twinkle",{"kishor","Dhanak"}))
        print(result)
        print('-------------------------------------------------------------------------------------')
        result = await (controller.getValueForKey("Twinkle"))
        print(result)
        print('-------------------------------------------------------------------------------------')
        result = await (controller.deleteKeyFromStore("Twinkle"))
        print(result)


## Check if the user is authenticated and authorized to perform operations
## result = checkIfUserIsValid(user):
# if result:
#     ## Continue with further processing, Implement OAuth token authentication, check user roles
#       loop = asyncio.get_event_loop()
#       c = KeyValueController()
#       loop.run_until_complete(c.initiateCalls())
# else:
#     print("user is not authorized to perform these operations!")    

loop = asyncio.get_event_loop()
c = KeyValueController()
loop.run_until_complete(c.initiateCalls())
    
