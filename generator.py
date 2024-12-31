def generate_effect(guaranteed=None):
    effects = []

    e = wchoice((
        ('attack', 40),
        ('shield', 30),  # 70
        ('effect', 15),  # 85
        ('draw', 12),  # 97
        ('heal', 3),  # 100
    )) if guaranteed is None else guaranteed
    effects.append(e)

    if e == 'attack':
        effects.append(wchoice((
            (2, 35),
            (3, 25),  # 60
            (4, 20),  # 80
            (5, 15),  # 95
            (6, 5)    # 5
        )))

    elif e == 'shield':
        effects.append(wchoice((
            (4, 35),
            (5, 25),  # 60
            (6, 20),  # 80
            (7, 15),  # 95
            (8, 5)    # 5
        )))

    return effects


# noinspection SpellCheckingInspection
def wchoice(item_weights):
    from random import choices
    items, weights = zip(*item_weights)
    return choices(items, weights=weights)[0]


__all__ = ["generate_effect"]
