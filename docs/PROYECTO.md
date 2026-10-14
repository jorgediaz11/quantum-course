# Proyecto Final: Búsqueda Cuántica de Perfiles con Algoritmo de Grover

## 1. Planteamiento del problema

Dada una base de datos no estructurada de N registros, localizar el único
registro que cumple una condición específica (el "perfil objetivo").

**Contexto de negocio:** en un dataset de clientes, encontrar el registro
con una combinación exacta de atributos de riesgo, sin índices previos.

## 2. Enfoque clásico vs cuántico

| Enfoque | Complejidad | Consultas (N = 8) |
|---|---|---|
| Clásico (búsqueda lineal) | O(N/2) promedio | 4 |
| Grover (cuántico) | O(√N) | 2 |

**Ventaja asintótica:** aceleración cuadrática. Ver gráfica
`results/proyecto_ventaja_grover.png`.

**Advertencia honesta:** para N pequeños (≤ 16) la ventaja es inexistente.
Este proyecto es **demostrativo/pedagógico**, no de escala industrial.

## 3. Alcance técnico

- **Qubits:** 3 (N = 8 estados posibles)
- **Estado objetivo:** |101⟩
- **Iteraciones de Grover:** 1 (óptima para N = 8)
- **Componentes:** oráculo (CNOT + Z), operador de difusión (H-X-CZ-X-H)

## 4. Criterios de éxito (medibles)

| # | Criterio | Umbral |
|---|---|---|
| 1 | Probabilidad de |101⟩ en simulador ideal | ≥ 90% |
| 2 | Probabilidad de |101⟩ con ruido (GenericBackendV2) | ≥ 70% |
| 3 | Probabilidad de |101⟩ tras mitigación de lectura | ≥ 85% |
| 4 | Estados no objetivo cada uno | ≤ 5% |

## 5. Entregables

- `notebooks/05_proyecto_final.ipynb` — implementación completa
- `results/` — gráficas de resultados ideal / ruidoso / mitigado
- `README.md` — documentación profesional
- Repositorio público en GitHub con release final

## 6. Riesgos identificados

- **Ruido:** con 3 qubits y 1 iteración el circuito es corto, lo que
  mitiga la decoherencia (ventaja de circuitos poco profundos).
- **Profundidad transpilada:** el backend real puede descomponer el oráculo
  en más compuertas de las esperadas, aumentando el error.