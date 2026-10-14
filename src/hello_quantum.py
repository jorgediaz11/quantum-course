"""
Tarea 1.5: Hello Quantum
Objetivo: Verificar la instalación ejecutando un circuito de superposición y medición.

Nota: Si el editor marca "Import could not be resolved", instala las dependencias con:
    pip install qiskit qiskit-aer
y asegúrate de seleccionar el intérprete de Python correcto (entorno virtual).
"""
try:
    from qiskit import QuantumCircuit  # pyright: ignore[reportMissingImports]
    from qiskit_aer import AerSimulator  # pyright: ignore[reportMissingImports]
except ImportError as exc:
    raise SystemExit(
        "❌ No se encontró Qiskit. Instálalo ejecutando:\n"
        "   pip install qiskit qiskit-aer"
    ) from exc

def main():
    print("🌌 Iniciando simulación cuántica...\n")
    
    # 1. Crear un circuito con 1 qubit (para procesar) y 1 bit clásico (para guardar el resultado)
    qc = QuantumCircuit(1, 1)
    
    # 2. Aplicar la compuerta Hadamard (H) al qubit 0
    # Esto pone al qubit en superposición: 50% probabilidad de ser 0, 50% de ser 1
    qc.h(0)
    
    # 3. Medir el qubit 0 y guardar el resultado en el bit clásico 0
    qc.measure(0, 0)
    
    # 4. Configurar el simulador
    simulator = AerSimulator()
    
    # 5. Ejecutar el circuito 1000 veces ("shots") para ver la distribución estadística
    print("Ejecutando 1000 mediciones (shots)...")
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    # 6. Mostrar resultados
    print("\n✅ ¡Hola Mundo Cuántico!")
    print(f"Resultados obtenidos: {counts}")
    
    # Verificación de éxito
    total_shots = sum(counts.values())
    prob_0 = counts.get('0', 0) / total_shots * 100
    prob_1 = counts.get('1', 0) / total_shots * 100
    
    print(f"\n📊 Estadísticas:")
    print(f"   - Probabilidad de '0': {prob_0:.1f}%")
    print(f"   - Probabilidad de '1': {prob_1:.1f}%")
    print("\n🎉 ¡Fase 1 completada exitosamente! El entorno cuántico está 100% operativo.")

if __name__ == "__main__":
    main()