listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar', 'Bogor', 'Bandung'
]

# skip jika i adalah bilangan genap
# dan lebih dari 0
i = -1
while i < len(listKota):
  i += 1
  if i % 2 == 0 and i > 0:
    print('skip')
    continue
  
  print(listKota[i])