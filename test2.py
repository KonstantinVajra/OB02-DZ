import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        principal = float(entry_principal.get())
        annual_rate = float(entry_rate.get()) / 100
        months = int(entry_months.get())

        # Период начисления (12 месяцев в году)
        n = 12
        time_in_years = months / 12

        # Формула сложных процентов
        amount = principal * (1 + annual_rate / n) ** (n * time_in_years)

        result_label.config(text=f"Итоговая сумма: {amount:.2f} ₽")
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные числа.")

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор сложных процентов")

# Ввод данных
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

tk.Label(frame, text="Сумма вклада (₽):").grid(row=0, column=0, pady=5, sticky="e")
entry_principal = tk.Entry(frame)
entry_principal.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Процентная ставка (% годовых):").grid(row=1, column=0, pady=5, sticky="e")
entry_rate = tk.Entry(frame)
entry_rate.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Срок вклада (в месяцах):").grid(row=2, column=0, pady=5, sticky="e")
entry_months = tk.Entry(frame)
entry_months.grid(row=2, column=1, pady=5)

# Кнопка расчета
calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.pack(pady=10)

# Отображение результата
result_label = tk.Label(root, text="Итоговая сумма: ", font=("Arial", 12))
result_label.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()
