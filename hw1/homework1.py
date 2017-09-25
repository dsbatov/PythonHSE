a =int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a % b == c:
	print("a дает остаток c при делении на b")
else:
	print("a не дает остаток c при делении на b")
if a * c + b == 0:
	print("с - решение линейного уравнения ax + b = 0")
else:
	print("с - не решение линейного уравнения ax + b = 0")