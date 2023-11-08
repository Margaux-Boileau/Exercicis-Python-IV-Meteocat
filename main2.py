from numpy.random import choice

 
sampleList = [100, 200, 300, 400, 500]

list = [0.055, 0.045, 0.2, 0.3, 0.4]
print(list)
# sum list
print(sum(list))

draw = choice(sampleList, 30, p=list)


print(draw)