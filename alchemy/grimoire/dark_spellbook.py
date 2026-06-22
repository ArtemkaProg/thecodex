from .dark_validator import validate_ingridients


def dark_spell_allowed_ingredients() -> tuple[str, ...]:
    return ("bats", "frogs", "arsenic", "eyeball")


def dark_spell_record(spell_name: str, ingredients: str) -> None:
    result = validate_ingridients(ingredients)
    print(f"Spell recorded: {spell_name} ({result})")
