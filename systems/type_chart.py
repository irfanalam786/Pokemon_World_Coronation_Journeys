TYPE_CHART = {
    "Electric": {
        "Water": 2.0,
        "Electric": 0.5,
        "Grass": 0.5,
        "Ground": 0.0
    },
    "Fire": {
        "Grass": 2.0,
        "Water": 0.5,
        "Fire": 0.5,
        "Rock": 0.5
    },
    "Water": {
        "Fire": 2.0,
        "Water": 0.5,
        "Grass": 0.5,
        "Rock": 2.0
    },
    "Grass": {
        "Water": 2.0,
        "Fire": 0.5,
        "Grass": 0.5,
        "Ground": 2.0,
        "Rock": 2.0
    },
    "Rock": {
        "Fire": 2.0,
        "Water": 0.5,
        "Grass": 0.5,
        "Rock": 0.5
    },
    "Psychic": {
        "Fighting": 2.0,
        "Poison": 2.0
    },
    "Normal": {},
    "Ground": {
        "Electric": 2.0,
        "Rock": 2.0,
        "Poison": 0.5
    }
}

def get_effectiveness(move_type, target_type):
    return TYPE_CHART.get(move_type, {}).get(target_type, 1.0)