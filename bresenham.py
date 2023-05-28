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

# Adds the algorithm to the grid
grid.add_algorithm(name="Render cells", parameters=None, algorithm=my_render_cells_algorithm)
grid.add_algorithm(name='Bresenham',    parameters=None, algorithm=bresenham_line)

grid.show()