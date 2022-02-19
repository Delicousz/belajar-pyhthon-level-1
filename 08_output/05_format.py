a = 5
b = 3

print(a, '+', b, '=', a + b)
# 5 + 3 = 8

print('{} + {} = {}'.format(a, b, a + b))
# 5 + 3 = 8

print('{} dan {}'.format('ukay', 'Dewi'))
# Huda dan Budi

print('{1} dan {0}'.format('ukay', 'Dewi'))
# Budi dan Huda

print('Halo {namaDepan} {namaBelakang}'
  .format(namaDepan='Mutiara', namaBelakang='Berlian'))
# Halo Mutiara Berlian

# begini juga bisa:
print('Halo {namaDepan} {namaBelakang}'
  .format(
    namaBelakang='Berlian',
    namaDepan='Mutiara'
  )
)
# Halo Mutiara Berlian