from tkinter.ttk import Label, Button, Combobox, Style
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import keyboard
import pyautogui as pg 
from window import hidden_client
import json
import threading
import pynput
import time

HOTKEYS = ['Desligado', 'F1', 'F2','F3', 'F4','F5', 'F6','F7', 'F8','F9', 'F10','F11', 'F12']

root = ThemedTk(theme="dark", themebg=True,)
root.title("MyInterface")
# root.geometry("500x500+150+150")
root.resizable(False, False)
Style = Style()
Style.configure('TButton',  font=("Roboto", 12))
Style.configure('Ativado.TButton', foreground="green")
Style.configure('Desativado.TButton', foreground="red")

def generate_widget(widget, row, column, sticky="NSEW", columnspan=None, **kwargs):
    my_widget = widget(**kwargs)
    my_widget.grid(row=row, column=column, padx=5, pady=5, columnspan=columnspan, sticky=sticky)
    return my_widget

def load_trash():
    load_image = Image.open('img/icone_lixeira.png')
    resized_image = load_image.resize((20, 20))
    return ImageTk.PhotoImage(resized_image)


lbl_food = generate_widget(Label, row=0, column=0, sticky="W", text = "Hotkey Eat Food", font=("Roboto",12))
cbx_food = generate_widget(Combobox, row=0, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12),width=12)
cbx_food.current(0)

lbl_cast = generate_widget(Label, row=1, column=0, sticky="W", text="Hotkey Cura Vida 1", font=("Roboto",12))
cbx_cast = generate_widget(Combobox, row=1, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12),width=12)
cbx_cast.current(0)
rgb = ''
vida_position = ''

lbl_cast1 = generate_widget(Label, row=3, column=0, sticky="W", text="Hotkey Cura Vida 2", font=("Roboto",12))
cbx_cast1 = generate_widget(Combobox, row=3, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12),width=12)
cbx_cast1.current(0)
rgb1 = ''
vida_position1 = ''

lbl_cast2 = generate_widget(Label, row=5, column=0, sticky="W", text="Hotkey Usar Pot Mana+-", font=("Roboto",12))
cbx_cast2 = generate_widget(Combobox, row=5, column=1, values=HOTKEYS, state="readonly", font=("Roboto", 12),width=12)
cbx_cast2.current(0)
rgb2 = ''
vida_position2 = ''

def get_vida_position():
    global rgb 
    global vida_position
    messagebox.showinfo(title="Vida Position", message="Posicione o mouse em cima da barra de mana e precione a tecla insert")
    keyboard.wait('insert')
    x, y = pg.position()
    rgb = pg.screenshot().getpixel((x, y))
    messagebox.showinfo(title='Vida Result', message=f"X: {x} Y: {y} - RGB: {rgb}")
    lbl_vida_position.configure(text=f"({x} , {y})")
    vida_position = [x, y]

def get_vida_position1():
    global rgb1 
    global vida_position1
    messagebox.showinfo(title="Vida Position1", message="Posicione o mouse em cima da barra de vida e precione a tecla insert")
    keyboard.wait('insert')
    x, y = pg.position()
    rgb1 = pg.screenshot().getpixel((x, y))
    messagebox.showinfo(title='Vida Result', message=f"X: {x} Y: {y} - RGB: {rgb1}")
    lbl_vida_position1.configure(text=f"({x} , {y})")
    vida_position1 = [x, y]

def get_vida_position2():
    global rgb2 
    global vida_position2
    messagebox.showinfo(title="mana position", message="Posicione o mouse em cima da barra de mana e precione a tecla insert")
    keyboard.wait('insert')
    x, y = pg.position()
    rgb2 = pg.screenshot().getpixel((x, y))
    messagebox.showinfo(title='Vida Result', message=f"X: {x} Y: {y} - RGB: {rgb2}")
    lbl_vida_position2.configure(text=f"({x} , {y})")
    vida_position2 = [x, y]
    


btn_vida_position = generate_widget(Button, row=2, column=0,text="Vida Position", command=get_vida_position) 
lbl_vida_position = generate_widget(Label, row=2, column=1, text="Empty", font=("Roboto", 12), sticky="W")

btn_vida_position1 = generate_widget(Button, row=4, column=0,text="Vida Position1", command=get_vida_position1,) 
lbl_vida_position1 = generate_widget(Label, row=4, column=1, text="Empty", font=("Roboto", 12), sticky="W")

btn_vida_position2 = generate_widget(Button, row=6, column=0,text="Mana Position", command=get_vida_position2) 
lbl_vida_position2 = generate_widget(Label, row=6, column=1, text="Empty", font=("Roboto", 12), sticky="W")

trash = load_trash()

def clear():
    lbl_vida_position.configure(text="Empty")
def clear1():
    lbl_vida_position1.configure(text="Empty")
def clear2():
    lbl_vida_position2.configure(text="Empty")


btn_vida_position_trash = generate_widget(Button, row=2, column=1, image=trash, sticky="E", command=clear)
btn_vida_position_trash1 = generate_widget(Button, row=4, column=1, image=trash, sticky="E", command=clear1)
btn_vida_position_trash2 = generate_widget(Button, row=6, column=1, image=trash, sticky="E", command=clear2)

def opacity():
    result = hidden_client()
    if result == 1:
        btn_opacity.configure(style='Ativado.TButton')
        return
    btn_opacity.configure(style='Desativado.TButton')
    
    
btn_opacity = generate_widget(Button, row=8, column=0, text="Apply Opacity", columnspan=2, command=opacity)

def save():
    print("Salvando arquivos")
    my_data = {
        "food": {
        "value": cbx_food.get(),
        "position": cbx_food.current()
        },
        "spell":{
        "value": cbx_cast.get(),
        "position": cbx_cast.current()
        },
        "spell1":{
        "value1": cbx_cast1.get(),
        "position1": cbx_cast1.current()
        },
        "spell2":{
        "value2": cbx_cast2.get(),
        "position2": cbx_cast2.current()
        },
        "vida_pos": {
            "position":vida_position,
            "rgb": rgb
        },
        "vida_pos1": {
            "position1":vida_position1,
            "rgb1": rgb1
        },
        "vida_pos2": {
            "position2":vida_position2,
            "rgb2": rgb2
        }
    }
    with open('infos.json','w') as file:
        file.write(json.dumps(my_data))

def load():
    with open('infos.json', 'r') as file:
        data = json.loads(file.read())
    cbx_food.current(data['food']['position'])
    cbx_cast.current(data['spell']['position'])
    lbl_vida_position.configure(text=data['vida_pos']['position'])
    cbx_cast1.current(data['spell1']['position1'])
    lbl_vida_position1.configure(text=data['vida_pos1']['position1'])
    cbx_cast2.current(data['spell2']['position2'])
    lbl_vida_position2.configure(text=data['vida_pos2']['position2'])
    return data

btn_load = generate_widget(Button, row=9, column=0, text="Load", command=load)

def run():
    wait_to_eat_food = 100
    time_food = time.time()
    while not myEvent.is_set():
        if data['vida_pos']['position'] is not None:
            x = data['vida_pos']['position'][0]
            y = data['vida_pos']['position'][1]
            if not pg.pixelMatchesColor(x, y, tuple(data['vida_pos']['rgb'])):
                if data['spell']['value'] != 'Desligado':
                    pg.press(data['spell']['value'])
                    pg.sleep(1)
        if data['vida_pos1']['position1'] is not None:
            x = data['vida_pos1']['position1'][0]
            y = data['vida_pos1']['position1'][1]
            if not pg.pixelMatchesColor(x, y, tuple(data['vida_pos1']['rgb1'])):
                if data['spell1']['value1'] != 'Desligado':
                    pg.press(data['spell1']['value1'])
                    pg.sleep(1)
        if data['vida_pos2']['position2'] is not None:
            x = data['vida_pos2']['position2'][0]
            y = data['vida_pos2']['position2'][1]
            if not pg.pixelMatchesColor(x, y, tuple(data['vida_pos2']['rgb2'])):
                if data['spell2']['value2'] != 'Desligado':
                    pg.press(data['spell2']['value2'])
                    pg.sleep(1)
            if data['food']['value'] != 'Desligado':
                if int(time.time() - time_food) >= wait_to_eat_food:
                    pg.press(data['food']['value'])
                    time_food = time.time()
    print("bot parado")
        

def key_code(key):
    if key == pynput.keyboard.Key.esc:
        myEvent.set()
        root.deiconify()
        return False
    
def Listener_keyboard():
    with pynput.keyboard.Listener(on_press=key_code) as Listener:
        Listener.join()

def start():
    root.iconify()
    save()
    global data
    data = load()
    global myEvent
    myEvent = threading.Event()
    global start_th
    start_th = threading.Thread(target=run)
    start_th.start()
    keyboard_th = threading.Thread(target=Listener_keyboard)
    keyboard_th.start()
    

btn_start = generate_widget(Button, row=9, column=1, text="Start", command=start)

root.mainloop()