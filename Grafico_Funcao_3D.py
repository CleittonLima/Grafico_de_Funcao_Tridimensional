# É preciso baixar as bibliotecas NUMPY e MATPLOTLIB.PYPLOT
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Função 1) z = −xye^−x^2−y^2 = -x*y*np.exp(-x**2-y**2)
# Função 2) z = sen(xy) = np.sin(x*y)

# solicita que o usuário insira a função e o intervalo
# Se for elevado usa: **
# Se a função for com o "e" = np.exp
# Se a função for Sen = np.sin
# Se a função for Cos = np.cos
função = input("Insira a função de duas variáveis (x,y): ")
raizQuadrada = input("A função contém raiz quadrada? (s/n): ")
x_min, x_max = input("Insira o intervalo de X (ex: -10, 10): ").split(',')
y_min, y_max = input("Insira o intervalo de Y (ex: -10, 10): ").split(',')
x_min, x_max, y_min, y_max = float(x_min), float(x_max), float(y_min), float(y_max)

# define a função a ser plotada
def f(x, y):
    if raizQuadrada.lower() == 's':
        try:
            return eval(função.replace('sqrt', 'np.sqrt'))
        except:
            return np.nan
    else:
        try:
            return eval(função)
        except:
            return np.nan

# cria os pontos para o eixo x e y
x = np.linspace(x_min, x_max, 1000)
y = np.linspace(y_min, y_max, 1000)
X, Y = np.meshgrid(x, y)

# calcula os valores da função para cada ponto (x, y)
Z = f(X, Y)

# cria o gráfico 3D
figura = plt.figure()
ax = figura.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# cria o gráfico de nível
figura2, ax2 = plt.subplots()
ax2.contour(X, Y, Z, levels=10, cmap='viridis')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title(f'Curva de nível da função {função}')


# define os rótulos dos eixos
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# define o título do gráfico
plt.title(f'Gráfico 3D da função {função}')

# ajusta a proporção dos eixos
# Caso queira testar sem isso é só comentar essa perte
# max_range = np.array([X.max()-X.min(), Y.max()-Y.min(), Z.max()-Z.min()]).max()
# Xn = 0.5*max_range*(X-X.mean())/max_range + X.mean()
# Yn = 0.5*max_range*(Y-Y.mean())/max_range + Y.mean()
# Zn = 0.1*max_range*(Z-Z.mean())/max_range + Z.mean()
# # O 0.1 é o tamanho de Z, pois sem esse valor no gráfico ele fica esticado
# max_range = np.array([Xn.max()-Xn.min(), Yn.max()-Yn.min(), Zn.max()-Zn.min()]).max()
# ax.set_box_aspect([np.ptp(Xn), np.ptp(Yn), 0.1*max_range])

# mostra o gráfico
plt.show()
