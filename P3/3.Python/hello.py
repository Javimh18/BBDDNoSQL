import redis, sys

if len(sys.argv) <= 2:
    print("ERROR:python <path_to_script> greetkey <Name>")
    exit(0)

name = sys.argv[2]

greeting = sys.argv[1]

r = redis.Redis(host="127.0.0.1", port=6379)

r.set(greeting, "Hello")

print(r.get(greeting).decode('ascii'), name)