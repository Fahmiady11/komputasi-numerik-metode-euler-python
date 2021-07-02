def fungsi(x, y):
    return x+y
def metodeEuler(x0, y0, xn, n):
    h = (xn-x0)/n
    print('x0\ty0\tslope\tyn')
    print('------------------------------')
    for i in range(n):
        tikMir = fungsi(x0, y0)
        yn = y0 + h * tikMir
        print('%.4f\t%.4f\t%0.4f\t%.4f' % (x0, y0, tikMir, yn))
        y0 = yn
        x0 = x0+h
    print('\nAt x=%.4f, y=%.4f' % (xn, yn))
print('Masukkan kondisi awal:')
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))

print('Masukkan poin perhitungan: ')
xn = float(input('xn = '))

print('Masukkan jumlah langkah:')
n = int(input('Jumlah langkah = '))

metodeEuler(x0, y0, xn, n)
