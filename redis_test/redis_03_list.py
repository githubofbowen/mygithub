import redis

redis_client = redis.Redis(host='47.96.177.182', port=6379, password='123456')
# a = redis_client.lpush('example', '0','1', '2', '3', '4')

data = [1, 2, 3, 4, 5]
redis_client.lpush('example_data', *data)
for i in redis_client.lrange('example_data', 0, -1):
	print(i)