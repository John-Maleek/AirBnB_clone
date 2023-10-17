#!/usr/bin/python3
"""
first Airbnb_clone project
"""

class AirbnbCommandInterpreter:
    def __init__(self):
        self.listings = []
        self.reservations = []

    def run(self):
            while True:
                user_input = input("Enter a command: ")
                self.process_command(user_input)

    def process_command(self, command):
        parts = command.split()

        if not parts:
            print("please enter a command.")
            return
        action = parts[0]

        if action == "create_listing":
            if len(parts) < 2:
                print("Usage: create_listing <listing_name>")
            else:
                listing_name = ' '.join(parts[1:])
                self.create_listing(listing_name)

        elif action == "list_listings":
            self.list_all_listings()

    def create_listing(self, name):
        self.listings.append(name)
        print(f"Created a new listing: {name}")

    def list_all_listings(self):
        print("Available listings:")
        for i, listing in enumerate(self.listings):
            print(f"{i + 1}. {listing}")

if __name__ == "__main__":
    interpreter = AirbnbCommandInterpreter()
    interpreter.run()
