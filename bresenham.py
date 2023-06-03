from grid import Grid
import sys
import numpy as np
print(sys.getrecursionlimit())

grid = Grid(extent=15, size=500)

def my_render_cells_algorithm(selected_cells, rendered_cells, parameters):
    for cell in selected_cells:
        grid.render_cell(cell)

def bresenham_line(selected_cells, rendered_cells, parameters):
    print(selected_cells)
    x0, y0 = selected_cells[0]
    x1, y1 = selected_cells[1]

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
    for c in points:
	    grid.render_cell(c)

def polilinha(selected_cells, rendered_cells, parameters):
    print(selected_cells)
    for i in range(0, len(selected_cells) - 1):
        bresenham_line([selected_cells[i], selected_cells[i + 1]], rendered_cells, parameters)

def recorte(selected_cells, rendered_cells, parameters):
    print(selected_cells)
    xMin, yMin = selected_cells[0]
    xMax, yMax = selected_cells[1]
    for i in rendered_cells:
        x, y = i
        if ((xMin <= x and x <= xMax) and (yMin <= y and y <= yMax)):
            continue
        grid.clear_cell((x, y))

        # bresenham_line([selected_cells[i], selected_cells[i + 1]], rendered_cells, parameters)

def preencher_recursivo(x, y, rendered_cells):
    if x > 10 or x < -10 or y > 10 or y < -10:
      print((x,y), 'sairam do limite')
      return
  
    if (x, y) not in rendered_cells:
        rendered_cells.append((x,y))
        print((x,y))
        preencher_recursivo(x + 1, y, rendered_cells)
        preencher_recursivo(x - 1, y, rendered_cells)
        preencher_recursivo(x, y + 1, rendered_cells)
        preencher_recursivo(x, y - 1, rendered_cells)
        return rendered_cells

def preencher(selected_cells, rendered_cells, parameters):
    print(selected_cells)
    x0, y0 = selected_cells[0]
    points = preencher_recursivo(x0, y0, rendered_cells)
    for c in points:
	    grid.render_cell(c)

def ponto_medio(selected_cells, rendered_cells, parameters):
    r = int(parameters['R'])
    coordenadas_circulo = []
    def desenha8(x, y, xc, yc):
        coordenadas_circulo.append((x + xc, y + yc))
        coordenadas_circulo.append((y + xc, x + yc))
        coordenadas_circulo.append((y + xc, -x + yc))
        coordenadas_circulo.append((x + xc, -y + yc))
        coordenadas_circulo.append((-x + xc, -y + yc))
        coordenadas_circulo.append((-y + xc, -x + yc))
        coordenadas_circulo.append((-y + xc, x + yc))
        coordenadas_circulo.append((-x + xc, y + yc))
    xc, yc = selected_cells[0]
    x = 0 
    y = r
    e = -r
    desenha8(x, y, xc, yc)    
    while (x <= y):
        e += 2*x + 1
        x += 1
        if (e >= 0):
            e += 2 - 2*y
            y -= 1
        desenha8(x, y, xc, yc)
    print(coordenadas_circulo)
    for c in coordenadas_circulo:
	    grid.render_cell(c)

def scanline(selected_cells, rendered_cells, parameters):
    points = rendered_cells
    # Determinar a linha de varredura mais baixa e mais alta
    y_min = min(point[1] for point in points)
    y_max = max(point[1] for point in points)

    # Percorrer cada linha de varredura
    for y in range(y_min, y_max + 1):
        # Encontrar os pontos de interseção entre a linha de varredura e os segmentos da polilinha
        intersections = []
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i+1) % len(points)]  # Ponto seguinte (considerando polilinha fechada)

            if (y1 <= y < y2) or (y2 <= y < y1):
                # Calcular interseção entre a linha de varredura e o segmento da polilinha
                x_intersect = int(x1 + (float(y - y1) / (y2 - y1)) * (x2 - x1))
                intersections.append(x_intersect)

        # Ordenar pontos de interseção em ordem crescente de coordenada x
        intersections.sort()

        # Preencher pixels entre pontos de interseção consecutivos
        for i in range(0, len(intersections), 2):
            x_start = intersections[i]
            x_end = intersections[i+1] if i+1 < len(intersections) else x_start

            # Preencher pixels na linha de varredura entre os pontos de interseção
            for x in range(x_start, x_end + 1):
                grid.render_cell((x, y))  # Função para preencher um pixel na coordenada (x, y)

def perspective_projection(selected_cells, rendered_cells, parameters):
    # points = selected_cells
    points = [
    (2, 2, 2), 
    (2, -2, 2), 
    (-2, -2, 2), 
    (-2, 2, 2), 
    (2, 2, -2), 
    (2, -2, -2), 
    (-2, -2, -2), 
    (-2, 2, -2) 
]
    d = 4
    projected_points = []
    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        projected_x = x * d / (d + z)
        projected_y = y * d / (d + z)
        projected_points.append((round(projected_x), round(projected_y)))
    print(projected_points)
    for c in projected_points:
        x, y = c
        grid.render_cell((x, y))

def translacao(selected_cells, rendered_cells, parameters):
    points = rendered_cells
    xt = int(parameters['x'])
    yt = int(parameters['y'])

    grid._clear_all()

    for i in points:
        x, y = i
        grid.render_cell((x + xt, y + yt))

def rotacao(selected_cells, rendered_cells, parameters):
    points = rendered_cells
    grid._clear_all()
    pivo_x = int(parameters['PivoX'])
    pivo_y = int(parameters['PivoY'])
    angulo = np.radians(int(parameters['grau']))
    rotacionado = []
    for i in points:
        x, y = i

        rotated_x = round(pivo_x + (x - pivo_x) * np.cos(angulo) - (y - pivo_y) * np.sin(angulo))
        rotated_y = round(pivo_y + (x - pivo_x) * np.sin(angulo) + (y - pivo_y) * np.cos(angulo))

        rotacionado.append((rotated_x, rotated_y))

    for i in rotacionado:
        grid.render_cell(i)

def escala(selected_cells, rendered_cells, parameters):
    points = rendered_cells
    xE = int(parameters['EscalaX'])
    yE = int(parameters['EscalaY'])

    scaledPoints = []
    for point in points:
        x = point[0]
        y = point[1]
        scaledX = x * xE
        scaledY = y * yE
        scaledPoint = (scaledX, scaledY)
        #scaledLinha = bres((x,y),(scaledPoint[0], scaledPoint[1]))

        scaledPoints.append(scaledPoint)
    
    print(scaledPoints)
    grid.render_cells(scaledPoints)


# Adds the algorithm to the grid
grid.add_algorithm(name="Render cells", parameters=None, algorithm=my_render_cells_algorithm)
grid.add_algorithm(name='Translação', parameters=['x', 'y'], algorithm=translacao)
grid.add_algorithm(name='Rotação', parameters=['grau', 'PivoX', 'PivoY'], algorithm=rotacao)
grid.add_algorithm(name='Escala', parameters=['EscalaX', 'EscalaY'], algorithm=escala)
grid.add_algorithm(name='Bresenham', parameters=None, algorithm=bresenham_line)
grid.add_algorithm(name='Polilinha', parameters=None, algorithm=polilinha)
grid.add_algorithm(name='Circulo', parameters=['R'], algorithm=ponto_medio)
grid.add_algorithm(name='Recorte', parameters=None, algorithm=recorte)
grid.add_algorithm(name='Preenchimento Recursivo', parameters=None, algorithm=preencher)
grid.add_algorithm(name='Preenchimento Scanline', parameters=None, algorithm=scanline)
grid.add_algorithm(name='Projeção Perspectiva', parameters=None, algorithm=perspective_projection)

grid.show()