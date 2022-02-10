#menghilangkan karakter spasi di awal dan di akhir string
# menggunakan metode strip(), lsrip(),rstrip()

nilai="88888selmat datang888888"
hasil=nilai.strip("8")
print(hasil)
# metode strip() untuk menghilangkan krakter spasi di awal dan di akhir sring
# dapat juga menghilangkan bagian teks di awal dan di akhir
nilai= "selamat datang"
hasil1=nilai.lstrip()
print(hasil1)
# metode lstrip() hanya untuk menghilangkan karakter spasi yang berada di awal string

nilai= "selamat datang"
hasil2=nilai.rstrip()
print(hasil)
# metode rstrip () hanya untuk menghilangkan karakter spasi yang berada di akhir string