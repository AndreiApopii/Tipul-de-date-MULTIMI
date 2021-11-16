B={'A','B' , 'C', 'D'}
print('submultimile posibile sunt:')
print(B)
y=set()
for a in B:
      for b in B:
         if ord(b)>ord(a):
                       y.update({a,b})
                       print(y)
                       y.clear()
         for c in B:
                   if ord(c)>ord(b) and ord(b)>ord(a):
                       y.update({a,b,c})
                       print(y)
                       y.clear()
      for d in B:
                   if ord(c)>ord(b) and ord(b)>ord(a) and ord(d)>ord(c):
                       y.update({a,b,c,d})
                       print(y)
                       y.clear()
for a in B:
    y.add(a)
    print(y)
    y.clear()