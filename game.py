import tkinter as tk

# Configurações
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PIXEL_SIZE = 10
GRID_WIDTH = WINDOW_WIDTH // PIXEL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // PIXEL_SIZE

# Inicialização do Tkinter
root = tk.Tk()

# Criação do canvas
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# Pintura dos pixels ao longo do eixo X
for x in range(GRID_WIDTH + 1):
    canvas.create_rectangle(x * PIXEL_SIZE, 0, (x + 1) * PIXEL_SIZE, PIXEL_SIZE, fill="black")
    canvas.create_rectangle(x * PIXEL_SIZE, WINDOW_HEIGHT - PIXEL_SIZE, (x + 1) * PIXEL_SIZE, WINDOW_HEIGHT, fill="black")

# Execução do loop principal
root.mainloop()
