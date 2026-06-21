from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingridients(ingridients: str):
    allowed = dark_spell_allowed_ingredients()
    splited1 = ingridients.split(", ")
    unpolished = splited1 + ingridients.split(" ")
    seen = []
    for s in unpolished:
        if s.lower() in allowed and s.lower() not in seen:
            seen.append(s.lower())
    status = "VALID" if seen else "INVALID"
    return ingridients + " - " + status