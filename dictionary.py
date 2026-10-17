# keyvalue paired,ordered,not indexed,mutable,no duplicate keys allowed
for i in range(10):
    if i==4:
        break
    print(i)

for i in range(10):
    if i==4:
        continue
    print(i)

for i in range(10):
    if i==4:
        pass
    print(i)

l=[]
while True:
    name=input("Enter your name:(or enter 'exit' to quit):")
    if name =='exit':
        break
    l.append("hello"+name)
    print(l)

# //////////////////////////////////////////////////////

d={}
d['name']='Niya'
d['name']='manu'

print(d)