from grid import Grid

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

# Adds the algorithm to the grid
grid.add_algorithm(name="Render cells", parameters=None, algorithm=my_render_cells_algorithm)
grid.add_algorithm(name='Bresenham', parameters=None, algorithm=bresenham_line)
grid.add_algorithm(name='Circulo', parameters=None, algorithm=ponto_medio)

grid.show()