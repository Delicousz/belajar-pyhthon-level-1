listnama = [
  'Fauzi', 'Ukay', 'Dewi', 'Berlin'
]

print('Tanpa enumerate:')

for nama in listnama:
  print(nama)

print('\nDengan enumerate:')

for i, nama in enumerate(listnama):
  print(i, nama)