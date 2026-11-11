# ruff: noqa
# type: ignore
# Actividad 1 · Programación lógica en Python (aima-python)
# Diagnóstico médico con lógica de primer orden

# region CORRECCIONES · ronda 2
# ✗ 1 · Bloques 2 y 3: no se ve nada en la terminal. Las consultas y las predicciones están bien, pero falta envolverlas en print(list(...)), como en la chuleta.
# ✗ 2 · Bloque 4 (coherencia, cuenta en la nota): Sintoma tiene DOS argumentos y en el bloque 1 UNO. Un predicado debe significar lo mismo en todo el trabajo, y «de qué enfermedad» ya lo dicen tus Causa. Elige una forma y úsala igual en las dos bases.
# ✓ 3 · Bloque 4: base propia kb2, síntomas unidos con Causa y predicción acertada. Buen plan: FactorDeRiesgo y Prueba suman en «creación detallada».
# endregion

# region CHULETA
# kb.tell(expr("Predicado(A, B)"))   → dictar un hecho a la libreta
# fol_bc_ask(kb, expr("Pregunta"))   → preguntar (envuélvelo en print(list(...)))
# Mayúscula = constante (Gripe) · minúscula = hueco / variable (x)
# Respuestas:  [{}] = sí  ·  [{x: Resfriado}] = sí, si x vale Resfriado  ·  [] = no
# Cada bloque «# %%» se ejecuta por separado con Ctrl + Alt + Enter: si uno falla, los demás siguen.
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
fol_bc_ask(  # ✗ 1
    kb, expr("Sintoma(x)")
)  # Creo que imprime: [{x: Fiebre}, {x: Tos}, {x: DolorDeGarganta}]
fol_bc_ask(kb, expr("Enfermedad(x)"))  # ✗ 1 · Creo que imprime: [{x: Gripe}, {x: Resfriado}]
# endregion


# %% 3 · Consulta pedida: todos los síntomas del resfriado
# Pista: es como Causa(x, Tos), pero el hueco va al otro lado.
# region TU TURNO
fol_bc_ask(  # ✗ 1
    kb, expr("Causa(Resfriado, x)")
)  # Creo que imprime: [{x: Tos}, {x: DolorDeGarganta}]
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
kb2.tell(expr("Sintoma(Temblor, Parkinson)"))  # ✗ 2
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
# endregion


# %% Paso 1 · lo que probaste para aprender
# region APUNTES (bórralo al final, no va en la entrega)
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Fiebre)"))))     → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(Resfriado, Tos)"))))    → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(x, Tos)"))))            → [{x: Resfriado}]   sí, si x = Resfriado
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Tos)"))))        → []                 no
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, x)"))))          → [{x: Fiebre}, {x: Tos}, {x: DolorDeGarganta}]   sí, si x vale alguno de esos
# endregion
