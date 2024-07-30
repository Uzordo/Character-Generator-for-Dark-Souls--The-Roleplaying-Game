import os
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
                        os.system("cls")
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
        text: list[str] = []
                
        strength: str = "Strength: " + str(stats_gen.StatsGenerator.generate_ability())
        text.append(strength)
        dexterity: str = "Dexterity: " + str(stats_gen.StatsGenerator.generate_ability())
        text.append(dexterity)
        constitution: str = "Constitution: " + str(stats_gen.StatsGenerator.generate_ability())
        text.append(constitution)
        intelligence: str =  "Intelligence :" + str(stats_gen.StatsGenerator.generate_ability())
        text.append(intelligence)
        wisdom: str = "Wisdom: " + str(stats_gen.StatsGenerator.generate_ability())
        text.append(wisdom)
        charisma: str = "Charisma: " + str(stats_gen.StatsGenerator.generate_ability())
        text.append(charisma)
        base_position_text: str = "Base Position: " + str(TerminalMenu.handle_base_position())
        text.append(base_position_text)
        temporary_position_text: str = "Temporary Position: " + str(TerminalMenu.handle_temporary_position())
        text.append(temporary_position_text)
        backstory: str = "Backstory: " + stats_gen.StatsGenerator.generate_backstory()
        text.append(backstory)
        memory: str = "Memory: " + stats_gen.StatsGenerator.generate_memories()
        text.append(memory)
        drive: str = "Drive: " + stats_gen.StatsGenerator.generate_drives()       
        text.append(drive)
        
        return text

    def generate_file(char: list[str]):
        with open("OUTPUT.txt", "w") as f:
            for text in char:
                f.write(text + "\n")