a=set(input('dati elementele multimii a :'))
b=set(input('dati elementele multimii b :'))
x=0
for i in a:
    if ord(i) not in range(65,91):
        x+=1

for i in b:
   if ord(i) not in range(65,91):
        x+=1
if x>0:
    print('Mulţimile a şi b trebuie sa fie formate din n literele mari ale alfabetului latin.')
if x==0:
  print('intersecţia mulţimilor =',a.intersection(b))
  print('reuniunea mulţimilor =',a.union(b))
  print('diferenţa mulţimilor a/b =',a.difference(b))
  print('diferenţa mulţimilor b/a =',b.difference(a))