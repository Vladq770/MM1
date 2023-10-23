import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from matplotlib.widgets import Button
import tkinter.filedialog as fd
from calculations import scheme_Euler, scheme_Euler_Kramer, scheme_Verle, scheme_Biman
mpl.use('TkAgg')
('Эйлера', 'Эйлера-Крамера', 'Верле', 'Бимана')
scheme_type = {'Эйлера': scheme_Euler, 'Эйлера-Крамера': scheme_Euler_Kramer, 'Верле': scheme_Verle, 'Бимана': scheme_Biman}

colors = ["red", "blue", "green", "black", "orange", "peru", "aqua", "pink", "olive", "lime"]
len_colors = 10
G = 6.67e-11
button = None

def v_center_mass(v, planets, general_m, n):
    impulse = 0
    for i in range(len(planets)):
        impulse += v[i][n] * planets[i][6]
    return impulse / general_m


def get_energy(x, y, vx, vy, planets, n):
    energy = 0
    for i in range(len(planets)):
        energy += planets[i][6] * (vx[i][n] ** 2 + vy[i][n] ** 2) / 2
    for i in range(len(planets)):
        for j in range(i + 1, len(planets)):
            energy -= G * planets[i][6] * planets[j][6] / ((x[i][n] - x[j][n]) ** 2 + (y[i][n] - y[j][n]) ** 2) ** 0.5
    return energy


def chart(win, time, step_time, scheme, planets):
    def save_data(event):
        sep = f'\n'
        data = f"{sep.join(f'x={i[0]} y={i[1]} vx={i[2]} vy={i[3]} m={i[6]}' for i in planets)}"
        ind = len(vx[0]) - 1
        vxm = v_center_mass(vx, planets, general_m, ind)
        vym = v_center_mass(vy, planets, general_m, ind)
        energy = get_energy(x, y, vx, vy, planets, ind)
        data += f'\nvxM = {vxm} vyM = {vym} E = {energy}'
        new_file = fd.asksaveasfile(title="Сохранить файл", defaultextension=".txt",
                                    filetypes=(("Текстовый файл", "*.txt"),))

        if new_file:
            new_file.write(data)
            new_file.close()

    def animate_func(num):
            global button, line_ani
            num *= n
            if num >= frames_all:
                num = frames_all - 1
            ax.clear()  # Очищаем фигуру для обновления линии, точки,
            # заголовка и осей  # Обновляем линию траектории (num+1 из-за индексации Python)
            for i in range(len(planets)):
                ax.plot(x[i][:num + 1], y[i][:num + 1], color=colors[i % len_colors],
                        label=f'Planet {i}')  # Обновляем локацию точки
                ax.scatter(x[i][num], y[i][num], color=colors[i % len_colors])  # Добавляем постоянную начальную точку

            ax.set_xlim([xmin - (xmax - xmin) * 0.2, xmax + (xmax - xmin) * 0.2])
            ax.set_ylim([ymin - (ymax - ymin) * 0.2, ymax + (ymax - ymin) * 0.2])
            vxm = v_center_mass(vx, planets, general_m, num)
            vym = v_center_mass(vy, planets, general_m, num)
            energy = get_energy(x, y, vx, vy, planets, num)
            # Добавляем метки
            ax.set_title(f'Time = {str(np.round(t[num], decimals=2))} sec \n'
                         f'Vx = {vxm} \n'
                         f'Vy = {vym} \n'
                         f'E = {energy}')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.legend(fontsize="small")
            button = Button(x_button, 'Сохранить')
            button.on_clicked(save_data)

    t, x, y, vx, vy = scheme_type[scheme](time, step_time, planets)
    n = 50
    frames_all = len(t)
    frames = frames_all // n + 2
    general_m = sum([i[6] for i in planets])
    xmin = xmax = x[0][0]
    ymin = ymax = y[0][0]
    for i in range(len(planets)):
        for j in range(len(x[0])):
            if xmin > x[i][j]:
                xmin = x[i][j]
            if xmax < x[i][j]:
                xmax = x[i][j]
            if ymin > y[i][j]:
                ymin = y[i][j]
            if ymax < y[i][j]:
                ymax = y[i][j]
    fig = plt.figure(figsize=(7, 7))
    ax = plt.axes()
    x_button = plt.axes((0.75, 0.005, 0.15, 0.04))
    line_ani = animation.FuncAnimation(fig, animate_func, interval=1,
                                       frames=frames, repeat=False, cache_frame_data=False)
    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, win)
    toolbar.update()

    canvas.get_tk_widget().pack()
