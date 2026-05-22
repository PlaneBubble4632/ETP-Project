import tkinter as tk
import random
window = tk.Tk()
window.geometry("1100x800")
window.title("ETP game")

title = tk.Label(window, text="Entreprenuership Game Simulator", font=("Arial", 30))
title.pack(pady=20)

# Labels for money, reputation, and customer satisfaction
money = 100
money_label = tk.Label(window, text=f"Money: ${money}", font=("Arial", 30))
money_label.pack()

reputation = 50
reputation_label = tk.Label(window, text=f"Reputation: {reputation}", font=("Arial", 30))
reputation_label.pack()

customer_satisfaction = 10
customer_satisfaction_label = tk.Label(window, text=f"Customer Satisfaction: {customer_satisfaction}", font=("Arial", 30))
customer_satisfaction_label.pack()

scenario = tk.Label(window, text="", font=("Arial", 20))


#Randomizer for scenarios
def random_scenario():
    scenarios = [price_complaint, spilled_drink]
    chosen_scenario = random.choice(scenarios)
    chosen_scenario()

#Scenarios
def price_complaint():
    scenario.config(text="Scenario: Customer complains the drink is too expensive")
    scenario.pack(pady=35)
    button1.config(text="Lower Price", command=lower_price)
    button1.pack(pady=20)
    button2.config(text="Improve Quality", command=improve_quality)
    button2.pack(pady=20)
    button3.config(text="Ignore", command=ignore)
    button3.pack(pady=20)

def spilled_drink():
    scenario.config(text="Scenario: Customer spilled their drink")

def update_label():
    money_label.config(text=f"Money: ${money}")
    reputation_label.config(text=f"Reputation: {reputation}")
    customer_satisfaction_label.config(text=f"Customer Satisfaction: {customer_satisfaction}")

#Options
def lower_price():
    global money
    money -= 10
    global customer_satisfaction
    customer_satisfaction += 5
    customer_satisfaction_label.config(text=f"Customer Satisfaction: {customer_satisfaction}")
    money_label.config(text=f"Money: ${money}")
    scenario.config(text="You lowered the price. Customers are happy but your profit is reduced.")
    window.after(5000, lambda: random_scenario())

def improve_quality():
    global money
    money -= 20
    global reputation
    reputation += 10
    money_label.config(text=f"Money: ${money}")
    reputation_label.config(text=f"Reputation: {reputation}")
    scenario.config(text="You improved the quality. Customers are happy and your reputation improves.")
    window.after(5000, lambda: random_scenario())

def ignore():
    global reputation
    reputation -= 20
    reputation_label.config(text=f"Reputation: {reputation}")
    global customer_satisfaction
    customer_satisfaction -= 10
    customer_satisfaction_label.config(text=f"Customer Satisfaction: {customer_satisfaction}")
    scenario.config(text="You ignored the complaint. Customers are dissatisfied.")
    window.after(5000, lambda: random_scenario())

def apologize_and_compensate():
    global money
    money -= 30
    global reputation
    reputation += 15
    global customer_satisfaction
    customer_satisfaction += 10
    money_label.config(text=f"Money: ${money}")
    reputation_label.config(text=f"Reputation: {reputation}")
    customer_satisfaction_label.config(text=f"Customer Satisfaction: {customer_satisfaction}")
    scenario.config(text="You apologized and gave compensation. Customers are very happy and your reputation improves.")
    window.after(5000, lambda: random_scenario())

def scold_customer():
    global reputation
    reputation -= 30
    reputation_label.config(text=f"Reputation: {reputation}")
    global customer_satisfaction
    customer_satisfaction -= 20
    customer_satisfaction_label.config(text=f"Customer Satisfaction: {customer_satisfaction}")
    scenario.config(text="You scolded the customer. Customers are very dissatisfied and your reputation suffers.")
    window.after(5000, lambda: random_scenario())

def update_buttons():
    button1.config(text="Apologize and give compensation", command=apologize_and_compensate)
    button2.config(text="Scold the Customer", command=scold_customer)
    button3.config(text="Ignore", command=ignore)

def hide_buttons():
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()

button1 = tk.Button(window, text="Start Game", font=("Arial", 20), command=lambda:(hide_buttons(), random_scenario()), width=15)
button1.pack(pady=20)

button2 = tk.Button(window, text="Quit", font=("Arial", 20), command=lambda:(hide_buttons(), window.destroy()), width=15)
button2.pack(pady=20)

button3 = tk.Button(window, text="", font=("Arial", 20), command=ignore, width=15)


window.configure(bg="lightblue")
window.mainloop()
