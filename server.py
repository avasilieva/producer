#!/bin/usr/env python
import redis, os, random, string


server_path = (os.environ["REDISPATH"]) #or raise 'not set env' 

password = os.environ["PASS"]
url, port = server_path.split(":")

redis_db = redis.StrictRedis(host=url, port=port, db=0, password=password)

def id_generator(size=6, chars=string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

while(True):
  random_key = id_generator()
  random_value = id_generator()
  status = redis_db.set(random_key, random_value)
  print(status)
  print(random_key, random_value)

