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

#Randomizer for scenarios
def random_scenario():
    global scenarios
    if len(scenarios) == 0:

        scenario.config(
            text="You completed all scenarios!"
        )
        hide_buttons()
        return
    chosen_scenario = random.choice(scenarios)
    chosen_scenario()


#Scenarios
def price_complaint():
    scenario.config(text="Scenario: Customer complains the drink is too expensive")
    scenario.pack(pady=35)
    button1.config(text="Lower Price", command=lower_price)
    button1.pack(pady=40)
    button2.config(text="Improve Quality", command=improve_quality)
    button2.pack(pady=40)
    button3.config(text="Ignore", command=ignore)
    button3.pack(pady=40)
    global scenarios
    scenarios.remove(price_complaint)
    

def spilled_drink():
    scenario.config(text="Scenario: Customer spilled their drink")
    button1.config(text="Apologize and give compensation", wraplength=200, command=apologize_and_compensate)
    button2.config(text="Scold the Customer", wraplength=200, command=scold_customer)
    button3.config(text="Ignore", command=ignore)
    scenario.pack(pady=35)
    button1.pack(pady=20)
    button2.pack(pady=20)
    button3.pack(pady=20)
    global scenarios
    scenarios.remove(spilled_drink)


#Labels
def update_label():
    money_label.config(text=f"Money: ${money}")
    reputation_label.config(text=f"Reputation: {reputation}")
    customer_satisfaction_label.config(text=f"Customer Satisfaction: {customer_satisfaction}")



#Actions
def lower_price():
    global money
    money -= 10
    global customer_satisfaction
    customer_satisfaction += 5
    update_label()
    scenario.config(text="You lowered the price. Customers are happy but your profit is reduced.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def improve_quality():
    global money
    money -= 20
    global reputation
    reputation += 10
    update_label()
    scenario.config(text="You improved the quality. Customers are happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def ignore():
    global reputation
    reputation -= 20
    global customer_satisfaction
    customer_satisfaction -= 10
    update_label()
    scenario.config(text="You ignored the complaint. Customers are dissatisfied.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def apologize_and_compensate():
    global money
    money -= 30
    global reputation
    reputation += 15
    global customer_satisfaction
    customer_satisfaction += 10
    update_label()
    scenario.config(text="You apologized and gave compensation. Customers are very happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def scold_customer():
    global reputation
    reputation -= 30
    global customer_satisfaction
    customer_satisfaction -= 20
    update_label()
    scenario.config(text="You scolded the customer. Customers are very dissatisfied and your reputation suffers.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def walk_away():
    global reputation
    reputation -= 10
    update_label()
    scenario.config(
        text="You walked away. Customers lost trust in you.")
    hide_buttons()
    window.after(5000, lambda:next_round())

def enable_button():
    button1.pack()
    button2.pack()
    button3.pack()

def next_round():
    enable_button()
    random_scenario()

def hide_buttons():
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()



button1 = tk.Button(window, text="Start Game", font=("Arial", 20), command=lambda:(hide_buttons(), random_scenario()), width=15)
button1.pack(pady=40)

button2 = tk.Button(window, text="Quit", font=("Arial", 20), command=lambda:(window.destroy()), width=15)
button2.pack(pady=40)

button3 = tk.Button(window, text="", font=("Arial", 20), command=ignore, width=15)

scenario = tk.Label(window, text="", font=("Arial", 20))
scenarios = [price_complaint, spilled_drink]

window.configure(bg="lightblue")
window.mainloop()
