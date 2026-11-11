# Actividad 1 - Programación lógica en Python (aima-python)
# Paso 1: mi primera base de conocimiento

from aima.logic import FolKB, fol_bc_ask
from aima.utils import expr

# 1. Crea la base de conocimiento (empieza vacía)

kb = FolKB()

# 2. Añade dos hechos con kb.tell(expr("..."))
#    - la gripe causa fiebre
#    - el resfriado causa tos
kb.tell(expr("Causa(Gripe, Fiebre)"))
kb.tell(expr("Causa(Resfriado, Tos)"))

# 3. Consulta
print(list(fol_bc_ask(kb, expr("Causa(Gripe, Fiebre)"))))


print(list(fol_bc_ask(kb, expr("Causa(Resfriado, Tos)"))))
# Devolvera True, ya que la base de conocimiento contiene el hecho Causa(Resfriado, Tos)
print(list(fol_bc_ask(kb, expr("Causa(x, Tos)"))))
# devolvera resfriado, ya que la base de conocimiento contiene el hecho Causa(Resfriado, Tos)
print(list(fol_bc_ask(kb, expr("Causa(Gripe, Tos)"))))
# Devolvera False, ya que la base de conocimiento no contiene el hecho Causa(Gripe, Tos)
