from .light_validator import validate_ingridients


def light_spell_allowed_ingredients():
    return ("earth", "air", "fire", "water")


def light_spell_record(spell_name: str, ingredients: str):
    result = validate_ingridients(ingredients)
    print(f"Spell recorded: {spell_name} ({result})")