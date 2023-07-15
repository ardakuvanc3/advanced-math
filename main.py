import tkinter as tk
from tkinter import ttk
import math

def calculate_log():
    base = log_base_entry.get()
    number = log_number_entry.get()
    if base and number:
        base = float(base)
        number = float(number)
        result = math.log(number, base)
        log_result_label.config(text=f"Sonuç: {result}")
    else:
        log_result_label.config(text="Herhangi bir sayı girmediniz!")

def calculate_exponential():
    base = exp_base_entry.get()
    exponent = exp_exponent_entry.get()
    if base and exponent:
        base = float(base)
        exponent = float(exponent)
        result = base ** exponent
        exp_result_label.config(text=f"Sonuç: {result}")
    else:
        exp_result_label.config(text="Herhangi bir sayı girmediniz!")

def calculate_square_root():
    degree = root_degree_entry.get()
    number = root_number_entry.get()
    if degree and number:
        degree = float(degree)
        number = float(number)
        result = number ** (1 / degree)
        root_result_label.config(text=f"Sonuç: {result}")
    else:
        root_result_label.config(text="Herhangi bir sayı girmediniz!")

window = tk.Tk()
window.title("Matematik Uygulaması")
window.geometry("500x300")
window.configure(bg="#212121")  # Arkaplan rengini daha siyaha yakın bir siyah olarak ayarlar

# Ana pencereye modern bir görünüm sağlamak için ttk stilini kullanalım
style = ttk.Style()
style.configure("TFrame", background="#212121")  # Sekme arkaplan rengini daha siyaha yakın bir siyah olarak ayarlar
style.configure("TLabel", background="#212121", foreground="white")  # Etiketlerin arka plan ve ön plan rengini ayarlar
style.configure("TButton", background="#333333")  # Düğmelerin arka plan rengini aynı tutar

# Hesapla düğmeleri için yeni bir stil oluşturup metin rengini siyah yapalım
style.configure("TBlackText.TButton", foreground="black")

tab_control = ttk.Notebook(window)

logarithm_tab = ttk.Frame(tab_control, style="TFrame")
exponential_tab = ttk.Frame(tab_control, style="TFrame")
square_root_tab = ttk.Frame(tab_control, style="TFrame")

tab_control.add(logarithm_tab, text="Logaritma")
tab_control.add(exponential_tab, text="Üslü Sayılar")
tab_control.add(square_root_tab, text="Köklü Sayılar")

tab_control.pack(expand=1, fill="both")

# Logaritma sekmesi içeriği
log_label = ttk.Label(logarithm_tab, text="Logaritma Hesaplayıcı", font=("Helvetica", 16), background="#212121", foreground="white")
log_label.pack(pady=10)

log_base_label = ttk.Label(logarithm_tab, text="Taban Değeri:", background="#212121", foreground="white")
log_base_label.pack()
log_base_entry = ttk.Entry(logarithm_tab)
log_base_entry.pack(pady=5)

log_number_label = ttk.Label(logarithm_tab, text="Sayı:", background="#212121", foreground="white")
log_number_label.pack()
log_number_entry = ttk.Entry(logarithm_tab)
log_number_entry.pack(pady=5)

log_calculate_button = ttk.Button(logarithm_tab, text="Hesapla", command=calculate_log, style="TBlackText.TButton")
log_calculate_button.pack(pady=10)

log_result_label = ttk.Label(logarithm_tab, text="", background="#212121", foreground="white")
log_result_label.pack()

# Üslü Sayılar sekmesi içeriği
exponential_label = ttk.Label(exponential_tab, text="Üslü Sayılar Hesaplayıcı", font=("Helvetica", 16), background="#212121", foreground="white")
exponential_label.pack(pady=10)

exp_base_label = ttk.Label(exponential_tab, text="Taban Değeri:", background="#212121", foreground="white")
exp_base_label.pack()
exp_base_entry = ttk.Entry(exponential_tab)
exp_base_entry.pack(pady=5)

exp_exponent_label = ttk.Label(exponential_tab, text="Üs Değeri:", background="#212121", foreground="white")
exp_exponent_label.pack()
exp_exponent_entry = ttk.Entry(exponential_tab)
exp_exponent_entry.pack(pady=5)

exp_calculate_button = ttk.Button(exponential_tab, text="Hesapla", command=calculate_exponential, style="TBlackText.TButton")
exp_calculate_button.pack(pady=10)

exp_result_label = ttk.Label(exponential_tab, text="", background="#212121", foreground="white")
exp_result_label.pack()

# Köklü Sayılar sekmesi içeriği
square_root_label = ttk.Label(square_root_tab, text="Köklü Sayılar Hesaplayıcı", font=("Helvetica", 16), background="#212121", foreground="white")
square_root_label.pack(pady=10)

root_degree_label = ttk.Label(square_root_tab, text="Kök Derecesi:", background="#212121", foreground="white")
root_degree_label.pack()
root_degree_entry = ttk.Entry(square_root_tab)
root_degree_entry.pack(pady=5)

root_number_label = ttk.Label(square_root_tab, text="Kök İçindeki Sayı:", background="#212121", foreground="white")
root_number_label.pack()
root_number_entry = ttk.Entry(square_root_tab)
root_number_entry.pack(pady=5)

root_calculate_button = ttk.Button(square_root_tab, text="Hesapla", command=calculate_square_root, style="TBlackText.TButton")
root_calculate_button.pack(pady=10)

root_result_label = ttk.Label(square_root_tab, text="", background="#212121", foreground="white")
root_result_label.pack()

# Pencere boyutunu küçültüp taban ve sayı kutucuklarını ortalamak için grid kullanalım
logarithm_tab.grid_columnconfigure(0, weight=1)
logarithm_tab.grid_rowconfigure(1, weight=1)
logarithm_tab.grid_rowconfigure(3, weight=1)

exponential_tab.grid_columnconfigure(0, weight=1)
exponential_tab.grid_rowconfigure(1, weight=1)
exponential_tab.grid_rowconfigure(3, weight=1)

square_root_tab.grid_columnconfigure(0, weight=1)
square_root_tab.grid_rowconfigure(1, weight=1)
square_root_tab.grid_rowconfigure(3, weight=1)

window.mainloop()
