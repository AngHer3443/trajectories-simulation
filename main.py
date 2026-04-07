import numpy as np
import matplotlib.pyplot as plt

# Tiempo
dt = 0.1
steps = 300

# Posiciones iniciales
target = np.array([0.0, 0.0])
pursuer = np.array([-50.0, -50.0])

# Velocidades
v_target = np.array([0.4, 0.3])  # movimiento recto
v_pursuer = 3

# Historial
target_path = []
pursuer_path = []

for _ in range(steps):
    # Guardar posiciones
    target_path.append(target.copy())
    pursuer_path.append(pursuer.copy())

    # Movimiento del target
    target = target + v_target * dt

    # Dirección hacia el target
    direction = target - pursuer
    distance = np.linalg.norm(direction)

    if distance > 0:
        direction = direction / distance  # normalizar

    # Movimiento del perseguidor
    pursuer = pursuer + v_pursuer * direction * dt

# Convertir a arrays
target_path = np.array(target_path)
pursuer_path = np.array(pursuer_path)

# Graficar
plt.plot(target_path[:,0], target_path[:,1], label="Target")
plt.plot(pursuer_path[:,0], pursuer_path[:,1], label="Pursuer")
plt.legend()
plt.title("Pure Pursuit Simulation")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
plt.savefig("results/trajectory.png")
plt.show()