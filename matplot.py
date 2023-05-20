import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        dx, dy = dy, dx
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    y = y0
    ystep = 1 if y0 < y1 else -1
    d_error = 2 * dy - dx
    points = []
    for x in range(x0, x1 + 1):
        points.append((y, x) if steep else (x, y))
        d_error += 2 * dy
        if d_error > 0:
            y += ystep
            d_error -= 2 * dx
    return points

# Coordenadas iniciais e finais
x0, y0 = 2, 2
x1, y1 = 6, 3
points = bresenham_line(x0, y0, x1, y1)

print(points)

fig, ax = plt.subplots()
ax.grid(True, which='both', color='gray', linestyle='--')
# Plotar os pontos
x_values, y_values = zip(*points)
plt.plot(x_values, y_values, marker='o')

# Definir limites do gráfico
plt.xlim(min(x0, x1) - 1, max(x0, x1) + 1)
plt.ylim(min(y0, y1) - 1, max(y0, y1) + 1)

# Exibir o gráfico
plt.show()
