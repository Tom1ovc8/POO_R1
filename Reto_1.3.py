# Ejercicio 3

def primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def filtrar_primos(lista):
        return [num for num in lista if primo(num)]
    
lista = list(map(int, input("Introduce una lista de números separados por espacios: ").split()))
print(filtrar_primos(lista))

"""
1. Se define la función `primo` que verifica si un número es primo.
2. Se define la función `filtrar_primos` que filtra los números primos de una lista.
3. Se solicita al usuario que introduzca una lista de números separados por espacios.
4. Se convierte la entrada en una lista de enteros.
5. Se imprime la lista de números primos filtrados.
6. Se utiliza la función `map` para aplicar la conversión a cada elemento de la lista.
7. Se utiliza la función `split` para separar los números introducidos por el usuario para analizar cada uno de ellos.
8. Se utiliza la función `print` para mostrar el resultado final.
"""