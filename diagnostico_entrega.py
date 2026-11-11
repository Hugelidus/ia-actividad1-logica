# Actividad 1 · Programación lógica en Python (aima-python)
# Diagnóstico médico con lógica de primer orden
# Autor: Hugo Gómez Bande

# ── Importaciones ─────────────────────────────────────────────────────────
# FolKB: base de conocimiento de lógica de primer orden (First-Order Logic Knowledge Base)
# fol_bc_ask: consulta la base por encadenamiento hacia atrás (backward chaining)
# expr: convierte un texto en una expresión lógica que aima entiende
from aima.logic import FolKB, fol_bc_ask
from aima.utils import expr


# ══ PARTE 1 · Gripe y resfriado ═══════════════════════════════════════════

# Base de conocimiento: empieza vacía y se le añaden hechos con tell()
kb = FolKB()

# Predicado Sintoma(x): «x es un síntoma».
# Un solo argumento: clasifica un objeto. Las constantes van en mayúscula
# y sin espacios (DolorDeGarganta).
kb.tell(expr("Sintoma(Fiebre)"))
kb.tell(expr("Sintoma(Tos)"))
kb.tell(expr("Sintoma(DolorDeGarganta)"))

# Predicado Enfermedad(x): «x es una enfermedad».
kb.tell(expr("Enfermedad(Gripe)"))
kb.tell(expr("Enfermedad(Resfriado)"))

# Predicado Causa(e, s): «la enfermedad e causa el síntoma s».
# Dos argumentos: es una relación, siempre en el orden (enfermedad, síntoma).
kb.tell(expr("Causa(Gripe, Fiebre)"))
kb.tell(expr("Causa(Gripe, Tos)"))
kb.tell(expr("Causa(Gripe, DolorDeGarganta)"))
kb.tell(expr("Causa(Resfriado, Tos)"))
kb.tell(expr("Causa(Resfriado, DolorDeGarganta)"))

# Comprobación de la base: todos los síntomas y todas las enfermedades.
# x (en minúscula) es una variable: fol_bc_ask busca los valores que la
# hacen verdadera y devuelve un generador de sustituciones {x: valor};
# list() las recoge todas para poder imprimirlas.
print(list(fol_bc_ask(kb, expr("Sintoma(x)"))))
print(list(fol_bc_ask(kb, expr("Enfermedad(x)"))))

# Consulta pedida: todos los síntomas que produce el resfriado.
# La enfermedad es fija (Resfriado) y el síntoma es la variable.
print(list(fol_bc_ask(kb, expr("Causa(Resfriado, x)"))))


# ══ PARTE 2 · Enfermedad elegida: Parkinson ═══════════════════════════════

# Base de conocimiento independiente para la segunda enfermedad
kb2 = FolKB()

# Mismos predicados y con el mismo significado que en la parte 1
kb2.tell(expr("Enfermedad(Parkinson)"))
kb2.tell(expr("Sintoma(Temblor)"))
kb2.tell(expr("Sintoma(Rigidez)"))
kb2.tell(expr("Sintoma(LentitudDeMovimientos)"))
kb2.tell(expr("Causa(Parkinson, Temblor)"))
kb2.tell(expr("Causa(Parkinson, Rigidez)"))
kb2.tell(expr("Causa(Parkinson, LentitudDeMovimientos)"))

# Predicado nuevo FactorDeRiesgo(e, f): f aumenta la probabilidad de
# padecer e, pero no la causa (por eso no se expresa con Causa).
kb2.tell(expr("FactorDeRiesgo(Parkinson, EdadAvanzada)"))
kb2.tell(expr("FactorDeRiesgo(Parkinson, AntecedentesFamiliares)"))

# Predicado nuevo Prueba(e, p): prueba p que se usa para estudiar e.
kb2.tell(expr("Prueba(Parkinson, ExamenNeurologico)"))
kb2.tell(expr("Prueba(Parkinson, ResonanciaMagnetica)"))

# Consultas: síntomas, factores de riesgo y pruebas del Parkinson
print(list(fol_bc_ask(kb2, expr("Causa(Parkinson, x)"))))
print(list(fol_bc_ask(kb2, expr("FactorDeRiesgo(Parkinson, x)"))))
print(list(fol_bc_ask(kb2, expr("Prueba(Parkinson, x)"))))
