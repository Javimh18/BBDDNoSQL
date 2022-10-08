local name=ARGV[1]
local greet=redis.call("get", KEYS[1])
local result=greet.." "..name
return result