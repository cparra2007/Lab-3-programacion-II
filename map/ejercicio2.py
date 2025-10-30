celsius = [0, 10, 20, 30]

# formula: celsiu * 9/5 + 32
# lambda se define directamente dentro de map
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("celsius a fahrenheit:")
print(f"grados celsius: {celsius}")
print(f"grados fahrenheit: {fahrenheit}")
