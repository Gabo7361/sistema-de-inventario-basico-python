inventario = ["cuerda", "soga", "comida"]
print ("\nestos son tus suministros:")
for objeto in inventario:
    print(f"- {objeto}")


nuevo_objeto = input("\nQue otro objeto deseas agregar?: ")
inventario.append(nuevo_objeto)

print(f"\n¡Has agregado {nuevo_objeto}, bien hecho!")

for objeto in inventario:
    print(f"- {objeto}")









