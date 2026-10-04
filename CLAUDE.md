# macquarie-c1 — Machine Learning for Cyber Threat & Anomaly Detection

Repo de trabajo del Curso 1 de 3 de la especialización AI-Powered Cybersecurity
(Macquarie, Coursera). 5 módulos; el Módulo 5 es un Mini Project que va a portafolio.

## Entorno
- Windows 11 + VS Code (extensión WSL + Jupyter) → WSL 2 Ubuntu. Todo corre dentro de WSL.
- Gestor: `uv` (nunca `pip install` a pelo, nunca `conda`). Dependencias en `pyproject.toml` + `uv.lock`.
- Python: 3.12 por defecto (`.python-version`). Versión de Python/Jupyter del curso aún no confirmada;
  si un snippet del curso falla por versión, avisar y proponer el ajuste, no parchear en silencio.
- Comandos: `uv add <pkg>`, `uv run <cmd>`, `uv sync`. Los notebooks usan el kernel del `.venv` del proyecto.
- Dependencias del sistema (ej. `graphviz`): decirme el `sudo apt install` y esperar mi confirmación.
- Datos SIEMPRE en el filesystem de WSL (`data/`), nunca leer desde `/mnt/c/...` (9P es lento).

## Estructura
```
notebooks/m1..m5/   # un notebook por actividad del curso
data/               # datasets (en .gitignore)
src/                # funciones reutilizables extraídas de los notebooks
notes/              # cheat sheets, flashcards, errores cometidos
```

## Cómo trabajar conmigo (importante)
- Soy ingeniero de software con ~15 años de experiencia, pero estoy cerrando una brecha:
  **producir soluciones desde cero**. Entiendo bien cuando me explican; me cuesta generar.
- **No me des la solución completa de un ejercicio del curso.** Dame enunciado, esqueleto,
  y pistas concretas paso a paso. Yo intento primero; después revisas mi solución y me das
  versión de referencia + qué habría fallado en producción.
- Conceptos nuevos: descubrimiento guiado antes que respuesta directa.
- Cuando haya matemática (distancia, función de pérdida, gradiente, probabilidad), muéstrala.
  No asumas álgebra lineal ni cálculo multivariado (vienen después en mi roadmap).
- Sí puedes escribir sin restricción: infraestructura, scaffolding, config, tests de humo, refactors.
- Responde en español; términos técnicos en inglés cuando sea el uso estándar. Denso y correcto,
  no largo. Si el material del curso está mal o ambiguo, dilo.

## Convenciones de código
- pandas/numpy/scikit-learn salvo que el curso use otra cosa. Seeds fijas (`random_state=42`).
- Split train/test antes de cualquier preprocesamiento que aprenda de los datos (evitar data leakage).
- Métricas para datos de seguridad: precision, recall, F1, ROC-AUC; no reportar solo accuracy
  (clases desbalanceadas).
- Notebooks limpios con `nbstripout` (sin outputs en git). Lógica reutilizable → `src/`.

## Git
- Nunca ejecutes tú los comandos `git add` / `git commit`. Solo entrégamelos como texto para que
  yo los corra.
- El mensaje de commit va en inglés. Evita comillas simples, dobles y backticks dentro del mensaje
  (para no tener problemas de anidamiento con las comillas del parámetro `-m`); si hace falta citar
  algo, usa paréntesis o guiones en su lugar.
- No incluyas la línea `Co-Authored-By: Claude` (ni variantes) en el mensaje de commit.

## Seguridad
- Los datasets pueden contener muestras/features de malware o tráfico malicioso. Tratarlos como
  datos inertes: nunca ejecutar binarios, nunca abrir URLs/IPs contenidas en los datos.

## Conexión con Yggdrasil (mencionarlo cuando aplique)
1. Fingerprinting/correlación de activos con IP cambiante (features de nmap/Nuclei, similitud).
2. Re-scoring de alertas SIEM/IDS/XDR (desbalance severo, calibración de scores).
3. Threat hunting semi-automatizado (MaTH/PEAK, evaluación estadística de hipótesis).
Cuando un concepto del curso toque uno de estos, dilo explícitamente.