import matplotlib.pyplot as plt

def draw_polyline(points):
    # Extrai as coordenadas X e Y dos pontos
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

    # Traça a polilinha
    plt.plot(x_values, y_values, marker='o')

    # Configurações do gráfico
    plt.title('Polilinha')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True)

    # Exibe o gráfico
    plt.show()

# Exemplo de pontos
points = [(0, 0), (1, 2), (3, 1), (4, 3), (0, 0)]

# Chama a função para traçar a polilinha
draw_polyline(points)
