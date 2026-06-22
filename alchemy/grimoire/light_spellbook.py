from .light_validator import validate_ingridients


def light_spell_allowed_ingredients() -> tuple[str, ...]:
    return ("earth", "air", "fire", "water")


def light_spell_record(spell_name: str, ingredients: str) -> None:
    result = validate_ingridients(ingredients)
    print(f"Spell recorded: {spell_name} ({result})")
