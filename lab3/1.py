import tkinter as tk
from tkinter import messagebox
import winsound
from keygen import generate_key


music_on = True


def close():
    winsound.PlaySound(None, winsound.SND_PURGE)
    window.destroy()


def generate():
    try:
        hex_input = entry_hex.get()
        key = generate_key(hex_input)
        entry_result.delete(0, 'end')
        entry_result.insert(0, key)
    except ValueError as e:
        messagebox.showerror('Ошибка', str(e))


def toggle_music():
    global music_on
    if music_on:
        winsound.PlaySound(None, winsound.SND_PURGE)
        btn_music['text'] = 'Включить звук'
        music_on = False
    else:
        winsound.PlaySound('music.wav', winsound.SND_ASYNC | winsound.SND_LOOP)
        btn_music['text'] = 'Выключить звук'
        music_on = True


# --- Анимация заголовка ---

colors = ['cyan', 'white', 'yellow', 'lime', 'magenta']
color_idx = 0

def animate():
    global color_idx
    lbl_title['fg'] = colors[color_idx]
    color_idx = color_idx + 1
    if color_idx >= len(colors):
        color_idx = 0
    window.after(400, animate)


# --- Главное окно ---

window = tk.Tk()
window.title('Keygen')
window.geometry('1200x600')
window.resizable(True, True)
window.protocol('WM_DELETE_WINDOW', close)

# --- Фоновое изображение ---

bg_img = tk.PhotoImage(file='1.png')
lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

# --- Панель генератора ---
frame = tk.Frame(window, bg='black', padx=20, pady=15)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Заголовок
lbl_title = tk.Label(frame, text='KEY GENERATOR', font=('Arial', 14, 'bold'), bg='black', fg='cyan')
lbl_title.grid(row=0, column=0, pady=(0, 15))

# Поле ввода HEX
lbl_hex = tk.Label(frame, text='Ввод HEX (5 знаков):', font=('Arial', 12), bg='black', fg='white')
lbl_hex.grid(row=1, column=0, pady=(0, 5))

entry_hex = tk.Entry(frame, font=('Consolas', 14), width=18, justify='center')
entry_hex.insert(0, '54CD1')
entry_hex.grid(row=2, column=0, pady=(0, 15))

# Кнопка генерации
btn_calc = tk.Button(frame, text='Сгенерировать', font=('Arial', 12, 'bold'), command=generate)
btn_calc.grid(row=3, column=0, pady=(0, 15), ipady=3)

# Поле вывода результата
lbl_result = tk.Label(frame, text='Ключ:', font=('Arial', 12), bg='black', fg='white')
lbl_result.grid(row=4, column=0, pady=(0, 5))

entry_result = tk.Entry(frame, font=('Consolas', 14), width=24, justify='center')
entry_result.grid(row=5, column=0, pady=(0, 15))

# Кнопка управления звуком
btn_music = tk.Button(frame, text='Выключить звук', font=('Arial', 10), command=toggle_music)
btn_music.grid(row=6, column=0, pady=(0, 10))

# Кнопка выхода
btn_close = tk.Button(frame, text='Выход', font=('Arial', 10), command=close)
btn_close.grid(row=7, column=0)

# --- Запуск музыки и анимации ---

winsound.PlaySound('music.wav', winsound.SND_ASYNC | winsound.SND_LOOP)

animate()

window.mainloop()
