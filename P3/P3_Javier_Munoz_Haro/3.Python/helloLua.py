import redis, sys

path_to_lua = "/Users/javiermunoz/Universidad/Master/Segundo/BBDDNoSQL/P3/2.LUA/hello.lua"

if len(sys.argv) <= 2:
    print("ERROR:python <path_to_script> greetkey <name>")
    exit(0)

name = sys.argv[2]
greeting = sys.argv[1]

f = open(path_to_lua, "r")

r = redis.Redis(host="127.0.0.1", port=6379)

r.set(greeting, "Hello")

luascript = r.register_script(f.read())

res = luascript(keys=[greeting], args=[name])

print(res.decode('ascii'))

