from fastapi import FastAPI, HTTPException
import sys
sys.path.append("..")
from Services import KeyValueService
from ExceptionHandler import CustomException
from Constants import GENERIC_EXCEPTION_CODE,GENERIC_EXCEPTION_MSG
import asyncio

# Instantiate an object
api = FastAPI()

## @TODO - Implement async-await
class KeyValueController:
    def __init__(self):
        ## @TODO
        ## We may be setting initial states/values/data needed by the controller
        # self.name = name
        pass        

    #1. Retrieve all keys in the store
    @api.get("/items/")
    def getAllKeys(self):
        try:
            service = KeyValueService()
            result = service.getAllKeys()
            return result
        except HTTPException:
            raise HTTPException(status_code=404, detail="Item not found")
        except Exception:
            return Exception     ## @TODO - Design a better error handling mechanicsm

    

# Run the main function
if __name__ == "__main__":
    obj2 = KeyValueController() ## @TODO - Change the parameter definition, we need to pass something else, not name
        # You need to await the coroutine function
    print(obj2.getAllKeys())  
