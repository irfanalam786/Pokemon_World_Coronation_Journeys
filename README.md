# 🎮 Pokémon Masters Journey RPG (Phase 1)

## 📌 Project Overview

Pokémon Masters Journey RPG is a **Python-based turn-based RPG battle system** inspired by Pokémon mechanics.
Phase 1 focuses on building the **core backend systems**, including battle logic, AI, progression, and persistence.

---

## 🚀 Features Implemented (Phase 1)

### ⚔️ Battle System

* Turn-based combat engine
* Speed-based move order
* Type effectiveness (Fire, Water, Electric, Grass)
* Damage calculation system
* Critical hit system
* Status effects:

  * Burn
  * Poison
  * Paralysis

---

### 🧠 AI System

* Basic AI (move selection)
* Advanced AI:

  * Type advantage decisions
  * HP-based switching
* Smart AI (Day 23):

  * Damage prediction
  * Weighted decision system
  * Strategic switching

---

### 📈 Progression System

* EXP gain after battle
* Level-up system
* Evolution system (level-based)
* IV system (random stat variation)
* Balance system (damage + EXP scaling)

---

### 🏆 Competitive Systems

* Rank system (Normal → Master ready)
* Points system (+20 win / -10 loss)
* Leaderboard system (JSON-based)
* Stats tracking:

  * Wins / Losses
  * Total battles
  * Total damage

---

### 🎯 Achievement System

* First Win
* 5 Wins
* Damage Dealer
* Rank Up

---

### 💾 Save System

* Full state save:

  * Pokémon HP
  * Level & EXP
  * Status effects
  * Team data
* Load system (resume gameplay)

---

### 🛠️ Stability & Systems

* Safe exit system
* Error handling
* HP system fix (no negative HP)
* Team reset after battle

---

## 🗂️ Project Structure

```
pokemon/
│
├── core/
│   ├── game_manager.py
│   ├── save_manager.py
│   ├── difficulty_system.py
│
├── models/
│   ├── pokemon.py
│   ├── trainer.py
│
├── engine/
│   ├── battle_engine.py
│
├── ai_system/
│   ├── advanced_ai.py
│
├── progression/
│   ├── balance_system.py
│   ├── stats_system.py
│   ├── achievement_system.py
│
├── ranking/
│   ├── leaderboard_system.py
│
├── decision_system/
│   ├── player_choices.py
│
├── main.py
└── README.md
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧪 Testing (Phase 1)

The system supports:

* Full battle simulation
* AI decision validation
* Save/Load testing
* Leaderboard updates

---

## 🎯 Learning Outcomes

This project demonstrates:

* Object-Oriented Programming (OOP)
* System design & modular architecture
* AI decision-making logic
* Game development fundamentals
* Data persistence using JSON

---

## 🔥 Project Level

✔ Intermediate → Advanced
✔ Above standard BCA projects
✔ Scalable for full game development

---

## 🚀 Next Phase

Phase 2 will introduce:

* Pygame UI
* Animations
* Interactive gameplay loop

---

## 👨‍💻 Author

Developed as part of a structured 112-day project plan.
