# Halaman 18 Modul Praktikum Algoritma Pemrograman
# Create by Desty 2270231090

# operasi komperasi
# setiap hasil dari operasi komperasi adalah boolean
#>,<,>=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print('========lebih besar dari (>)')
hasil = a>3
print(a,'>',3,'=',hasil)
hasil = b>3
print(b,'>',3,'=',hasil)
hasil = b>2
print(b,'>',2,'=',hasil)

# kurang dari <
print('========lebih kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)

# lebih dari sama dengan >=
print('========lebih kurang dari (>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)

# kurang dari sama dengan <=
print('========lebih kurang dari (<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)

# sama dengan (==)
print('========lebih kurang dari (==)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)

# tidak sama dengan (!=)
print('========lebih kurang dari (!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object identity
print('========lebih kurang dari (is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id=',hex(id(x)))
print('nilai y =',y,',id=',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6

print('nilai y =',x,',id=',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

print('======== object identuty(is not)')
x =  5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id=',hex(id(x)))
print('nilai y =',y,',id=',hex(id(y)))
hasil = x is not y
print('x is y=',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id=',hex(id(x)))
print('nilai y =',y,',id=',hex(id(y)))
hasil = x is not y
print('x is y=',hasil)


