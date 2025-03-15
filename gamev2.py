import time
import random
from collections import deque
from constants import common_treasure

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
        
    def crack_magic_lock(self):
        """
        Binary Search feature for cracking a magic lock using a spellbook.
        The player must find the correct spell from their sorted spellbook
        to open an ancient door.
        
        STUDENT TASK: Implement the binary search algorithm to find the correct spell.
        """
        print("\n🔮 ANCIENT DOOR UNLOCKING SYSTEM 🔮")
        print("You've encountered an ancient magical door with strange inscriptions.")
        print("The door requires a specific spell from your spellbook to unlock.")
        print("Your spellbook contains hundreds of spells in alphabetical order.")
        print("The door will give you hints if you're getting 'warmer' or 'colder'.")
        
        # Create a sorted list of spells (100 spells for demonstration)
        spells = [
            "Arcane Sight", "Astral Shield", "Aura Reading", "Banishment", "Binding Chains",
            "Blinding Flash", "Blink Step", "Blood Boil", "Bone Shatter", "Call Lightning",
            "Chaos Wave", "Chrono Shift", "Circle of Protection", "Clairvoyance", "Control Weather",
            "Counterspell", "Dark Vision", "Deadlight", "Deafening Thunder", "Demon Summoning",
            "Detect Magic", "Dimensional Door", "Disintegration", "Dispel Magic", "Dragon's Breath",
            "Dream Walk", "Earth Tremor", "Eldritch Blast", "Elemental Form", "Enchant Item",
            "Energy Drain", "Ethereal Form", "Exploding Runes", "Familiar Bond", "Feather Fall",
            "Fireball", "Flame Strike", "Flesh to Stone", "Floating Disk", "Freezing Touch",
            "Gale Force", "Ghostly Hand", "Glowing Orb", "Gravity Well", "Greater Healing",
            "Haste", "Heroism", "Ice Storm", "Identify Object", "Illusory Double",
            "Imprisoning Sphere", "Incorporeal Form", "Invisibility", "Invulnerability", "Kinetic Barrier",
            "Levitation", "Life Drain", "Light", "Locate Object", "Locking Seal",
            "Mage Armor", "Magic Missile", "Magnetic Pull", "Mass Confusion", "Memory Alteration",
            "Mental Barrier", "Mind Reading", "Mirror Image", "Mist Form", "Mystic Binding",
            "Necromantic Touch", "Night Vision", "Nullify Magic", "Obscuring Fog", "Paralyzing Touch",
            "Phantom Steed", "Planar Binding", "Portal Creation", "Power Word: Kill", "Prismatic Spray",
            "Psychic Scream", "Purify Food", "Raise Dead", "Ray of Frost", "Reality Distortion",
            "Regeneration", "Repulsion Field", "Revealing Light", "Reverse Gravity", "Runic Ward",
            "Scrying", "Shadow Step", "Shield", "Sleep", "Slow",
            "Soul Trap", "Spectral Sight", "Spell Reflection", "Spirit Guardian", "Stone Skin",
            "Summon Elemental", "Telekinesis", "Telepathic Bond", "Teleport", "Time Stop"
        ]
        
        # Sort the spells alphabetically (they're already sorted, but just to be sure)
        spells.sort()
        
        # Randomly select a correct spell
        correct_spell_index = random.randint(0, len(spells) - 1)
        correct_spell = spells[correct_spell_index]
        
        print(f"\nYour spellbook contains {len(spells)} spells.")
        print("The door's magical lock will react to your attempts, guiding you to the right spell.")
        print("The door's inscription glows when you get close to the right page.")
        
        # Track attempts
        attempts = 0
        max_attempts = 10  # Give them more than log2(100) ≈ 7 attempts
        
        # STUDENT TASK: Initialize your search boundaries
        # left = ?
        # right = ?
        
        found = False
        
        while attempts < max_attempts and not found:
            # STUDENT TASK: Calculate the middle index for binary search
            # mid = ?
            
            attempts += 1
            
            # Show current spell range being considered
            print(f"\n📚 Current search area: {spells[left]} to {spells[right]}")
            print(f"🔍 Attempt {attempts}/{max_attempts}")
            
            # Show binary search educational component
            print(f"\n💡 Binary search suggests trying: {spells[mid]}")
            
            # Get player's choice - they can follow the suggestion or try another spell
            print("\nOptions:")
            print(f"1) Try the suggested spell ({spells[mid]})")
            print("2) Choose a different spell")
            
            choice = input("Your choice (1 or 2): ")
            
            if choice == "2":
                # Player wants to choose their own spell
                print("\nAvailable spells in your current search area:")
                for i in range(left, right + 1):
                    print(f"{i+1}. {spells[i]}")
                
                try:
                    spell_choice = int(input(f"Choose a spell (enter number 1-{right-left+1}): "))
                    if 1 <= spell_choice <= (right-left+1):
                        mid = left + spell_choice - 1
                    else:
                        print("❌ Invalid choice. Using suggested spell instead.")
                except ValueError:
                    print("❌ Invalid input. Using suggested spell instead.")
            
            # Show the chosen spell
            current_spell = spells[mid]
            print(f"\n✨ You cast {current_spell} at the door...")
            time.sleep(1.5)  # Dramatic pause
            
            # Compare with the correct spell
            if current_spell == correct_spell:
                print("\n🎉 THE DOOR UNLOCKS!")
                print(f"✅ You found the correct spell '{correct_spell}' in {attempts} attempts!")
                
                # Reward based on efficiency
                if attempts <= 3:
                    print("🏆 MASTER SPELLCASTER! Your efficiency was remarkable!")
                    reward = random.choice(["Ancient Grimoire", "Staff of Power", "Archmage's Amulet"])
                elif attempts <= 6:
                    print("🏆 SKILLED SPELLCASTER! You found the spell efficiently!")
                    reward = random.choice(["Magic Wand", "Scroll of Wisdom", "Enchanted Ring"])
                else:
                    print("🏆 NOVICE SPELLCASTER! You unlocked the door successfully!")
                    reward = random.choice(["Minor Spell Scroll", "Apprentice's Charm", "Magic Dust"])
                
                self.inventory.add_item(reward)
                
                # Add a follow-up quest
                followup_quest = f"Explore the chamber beyond the Ancient Door"
                self.quests.add_quest(followup_quest)
                
                found = True
                
            # STUDENT TASK: Implement the binary search logic
            # What should happen if current_spell < correct_spell?
            # What should happen if current_spell > correct_spell?
            
            # Show educational component after each attempt
            if not found:
                print("\n📘 BINARY SEARCH LESSON:")
                print(f"- We've narrowed down to {right - left + 1} spells")
                print(f"- Next optimal guess would be spell #{(left + right) // 2 + 1}: {spells[(left + right) // 2]}")
                
        if not found:
            print("\n❌ You've exhausted your magical energy and failed to unlock the door.")
            print(f"The correct spell was '{correct_spell}'.")
            print("Perhaps you can try again when you've rested.")
            
            # Take some health as penalty
            damage = random.randint(5, 15)
            self.health = max(0, self.health - damage)
            print(f"💥 The magical backlash costs you {damage} health points!")
            
            if self.health <= 0:
                print("☠️ The magical backlash was too strong! You collapse...")
                self.health = self.max_health // 2  # Return with half health
                self.location = "Village"
    
    def track_enemy(self):
        """
        Binary Search feature for tracking and hunting a moving enemy.
        Uses binary search algorithm to efficiently find the enemy's location.
        """
        print("\n🔍 ENEMY TRACKING SYSTEM 🔍")
        print("A dangerous enemy has been spotted in the forest!")
        print("Intelligence reports suggest it's hiding somewhere in regions 1-100.")
        print("Your mission: Find and defeat this enemy using the tracking system.")
        print("The tracking system will tell you if the enemy is in a higher or lower region.")
        
        # Generate a random location for the enemy
        enemy_location = random.randint(1, 100)
        
        # Track number of guesses (to show efficiency of binary search)
        guesses = 0
        max_guesses = 7  # Theoretical max for binary search on range 1-100
        
        # Player's health cost for each guess (makes it strategic)
        guess_cost = 5
        
        left = 1
        right = 100
        
        print("\n💡 TIP: Using binary search is the most efficient strategy!")
        print(f"❤️ Each scan costs {guess_cost} health points.")
        
        while left <= right:
            guesses += 1
            
            # Show the current search range
            print(f"\n🔎 Current search area: Regions {left} to {right}")
            
            # Get player's guess - encourage binary search thinking
            try:
                player_guess = int(input(f"Enter your guess (or enter the middle value {(left + right) // 2} for optimal binary search): "))
                
                # Validate the input
                if player_guess < left or player_guess > right:
                    print(f"❌ Please enter a number between {left} and {right}.")
                    continue
                    
            except ValueError:
                print("❌ Please enter a valid number.")
                continue
            
            # Apply health cost for each guess
            self.health = max(0, self.health - guess_cost)
            print(f"❤️ Health: {self.health}/{self.max_health} (-{guess_cost} for scan)")
            
            # Check if player's health is depleted
            if self.health <= 0:
                print("☠️ You've exhausted yourself from scanning and collapsed!")
                print(f"The enemy was hiding in region {enemy_location}.")
                self.health = self.max_health // 4  # Return with quarter health
                return
                
            # Compare with the enemy's actual location
            if player_guess == enemy_location:
                print(f"\n🎯 ENEMY FOUND IN REGION {enemy_location}!")
                print(f"✅ You found the enemy in {guesses} scans.")
                
                # Reward based on efficiency (using fewer guesses)
                efficiency_bonus = max(0, max_guesses - guesses) * 10
                
                # Add a quest reward
                reward = random.choice(["Legendary Bow", "Enemy's Treasure Map", "Magic Amulet", "Enchanted Armor"])
                self.inventory.add_item(reward)
                
                # Add health bonus for efficiency
                if efficiency_bonus > 0:
                    self.health = min(self.max_health, self.health + efficiency_bonus)
                    print(f"🏆 Your efficient tracking earned you a +{efficiency_bonus} health bonus!")
                    
                print(f"⚔️ You successfully defeated the enemy and found: {reward}!")
                
                # Add a follow-up quest
                followup_quest = f"Hunt down the {reward.split()[-1]} Master"
                self.quests.add_quest(followup_quest)
                
                return
                
            elif player_guess < enemy_location:
                print("📡 Scanning... Enemy detected in a HIGHER region.")
                left = player_guess + 1  # Update the search range
                
            else:  # player_guess > enemy_location
                print("📡 Scanning... Enemy detected in a LOWER region.")
                right = player_guess - 1  # Update the search range
                
            # Educational component: suggest the optimal next guess
            optimal_next = (left + right) // 2
            print(f"💡 Binary search tip: The optimal next guess would be region {optimal_next}")
        
        # This should only happen if there's a logic error
        print("❌ Strange... the enemy seems to have vanished.")
    
    def display_menu(self):
        print(f"\n❤️ Health: {self.health}/{self.max_health}")
        print("\n🌍 You are in:", self.location)
        print("1️⃣ Explore")
        print("2️⃣ Check Inventory")
        print("3️⃣ Use an Item")
        print("4️⃣ View Quests")
        print("5️⃣ Complete a Quest")
        print("6️⃣ Track Enemy (Binary Search)")
        print("7️⃣ Crack Magic Lock (Binary Search)")
        print("8️⃣ Quit")

    # ------------------ RECURSIVE DUNGEON EXPLORATION ------------------
    def explore_dungeon(self, depth=1, max_depth=5):
        # STUDENT TASK: Implement recursive dungeon exploration
        if depth > max_depth:  # Stop recursion after max_depth levels
            print("🛑 You've reached the end of the dungeon!")
            treasure = random.choice(["Bramble's Blade", "The Panacea", "Rosegold Bow", "Eye of the Void"])
            print(f"💰 You found a rare treasure: {treasure}!")
            self.inventory.add_item(treasure)
            return
            
        print(f"🕳️ Exploring Dungeon Level {depth}...")
        time.sleep(1)  # Add suspense
        
        event = random.choice(["enemy", "treasure", "passage", "trap"])
        
        if event == "enemy":
            enemy_types = ["Dungeon Rat", "Skeleton Warrior", "Cave Troll", "Shadow Lurker"]
            enemy = random.choice(enemy_types)
            print(f"⚔️ A {enemy} appears!")
            
            # STUDENT TASK: Implement dungeon combat
            if self.inventory.stack:  # Can be commented out for student implementation
                print("You fight the enemy...")  # Can be commented out for student implementation
                time.sleep(1)  # Can be commented out for student implementation
                used_item = self.inventory.use_item()  # Can be commented out for student implementation
                print(f"🔥 You defeated the {enemy} using {used_item}!")  # Can be commented out for student implementation
                
                # Chance to find a passage after defeating an enemy
                if random.random() < 0.4:  # Can be commented out for student implementation
                    print("🔽 Behind the defeated enemy, you find a passage leading deeper...")  # Can be commented out for student implementation
                    self.explore_dungeon(depth + 1, max_depth)  # Can be commented out for student implementation
            else:  # Can be commented out for student implementation
                damage = random.randint(15, 30)  # Can be commented out for student implementation
                self.health = max(0, self.health - damage)  # Can be commented out for student implementation
                print(f"💀 You have no weapons! You took {damage} damage!")  # Can be commented out for student implementation
                
                if self.health <= 0:  # Can be commented out for student implementation
                    print("☠️ You have been defeated! Escaping the dungeon...")  # Can be commented out for student implementation
                    self.health = self.max_health // 2  # Return with half health  # Can be commented out for student implementation
                    self.location = "Village"  # Can be commented out for student implementation
                    return  # Can be commented out for student implementation
                else:  # Can be commented out for student implementation
                    print(f"You barely escape with {self.health} health remaining.")  # Can be commented out for student implementation
                    return  # Can be commented out for student implementation
                
        elif event == "treasure":
            common_items = ["Copper Coin", "Silver Coin", "Gold Coin", "Platinum Coin"]
            natural_items = ["Small Citrine Gem", "Small Ruby Gem", "Small Amber Gem"]
            uncommon_items = ["Small Money Bag", "Medium Money Bag", "Large Money Bag"]
            unusual_items = ["Small Gold Nugget", "Small Silver Nugget", "Rosegold Coin"]
            semirare_items = ["Small Stack of Copper Coins", "Small Stack of Silver Coins"]
            rare_items = ["Small Stack of Gold Coins", "Small Stack of Platinum Coins"]
            very_rare_items = ["Medium Citrine Gem", "Medium Ruby Gem", "Medium Amber Gem"]
            epic_items = ["Copper Goblet", "Silver Goblet", "Gold Goblet", "Crystal Goblet"]
            supreme_items = ["White Gold Coin", "Pale Gold Coin", "Small Stack of Rosegold Coins"]
            legendary_items = ["BRAMBLE TOKEN", "Copper Ingot", "Silver Ingot", "Gold Ingot"]
            mythical_items = ["Platinum Ingot", "Rosegold Ingot", "Sterling Silver Coin"]
            item = random.choice(common_items)
            print(f"💰 You found a {item}!")
            self.inventory.add_item(item)
            
            # STUDENT TASK: Implement chance to find a passage after finding treasure
            if random.random() < 0.6:  # Can be commented out for student implementation
                print("🔽 Behind the treasure chest, you notice a passage leading deeper...")  # Can be commented out for student implementation
                self.explore_dungeon(depth + 1, max_depth)  # Can be commented out for student implementation
            
        elif event == "trap":
            print("⚠️ You triggered a trap!")
            # STUDENT TASK: Implement trap mechanics
            damage = random.randint(5, 15)  # Can be commented out for student implementation
            self.health = max(0, self.health - damage)  # Can be commented out for student implementation
            print(f"💥 You took {damage} damage from the trap!")  # Can be commented out for student implementation
            
            if self.health <= 0:  # Can be commented out for student implementation
                print("☠️ You have been defeated by the trap! Escaping the dungeon...")  # Can be commented out for student implementation
                self.health = self.max_health // 2  # Return with half health  # Can be commented out for student implementation
                self.location = "Village"  # Can be commented out for student implementation
                return  # Can be commented out for student implementation
            
            # Chance to find a passage after surviving a trap
            if random.random() < 0.3:  # Can be commented out for student implementation
                print("🔽 After avoiding the worst of the trap, you notice a passage leading deeper...")  # Can be commented out for student implementation
                self.explore_dungeon(depth + 1, max_depth)  # Can be commented out for student implementation
            
        else:  # passage
            print("🔽 You find a passage leading deeper into the dungeon...")
            # STUDENT TASK: Implement recursive call to explore deeper
            self.explore_dungeon(depth + 1, max_depth)  # Can be commented out for student implementation

    def explore(self):
        places = ["Dark Forest", "Abandoned Ruins", "Mysterious Cave", "Merchant's Bazaar", "Ancient Dungeon Entrance"]
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
                    print("☠️ You have been defeated! Returning to Calico Village to recover...")
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
        print("🎮 Welcome to Bramblewood Park!")
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
                self.track_enemy()
            elif choice == "7":
                self.crack_magic_lock()
            elif choice == "8":
                print("👋 Thanks for playing! Goodbye.")
                self.running = False
            else:
                print("❌ Invalid choice! Try again.")

# ------------------ START THE GAME ------------------
if __name__ == "__main__":
    game = AdventureGame()
    game.start_game()
