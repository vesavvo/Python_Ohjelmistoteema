import math

eka = -9
toka = 12_456_123_180
kolmas = 4.973
neljäs = -4 + 2j

print (eka)
print (toka)
print (kolmas)
print (neljäs)
print (neljäs.real)
print (neljäs.imag)


print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")

fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = int((fahrenheit-32)*5/9)
print(f"Lämpötila Celsius-asteina: {celsius:6d}")


