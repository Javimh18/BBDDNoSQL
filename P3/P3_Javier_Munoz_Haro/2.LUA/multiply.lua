local keyNumber=redis.call("get", KEYS[1])
local valueNumber=ARGV[1]
local result=valueNumber*keyNumber
return result