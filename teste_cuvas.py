import numpy as np
import matplotlib.pyplot as plt

def de_casteljau(points, t):
    while len(points) > 1:
        new_points = []
        for i in range(len(points) - 1):
            p_i = points[i]
            p_i_plus_1 = points[i + 1]
            new_point = tuple((1 - t) * np.array(p_i) + t * np.array(p_i_plus_1))
            new_points.append(new_point)
        points = new_points
    return points[0]

def rasterize_bezier(points, num_segments):
    curve_points = []
    t_values = np.linspace(0, 1, num_segments)
    
    for t in t_values:
        point = de_casteljau(points, t)
        curve_points.append(point)
    
    rasterized_points = []
    
    for i in range(len(curve_points) - 1):
        p0 = curve_points[i]
        p1 = curve_points[i + 1]
        rasterized_segment = rasterize_line(p0, p1)
        rasterized_points.extend(rasterized_segment)
    
    return rasterized_points

def rasterize_line(p0, p1):
    x0, y0 = int(p0[0]), int(p0[1])
    x1, y1 = int(p1[0]), int(p1[1])
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    steep = dy > dx
    if steep:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    swapped = x0 > x1
    if swapped:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    error = dx // 2
    y = y0
    y_step = 1 if y0 < y1 else -1
    rasterized_points = []
    
    for x in range(x0, x1 + 1):
        point = (y, x) if steep else (x, y)
        rasterized_points.append(point)
        error -= dy
        if error < 0:
            y += y_step
            error += dx
    
    return rasterized_points

# Exemplo de uso

# Pontos de controle da curva de Bézier
control_points = [(0, 0), (2, 4), (8, 5)]

# Rasteriza a curva de Bézier com 100 segmentos
rasterized_curve = rasterize_bezier(control_points, 100)

# Plotagem dos pontos rasterizados
x_values, y_values = zip(*rasterized_curve)
plt.plot(x_values, y_values, 'ro')
plt.show()
