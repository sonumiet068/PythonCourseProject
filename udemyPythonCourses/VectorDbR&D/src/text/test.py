
def add(element):
  for i in range(2):
    yield element+100
    
for i in range(5):
   a=next(add(i))
   print(a)
