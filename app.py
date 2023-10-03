from tkinter import *
from tkinter import ttk
from label_frame import FrameLEB, Row, FrameLE
from chart import chart

rows = []


def build_chart(root, time, step_time, scheme):
    print(time)
    print(step_time)
    print(scheme)
    planets = []
    for i in rows:
        temp = []
        temp.append(int(i.entry_x.get()))
        temp.append(int(i.entry_y.get()))
        temp.append(int(i.entry_vx.get()))
        temp.append(int(i.entry_vy.get()))
        temp.append(int(i.entry_ax.get()))
        temp.append(int(i.entry_ay.get()))
        temp.append(float(i.entry_m.get()))
        planets.append(temp)
    print(planets)
    newWindow = Toplevel(root)
    newWindow.grab_set()
    chart(newWindow, time, step_time, scheme, planets)


def enter():
    global rows
    for i in rows:
        i.label_frame.pack_forget()
    rows = []
    for i in range(int(label_count.get())):
        rows.append(Row(f'Planet {i}', frame))



win = Tk()
win.geometry('1000x1000')
win.title('MM1')
#win.resizable(False, False)
wrapper1 = LabelFrame(win)
#wrapper2 = LabelFrame(win)
canvas = Canvas(wrapper1, bg="white", width=1000, height=1000)
canvas.pack(side=LEFT)
sb = ttk.Scrollbar(wrapper1, orient='vertical', command=canvas.yview)
sb.pack(side=RIGHT, fill='y')
canvas.configure(yscrollcommand=sb.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='n')
wrapper1.pack(fill='both', expand=True, padx=10, pady=10)

font = ('Times 14')
label_count = FrameLEB("Число планет", "Ввод", frame, enter, ())
label_time = FrameLE("Время, с.", frame)
label_step_time = FrameLE("Шаг, с.", frame)
scheme_label = LabelFrame(frame)
label_scheme = Label(scheme_label, text='Тип схемы', width=15, font=('Times 14'))
label_scheme.pack(side=LEFT)
scheme = ('Эйлера', 'Эйлера-Крамера', 'Верле', 'Бимана')
var = StringVar(value=scheme[0])
combobox = ttk.Combobox(scheme_label, textvariable=var)
combobox['values'] = scheme
combobox['state'] = 'readonly'
combobox.pack(side=LEFT)
scheme_label.pack(side=TOP, fill='both')
table_labels = LabelFrame(frame)
label1 = Label(table_labels, text='№', width=10, font=('Times 14'))
label1.pack(side=LEFT)
label2 = Label(table_labels, text='X', width=10, font=('Times 14'))
label2.pack(side=LEFT)
label3 = Label(table_labels, text='Y', width=10, font=('Times 14'))
label3.pack(side=LEFT)
label4 = Label(table_labels, text='Vx', width=10, font=('Times 14'))
label4.pack(side=LEFT)
label5 = Label(table_labels, text='Vy', width=10, font=('Times 14'))
label5.pack(side=LEFT)
label6 = Label(table_labels, text='ax', width=10, font=('Times 14'))
label6.pack(side=LEFT)
label7 = Label(table_labels, text='ay', width=10, font=('Times 14'))
label7.pack(side=LEFT)
label8 = Label(table_labels, text='m', width=10, font=('Times 14'))
label8.pack(side=LEFT)
table_labels.pack(side=TOP, fill='both')
button = Button(frame, text='Построить', font=('Times 14'), command=lambda: build_chart(win, int(label_time.entry.get()),
                    int(label_step_time.entry.get()), combobox.get()))
button.pack(side=BOTTOM)

win.mainloop()
