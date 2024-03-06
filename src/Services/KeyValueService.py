# For Local
# import sys
# sys.path.append("..")

#For Container
import sys
import os
file_path = os.path.abspath(os.path.dirname(__file__)).replace('\\', '/')
lib_path = os.path.abspath(os.path.join(file_path, '../')).replace('\\', '/')
sys.path.append(lib_path)

from Constants import REDIS_HOST,REDIS_PORT,REDISJSON_KEY
import redis
import huey
from huey import RedisHuey
import json
from ExceptionHandler import CambaiServiceException
import logging
from fastapi import HTTPException
import asyncio

# Configure Huey to use Redis in Kubernetes container
redisInstance = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
hueyInstance = RedisHuey('cambai', host=REDIS_HOST, port=REDIS_PORT)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class KeyValueService:
    def __init__(self):
        pass


    ## 1. Checking if a key exists (generic and can be used by all methods)
    @hueyInstance.task()
    async def obj_key_exists_task(key, path):
        await asyncio.sleep(5)
        return redisInstance.execute_command('JSON.OBJKEYEXISTS', key, path)

    async def doesKeyExists(self,key,path):
        try:
            print("Checking if exists, Key: ",key)
            result = await (self.obj_key_exists_task(key,path).enqueue())
            return result
        except HTTPException:
            raise HTTPException(status_code=404, detail="Item not found")    
        except Exception as e:
            error_code = getattr(e, 'error_code', None)
            logging.error(f"Error in checking if key exists, code: {error_code}, Message: {e}")
            raise CambaiServiceException("Exception in getting value for key: ", e)



    ## 2. Set value for a given key
    @hueyInstance.task()
    async def setValueForKey1(key, value):
        # Convert value to JSON format
        await asyncio.sleep(5)
        json_value = json.dumps(value)
        return redisInstance.execute_command('JSON.SET', REDISJSON_KEY, key, json_value)

    async def setValueForKey(self,key,value):
        try:
            print("Setting value: ",value)
            print("Given Key: ",key)
            return await (self.setValueForKey1(key,value).enqueue())
        except Exception as e:
            error_code = getattr(e, 'error_code', None)
            logging.error(f"Error in setting value for key, code: {error_code}, Message: {e}")
            raise CambaiServiceException("Exception in setting value for key: ", e)



    ## 3. Get value for a given key
    @hueyInstance.task()
    async def get_key_value(key):
        try: 
            await asyncio.sleep(5)
            json_value = redisInstance.execute_command('JSON.GET', REDISJSON_KEY, key)
            if json_value:
                value = json.loads(json_value)
                return value
            else:
                return None
        except Exception as e:
            error_code = getattr(e, 'error_code', None)
            logging.error(f"Error in getting value for key, code: {error_code}, Message: {e}")
            raise CambaiServiceException(error_code, e)          

    async def getValueForKey(self,key):
        try: 
            await (asyncio.sleep(5))
            print("Getting value for key: ",key)  
            # Check to see is key exists or not
            result = await (self.doesKeyExists(key,""))
            if result:
                return await (self.get_key_value(key).enqueue()) 
            else:
                return None    
        except HTTPException:
            raise HTTPException(status_code=404, detail="Item not found")    
        except Exception as e:
            error_code = getattr(e, 'error_code', None)
            logging.error(f"Error in getting value for key, code: {error_code}, Message: {e}")
            raise CambaiServiceException("Exception in getting value for key: ", e)


    ## 4. Delete a given key
    @hueyInstance.task()
    async def delete_key(key):
        await asyncio.sleep(5)
        return redisInstance.execute_command('JSON.DEL', REDISJSON_KEY, key)

    async def deleteKey(self,key):
        try:
            result = await (self.doesKeyExists(key,""))
            if result:
                print("Deleting Key: ",key)
                return await (self.delete_key(key).enqueue())
            else:
                return None    
        except HTTPException:
            raise HTTPException(status_code=404, detail="Item not found")    
        except Exception as e:
            error_code = getattr(e, 'error_code', None)
            logging.error(f"Error in deleting key, code: {error_code}, Message: {e}")
            raise CambaiServiceException("Exception in deleting key: ", e)
    

   
    ## 5. Get all the keys
    @hueyInstance.task()
    async def getKeys(self):
        ## Implement logic to get all keys
        await asyncio.sleep(5)
        pass

    async def getAllKeys(self):
        print("Getting all keys")
        ## Implement logic to get all keys
        

    

     

       
    
