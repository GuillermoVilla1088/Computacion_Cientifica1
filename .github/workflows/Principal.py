import Funciones
# Vamos a crear el menú con las 20 opciones
while True:
    print('1. Solución Ecuación cuadrática')
    print('2. Sumar a + b')
    print('3. Contador de n primeros números')
    print('4. Contador de n números pares')
    print('5. Contador de n números impares')
    print('6. Conjetura de Collatz')
    print('7. Raíz de la suma de impartes')
    print('8. Multiplos hasta 10')
    print('9. Inversa de una matríz')
    print('10. Volumen de un cono')
    print('11. Variable de entrada')
    print('12. Encontrar IVA')
    print('13. Encontrar área de un círculo')
    print('14. Verificar número primo')
    print('15. El cuadrado de un vector')
    print('16. Hallar IMC')
    print('17. Porcentaje de grasa')
    print('18. Calorias en reposo')
    print('19. Calorias en actividad física')
    print('20. Consumo calorias para adelgazar')
    print('x. salir \n')
    op=input('Ingrese una opción: ')
    if op == '1':
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        x1,x2 = Funciones.sln_cuadratica(a, b, c)
        print('Valores ',x1,x2)
    elif op == '2':
        a = float(input("Ingrese a : "))
        b = float(input("Ingrese b : "))
        print('La suma es = ',Funciones.sum_num(a,b))
    elif op == '3':
        n = int(input('Ingrese un número n = '))
        print(Funciones.contador_i(n))
    elif op == '4':
        n = int(input('Ingrese un número n = '))
        print(Funciones.contador_pares(n))
    elif op == '5':
        n = int(input('Ingrese un número n = '))
        print(Funciones.contador_impares(n))
    elif op == '6':
        n = int(input('Ingrese un número n = '))
        print('La conjetura de Collatz con respecto al número n es:')
        print(Funciones.prueba_collatz(n))
    elif op == '7':
        n = int(input('Ingrese un número n = '))
        print('La raíz de la suma de los números impares en rango n es =',Funciones.raiz_sum(n))
    elif op == '8':
        n = int(input('Ingrese un número n = '))
        print('La tabla de multiplicar hasta el número n es =',Funciones.multiplos(n))
    elif op == '9':
        n = int(input('filas de A, n= '))
        m = n
        print('La matríz A es = ',Funciones.coeficientes(n,m))
    elif op == '10':
        r = float(input('Ingrese el valor del radio = '))
        h = float(input('Ingrese el valor de la altura = '))
        print('El valor del volumen del cono es = ',Funciones.vol_cono(r,h))
    elif op == '11':
       variable_entrada = int(input('Ingrese el valor de la variable de entrada = '))
       print('El valor de salida será = ',Funciones.function(variable_entrada))
    elif op == '12':
        iva = int(input('Ingrese el valor del IVA = '))
        precio_inicial = int(input('Ingrese el valor del precio inicial = '))
        print('El valor de la factura con el IVA aplicado será = ',Funciones.encontrar_IVA(precio_inicial, iva))
    elif op == '13':
        r = float(input('Ingrese el valor del radio = '))
        print('El valor del área del círculo será = ',Funciones.area_cir(r))
    elif op == '14':
        n = int(input("Ingrese un número entero positivo = "))
        print(Funciones.verificar_primo(n))
    elif op == '15':
        n = int(input('Ingrese el valor de columnas = '))
        print(Funciones.cuadrado_vi(n))
    elif op == '16':
        peso = float(input('Ingrese el valor del peso en kg = '))
        altura = float(input('Ingrese el valor de al altura en cm = '))
        print('El IMC de la persona es = ',Funciones.hallar_IMC(peso, altura))
    elif op == '17':
        peso = float(input('Ingrese el valor del peso en kg = '))
        altura = float(input('Ingrese el valor de al altura en cm = '))
        edad = int(input('Ingrese el valor de la edad = '))
        print('Valor de genero masculino = 5. Valor de genero femenino = -161')
        genero = int(input('Ingrese el valor del genero de la persona = '))
        print('El porcetanje de grasa del paciente es = ',Funciones.por_grasa(peso, altura, edad, genero))
    elif op == '18':
        peso = float(input('Ingrese el valor del peso en kg = '))
        altura = float(input('Ingrese el valor de al altura en cm = '))
        edad = int(input('Ingrese el valor de la edad = '))
        print('Valor de genero masculino = 5. Valor de genero femenino = -161')
        genero = int(input('Ingrese el valor del genero de la persona = '))
        print('El porcetanje de calorias de la persona en reposo es = ',Funciones.cal_calorias_reposo(peso, altura, edad, genero))
    elif op == '19':
        peso = float(input('Ingrese el valor del peso en kg = '))
        altura = float(input('Ingrese el valor de al altura en cm = '))
        edad = int(input('Ingrese el valor de la edad = '))
        print('Valor de genero masculino = 5. Valor de genero femenino = -161')
        genero = int(input('Ingrese el valor del genero de la persona = '))
        print('Los valores de actividad física son: poca actividad = 1.2')
        print('Ejercicio 1-3 veces por semana = 1.375')
        print('Ejercicio 3-5 veces a la semana = 1.55')
        print('Ejercicio 6-7 veces a la semana = 1.725')
        print('Atleta profesional = 1.9')
        actividad = float(input('Ingrese el valor de actividad física = '))
        print('El valor de calorías en actividad física es = ',Funciones.cal_calorias_actividad(peso, altura, edad, genero, actividad))
    elif op == '20':
        peso = float(input('Ingrese el valor del peso en kg = '))
        altura = float(input('Ingrese el valor de al altura en cm = '))
        edad = int(input('Ingrese el valor de la edad = '))
        print('Valor de genero masculino = 5. Valor de genero femenino = -161')
        genero = int(input('Ingrese el valor del genero de la persona = '))
        print('El porcentaje de calorias que se recomienda consumir es = ',Funciones.consumo_calorias_adelgazar(peso,altura,edad,genero))
    elif op == 'x':
        print('Salir')
        break
    else:
        print('Repite menú')

