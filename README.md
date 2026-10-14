# 🔮 Proyecto Final: Búsqueda Cuántica con Algoritmo de Grover

## 📋 Descripción del Proyecto
Este proyecto implementa el **Algoritmo de Grover** para resolver un problema de búsqueda no estructurada. Dada una base de datos de $N=8$ elementos (representados por 3 qubits), el objetivo es localizar un registro específico (estado `|101⟩`) con una aceleración cuadrática respecto a los métodos clásicos.

El proyecto no solo demuestra la implementación teórica, sino que somete el circuito a condiciones de **ruido realista** (simulando hardware NISQ) y aplica técnicas de **mitigación de errores de lectura** para recuperar la fidelidad del resultado.

---

## 🏗️ Estructura del Proyecto
```text
quantum-course/
├── data/               # (Reservado para datasets si se requiere)
├── docs/
│   └── PROYECTO.md     # Especificación técnica y criterios de éxito
├── notebooks/
│   ├── 01_fundamentos_cuant.ipynb       # Fase 2: Fundamentos y Esfera de Bloch
│   ├── 02_operaciones_multiqubit.ipynb  # Fase 3: Entrelazamiento y Teleportación
│   ├── 03_algoritmos_cuant.ipynb        # Fase 4: Deutsch-Jozsa, QFT, Grover, Shor
│   ├── 04_hardware_real.ipynb           # Fase 5: Análisis de ruido y mitigación
│   └── 05_proyecto_final.ipynb          # Fase 6: Implementación completa de Grover
├── results/
│   ├── proyecto_ventaja_grover.png      # Gráfica de complejidad O(N) vs O(√N)
│   ├── proyecto_grover_ideal.png        # Resultados del simulador ideal
│   └── proyecto_grover_comparativo.png  # Comparativa: Ideal vs Ruidoso vs Mitigado
├── src/                # Scripts reutilizables de Python
├── .gitignore          # Reglas de exclusión de Git
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Este archivo