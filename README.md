# 🐍 Terminal Pokémon RPG

A **terminal-based Pokémon RPG** written in **Python**, where players can explore the world, capture Pokémon, battle enemies, and save/load their progress.

This project was built as a learning exercise to practice **object-oriented programming (OOP)**, randomness, and file persistence.

---

## 🎮 Features

- Choose a **starter Pokémon** (Bulbasaur, Charmander, or Squirtle)
- Explore the world and encounter **wild Pokémon**
- Capture Pokémon with a chance-based system
- Battle enemies using turn-based combat
- Earn money by winning battles
- Inspect your Pokémon collection
- **Save and load** game progress
- Colorful terminal output for better UX

---

## 📁 Project Structure

```
Terminal-Pokemon-RPG/
│
├── main.py        # Game entry point, menus, save/load logic
├── person.py      # Player, Enemy, and battle logic
├── pokemon.py     # Pokémon classes, attacks, colors
└── save.db        # Generated save file (after saving the game)
```

---

## ▶️ How to Run

Make sure you have **Python 3.8+** installed.

```bash
python main.py
```

The game runs entirely in the terminal.

---

## 🧠 Gameplay Overview

1. Enter your player name  
2. Choose your starter Pokémon  
3. Navigate the main menu:
   - Explore the world
   - Fight enemies
   - Inspect your collection
   - Save / load your game  
4. Win battles to earn money and grow stronger

---

## 💾 Save System

The game uses Python’s built-in `pickle` module to serialize and deserialize the player object.

- Save file: `save.db`
- You can load your progress anytime from the menu

---

## 🧩 Concepts Used

- Object-Oriented Programming (Inheritance & Polymorphism)
- Randomized game events
- Turn-based battle system
- File persistence with `pickle`
- Terminal UI formatting (ANSI colors)

---

## 🚧 Known Limitations / Future Improvements

- No Pokémon type effectiveness
- HP is not restored after battles
- No leveling or experience system
- No inventory or healing items

These are good candidates for future updates.

---

## 📚 Disclaimer

This project is for **educational purposes only**.  
It is inspired by Pokémon but is **not affiliated** with Nintendo, Game Freak, or The Pokémon Company.

---

## 🧑‍💻 Author

**Arthur Hoffmann**
