# Neccessário baixar as bibliotecas NUMPY, MATPLOTLIB.PYPLOT e MPL_TOOLKITS>MPLOT3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Solicita que o usuário insira a função e o intervalo e se é raiz quadrada
# Se for elevado usa: **
# Se a função for com o "e" = np.exp
# Se a função for Sen = np.sin
# Se a função for Cos = np.cos
func_str = input("Insira a função (use x, y como variáveis): ")
# Pergunta se a função está em raiz quadrada
sqrt_input = input("A função contém raiz quadrada? (s/n)")
# Pede o intervalo de X
x_min, x_max = input("Insira o intervalo de X (ex: -10, 10): ").split(',')
# Pede o intervalo de Y
y_min, y_max = input("Insira o intervalo de Y (ex: -10, 10): ").split(',')
x_min, x_max, y_min, y_max = float(x_min), float(x_max), float(y_min), float(y_max)

# Caso a função seja em raiz
# Define a função a ser plotada
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

# Cria os pontos para o eixo X e Y
x = np.linspace(x_min, x_max, 100)
y = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x, y)

# Calcula os valores da função para cada ponto (x, y)
Z = f(X, Y)

# Cria o gráfico 3D
figura = plt.figure()
ax = figura.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Define os nomes dos eixos X, Y e Z
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Define o título do gráfico
plt.title(f'Gráfico 3D da função {func_str}')

# Mostra o gráfico
plt.show()