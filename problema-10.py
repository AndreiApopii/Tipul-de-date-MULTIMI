A={5, 6, 7, 8}
print('submultimile posibile sunt:')
print(A)
x=set()
for a in A:
      for b in A:
         if b>a:
                       x.update({a,b})
                       print(x)
                       x.clear()
         for c in A:
                   if c>b and b>a:
                       x.update({a,b,c})
                       print(x)
                       x.clear()
      for d in A:
                   if c>b and b>a and d>c:
                       x.update({a,b,c,d})
                       print(x)
                       x.clear()
for a in A:
    x.add(a)
    print(x)
    x.clear()