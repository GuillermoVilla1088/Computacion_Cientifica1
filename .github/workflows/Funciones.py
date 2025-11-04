import numpy as np
import random
import math
import matplotlib.pyplot as plt
pi = math.pi
def sum_num(a,b):
  sum_num = a+b
  return sum_num


def sln_cuadratica(a,b,c):
  print("Esta función resuelve la ec. cuadrática para ax^2+bx+c=0")
  d = pow(b,2)-4*a*c
  if d==0:
   print("La soluciónes son iguales")
   x1 = (-b)/(2*a)
   x2 = x1
  elif d>0:
    print("La soluciónes son diferentes")
    x1 = (-b+pow(d,1/2))/(2*a)
    x2 = (-b-pow(d,1/2))/(2*a)
  else:
    print("Las soluciones son complejas")
    x1 = (-b+pow(d,1/2))/(2*a)
    x2 = (-b-pow(d,1/2))/(2*a)
  return x1,x2

def contador_pares(n):
 conteo = "Esta función imprime el conteo de i=0 hasta el número n es:\n"
 for i in range(n+1):
  if i%2==0:
   conteo += "i = " + str(i) + "\n"
 return conteo

def contador_i(n):
    conteo = "Esta función imprime el conteo de i=0 hasta el número n es:\n"
    for i in range(n + 1):
        conteo += "i = " + str(i) + "\n"
    return conteo


def contador_impares(n):
 conteo = "Esta función imprime el conteo de i=0 hasta el número n es:\n"
 for i in range(n+1):
  if i%2==1:
   conteo += "i = " + str(i) + "\n"
 return conteo

def prueba_collatz(n):
 conteo = ""
 while n !=1:
  if n%2==0:
   n = n/2
   n = int(n)
   print("n= ",n)
  else:
   n = n*3+1
   conteo += "n = " + str(n) + "\n"
 return conteo

def raiz_sum(n):
  print("Calcular la raíz de la suma de números imapres hasta n")
  a = 0
  for i in range(1,n+1,2):
   a = a + i
  a = pow(a,1/2)
  return int(a)

def multiplos(n):
    tablas = ''
    for i in range(1,n+1):
       tablas += str(n) + " x " + str(i) + " = " + str(n*i) + "\n"
    return tablas 

def coeficientes(n,m):
  A = np.zeros((n,m))
  for i in range(n):
    for j in range(m):
      A[i][j] = float(input("A_"+str(i)+str(j)+"= "))
  return np.linalg.inv(A)
 
def vol_cono(r,h):
 v = pi*r**2*h/3
 return v

def function(variable_entrada):
  variable_salida = variable_entrada + 1
  return variable_salida

def encontrar_IVA(precio_inicial,iva):
  if iva==0:
   valor_total=precio_inicial+precio_inicial*0.21
  else:
    valor_total=precio_inicial+precio_inicial*iva/100
  return valor_total

def area_cir(r):
 area = pi*r**2 
 return area

def vol_cil(r,h):
 vol = area_cir(r)*h
 return vol

def sqr_vi(v,n):
 s_vi = np.zeros(n)
 for j in range(n):
   s_vi[j] = v[j]**2
 return s_vi

def verificar_primo(n):
    if n == 1:
        print("No es primo")
        return
    if n == 2:
        print("Es primo")
        return
    if n % 2 == 0:
        print("No es primo, es par")
        return
    con = 0
    for i in range(1, n + 1):
        if n % i == 0:
            con += 1
    if con == 2:
        print("El número es primo")
    else:
        print("El número no es primo")

def cuadrado_vi(n):
    v = np.zeros(n)
    for i in range(n):
        v[i] = float(input(f'v_{i+1} = '))
    print('Vector inicial =', v)
    def sqr_vi(v, n):
        s_vi = np.zeros(n)
        for j in range(n):
            s_vi[j] = v[j] ** 2
        return s_vi
    print('Vector final =', sqr_vi(v, n))
    return None

def hallar_IMC(peso,altura):
    imc = peso/pow(altura,2)
    return round(imc,2)
  
def por_grasa(peso,altura,edad,genero):
    def hallar_IMC(peso, altura):
        return round(peso / pow(altura, 2), 2)
    imc = hallar_IMC(peso, altura)
    pg = 1.2*hallar_IMC(peso,altura)+0.23*edad-5.4-genero
    return imc, round(pg, 2)

def cal_calorias_reposo(peso,altura,edad,genero):
    tmb = 10*peso+6.25*altura-5*edad+genero
    return round(tmb,2)

def cal_calorias_actividad(peso, altura, edad, genero, actividad):
    def por_grasa(peso, altura, edad, genero):
        def hallar_IMC(peso, altura):
            return round(peso / pow(altura, 2), 2)
        imc = hallar_IMC(peso, altura)
        tmb = 10 * peso + 6.25 * altura - 5 * edad + genero
        return imc, round(tmb, 2)
    imc, tmb = por_grasa(peso, altura, edad, genero)
    tmb_af = tmb * actividad
    return imc, tmb, round(tmb_af, 2)

def consumo_calorias_adelgazar(peso,altura,edad,genero):
    def cal_calorias_en_actividad(peso, altura, edad, genero, actividad):
        def por_grasa(peso, altura, edad, genero):
            def hallar_IMC(peso, altura):
                return round(peso / pow(altura, 2), 2)
            imc = hallar_IMC(peso, altura)
            tmb = 10 * peso + 6.25 * altura - 5 * edad + genero
            return imc, round(tmb, 2)
        imc, tmb = por_grasa(peso, altura, edad, genero)
        tmb_af = tmb * actividad
        return imc, tmb, round(tmb_af, 2)
    minimo = round(cal_calorias_reposo(peso,altura,edad,genero)*0.80,2)
    maximo = round(cal_calorias_reposo(peso,altura,edad,genero)*0.85,2)
    return (minimo,maximo)
