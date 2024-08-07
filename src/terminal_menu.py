import os
import platform
import src.stats_gen as stats_gen

class TerminalMenu():
    def __init__():
        pass

    def main_menu() -> None:
        while True:  
                print("1. Generate a new character")
                print("2. Quit")  
                       
                key = input()
                
                match key:
                    case "1":
                        TerminalMenu.generate_file(TerminalMenu.generate_all_stats())
                        
                        if platform.system() == "Windows":
                            os.system("cls")
                        elif platform.system() == "Linux" or platform.system == "Darwin": # I think this will work on Linux and macOS
                            os.system("clear")
                        print("Character file created!!!!")
                    case "2":
                        break  
      
    def handle_base_position() -> int:
        base_positon: int = 0
        
        player_level: int = 0
        
        constitution_modifier: int = 0
        maximum_value_origin_position_dice: int = 0
        
        print("CALCULATING BASE POSITION")
        constitution_modifier = int(input("Give the constitution modifier: "))
        maximum_value_origin_position_dice = int(input("Give the maximum value origin position dice: "))
        player_level = int(input("Give the current player level: "))
        return stats_gen.StatsGenerator.generate_base_positon(constitution_modifier, maximum_value_origin_position_dice, player_level)
    

    def handle_temporary_position() -> int:
        
        origin_position_dice: int = 0
        player_level: int = 0
        
        print("CALCULATING THE TEMPORARY POSITION")
        origin_position_dice = int(input("Give the origin position dice: "))
        player_level = int(input("Give the current player level: "))
        return stats_gen.StatsGenerator.generate_temporary_position(origin_position_dice, player_level)
        
                        
    def generate_all_stats() -> list[str]:
        text: list[str] = [
            "Strength: " + str(stats_gen.StatsGenerator.generate_ability()),
            "Dexterity: " + str(stats_gen.StatsGenerator.generate_ability()),
            "Constitution: " + str(stats_gen.StatsGenerator.generate_ability()),
            "Intelligence :" + str(stats_gen.StatsGenerator.generate_ability()),
            "Wisdom: " + str(stats_gen.StatsGenerator.generate_ability()),
            "Charisma: " + str(stats_gen.StatsGenerator.generate_ability()),
            "Base Position: " + str(TerminalMenu.handle_base_position()),
            "Temporary Position: " + str(TerminalMenu.handle_temporary_position()),
            "Backstory: " + stats_gen.StatsGenerator.generate_backstory(),
            "Memory: " + stats_gen.StatsGenerator.generate_memories(),
            "Drive: " + stats_gen.StatsGenerator.generate_drives()
        ]

        return text

    def generate_file(char: list[str]):
        with open("OUTPUT.txt", "w") as f:
            for text in char:
                f.write(text + "\n")