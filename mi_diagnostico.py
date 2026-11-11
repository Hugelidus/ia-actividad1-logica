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


# --- Predicado 2: enfermedades ------------------------------------------------
# Igual que el anterior, pero «X es una enfermedad». Enfermedades: gripe, resfriado.
# TU TURNO (2 líneas):


# --- Predicado 3: causas ------------------------------------------------------
# Causa(enfermedad, síntoma), siempre en ese orden.
kb.tell(expr("Causa(Gripe, Fiebre)"))
kb.tell(expr("Causa(Resfriado, Tos)"))
# TU TURNO: faltan 3 (gripe → tos, gripe → dolor de garganta, resfriado → dolor de garganta)


# %% 2 · Comprobar la base
# Antes de la consulta que piden, comprueba que has dictado bien todo.
# TU TURNO: una consulta que saque TODOS los síntomas y otra con TODAS las enfermedades.
# Creo que imprime: ...


# %% 3 · Consulta pedida: todos los síntomas del resfriado
# Pista: es como Causa(x, Tos), pero el hueco va al otro lado.
# Creo que imprime: ...
# TU TURNO:


# %% 4 · Mi enfermedad (20 % de la nota)
# Crea OTRA base de conocimiento (kb2 = FolKB()) para una enfermedad que elijas tú.
# Primero el plan, sin código (rellénalo):
#   Enfermedad: ...
#   Síntomas: ...
#   ¿Algún predicado nuevo? (factores de riesgo, pruebas, tratamiento…)
# TU TURNO:


# %% Paso 1 · lo que probaste para aprender (bórralo al final, no va en la entrega)
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Fiebre)"))))     → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(Resfriado, Tos)"))))    → [{}]               sí
# print(list(fol_bc_ask(kb, expr("Causa(x, Tos)"))))            → [{x: Resfriado}]   sí, si x = Resfriado
# print(list(fol_bc_ask(kb, expr("Causa(Gripe, Tos)"))))        → []                 no
