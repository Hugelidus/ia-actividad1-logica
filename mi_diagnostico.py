# ruff: noqa
# type: ignore
# Actividad 1 · Programación lógica en Python (aima-python)
# Diagnóstico médico con lógica de primer orden
#
# CHULETA (lo que ya sabes)
#   kb.tell(expr("Predicado(A, B)"))   → dictar un hecho a la libreta
#   fol_bc_ask(kb, expr("Pregunta"))   → preguntar (envuélvelo en list() y print())
#   Mayúscula = constante (Gripe) · minúscula = hueco / variable (x)
#   Respuestas:  [{}] = sí  ·  [{x: Resfriado}] = sí, si x vale Resfriado  ·  [] = no
#
# Cada bloque «# %%» se ejecuta por separado con Ctrl + Alt + Enter: si uno falla, los demás siguen.

# %% 0 · Imports
from aima.logic import FolKB, fol_bc_ask
from aima.utils import expr


# %% 1 · Base de conocimiento: gripe y resfriado (40 % de la nota)
kb = FolKB()

# --- Predicado 1: síntomas ----------------------------------------------------
# Un predicado que diga «X es un síntoma». Solo habla de UNA cosa.
# Síntomas: fiebre, tos, dolor de garganta (los nombres no pueden llevar espacios).
# TU TURNO (3 líneas):
kb.tell(expr("Sintoma(Fiebre)"))
kb.tell(expr("Sintoma(Tos)"))
kb.tell(expr("Sintoma(DolorDeGarganta)"))

# --- Predicado 2: enfermedades ------------------------------------------------
# Igual que el anterior, pero «X es una enfermedad». Enfermedades: gripe, resfriado.
# TU TURNO (2 líneas):
kb.tell(expr("Enfermedad(Gripe)"))
kb.tell(expr("Enfermedad(Resfriado)"))

# --- Predicado 3: causas ------------------------------------------------------
# Causa(enfermedad, síntoma), siempre en ese orden.
kb.tell(expr("Causa(Gripe, Fiebre)"))
kb.tell(expr("Causa(Resfriado, Tos)"))
# TU TURNO: faltan 3 (gripe → tos, gripe → dolor de garganta, resfriado → dolor de garganta)
kb.tell(expr("Causa(Gripe, Tos)"))
kb.tell(expr("Causa(Gripe, DolorDeGarganta)"))
kb.tell(expr("Causa(Resfriado, DolorDeGarganta)"))

# %% 2 · Comprobar la base
# Antes de la consulta que piden, comprueba que has dictado bien todo.
# TU TURNO: una consulta que saque TODOS los síntomas y otra con TODAS las enfermedades.
# ✗ CORRECCIÓN (pendiente): consultas y predicciones bien, pero no se ve nada en la terminal: falta envolverlas en print(list(...)), como en la chuleta del final.
fol_bc_ask(
    kb, expr("Sintoma(x)")
)  # Creo que imprime: [{x: Fiebre}, {x: Tos}, {x: DolorDeGarganta}]
fol_bc_ask(kb, expr("Enfermedad(x)"))  # Creo que imprime: [{x: Gripe}, {x: Resfriado}]


# %% 3 · Consulta pedida: todos los síntomas del resfriado
# Pista: es como Causa(x, Tos), pero el hueco va al otro lado.
# Creo que imprime: ...
# TU TURNO:
# ✗ CORRECCIÓN (pendiente): consulta correcta (el hueco va en el síntoma), pero igual que en el bloque 2: falta print(list(...)).
fol_bc_ask(
    kb, expr("Causa(Resfriado, x)")
)  # Creo que imprime: [{x: Tos}, {x: DolorDeGarganta}]

# %% 4 · Mi enfermedad (20 % de la nota)
# Crea OTRA base de conocimiento (kb2 = FolKB()) para una enfermedad que elijas tú.
# Primero el plan, sin código (rellénalo):
#   Enfermedad: Parkinson
#   Síntomas: temblor, rigidez, lentitud de movimientos
#   ¿Algún predicado nuevo? (factores de riesgo, pruebas, tratamiento…)
#   Factores de riesgo: edad avanzada, antecedentes familiares
#   Pruebas: examen neurológico, resonancia magnética
# TU TURNO:
# ✓ Buen plan: añadir FactorDeRiesgo y Prueba hace la base más completa (suma en «creación detallada»).
# ✓ Corregido: base propia kb2, síntomas unidos con Causa y consulta con predicción acertada. (Cuando lo leas, borra las dos líneas de ✓.)

kb2 = FolKB()
kb2.tell(expr("Enfermedad(Parkinson)"))
# ✗ CORRECCIÓN (coherencia, cuenta en la nota): aquí Sintoma tiene DOS argumentos y en el bloque 1 UNO, Sintoma(Fiebre). Un predicado debe significar lo mismo en todo el trabajo; además, «de qué enfermedad» ya lo dicen tus Causa de abajo. Elige una forma y úsala igual en las dos bases.
kb2.tell(expr("Sintoma(Temblor, Parkinson)"))
kb2.tell(expr("Sintoma(Rigidez, Parkinson)"))
kb2.tell(expr("Sintoma(LentitudDeMovimientos, Parkinson)"))
kb2.tell(expr("Causa(Parkinson, Temblor)"))
kb2.tell(expr("Causa(Parkinson, Rigidez)"))
kb2.tell(expr("Causa(Parkinson, LentitudDeMovimientos)"))
kb2.tell(expr("FactorDeRiesgo(Parkinson, EdadAvanzada)"))
kb2.tell(expr("FactorDeRiesgo(Parkinson, AntecedentesFamiliares)"))
kb2.tell(expr("Prueba(Parkinson, ExamenNeurologico)"))
kb2.tell(expr("Prueba(Parkinson, ResonanciaMagnetica)"))

# Consulta: todos los síntomas del Parkinson
# Creo que imprime: [{x: Temblor}, {x: Rigidez}, {x: LentitudDeMovimientos}]
print(list(fol_bc_ask(kb2, expr("Causa(Parkinson, x)"))))


# %% Paso 1 · lo que probaste para aprender (bórralo al final, no va en la entrega)
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Fiebre)"))))     → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(Resfriado, Tos)"))))    → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(x, Tos)"))))            → [{x: Resfriado}]   sí, si x = Resfriado
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Tos)"))))        → []                 no
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, x)"))))          → [{x: Fiebre}, {x: Tos}, {x: DolorDeGarganta}]   sí, si x vale alguno de esos
