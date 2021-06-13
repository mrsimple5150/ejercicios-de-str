print("***String items***")

cadena = "si, profe, es cierto... yo me comí la tarea"
st1 = cadena[10]# obtiene un espacio vacio
st2 = cadena[-1]# obtiene el ultimo caracter. See:st8
st3 = cadena[0:9]# desde el 0 al 9
st4 = cadena[::3]# brinca de 3 en 3
st5 = cadena[::-1]# devuelve la cadena al reves
st6 = cadena[4:9]# desde el 4 al 9

for m in [st1,st2,st3,st4,st5,st6]:
    print(m)

print("\n*****************\n")

s = "   Hola, ¿cómo estás?" # s = 21

st7 = s[::-1]# devuelve la cadena al reves
st8 = s[len(s)-1]#obtiene el ultimo caracter de la cadena. See:st2
st9 = s.count("o")
st10 = s.count("hola")
st11 = s[-4:]#comienza desde el -4 't' y sigue a la derecha
st12 = s[15:]#llega hasta el punto 15 y sigue hasta el final
st13 = s.find("o")#localiza en donde se encuentra y devuelve un numero
st14 = s.strip()
st15 = s.upper()
st16 = st15 == s# False
st17 = s[14:].upper()#obtiene desde el 14 en adelante y lo pone en mayusculas
st18 = len(s)%2!=0# esto es para saber si la cadena es impar / ==1
st19 = s.replace(" ", "*")
st20 = s.replace("z", "Z")#la z no existe en str y no da error. 

for x in [st7,st8,st9,st10,st11,st12,st13,st14,st15,st16,st17,st18,st19,st20]:
    print(x)

print("\n*****************\n")

y = "struggle"
st21 = y[-1] # y[len(y)-1] otra forma de obtener el ultimo caracter

string = "hola"
st22 = string.find("2")# el "2" en formato str no existe por eso retorna -1 no encontro lo que le pedimos

d = "dátiles"
st23 = "a" in ("dátiles")#es solo para saber si se encuentra o no

c = "me gusta programar"
st24 = c.find(" ")
st25 = c.count(" ")

st26 = string[0]#="H"check no puedo guardar la "H" en la posicion 0 da error. See st27

st27 = "C" + string[1:]# agrega la C desde el caracter en posicion 1 

k = "Él está muy cómodo en su sillón."
st28 = k.replace("É","E").replace("á","a").replace("ó","o")

st29 = len(c)%2==0

st30 = c.count("a")+c.count("e")+c.count("i")+c.count("o")+c.count("u")

for r in [st21,st22,st23,st24,st25,st26,st27,st28,st29,st30]:
    print(r)