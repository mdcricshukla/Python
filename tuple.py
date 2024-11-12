t=tuple()
s=(1,2,3)+('ab',4)
# print(s*3)
newtuple=tuple("Hello World!")
d={"ram":30,"jai":40}
print(d)
d.update({'harry':42})
print(d)
d.setdefault('harry',26)
print(d)

for i,j in d.items():
    print(i,j)
