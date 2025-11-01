# Lex & Misi's Clickable Piano 🎹
# Fun piano for kids — upgraded!

import tkinter as tk
import winsound  # Windows-only sound support

root = tk.Tk()
root.title("🎶 Lex & Misi's Piano 🎶")
root.geometry("750x400")
root.configure(bg="lightblue")

# Frequencies (Hz) for piano notes
notes = {
    "C": 261,
    "C#": 277,
    "D": 293,
    "D#": 311,
    "E": 329,
    "F": 349,
    "F#": 370,
    "G": 392,
    "G#": 415,
    "A": 440,
    "A#": 466,
    "B": 493
}

# Keyboard mapping (qwerty)
key_bindings = {
    'a': 'C',
    'w': 'C#',
    's': 'D',
    'e': 'D#',
    'd': 'E',
    'f': 'F',
    't': 'F#',
    'g': 'G',
    'y': 'G#',
    'h': 'A',
    'u': 'A#',
    'j': 'B'
}

active_keys = {}  # Store button references for visual feedback

# Play note sound and flash the button
def play_note(note):
    if note in notes:
        winsound.Beep(notes[note], 300)
        btn = active_keys.get(note)
        if btn:
            original_color = btn.cget("bg")
            btn.config(bg="white")
            root.after(150, lambda: btn.config(bg=original_color))

# Draw white key
def make_white_key(note, x):
    btn = tk.Button(root, text=note, font=("Arial", 18, "bold"),
                    bg="white", fg="black", width=4, height=10,
                    command=lambda: play_note(note))
    btn.place(x=x, y=100)
    active_keys[note] = btn

# Draw black key
def make_black_key(note, x):
    btn = tk.Button(root, text=note, font=("Arial", 14, "bold"),
                    bg="black", fg="white", width=2, height=5,
                    command=lambda: play_note(note))
    btn.place(x=x, y=100)
    active_keys[note] = btn

# White keys (natural notes)
white_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
x_pos = 50
white_key_positions = {}  # Store X for black keys
for note in white_notes:
    make_white_key(note, x_pos)
    white_key_positions[note] = x_pos
    x_pos += 70

# Black keys (sharps) — positioned between white keys
black_keys = {
    'C#': ('C', 'D'),
    'D#': ('D', 'E'),
    'F#': ('F', 'G'),
    'G#': ('G', 'A'),
    'A#': ('A', 'B')
}
for sharp, (left, right) in black_keys.items():
    if left in white_key_positions and right in white_key_positions:
        lx = white_key_positions[left]
        rx = white_key_positions[right]
        x = (lx + rx) // 2 + 15
        make_black_key(sharp, x)

# Label
label = tk.Label(root, text="🎹 Click or Press Keys (A-W-S-E-D-F-T-G-Y-H-U-J)",
                 font=("Comic Sans MS", 16, "bold"), bg="lightblue", fg="darkblue")
label.pack(pady=20)

# Keyboard event handler
def key_press(event):
    key = event.char.lower()
    if key in key_bindings:
        note = key_bindings[key]
        play_note(note)

root.bind("<Key>", key_press)

# Start app
root.mainloop()