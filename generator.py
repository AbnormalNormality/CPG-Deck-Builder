from random import choices, randint

attributes = {
    "attack": {
        "weight": 1
    },

    "shield": {
        "weight": 1
    }
}


def generate_attribute(rarity=0):
    item_keys = list(attributes.keys())
    item_weights = [attributes[key]["weight"] for key in item_keys]

    selected_attribute = choices(item_keys, weights=item_weights, k=1)[0]

    power = max(1, 1 + rarity * randint(85, 115) // 100)

    return selected_attribute, power
