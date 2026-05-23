import tkinter as tk
import customtkinter as ctk
import random
window = ctk.CTk()
window.geometry("1100x800")
window.title("ETP game")
window.configure(fg_color="#88BACF")

title = tk.Label(window, text="Entreprenuership Game Simulator", font=("Arial", 30))
title.pack(pady=20)

top_frame = ctk.CTkFrame(window, fg_color="#88BACF", width=900, height=90, corner_radius=12)
top_frame.place(relx=0.5, rely=0.1, anchor="n")
top_frame.grid_propagate(False)

# Distribute spacing evenly
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)

# ========================================================
# 1. MONEY CARD WITH SHADOW
# ========================================================
money = 100

# Container holds both the shadow and the card together in Column 0
money_container = ctk.CTkFrame(top_frame, fg_color="transparent", width=220, height=65)
money_container.grid(row=0, column=0, padx=10, pady=10)
money_container.pack_propagate(False)

# The White Card (Placed second, sitting directly on top)
money_frame = ctk.CTkFrame(money_container, fg_color="white", corner_radius=10, border_width=3, border_color="#e4edf3")
money_frame.place(relx=0, rely=0, relwidth=1, relheight=0.93) # Lifted slightly up

money_label = ctk.CTkLabel(money_frame, text=f"Money: ${money}", font=("Arial", 20, "bold"), text_color="#6d7e95")
money_label.pack(expand=True)


# ========================================================
# 2. CUSTOMER SATISFACTION CARD WITH SHADOW
# ========================================================
customer_satisfaction = 10

# Container in Column 1
customer_container = ctk.CTkFrame(top_frame, fg_color="transparent", width=260, height=65)
customer_container.grid(row=0, column=1, padx=10, pady=10)
customer_container.pack_propagate(False)

# The White Card
cust_frame = ctk.CTkFrame(customer_container, fg_color="white", corner_radius=10, border_width=3, border_color="#e4edf3")
cust_frame.place(relx=0, rely=0, relwidth=1, relheight=0.93)

customer_satisfaction_label = ctk.CTkLabel(cust_frame, text=f"Satisfaction: {customer_satisfaction}", font=("Arial", 20, "bold"), text_color="#6d7e95")
customer_satisfaction_label.pack(expand=True)


# ========================================================
# 3. REPUTATION CARD WITH SHADOW
# ========================================================
reputation = 50

# Container in Column 2
rep_container = ctk.CTkFrame(top_frame, fg_color="transparent", width=220, height=65)
rep_container.grid(row=0, column=2, padx=10, pady=10)
rep_container.pack_propagate(False)

# The White Card
rep_frame = ctk.CTkFrame(rep_container, fg_color="white", corner_radius=10, border_width=3, border_color="#e4edf3")
rep_frame.place(relx=0, rely=0, relwidth=1, relheight=0.93)

reputation_label = ctk.CTkLabel(rep_frame, text=f"Reputation: {reputation}", font=("Arial", 20, "bold"), text_color="#6d7e95")
reputation_label.pack(expand=True)

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

button_frame = ctk.CTkFrame(window, fg_color="#88BACF", width=900, height=90, corner_radius=12)
button_frame.place(relx=0.5, rely=0.5, anchor="center")
button_frame.grid_propagate(True)

button1 = ctk.CTkButton(button_frame, text="Start Game", font=("Arial", 20), command=lambda:(hide_buttons(), random_scenario()),corner_radius=10, width=15, height=70)
button1.pack(pady=50)

button2 = ctk.CTkButton(button_frame, text="Quit", font=("Arial", 20), command=lambda:(window.destroy()), corner_radius=10, width=15, height=70)
button2.pack(pady=70)

button3 = ctk.CTkButton(button_frame, text="", font=("Arial", 20), command=ignore, corner_radius=10, width=15, height=70)

scenario = tk.Label(window, text="", font=("Arial", 20))
scenarios = [price_complaint, spilled_drink]

window.mainloop()
