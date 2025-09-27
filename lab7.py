car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d = {1: 'yg',2:'sachin'}
print(d)
d.popitem()

print(car)
x = car.setdefault("model","white")
print(x)
car.update({"color":"white"})
print(car)


