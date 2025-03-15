import time
import random
from collections import deque

# ------------------ INVENTORY SYSTEM (STACK) ------------------
class Inventory:
    def __init__(self, max_size=5):
        self.stack = []
        self.max_size = max_size

    def add_item(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            print(f"🔹 {item} added to inventory.")
        else:
            print("❌ Inventory full! Cannot pick up more items.")

    def use_item(self):
        if self.stack:
            item = self.stack.pop()
            print(f"⚔️ Used {item}.")
            if item in ["Healing Potion", "Health Kit"]:
                game.health = min(game.max_health, game.health + 30)
                print(f"❤️ Healed! Current health: {game.health}")
            return item
        else:
            print("❌ No items left!")
            return None

    def show_inventory(self):
        print("\n🎒 Inventory:", self.stack[::-1] if self.stack else "Empty")

# ------------------ QUEST SYSTEM (QUEUE) ------------------
class QuestLog:
    def __init__(self):
        self.queue = deque()

    def add_quest(self, quest):
        self.queue.append(quest)
        print(f"📜 New Quest: {quest}")

    def complete_quest(self):
        if self.queue:
            quest = self.queue.popleft()
            print(f"✅ Quest Completed: {quest}")
        else:
            print("❌ No quests left!")

    def show_quests(self):
        print("\n📖 Quest Log:", list(self.queue) if self.queue else "No quests available.")

# ------------------ GAME SYSTEM ------------------
class AdventureGame:
    def __init__(self):
        self.inventory = Inventory()
        self.quests = QuestLog()
        self.running = True
        self.location = "Village"
        self.health = 100 
        self.max_health = 100
    
    def display_menu(self):
        print(f"\n❤️ Health: {self.health}/{self.max_health}")
        print("\n🌍 You are in:", self.location)
        print("1️⃣ Explore")
        print("2️⃣ Check Inventory")
        print("3️⃣ Use an Item")
        print("4️⃣ View Quests")
        print("5️⃣ Complete a Quest")
        print("6️⃣ Quit")

    # ------------------ RECURSIVE DUNGEON EXPLORATION ------------------
    def explore_dungeon(self, depth=1, max_depth=5):
        """
        STUDENT TASK: Implement recursive dungeon exploration
        
        This function should explore a dungeon recursively, with each recursive call
        representing going deeper into the dungeon.
        
        Parameters:
        - depth: Current depth level in the dungeon (starts at 1)
        - max_depth: Maximum depth of the dungeon
        
        Tips for implementation:
        1. Base case: When depth > max_depth, you've reached the end of the dungeon
           - Print a message that the player reached the end
           - Give the player a rare treasure
           - Return from the function
           
        2. Print the current dungeon level being explored
        
        3. Generate a random event (enemy, treasure, passage, or trap)
        
        4. For each event type, implement the appropriate logic:
           - enemy: Combat system (use inventory items or take damage)
           - treasure: Find and add items to inventory
           - passage: Automatically go deeper (recursive call)
           - trap: Take damage and possibly go deeper
           
        5. Include recursive calls in appropriate places to explore deeper
           - After defeating an enemy (with some probability)
           - After finding treasure (with some probability)
           - After surviving a trap (with some probability)
           - When finding a passage (always)
        """
        # Your code here
        
        # Base case example (you can modify this):
        if depth > max_depth:
            print("🛑 You've reached the end of the dungeon!")
            treasure = random.choice(["Fire Aspect Netherite Sword", "Bottle of Panacea", "Enchanted Golden Apple", "Totem of Undying", "Coast Armor Trim", "Staff of Summoning", "Stash of Gold"])
            print(f"💰 You found a rare treasure: {treasure}!")
            self.inventory.add_item(treasure)
            return
            
        print(f"🕳️ Exploring Dungeon Level {depth}...")
        time.sleep(1)  # Add suspense
        
        # Generate a random event
        event = random.choice(["enemy", "treasure", "passage", "trap"])
        
        # TODO: Implement the logic for each event type
        
        # Example for the "enemy" event (you should complete this):
        if event == "enemy":
            enemy_types = ["Reanimated Guard", "Poltergeist", "Fire Elemental", "Goblin Scout", "Stone Golem", "Gelatinous Cube", "Resin Skeleton", "Cave Spider", "Zombified Prisoner", "Paper Demon"]
            enemy = random.choice(enemy_types)
            print(f"⚔️ A {enemy} appears!")
            
            # TODO: Implement combat logic
            # - If player has items, use one to defeat the enemy
            # - If no items, take damage
            # - With some probability, find a passage deeper after defeating an enemy
            
        # TODO: Implement the "treasure" event
        elif event == "treasure":
            # - Find a random item
            # - Add it to inventory
            # - With some probability, find a passage deeper
            common_treasures = random.choice(["Coal", "Fire Charge", "Bottle o' Enchanting", "Bag of Redstone", "Contraband Rucksack", "Spectral Arrows"])
            uncommon_treasures = random.choice(["Bottle o' Glowstone", "Golden Carrot"])
            unusual_treasure = random.choice([""])

        # TODO: Implement the "trap" event
        elif event == "trap":
            # - Take damage from the trap
            # - Check if player is defeated
            # - With some probability, find a passage deeper
            pass
            
        # TODO: Implement the "passage" event
        else:  # passage
            # - Find a passage
            # - Make a recursive call to explore deeper
            pass

    def explore(self):
        places = ["Cherry Grove", "Trial Ruins", "Mesa Mineshaft", "Beneath the Village", "Blackstone Bastion", "Necropolis in the End", "Ancient Dungeon Entrance"]
        self.location = random.choice(places)
        print(f"🚶 You explored and arrived at {self.location}.")

        # Special case for dungeon
        if self.location == "Ancient Dungeon Entrance":
            print("You find an entrance to an ancient dungeon. Do you want to enter?")
            choice = input("Enter (y/n): ").lower()
            if choice == 'y':
                max_depth = random.randint(3, 7)  # Random dungeon depth
                print(f"You descend into the dungeon which seems to go {max_depth} levels deep...")
                self.explore_dungeon(1, max_depth)
                self.location = "Village"  # Return to village after dungeon
                return
            else:
                print("You decide not to enter the dungeon and return to exploring.")
                self.location = random.choice(["Dark Forest", "Abandoned Ruins", "Mysterious Cave", "Merchant's Bazaar"])

        event = random.choice(["item", "enemy", "quest", "nothing"])
        
        if event == "item":
            item = random.choice(["Healing Potion", "Steel Sword", "Magic Scroll", "Shield", "Health Kit"]) 
            print(f"✨ You found a {item}!")
            self.inventory.add_item(item)

        elif event == "enemy":
            enemy = random.choice(["Goblin", "Skeleton", "Dark Mage"])
            print(f"⚔️ A wild {enemy} appears!")
            if self.inventory.stack:
                print("You fight the enemy...")
                time.sleep(1)
                used_item = self.inventory.use_item()
                print(f"🔥 You defeated the {enemy} using {used_item}!")
            else:
                damage = random.randint(10, 25)
                self.health = max(0, self.health - damage)
                print(f"💀 You have no weapons! You took {damage} damage!")
                
                if self.health <= 0:
                    print("☠️ You have been defeated! Returning to Village to recover...")
                    self.health = self.max_health
                else:
                    print(f"You barely escape with {self.health} health remaining.")
                self.location = "Village"

        elif event == "quest":
            quest = random.choice(["Find the Lost Amulet", "Defeat the Bandit Leader", "Rescue the Captured Villager", "Explore the Ancient Dungeon"])
            self.quests.add_quest(quest)

        else:
            print("🌾 Nothing special happened.")

    def start_game(self):
        print("🎮 Welcome to the Adventure Game!")
        while self.running:
            self.display_menu()
            choice = input("Choose an action: ")

            if choice == "1":
                self.explore()
            elif choice == "2":
                self.inventory.show_inventory()
            elif choice == "3":
                self.inventory.use_item()
            elif choice == "4":
                self.quests.show_quests()
            elif choice == "5":
                self.quests.complete_quest()
            elif choice == "6":
                print("👋 Thanks for playing! Goodbye.")
                self.running = False
            else:
                print("❌ Invalid choice! Try again.")

# ------------------ START THE GAME ------------------
if __name__ == "__main__":
    game = AdventureGame()
    game.start_game()
