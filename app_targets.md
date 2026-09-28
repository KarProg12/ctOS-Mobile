# ctOS Mobile

«A terminal-based mobile system inspired by the ctOS interface from "watch_dogs2".»

---

# 🎯 Goal

Create a terminal-based ctOS Mobile application that allows the user to monitor and interact with information about their phone and system through Termux.

---

# 🚧 V0.1 — First Version

# Features

- [ ] Startup screen
- [ ] Main menu
- [ ] System Info
- [ ] Battery
- [ ] Exit

---

# 🔄 Program Flow

START
  │
  ▼
Startup Screen
  │
  ▼
Main Menu
  │
  ▼
User Selection
  │
  ├── System Info ──► Display system information
  │                         │
  │                         ▼
  ├── Battery ─────► Display battery information
  │                         │
  │                         ▼
  └── Exit ─────────► Close program
                            │
                            ▼
                           END

After executing an action:
        │
        ▼
   Return to Menu

---

# 🧩 Components

## 1. Startup Screen

Responsible for:

- ctOS logo/name
- application version
- basic device information

## 2. Main Menu

Responsible for:

- displaying available options
- receiving the user's selection
- directing the program to the selected feature

## 3. System Info

Responsible for displaying:

- operating system information
- device information
- system information available through Termux

## 4. Battery

Responsible for displaying:

- battery level
- charging status

## 5. Exit

Terminates the application.

---

# 📁 Initial Project Structure

## At the beginning:

ctos/
└── main.py

There is no need to create multiple files until the project actually requires them.

Later, the structure can grow:

ctos/
│
├── main.py
│
├── ui/
│   ├── menu.py
│   └── screens.py
│
├── system/
│   ├── info.py
│   └── battery.py
│
└── network/
    └── scanner.py

---

# 🧠 Problem-Solving Approach

Do not start by asking:

«"What code should I write?"»

Start with:

What do I want to achieve?
          ↓
What does it depend on?
          ↓
How can I break the problem down?
          ↓
What is the first thing I don't know?
          ↓
Solve only that problem
          ↓
      Does it work?
       ↙       ↘
     YES       NO
      ↓         ↓
 Go back     Break the
  higher     problem down

---

# 📌 Current Next Step

Do not add new features yet.

First, design and implement the basic program structure:

START
  ↓
MENU
  ↓
USER SELECTION
  ↓
ACTION
  ↓
RETURN TO MENU
  ↓
...

Only after this basic structure works should real system information be added.
