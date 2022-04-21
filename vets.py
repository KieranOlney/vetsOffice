from animals import *

cookie = cat(8,"Cookie")
print(cookie.name,cookie.age)
print(cookie.move())
print(cookie.eat())
print(cookie.isAlive)
cookie.die()
print(cookie.isAlive)