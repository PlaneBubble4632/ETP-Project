import tkinter as tk
import customtkinter as ctk
import random
import pygame
import os
BASE_DIR = os.path.dirname(__file__)
window = ctk.CTk()
window.geometry("1100x800")
window.title("ETP game")
window.configure(fg_color="#8ecae6")

#Audios (to run inside program something.play())
pygame.mixer.init()

click_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "freesoundeffects-button-click-289742.wav"))

lose_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "u_l5xum8z250-losing-horn-313723.wav"))

win_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "u_ss015dykrt-brass-fanfare-with-timpani-and-winchimes-reverberated-146260.wav"))

menu_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "dragon-studio-menu-open-sound-effect-432999.wav"))

status_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "sounds", "freesound_community-menu-button-89141.wav"))

click_sound.set_volume(0.1)
lose_sound.set_volume(0.3)
win_sound.set_volume(0.3)
menu_sound.set_volume(0.2)
status_sound.set_volume(0.2)

window.bind("<Button-1>", lambda event: click_sound.play())

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
customer_container = ctk.CTkFrame(top_frame, fg_color="transparent", width=290, height=65)
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
        hide_buttons_end()
        window.after(5000, back_to_menu)
    chosen_scenario = random.choice(scenarios)
    chosen_scenario()



#Scenarios
def price_complaint():
    scenario.configure(text="Scenario: Customer complains the drink is too expensive")
    button1.configure(text="Lower Price", command=lambda: lower_price(-10, +5, 0))
    button2.configure(text="Improve Quality", command=lambda: improve_quality(-20, 0, +10))
    button3.configure(text="Ignore", command=lambda: ignore(0, -10, -20))
    global scenarios
    scenarios.remove(price_complaint)    

def spilled_drink():
    scenario.configure(text="Scenario: Customer spilled their drink")
    button1.configure(text="Apologize and give compensation", command=lambda: apologize_and_compensate(-30, +10, +15))
    button2.configure(text="Scold the Customer", command=lambda: scold_customer(0, -20, -30))
    button3.configure(text="Walk Away", command=lambda: walk_away(0, 0, -10))
    global scenarios
    scenarios.remove(spilled_drink)
    
def complains():
    scenario.configure(text="Scenario: A karen immediately jumps in the store to complain about how the cafe ruins the beautiful view of the street.")
    button1.configure(text="Kick her out", command=lambda: kick_out(-20, 0, +20))
    button2.configure(text="Give her free drink", command=lambda: free_drink(-5, 0, 0))
    button3.configure(text="Ignore", command=lambda: ignore(-10, 0, +10))
    global scenarios
    scenarios.remove(complains)

def drugs():
    scenario.configure(text="Scenario: Out of the blues, a cop comes storming in with a claim that you are infusing narcotics with food.")
    button1.configure(text="Disagree with Accusation", command=lambda: disagree(-20, 0, -10))
    button2.configure(text="Show Rep as Proof it is False", command=lambda: proof(0,0,0))
    button3.configure(text="Bribe", command=lambda: bribe(-40, 0, -10))
    global scenarios
    scenarios.remove(drugs)

def toddler():
    scenario.configure(text="Scenario: A toddler went on a tantrum and spills drinks everywhere, disrupting other customers.")
    button1.configure(text="Reprimand the Toddler", command=lambda: reprimand(-10, 0, +10))
    button2.configure(text="Ask for a fine", command=lambda: fine(+15, 0, -5))
    button3.configure(text="Scold the Family", command=lambda: family(-15, 0, +15))
    global scenarios
    scenarios.remove(toddler)

def salty():
    scenario.configure(text="Scenario: A toddler went on a tantrum and spills drinks everywhere, disrupting other customers.")
    button1.configure(text="Adjust Recipe", command=lambda: reprimand(-10, +10, +15))
    button2.configure(text="Give Extra Salt Dip", command=lambda: fine(-5, +10, +5))
    button3.configure(text="Ignore", command=lambda: family(0, -5, 0))
    global scenarios
    scenarios.remove(salty)

def lamp():
    scenario.configure(text="Scenario: The ceiling lamp above just went out. As an employee, what are you going to do?")
    button1.configure(text="Replace the Ball Lamp", command=lambda: reprimand(-15, +10, +5))
    button2.configure(text="Use a Dim Spare one", command=lambda: fine(-5, -5, 0))
    button3.configure(text="Ignore", command=lambda: family(0, -5, -5))
    global scenarios
    scenarios.remove(lamp)

def newt():
    scenario.configure(text="Scenario: Just as you were about to enjoy your day, a random newt just fell onto a customer's plate.")
    button1.configure(text="Compensate", command=lambda: reprimand(-10, +15, +10))
    button2.configure(text="Only Apologize", command=lambda: fine(0, -5, 0))
    button3.configure(text="Focus on Other Customers", command=lambda: family(-20, +25, -10))
    global scenarios
    scenarios.remove(newt)

clicks = 0
def start_minigame():
    global clicks, scenario

    scenario.configure(
        text="RUSH HOUR! Click the button as fast as possible!"
    )

    button1.configure(
        text="SERVE CUSTOMER",
        command=click_customer
    )

    scenario.place(relx=0.5, rely=0.5, anchor="center")
    button1.pack()
    button2.destroy()
    button3.destroy()

    window.after(5000, end_minigame)



#Actions

change_m = 0
change_c = 0
change_r = 0

def click_customer():

    global clicks

    clicks += 1

    scenario.configure(
        text=f"Customers served: {clicks}"
    )

def end_minigame():

    global money

    reward = clicks * 3

    money += reward

    update_label()

    scenario.configure(
        text=f"Rush hour ended! You earned ${reward}"
    )

    window.after(3000, next_round)

def family(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global reputation, customer_satisfaction
    reputation += change_r
    customer_satisfaction += change_c
    update_label()
    scenario.configure(text="You scolded the family. Customers are very dissatisfied and your reputation suffers.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def fine(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money, reputation
    money += change_m
    reputation += change_r
    update_label()
    scenario.configure(text="You fined the customer. Customers are happy and your profit increases.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def reprimand(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money, reputation
    money += change_m
    reputation += change_r
    update_label()
    scenario.configure(text="You reprimanded the customer. Customers are happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def proof(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global reputation
    if reputation >= 30:
        change_r = +20
        reputation += change_r
    else:
        change_r = -20
        reputation += change_r
    update_label()
    scenario.configure(text="You showed your good rep as proof. Customers are happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())
    
def bribe(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money, reputation
    money += change_m
    reputation += change_r
    update_label()
    scenario.configure(text="You bribed the cop. Customers are dissatisfied and your reputation suffers.")
    hide_buttons()
    window.after(5000, lambda: next_round())
    
def disagree(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global reputation
    reputation += change_r
    update_label()
    scenario.configure(text="You disagreed with the accusation. Customers are happy and your reputation improves.") ############################
    hide_buttons()
    window.after(5000, lambda: next_round())

def ignore_karen(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money, reputation
    money += change_m  
    reputation += change_r
    update_label()
    scenario.configure(text="You ignored the karen. Customers are dissatisfied and your reputation suffers.") #####################
    hide_buttons()
    window.after(5000, lambda: next_round())

def free_drink(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money, reputation
    money += change_m
    reputation += change_r
    update_label()
    scenario.configure(text="You gave the customer a free drink. Customers are happy but your profit is reduced.") ##########################
    hide_buttons()
    window.after(5000, lambda: next_round())

def kick_out(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money
    money += change_m
    global reputation
    reputation += change_r
    update_label()
    scenario.configure(text="You kicked out the customer. Customers are happy but your reputation suffers.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def lower_price(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money
    money += change_m
    global customer_satisfaction
    customer_satisfaction += change_c
    update_label()
    scenario.configure(text="You lowered the price. Customers are happy but your profit is reduced.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def improve_quality(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money
    money += change_m
    global reputation
    reputation += change_r
    update_label()
    scenario.configure(text="You improved the quality. Customers are happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def ignore(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global customer_satisfaction
    customer_satisfaction += change_c
    global reputation
    reputation += change_r
    update_label()
    scenario.configure(text="You ignored the complaint. Customers are dissatisfied.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def apologize_and_compensate(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global money
    money += change_m
    global customer_satisfaction
    customer_satisfaction += change_c
    global reputation
    reputation += change_r
    update_label()
    scenario.configure(text="You apologized and gave compensation. Customers are very happy and your reputation improves.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def scold_customer(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global customer_satisfaction
    customer_satisfaction += change_c
    global reputation
    reputation += change_r
    update_label()
    scenario.configure(text="You scolded the customer. Customers are very dissatisfied and your reputation suffers.")
    hide_buttons()
    window.after(5000, lambda: next_round())

def walk_away(money_stat, customer_stat, reputation_stat):
    changes(money_stat, customer_stat, reputation_stat)
    global reputation
    reputation += change_r
    update_label()
    scenario.configure(
        text="You walked away. Customers lost trust in you.")
    hide_buttons()
    window.after(5000, lambda:next_round())

def changes(money_stat, customer_stat, reputation_stat):
    global change_m, change_c, change_r
    change_m = money_stat
    change_c = customer_stat
    change_r = reputation_stat

def enable_button():
    button1.pack()
    button2.pack()
    button3.pack()

def next_round():
    enable_button()
    random_scenario()
    game_over_check()

def hide_buttons_end():
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()

def hide_buttons():
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    status_change()

def change_color():
    global container_two
    container_two.configure(fg_color="#237864")

#Status Change

def status_change():
    status_place = ctk.CTkFrame(
        window,
        fg_color="#8ecae6",
        width=700,
        height=150,
        corner_radius=8,
        border_width=4,
        border_color="#101729"
    )
    status_place.place(relx=0.5, rely=0.55, anchor="center")
    status_place.grid_propagate(False)

    status_place.grid_columnconfigure(0, weight=1)
    status_place.grid_columnconfigure(1, weight=1)
    status_place.grid_columnconfigure(2, weight=1)
    status_place.grid_rowconfigure(0, weight=1)
    status_place.grid_rowconfigure(1, weight=1)
    status_place.grid_rowconfigure(2, weight=1)

    global change_m, change_c, change_r

    status_container_money = ctk.CTkFrame(status_place, fg_color="transparent", width=170, height=50)
    status_container_money.grid(row=1, column=0, padx=10)

    status_container_customer = ctk.CTkFrame(status_place, fg_color="transparent", width=300, height=50)
    status_container_customer.grid(row=1, column=1, padx=10)

    status_container_reputation = ctk.CTkFrame(status_place, fg_color="transparent", width=200, height=50)
    status_container_reputation.grid(row=1, column=2, padx=10)

    #Money Status

    if change_m < 0:
        status_frame_money = ctk.CTkFrame(
            status_container_money, 
            fg_color="#fcecec",
            border_width=2,
            border_color="#fac9cb"
            )
        status_frame_money.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        status_label_money = ctk.CTkLabel(
            status_frame_money, 
            text=f"{change_m} Money", 
            font=("Helvetica", 18, "bold"), 
            text_color="#fb4b4b",
            )
        status_label_money.place(relx=0.5, rely=0.5, anchor="center")
    elif change_m > 0:
        status_frame_money = ctk.CTkFrame(
            status_container_money, 
            fg_color="#e8faee",
            border_width=2,
            border_color="#bfeed2"
            )
        status_frame_money.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        status_label_money = ctk.CTkLabel(
            status_frame_money, 
            text=f"+{change_m} Money", 
            font=("Helvetica", 18, "bold"), 
            text_color="#23c463",
            )
        status_label_money.place(relx=0.5, rely=0.5, anchor="center")

    #Customer Satisfaction

    if change_c < 0:
        status_frame_customer = ctk.CTkFrame(
            status_container_customer, 
            fg_color="#fcecec",
            border_width=2,
            border_color="#fac9cb"
            )
        status_frame_customer.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        status_label_customer = ctk.CTkLabel(
            status_frame_customer, 
            text=f"{change_c} Customer Satisfaction", 
            font=("Helvetica", 18, "bold"), 
            text_color="#fb4b4b",
            )
        status_label_customer.place(relx=0.5, rely=0.5, anchor="center")

    elif change_c > 0:
        status_frame_customer = ctk.CTkFrame(
            status_container_customer, 
            fg_color="#e8faee",
            border_width=2,
            border_color="#bfeed2"
            )
        status_frame_customer.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        status_label_customer = ctk.CTkLabel(
            status_frame_customer, 
            text=f"+{change_c} Customer Satisfaction", 
            font=("Helvetica", 18, "bold"), 
            text_color="#23c463",
            )
        status_label_customer.place(relx=0.5, rely=0.5, anchor="center")

    #Reputation

    if change_r < 0:
        status_frame_reputation = ctk.CTkFrame(
            status_container_reputation, 
            fg_color="#fcecec",
            border_width=2,
            border_color="#fac9cb"
            )
        status_frame_reputation.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        status_label_reputation = ctk.CTkLabel(
            status_frame_reputation, 
            text=f"{change_r} Reputation", 
            font=("Helvetica", 18, "bold"), 
            text_color="#fb4b4b",
            )
        status_label_reputation.place(relx=0.5, rely=0.5, anchor="center")

    elif change_r > 0:
        status_frame_reputation = ctk.CTkFrame(
            status_container_reputation, 
            fg_color="#e8faee",
            border_width=2,
            border_color="#bfeed2"
            )
        status_frame_reputation.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        status_label_reputation = ctk.CTkLabel(
            status_frame_reputation, 
            text=f"+{change_r} Reputation", 
            font=("Helvetica", 18, "bold"), 
            text_color="#23c463",
            )
        status_label_reputation.place(relx=0.5, rely=0.5, anchor="center")

    status_place.after(4500, lambda: status_place.destroy())

#Game Over
def game_over_check():
    global money, reputation, customer_satisfaction, scenario
    if money <= 0 or reputation <= 0 or customer_satisfaction <= 0:
        scenario.configure(text="Game Over! You ran out of money or your reputation dropped too low.")
        hide_buttons_end()
        lose_sound.play()
        back_to_menu()
    else:
        pass

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
    command=lambda:(random_scenario(), change_color(), menu_sound.play(), enable_button()),
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
    command=lambda:(window.destroy(), click_sound.play()),
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

scenarios = [start_minigame]

#Button for back to menu (appears after game over)

def back_to_menu(): 
    global money, customer_satisfaction, reputation, scenarios
    money = 100
    customer_satisfaction = 10
    reputation = 50
    update_label()

    global scenario, button1, button2, button3
    button1.configure(text="Restart Game", command=lambda: (random_scenario(), change_color(), menu_sound.play(), enable_button()))
    button1.pack()
    button2.configure(text="Quit", command=lambda: (window.destroy(), click_sound.play()))
    button2.pack()
    button3.pack_forget()
    scenario_place.forget()

    scenarios = [price_complaint, spilled_drink]

window.mainloop()