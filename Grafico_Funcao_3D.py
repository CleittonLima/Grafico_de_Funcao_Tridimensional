import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# solicita que o usuário insira a função e o intervalo
# Se for elevado usa: **
# Se a função for com o "e" = np.exp
# Se a função for Sen = np.sin
# Se a função for Cos = np.cos
func_str = input("Insira a função (use x, y como variáveis): ")
sqrt_input = input("A função contém raiz quadrada? (s/n)")
x_min, x_max = input("Insira o intervalo de X (ex: -10, 10): ").split(',')
y_min, y_max = input("Insira o intervalo de Y (ex: -10, 10): ").split(',')
x_min, x_max, y_min, y_max = float(x_min), float(x_max), float(y_min), float(y_max)

# converte a string do intervalo em uma tupla

# define a função a ser plotada
def f(x, y):
    if sqrt_input.lower() == 's':
        try:
            return eval(func_str.replace('sqrt', 'np.sqrt'))
        except:
            return np.nan
    else:
        try:
            return eval(func_str)
        except:
            return np.nan

# cria os pontos para o eixo x e y
x = np.linspace(x_min, x_max, 100)
y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x, y)

# calcula os valores da função para cada ponto (x, y)
Z = f(X, Y)

# cria o gráfico 3D
figura = plt.figure()
ax = figura.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# define os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# define o título do gráfico
plt.title(f'Gráfico 3D da função {func_str}')

# mostra o gráfico
plt.show()
