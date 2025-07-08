#!/usr/bin/env python3
# coffee_chatbot_template.py
"""
Refactored for Flask: handlers return strings, and there's a single `get_reply` function.
"""


def handle_menu():
    return "Our menu: Espresso, Latte, Cappuccino, Mocha, Green Tea."


def handle_hours():
    return "We’re open daily from 7am to 7pm."


def handle_location():
    return "Find us at 123 Brew St., Beanville."


def handle_specials():
    return "Today's special: Pumpkin Spice Latte!"


def handle_wifi():
    return "Wi-Fi is free! Connect to 'CoffeeShopGuest' and ask staff for the password."


def handle_contact():
    return "Call us at (555) 123-4567 or email hello@coffeebot.com."


def handle_parking():
    return "Street parking available; use the lot behind the shop after 6pm."


def handle_loyalty():
    return "Join our loyalty program: buy 9 drinks, get the 10th free."


def handle_events():
    return "Live music on Fridays at 6pm and Latte Art workshops on Saturdays."


def handle_order():
    return "Order online at coffee.example.com or pop in and order at the counter."


def handle_fallback():
    return "Sorry, I don't have that info. Ask about menu, hours, location, specials, etc."


def get_reply(msg: str) -> str:
    """
    Normalize the message and dispatch to the right handler.
    Returns the handler’s string response.
    """
    text = msg.lower().strip()
    if "menu" in text:
        return handle_menu()
    if "hour" in text or "open" in text:
        return handle_hours()
    if "location" in text or "address" in text:
        return handle_location()
    if "special" in text:
        return handle_specials()
    if "wifi" in text:
        return handle_wifi()
    if "contact" in text:
        return handle_contact()
    if "park" in text:
        return handle_parking()
    if "loyalty" in text:
        return handle_loyalty()
    if "event" in text:
        return handle_events()
    if "order" in text:
        return handle_order()
    return handle_fallback()


# Optional CLI test
def get_intent_handler():
    print("Coffee Bot CLI – type 'exit' to quit")
    while True:
        user = input("> ")
        if user.lower().strip() in ("exit", "quit"):
            print("Goodbye!")
            break
        print(get_reply(user))
