import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import datetime
import random

if not os.path.exists("images"):
    os.makedirs("images")

MINERALS = [
    {
        "name": "Аметист",
        "description": "Фиолетовая разновидность кварца. Красивый полудрагоценный камень.",
        "color": "Фиолетовый", "structure": "Кристаллическая", "hardness": "7", "value": "700-1500",
        "image": "images/amethyst.jpg"
    },
    {
        "name": "Горный хрусталь",
        "description": "Прозрачный бесцветный кварц. Образует красивые кристаллы.",
        "color": "Прозрачный", "structure": "Кристаллическая", "hardness": "7", "value": "300-800",
        "image": "images/quartz.jpg"
    },
    {
        "name": "Малахит",
        "description": "Зеленый минерал с красивым узором. Поделочный камень.",
        "color": "Зеленый с узорами", "structure": "Почковидная", "hardness": "3.5-4", "value": "500-1200",
        "image": "images/malachite.jpg"
    },
    {
        "name": "Флюорит",
        "description": "Разноцветный минерал. Светится в ультрафиолете.",
        "color": "Разноцветный", "structure": "Кубическая", "hardness": "4", "value": "400-900",
        "image": "images/fluorite.jpg"
    },
    {
        "name": "Изумруд",
        "description": "Драгоценный камень ярко-зеленого цвета. Разновидность берилла.",
        "color": "Ярко-зеленый", "structure": "Призматическая", "hardness": "7.5-8", "value": "50000+",
        "image": "images/emerald.jpg"
    },
    {
        "name": "Рубин",
        "description": "Красный драгоценный камень, уступающий в твердости только алмазу.",
        "color": "Красный", "structure": "Тригональная", "hardness": "9", "value": "45000+",
        "image": "images/ruby.jpg"
    },
    {
        "name": "Сапфир",
        "description": "Драгоценный камень синего цвета. Символ мудрости и спокойствия.",
        "color": "Синий", "structure": "Кристаллическая", "hardness": "9", "value": "40000+",
        "image": "images/sapphire.jpg"
    },
    {
        "name": "Янтарь",
        "description": "Окаменевшая ископаемая смола древних хвойных деревьев.",
        "color": "Медово-желтый", "structure": "Аморфная", "hardness": "2-2.5", "value": "200-1000",
        "image": "images/amber.jpg"
    },
    {
        "name": "Алмаз",
        "description": "Самый твердый минерал на Земле. Кубическая форма углерода.",
        "color": "Прозрачный/Белый", "structure": "Кубическая", "hardness": "10", "value": "500000+",
        "image": "images/almaz.jpg"
    },
    {
        "name": "Обсидиан",
        "description": "Вулканическое стекло, образующееся при быстром остывании лавы.",
        "color": "Черный", "structure": "Стекловатая", "hardness": "5-5.5", "value": "150-400",
        "image": "images/obsidian.jpg"
    }
]

FACTS = [
    "Алмаз и графит состоят из одного элемента — углерода",
    "Самый дорогой минерал в мире — красный алмаз",
    "В космосе существуют целые алмазные планеты",
    "Малахит в древности использовали как тени для век"
]

view_counts = {m["name"]: 0 for m in MINERALS}

COLORS = {
    "bg_dark": "#1a1a2e",
    "bg_light": "#16213e",
    "accent": "#e94560",
    "accent_hover": "#c0392b",
    "text_dark": "#4287f5",
    "text_light": "#ecf0f1"
}

FONTS = {
    "title": ("Helvetica", 36, "bold"),
    "subtitle": ("Helvetica", 19, "italic"),
    "mineral_name": ("Courier", 27, "bold"),
    "regular": ("Helvetica", 17),
    "bold_info": ("Helvetica", 16, "bold"),
    "small": ("Helvetica", 15)
}

root = tk.Tk()
root.title("Моя коллекция минералов")
root.geometry("1280x720")
root.configure(bg=COLORS["bg_dark"])

main_container = ttk.Frame(root)
main_container.pack(fill=tk.BOTH, expand=True)


def create_placeholder_image(parent):
    placeholder = tk.Frame(parent, bg="#dfe6e9", width=250, height=250)
    placeholder.pack(expand=True)
    placeholder.pack_propagate(False)
    tk.Label(placeholder, text="✨\nМинерал\nскоро появится", font=FONTS["regular"],
             bg="#dfe6e9", fg=COLORS["text_dark"]).pack(expand=True)

def load_mineral_image(parent, image_path):
    try:
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image.thumbnail((400, 450))
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(parent, image=photo, bg="white")
            image_label.image = photo
            image_label.pack(expand=True)
        else:
            create_placeholder_image(parent)
    except:
        create_placeholder_image(parent)

def create_title_screen():
    for widget in main_container.winfo_children(): widget.destroy()
    title_frame = tk.Frame(main_container, bg=COLORS["bg_dark"])
    title_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(title_frame, text="💎 ⚒️ 💎", font=("Helvetica", 60),
             bg=COLORS["bg_dark"], fg=COLORS["accent"]).pack(pady=(40, 0))
    tk.Label(title_frame, text="МОЯ КОЛЛЕКЦИЯ МИНЕРАЛОВ", font=FONTS["title"],
             bg=COLORS["bg_dark"], fg=COLORS["text_light"]).pack(pady=10)

    hour = datetime.datetime.now().hour
    greeting = "Доброе утро!" if hour < 12 else "Добрый день!" if hour < 18 else "Добрый вечер!"
    tk.Label(title_frame, text=f"{greeting} В коллекции {len(MINERALS)} экспонатов",
             font=FONTS["subtitle"], bg=COLORS["bg_dark"], fg=COLORS["accent"]).pack(pady=5)

    tk.Label(title_frame, text=f"Знаете ли вы? {random.choice(FACTS)}",
             font=("Helvetica", 15, "italic"), bg=COLORS["bg_dark"],
             fg="#95a5a6", wraplength=600).pack(side=tk.BOTTOM, pady=40)

    tk.Label(title_frame, text="Мой сайтик: jiarbuz.lol", font=("Helvetica", 14),
             bg=COLORS["bg_dark"], fg="gray").pack(side=tk.BOTTOM, pady=5)

    tk.Label(title_frame, text="© 2026 Коллекция Савелий Сизых", font=("Helvetica", 15),
             bg=COLORS["bg_dark"], fg="gray").pack(side=tk.BOTTOM, pady=6)

    btn = tk.Button(title_frame, text="Начать просмотр", font=FONTS["subtitle"],
                    bg=COLORS["accent"], fg="white", padx=30, pady=10, relief=tk.FLAT,
                    command=create_collection_view, cursor="hand2")
    btn.pack(pady=30)
    btn.bind("<Enter>", lambda e: btn.configure(bg=COLORS["accent_hover"]))
    btn.bind("<Leave>", lambda e: btn.configure(bg=COLORS["accent"]))

def create_mineral_tab(mineral, index):
    tab_frame = tk.Frame(notebook, bg="white")
    notebook.add(tab_frame, text=mineral["name"])

    content_frame = tk.Frame(tab_frame, bg="white")
    content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    header = tk.Frame(content_frame, bg="white")
    header.pack(fill=tk.X)
    tk.Label(header, text=mineral["name"], font=FONTS["mineral_name"], bg="white", fg=COLORS["text_dark"]).pack(
        side=tk.LEFT)

    count_label = tk.Label(header, text=f"Просмотров: {view_counts[mineral['name']]}", font=FONTS["small"], bg="white",
                           fg="gray")
    count_label.pack(side=tk.RIGHT, pady=15)

    def update_counter(event):
        if notebook.tab(notebook.select(), "text") == mineral["name"]:
            view_counts[mineral["name"]] += 1
            count_label.config(text=f"Просмотров: {view_counts[mineral['name']]}")

    tab_frame.bind("<Visibility>", update_counter)

    body = tk.Frame(content_frame, bg="white")
    body.pack(fill=tk.BOTH, expand=True, pady=10)

    img_f = tk.Frame(body, bg="white", width=500, height=500)
    img_f.pack(side=tk.LEFT, padx=20)
    img_f.pack_propagate(False)
    load_mineral_image(img_f, mineral["image"])

    desc_f = tk.Frame(body, bg="white")
    desc_f.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)

    txt = tk.Text(desc_f, wrap=tk.WORD, font=FONTS["regular"], bg="white", fg=COLORS["text_dark"], relief=tk.FLAT,
                  height=4)
    txt.insert(tk.END, mineral["description"])
    txt.config(state=tk.DISABLED)
    txt.pack(fill=tk.X, pady=(0, 10))

    info_table = tk.Frame(desc_f, bg="#f8f9fa", padx=10, pady=10)
    info_table.pack(anchor="w", pady=5)

    specs = [
        ("Цвет:", mineral["color"]),
        ("Структура:", mineral["structure"]),
        ("Твердость:", mineral["hardness"]),
        ("Ценность:", f"{mineral['value']} руб за 100 грамм")
    ]

    for i, (label, value) in enumerate(specs):
        tk.Label(info_table, text=label, font=FONTS["bold_info"], bg="#f8f9fa", fg="#555").grid(row=i, column=0,
                                                                                                sticky="w", pady=2)
        tk.Label(info_table, text=value, font=FONTS["regular"], bg="#f8f9fa", fg=COLORS["text_dark"]).grid(row=i,
                                                                                                           column=1,
                                                                                                           sticky="w",
                                                                                                           padx=10)

    rating_f = tk.Frame(desc_f, bg="white")
    rating_f.pack(anchor="w", pady=15)
    tk.Label(rating_f, text="Моя оценка:", font=FONTS["small"], bg="white").pack(side=tk.LEFT)
    stars_lbl = tk.Label(rating_f, text="☆☆☆☆☆", font=("Helvetica", 18), bg="white", fg="gold")
    stars_lbl.pack(side=tk.LEFT, padx=10)

    stars_lbl.bind("<Button-1>", lambda e: stars_lbl.config(
        text="★" * ((stars_lbl.cget("text").count("★") % 5) + 1) + "☆" * (
                    5 - ((stars_lbl.cget("text").count("★") % 5) + 1))))

def create_collection_view():
    global notebook
    for widget in main_container.winfo_children(): widget.destroy()
    top = tk.Frame(main_container, bg=COLORS["bg_dark"])
    top.pack(fill=tk.X, padx=10, pady=5)
    tk.Button(top, text="← На главную", font=FONTS["small"], bg=COLORS["accent"], fg="white", relief=tk.FLAT,
              command=create_title_screen).pack(side=tk.LEFT)
    notebook = ttk.Notebook(main_container)
    notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    for i, m in enumerate(MINERALS): create_mineral_tab(m, i)

create_title_screen()
root.mainloop()
