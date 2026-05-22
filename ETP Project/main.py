import tkinter as tk
window = tk.Tk()
window.geometry("900x600")
window.title("ETP game")

title = tk.Label(window, text="Entreprenuership Game Simulator", font=("Arial", 30))
title.pack(pady=20)

money = 100
money_label = tk.Label(window, text=f"Money: ${money}", font=("Arial", 30))
money_label.pack()

reputation = 50
reputation_label = tk.Label(window, text=f"Reputation: {reputation}", font=("Arial", 30))
reputation_label.pack()

customer_satisfaction = 10
customer_satisfaction_label = tk.Label(window, text=f"Customer Satisfaction: {customer_satisfaction}", font=("Arial", 30))
customer_satisfaction_label.pack()

scenario = tk.Label(window, text="Scenario: Customer complains the drink is too expensive", font=("Arial", 20))
scenario.pack(pady=35)

def update_scenario():
    global money
    global reputation
    global customer_satisfaction
    if money < 50:
        scenario.config(text="Scenario: You are running low on funds. Consider lowering prices or improving quality.")
    elif reputation < 30:
        scenario.config(text="Scenario: Your reputation is suffering. Consider improving quality.")
    elif customer_satisfaction < 5:
        scenario.config(text="Scenario: Customer satisfaction is very low. Consider lowering prices or improving quality.")
    else:
        scenario.config(text="Scenario: Business is doing well. Keep up the good work!")

def lower_price():
    global money
    money -= 10
    global customer_satisfaction
    customer_satisfaction += 5
    customer_satisfaction_label.config(text=f"Customer Satisfaction: {customer_satisfaction}")
    money_label.config(text=f"Money: ${money}")
    scenario.config(text="You lowered the price. Customers are happy but your profit is reduced.")
    update_scenario()

def improve_quality():
    global money
    money -= 20
    global reputation
    reputation += 10
    money_label.config(text=f"Money: ${money}")
    reputation_label.config(text=f"Reputation: {reputation}")
    scenario.config(text="You improved the quality. Customers are happy and your reputation improves.")
    update_scenario()

def ignore():
    scenario.config(text="You ignored the complaint. Customers are dissatisfied.")
    update_scenario()


button1 = tk.Button(window, text="Lower Price", font=("Arial", 20), command=lower_price, width=15)
button1.pack(pady=20)

button2 = tk.Button(window, text="Improve Quality", font=("Arial", 20), command=improve_quality, width=15)
button2.pack(pady=20)

button3 = tk.Button(window, text="Ignore", font=("Arial", 20), command=ignore, width=15)
button3.pack(pady=20)

window.configure(bg="lightblue")
window.mainloop()
