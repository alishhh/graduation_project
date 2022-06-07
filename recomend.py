a = "У меня грипп, простуда, и насморк и головная боль."
az = a.replace(',', '')
at = az.replace('.', '')
a = at.split()
a.sort()

ali = []
for i in a:
  if i not in ali:
    ali.append(i)


b = "головная боль, простуда, насморк, грипп"
bz = b.replace(',', '')
bt = bz.replace('.', '')
b = bt.split()
b.sort()

bli = []
for j in b:
  if j not in bli:
    bli.append(j)


print(ali)
print(bli)

result = list(set(ali) & set(bli))
result = len(result)

if result > 2:
    print("есть " + str(result) + " совпадений")




