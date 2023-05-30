from grid import Grid
import sys
print(sys.getrecursionlimit())

grid = Grid(extent=10, size=500)

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
    for i in range(0, len(selected_cells) - 1):
        bresenham_line([selected_cells[i], selected_cells[i + 1]], rendered_cells, parameters)
     
            
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
    r = 5
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
    xc = 0 
    yc = 0 
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

    # Inicializar lista de pontos críticos
    critical_points = []

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

# Adds the algorithm to the grid
grid.add_algorithm(name="Render cells", parameters=None, algorithm=my_render_cells_algorithm)
grid.add_algorithm(name='Bresenham', parameters=None, algorithm=bresenham_line)
grid.add_algorithm(name='Polilinha', parameters=None, algorithm=polilinha)
grid.add_algorithm(name='Circulo', parameters=None, algorithm=ponto_medio)
grid.add_algorithm(name='Preenchimento Recursivo', parameters=None, algorithm=preencher)
grid.add_algorithm(name='Preenchimento Scanline', parameters=None, algorithm=scanline)

grid.show()