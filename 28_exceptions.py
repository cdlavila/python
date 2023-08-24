try:
    num = int(input("Ingrese un número: "))
    result = 10 / num
    print("El resultado es:", result)
except ValueError:
    print("Error: Ingrese un valor numérico válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except Exception as e:
    print("Error inesperado:", e)
else:
    print("¡Todo funcionó correctamente!")
finally:
    print("Fin del programa.")
