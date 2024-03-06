
## Redis Connectivity in Kubernetes Container
## @TODO - Check if this must be redis service or redisjson service
REDIS_HOST = 'redisjson-service'  # Service name defined in the Redis service YAML file
REDIS_PORT = 6380  
# Define RedisJSON key for storing key-value pairs
REDISJSON_KEY = 'key_value_store'



## Error-Handling
GENERIC_EXCEPTION_CODE = 400
GENERIC_EXCEPTION_MSG = "Please try again later!"