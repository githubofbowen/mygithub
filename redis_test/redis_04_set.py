import redis

redis_cli = redis.Redis(host='47.96.177.182', password='123456')
redis_cli.sadd('ex_set', 'hello')
redis_cli.sadd('ex_set', 1, 2.0, '四')
datas = [9, 8.0, 'seven', 'VI']
redis_cli.sadd('ex_set', *datas)
print(redis_cli.smembers('ex_set'))
#
#
#
print(redis_cli.scard('ex_set'))

print("************")
# 循环从redis集合中获取元素
for _ in range(3):
    print(redis_cli.spop('ex_set'))

print(redis_cli.smembers('ex_set'))

redis_cli.srem('ex_set', 'hello')

print(redis_cli.smembers('ex_set'))

redis_cli.sadd('ex_set1', 1, 2, 3, 4, 5)
redis_cli.sadd('ex_set2', 1, 2, 6, 7, 8)
print(redis_cli.smembers('ex_set1'), redis_cli.smembers('ex_set2'))
print(redis_cli.sinter('ex_set1', 'ex_set2'))
print(redis_cli.sunion('ex_set1', 'ex_set2'))
print(redis_cli.sdiff('ex_set1', 'ex_set2'))
