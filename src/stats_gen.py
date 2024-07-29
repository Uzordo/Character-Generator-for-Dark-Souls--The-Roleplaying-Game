import random

class StatsGenerator():
    def __init__():
        pass
    
    def generate_ability() -> int:
        
        numbers: list = []
        min_numbers: int = 0
        min_index: int = 0
        number_sum: int = 0
        
        for i in range(4):
            numbers.append(random.randint(1, 6)) 
        
        min_number = min(numbers)
        min_index = numbers.index(min_number)
        numbers.pop(min_index)
        
        for i in range(len(numbers)):
            number_sum += numbers[i]
        
        return number_sum

    def generate_temporary_position(origin_position_dice: int, player_level: int) -> int:
        return origin_position_dice * player_level
    
    def generate_base_positon(constitution_modifier: int, maximum_value_origin_position_dice: int, current_level: int):
        return constitution_modifier + maximum_value_origin_position_dice + current_level

    def generate_backstory() -> str:
        
        random_backstory: int = 0
        
        with open("txt/backstories.txt") as f:
            content = f.readlines()
        
            random_backstory = random.randint(0, len(content)) 
        
        return content[random_backstory - 1]

    def generate_memories() -> str:
        
        random_memory: int = 0
        
        with open("txt/memories.txt") as f:
            content = f.readlines()
        
            random_memory = random.randint(0, len(content))
        
        return content[random_memory - 1]

    def generate_drives() -> str:
        
        random_drive: int = 0
        
        with open("txt/drives.txt") as f:
            content = f.readlines()
        
            random_drive = random.randint(0, len(content))
        
        return content[random_drive - 1]


StatsGenerator.generate_ability()