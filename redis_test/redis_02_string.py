import redis

redis_client = redis.Redis(host='47.96.177.182', port=6379, password='123456')

redis_client.set('string5', '5', nx=True)
redis_client.append('strings', '12131516')
print(redis_client.keys())
print(redis_client.get('strings'))
    