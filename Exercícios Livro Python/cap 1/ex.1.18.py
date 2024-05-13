from math import pi

angulo_rad = float(input("Digite o ângulo em radianos: "))

angulo_graus = angulo_rad * 180 / pi

print(f"O ângulo {angulo_rad:.2f} radianos é equivalente a {angulo_graus:.2f} graus.")