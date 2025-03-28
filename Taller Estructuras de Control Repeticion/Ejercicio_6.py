d=int(input())
v=int(input())
c = 0
while d >= v: d, c = d - v, c + 1
print(c, d)