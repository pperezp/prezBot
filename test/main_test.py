from model.Comandos import Comandos

Comandos.init()
"""
str = Comandos.print()

print(str)
"""
c = Comandos.get("hora")

if c is not None:
    if c.accion is None:
        print(c.mensaje)
    else:
        c.accion()
else:
    print("No se reconoce el comando")