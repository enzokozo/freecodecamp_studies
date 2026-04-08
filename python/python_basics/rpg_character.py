def create_character(name, strength, intelligence, charisma):
    """
    This function creates a new RPG character with the specified attributes.
    """

    # Name validation
    if not isinstance(name, str):
        return 'The character name should be a string' 
    
    if not name:
        return 'The character should have a name'
    
    if len(name) > 10:
        return 'The character name is too long'
    
    if ' ' in name:
        return 'The character name should not contain spaces'

    # Stats (grouped) validation
    stats = (strength, intelligence, charisma)

    if not all(isinstance(s, int) for s in stats):
        return 'All stats should be integers'
    
    if min(stats) < 1:
        return 'All stats should be no less than 1'

    if max(stats) > 4:
        return 'All stats should be no more than 4'

    if sum(stats) != 7:
        return 'The character should start with 7 points'
    
    # Defining chars for full and empty dots locally
    f = '●'
    e = '○'

    return (
        f'{name}\n'
        f'STR {f * strength}{e * (10 - strength)}\n'
        f'INT {f * intelligence}{e * (10 - intelligence)}\n'
        f'CHA {f * charisma}{e * (10 - charisma)}'
    )

print(create_character('Aragorn', 3, 2, 2))
