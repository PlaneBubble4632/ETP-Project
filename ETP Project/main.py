import tkinter as tk
import customtkinter as ctk
import random
window = ctk.CTk()
window.geometry("1100x800")
window.title("ETP game")
window.configure(fg_color="#8ecae6")

title = tk.Label(window, text="Entreprenuership Game Simulator", font=("Arial", 30, "bold"), bg="#8ecae6")
title.pack(pady=20)

top_frame = ctk.CTkFrame(window, fg_color="#8ecae6", width=900, height=90, corner_radius=12)
top_frame.place(relx=0.5, rely=0.1, anchor="n")
top_frame.grid_propagate(False)

# Distribute spacing evenly
top_frame.grid_columnconfigure(0, weight=1)
top_frame.grid_columnconfigure(1, weight=1)
top_frame.grid_columnconfigure(2, weight=1)



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



customer_satisfaction = 10

# Container in Column 1
customer_container = ctk.CTkFrame(top_frame, fg_color="transparent", width=260, height=65)
customer_container.grid(row=0, column=1, padx=10, pady=10)
customer_container.pack_propagate(False)

# The White Card
cust_frame = ctk.CTkFrame(customer_container, fg_color="white", corner_radius=10, border_width=3, border_color="#e4edf3")
cust_frame.place(relx=0, rely=0, relwidth=1, relheight=0.93)

customer_satisfaction_label = ctk.CTkLabel(cust_frame, text=f"Customer Satisfaction: {customer_satisfaction}", font=("Arial", 20, "bold"), text_color="#6d7e95")
customer_satisfaction_label.pack(expand=True)



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



#Labels
def update_label():
    money_label.configure(text=f"Money: ${money}")
    reputation_label.configure(text=f"Reputation: {reputation}")
    customer_satisfaction_label.configure(text=f"Customer Satisfaction: {customer_satisfaction}")



#Randomizer for scenarios
def random_scenario():
    global scenarios
    if len(scenarios) == 0:
        scenario.configure(
            text="You completed all scenarios!"
        )
        hide_buttons()
        return
    chosen_scenario = random.choice(scenarios)
    chosen_scenario()



#Scenarios
def price_complaint():
    scenario.configure(text="Scenario: Customer complains the drink is too expensive")
    button1.configure(text="Lower Price", command=lower_price)
    button1.pack()
    button2.configure(text="Improve Quality", command=improve_quality)
    button2.pack()
    button3.configure(text="Ignore", command=ignore)
    button3.pack()
    global scenarios
    scenarios.remove(price_complaint)    

def spilled_drink():
    scenario.configure(text="Scenario: Customer spilled their drink")
    button1.configure(text="Apologize and give compensation", command=apologize_and_compensate)
    button2.configure(text="Scold the Customer", command=scold_customer)
    button3.configure(text="Ignore", command=ignore)
    button1.pack()
    button2.pack()
    button3.pack()
    global scenarios
    scenarios.remove(spilled_drink)



#Actions
def lower_price():
    global money
    money -= 10
    global customer_satisfaction
    customer_satisfaction += 5
    update_label()
    scenario.configure(text="You lowered the price. Customers are happy but your profit is reduced.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def improve_quality():
    global money
    money -= 20
    global reputation
    reputation += 10
    update_label()
    scenario.configure(text="You improved the quality. Customers are happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def ignore():
    global reputation
    reputation -= 20
    global customer_satisfaction
    customer_satisfaction -= 10
    update_label()
    scenario.configure(text="You ignored the complaint. Customers are dissatisfied.")
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
    scenario.configure(text="You apologized and gave compensation. Customers are very happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def scold_customer():
    global reputation
    reputation -= 30
    global customer_satisfaction
    customer_satisfaction -= 20
    update_label()
    scenario.configure(text="You scolded the customer. Customers are very dissatisfied and your reputation suffers.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def walk_away():
    global reputation
    reputation -= 10
    update_label()
    scenario.configure(
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

def change_color():
    global container_two
    container_two.configure(fg_color="#237864")

#BUTTONS

button_frame = ctk.CTkFrame(
    window, 
    fg_color="#8ecae6", 
    width=2000, 
    height=600
    )
button_frame.place(relx=0.5, rely=0.4, anchor="n")
button_frame.grid_propagate(False)

button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_rowconfigure(1, weight=1)
button_frame.grid_rowconfigure(2, weight=1)
button_frame.grid_rowconfigure(3, weight=1)
button_frame.grid_rowconfigure(4, weight=1)
button_frame.grid_rowconfigure(5, weight=1)
button_frame.grid_rowconfigure(6, weight=1)
button_frame.grid_rowconfigure(7, weight=1)
button_frame.grid_rowconfigure(8, weight=1)
button_frame.grid_rowconfigure(9, weight=1)
button_frame.grid_rowconfigure(10, weight=1)

button_frame.grid_columnconfigure(0, weight=1)

#Button 1

button1_container = ctk.CTkFrame(button_frame, fg_color="transparent")
button1_container.grid(row=2, column=0, padx=10, pady= 10)

button1 = ctk.CTkButton(
    button1_container, 
    text="Start Game", 
    font=("Helvetica", 23, "bold"), 
    command=lambda:(hide_buttons(), random_scenario(), change_color()),
    fg_color="#0077b6",
    text_color="#bde0fe",
    height=70,
    width=300
)
button1.pack()

#Button 2

button2_container = ctk.CTkFrame(button_frame, fg_color="transparent")
button2_container.grid(row=3, column=0, padx=10, pady= 10)

button2 = ctk.CTkButton(
    button2_container, 
    text="Quit", 
    font=("Helvetica", 23, "bold"), 
    command=lambda:(window.destroy()),
    fg_color="#0077b6",
    text_color="#bde0fe",
    height=70,
    width=300
)
button2.pack()

#Button 3

button3_container = ctk.CTkFrame(button_frame, fg_color="transparent")
button3_container.grid(row=4, column=0, padx=10, pady= 10)

button3 = ctk.CTkButton(
    button3_container, 
    text="", 
    font=("Helvetica", 23, "bold"), 
    fg_color="#0077b6",
    text_color="#bde0fe",
    height=70,
    width=300
)



#Scenario

scenario_place = ctk.CTkFrame(
    window, 
    fg_color="transparent",  
    width=1000,           
    height=125
)
scenario_place.place(relx=0.5, rely=0.3065, anchor="center")

# ==========================================
# 2. CONTAINER 1 (Inside Main Frame)
# ==========================================
container_one = ctk.CTkFrame(
    scenario_place, 
    fg_color="transparent",    
)
container_one.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

# ==========================================
# 3. CONTAINER 2 (Inside Container 1)
# ==========================================
container_two = ctk.CTkFrame(
    container_one, 
    fg_color="transparent",    
)
container_two.place(relx=0.02, rely=0.1, relwidth=0.96, relheight=0.8)

# ==========================================
# 4. THE TEXT LABEL (Inside Container 2)
# ==========================================
scenario = ctk.CTkLabel(
    container_two,
    text="", 
    font=("Helvetica", 23, "bold"), 
    text_color="#bde0fe",
    wraplength= 800
)
# Snaps the text to the dead center of Container 2
scenario.place(relx=0.5, rely=0.5, anchor="center")

scenarios = [price_complaint, spilled_drink]

window.mainloop()
