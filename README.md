# Pokémon Anime RPG (SSS Project)

## Overview

A turn-based Pokémon RPG featuring anime-style battles, character progression, and strategic combat. Built with a modular architecture for easy expansion.

## Features

### Core Systems
- **Turn-based Battle Engine**: Real-time combat with type advantages, critical hits, and special abilities
- **Pokemon Management**: 10+ Pokemon with evolution, leveling, and stat progression
- **Trainer System**: Multiple opponents with different personalities and strategies
- **Save/Load System**: Persistent game state with JSON storage
- **Difficulty Scaling**: Progressive challenge with adjustable multipliers

### Pokemon Features
- **Evolution System**: Automatic evolution at level thresholds
- **Bond Mechanics**: Friendship affects battle performance
- **Clutch Mode**: Special ability activation in critical situations
- **Type Effectiveness**: Full type chart with super-effective and resisted moves

### Battle Features
- **Move Selection**: Choose from multiple moves per Pokemon
- **Type Advantages**: Strategic combat with elemental strengths/weaknesses
- **Critical Hits**: Random chance for increased damage
- **Status Effects**: Burn, paralysis, and other battle conditions

## Project Structure

```
pokemon/
├── core/                 # Main game logic
│   └── game.py          # Game initialization and flow
├── models/              # Data models
│   ├── pokemon.py       # Pokemon class and mechanics
│   └── trainer.py       # Trainer class and team management
├── engine/              # Core systems
│   ├── battle_engine.py # Battle mechanics
│   └── json_loader.py   # Data loading utilities
├── systems/             # Supporting systems
│   ├── type_chart.py    # Type effectiveness system
│   ├── dialogue_manager.py # Text display system
│   ├── save_manager.py  # Save/load functionality
│   └── difficulty_manager.py # Difficulty scaling
├── data/                # Game data files
│   ├── pokemon.json     # Pokemon definitions
│   ├── trainers.json    # Trainer definitions
│   └── moves.json       # Move definitions
└── save/                # Save game files
    └── player_save.json # Player save data
```

## Installation & Running

### Requirements
- Python 3.7+
- No external dependencies (uses only standard library)

### Setup
```bash
# Clone or download the project
cd pokemon/

# Install requirements (if any)
pip install -r requirements.txt

# Run the game
python main.py
```

## Game Controls

- **Move Selection**: Enter the number of the move you want to use
- **Battle Flow**: Alternating turns between player and opponent
- **Save/Load**: Automatic save after each battle

## Data Files

### Pokemon (pokemon.json)
Contains 10 Pokemon with stats, moves, and evolution data:
- Pikachu, Charmander, Bulbasaur, Squirtle
- Onix, Geodude, Staryu, Starmie
- Vileplume, Tangela

### Moves (moves.json)
13 battle moves with power and type:
- Thunderbolt, Ember, Vine Whip, Water Gun
- Rock Throw, Psychic, Solar Beam, etc.

### Trainers (trainers.json)
5 trainers with different teams and personalities:
- Rival, Brock, Misty, Lt. Surge, Erika

## Development Status

### Completed ✅
- Core battle engine with type effectiveness
- Pokemon evolution and leveling system
- Trainer AI with personality-based behavior
- Save/load system with JSON persistence
- Modular architecture for easy expansion
- Type chart with full effectiveness calculations

### Known Issues
- Limited Pokemon variety (10 species)
- Basic AI (random move selection)
- No graphical interface (console-only)
- Limited move pool (13 moves)

## Future Plans

### Phase 2: Pygame UI
- Graphical battle interface
- Animated sprites and effects
- Menu system with mouse/keyboard controls
- Sound effects and music

### Phase 3: World Exploration
- Overworld map navigation
- NPC interactions
- Item collection and usage
- Story progression

### Phase 4: Advanced Features
- Multiplayer battles
- Custom Pokemon creation
- Advanced AI opponents
- Tournament mode

## Contributing

This is a student project for learning purposes. Feel free to fork and experiment!

## License

See LICENSE.txt for details.