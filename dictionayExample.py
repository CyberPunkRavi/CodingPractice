from collections import defaultdict
t=int(input())
for i in range(t):
  n=input()
  l=input()
  li=[int(i) for i in l.split()]
  li.sort()
  #print (li)
  di=defaultdict(list)
  for j in li:
    bi = bin(j)[2:]
    k = bi.count('1')
    di[k].append(j)
  for key in di:
    print (min(di[key]),end=" ")
  print()
