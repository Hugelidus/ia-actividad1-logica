# ruff: noqa
# type: ignore
# Actividad 1 · Programación lógica en Python (aima-python)
# Diagnóstico médico con lógica de primer orden

# region CORRECCIONES · ronda 3
# ✓ 1 · Bloques 2 y 3: ya se ven las respuestas con print(list(...)) y las tres predicciones han clavado la salida.
# ✓ 2 · Bloque 4: Sintoma con un solo argumento en las dos bases. Coherente: Sintoma dice qué es un síntoma y Causa, de qué enfermedad.
# endregion

# region CHULETA
# kb.tell(expr("Predicado(A, B)"))   → dictar un hecho a la libreta
# fol_bc_ask(kb, expr("Pregunta"))   → preguntar (envuélvelo en print(list(...)))
# Mayúscula = constante (Gripe) · minúscula = hueco / variable (x)
# Respuestas:  [{}] = sí  ·  [{x: Resfriado}] = sí, si x vale Resfriado  ·  [] = no
# Cada bloque (las líneas con %% y título) se ejecuta por separado con Ctrl + Alt + Enter: si uno falla, los demás siguen.
# endregion


# %% 0 · Imports
from aima.logic import FolKB, fol_bc_ask
from aima.utils import expr


# %% 1 · Base de conocimiento: gripe y resfriado (40 % de la nota)
kb = FolKB()

# Predicado 1 · síntomas: «X es un síntoma» (habla de UNA cosa). Síntomas: fiebre, tos, dolor de garganta.
# region TU TURNO
kb.tell(expr("Sintoma(Fiebre)"))
kb.tell(expr("Sintoma(Tos)"))
kb.tell(expr("Sintoma(DolorDeGarganta)"))
# endregion

# Predicado 2 · enfermedades: «X es una enfermedad». Enfermedades: gripe, resfriado.
# region TU TURNO
kb.tell(expr("Enfermedad(Gripe)"))
kb.tell(expr("Enfermedad(Resfriado)"))
# endregion

# Predicado 3 · causas: Causa(enfermedad, síntoma), siempre en ese orden. Son 5.
# region TU TURNO
kb.tell(expr("Causa(Gripe, Fiebre)"))
kb.tell(expr("Causa(Resfriado, Tos)"))
kb.tell(expr("Causa(Gripe, Tos)"))
kb.tell(expr("Causa(Gripe, DolorDeGarganta)"))
kb.tell(expr("Causa(Resfriado, DolorDeGarganta)"))
# endregion


# %% 2 · Comprobar la base
# Antes de la consulta que piden, comprueba que has dictado todo bien: una consulta con TODOS los síntomas y otra con TODAS las enfermedades.
# region TU TURNO
# Creo que imprime: [{x: Fiebre}, {x: Tos}, {x: DolorDeGarganta}]
print(list(fol_bc_ask(kb, expr("Sintoma(x)"))))
# Creo que imprime: [{x: Gripe}, {x: Resfriado}]
print(list(fol_bc_ask(kb, expr("Enfermedad(x)"))))
# endregion


# %% 3 · Consulta pedida: todos los síntomas del resfriado
# Pista: es como Causa(x, Tos), pero el hueco va al otro lado.
# region TU TURNO
# Creo que imprime: [{x: Tos}, {x: DolorDeGarganta}]
print(list(fol_bc_ask(kb, expr("Causa(Resfriado, x)"))))
# endregion


# %% 4 · Mi enfermedad (20 % de la nota)
# OTRA base de conocimiento (kb2) para una enfermedad elegida por ti. Tu plan:
#   Enfermedad: Parkinson
#   Síntomas: temblor, rigidez, lentitud de movimientos
#   Factores de riesgo: edad avanzada, antecedentes familiares
#   Pruebas: examen neurológico, resonancia magnética
# region TU TURNO
kb2 = FolKB()
kb2.tell(expr("Enfermedad(Parkinson)"))
kb2.tell(expr("Sintoma(Temblor)"))
kb2.tell(expr("Sintoma(Rigidez)"))
kb2.tell(expr("Sintoma(LentitudDeMovimientos)"))
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
# endregion


# %% Paso 1 · lo que probaste para aprender
# region APUNTES (bórralo al final, no va en la entrega)
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Fiebre)"))))     → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(Resfriado, Tos)"))))    → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(x, Tos)"))))            → [{x: Resfriado}]   sí, si x = Resfriado
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Tos)"))))        → []                 no
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, x)"))))          → [{x: Fiebre}, {x: Tos}, {x: DolorDeGarganta}]   sí, si x vale alguno de esos
# endregion
