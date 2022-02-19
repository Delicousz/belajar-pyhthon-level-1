listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar', 'Bogor', 'Bandung'
]

kotaYangDicari = input('Ketik nama kota yang kamu cari: ')

for i, kota in enumerate(listKota):
  # kita ubah katanya ke lowercase agar 
  # menjadi case insensitive
  if kota.lower() == kotaYangDicari.lower():
    print('Kota yang anda cari berada pada indeks', i)
    break
  elif (kotaYangDicari.lower() == 'bekasi'):
    print('Kota tersebut pindah ke neraka')
    break
else:
  print('Maaf, kota yang anda cari tidak ada')
