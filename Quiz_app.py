import tkinter as tk
from tkinter import messagebox

# ── Question Bank ────────────────────────────────────────────────
QUIZ_BANK = {
    "HTML": [
        {"question": "What does HTML stand for?",
         "options": [
             "Hyper Text Markup Language",
             "Home Tool Markup Language",
             "Hyperlinks and Text Markup Language",
             "High‑level Text Manipulation Language"],
         "answer": "Hyper Text Markup Language"},
        {"question": "<img> is:",
         "options": ["Empty element", "Block element", "Semantic element", "Inline‑block element"],
         "answer": "Empty element"},
        {"question": "Which tag defines a hyperlink?",
         "options": ["<link>", "<a>", "<href>", "<url>"],
         "answer": "<a>"},
        {"question": "Which HTML element is used to define important text?",
         "options": ["<important>", "<strong>", "<b>", "<bold>"],
         "answer": "<strong>"},
    ],
    "CSS": [
        {"question": "Which property controls text size?",
         "options": ["font-style", "text-size", "font-size", "type-size"],
         "answer": "font-size"},
        {"question": "Flexbox axis that runs vertically by default is called:",
         "options": ["Main axis", "Cross axis", "Inline axis", "Column axis"],
         "answer": "Cross axis"},
        {"question": "Which CSS property sets the background color?",
         "options": ["background-image", "bgcolor", "color", "background-color"],
         "answer": "background-color"},
        {"question": "Which keyword is used for media queries?",
         "options": ["responsive", "media", "@media", "@responsive"],
         "answer": "@media"},
    ],
    "JavaScript": [
        {"question": "Which keyword creates a constant?",
         "options": ["let", "const", "var", "static"],
         "answer": "const"},
        {"question": "JSON.parse converts JSON text into:",
         "options": ["A string", "A JavaScript object", "An array buffer", "A DOM node"],
         "answer": "A JavaScript object"},
        {"question": "Which method is used to write to the console?",
         "options": ["log()", "print()", "console.log()", "document.log()"],
         "answer": "console.log()"},
        {"question": "Which symbol is used for comments in JavaScript?",
         "options": ["//", "#", "<!--", "**"],
         "answer": "//"},
    ],
    "Accessibility": [
        {"question": "The attribute to describe images for screen readers is:",
         "options": ["title", "aria-label", "alt", "longdesc"],
         "answer": "alt"},
        {"question": "WCAG stands for:",
         "options": [
             "Web Content Accessibility Guidelines",
             "World Consortium for Accessible Graphics",
             "Wide Community Access Group",
             "Website Compliance Audit Guide"],
         "answer": "Web Content Accessibility Guidelines"},
        {"question": "Which HTML tag improves accessibility for navigation?",
         "options": ["<menu>", "<nav>", "<header>", "<aside>"],
         "answer": "<nav>"},
        {"question": "Screen readers primarily use what to interpret content?",
         "options": ["CSS styles", "Keyboard events", "Semantic HTML", "JavaScript"],
         "answer": "Semantic HTML"},
    ],
}

# ── Theme ──────────────────────────────────────────────────────
THEME = {
    "bg": "#d7e0ee",
    "card": "#2e3f6d",
    "title": "#ffffff",
    "subtitle": "#9ca6c4",
    "btn_bg": "#273469",
    "btn_fg": "#ffffff"
}

# ── Application ────────────────────────────────────────────────
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Frontend Quiz App")
        self.root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        self.root.configure(bg=THEME["bg"])

        self.subject = None
        self.q_idx = 0
        self.score = 0
        self.choice = tk.StringVar()

        self.card = tk.Frame(root, bg=THEME["card"], padx=40, pady=40)
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        self._show_welcome()

    def _show_welcome(self):
        self._clear_card()

        left = tk.Frame(self.card, bg=THEME["card"])
        left.grid(row=0, column=0, sticky="nw", padx=(0, 60))

        tk.Label(left, text="Welcome to the\nFrontend Quiz!", font=("Segoe UI", 36, "bold"),
                 bg=THEME["card"], fg=THEME["title"], justify="left").pack(anchor="w")
        tk.Label(left, text="Pick a subject to get started.", font=("Segoe UI", 16),
                 bg=THEME["card"], fg=THEME["subtitle"]).pack(anchor="w", pady=(20, 0))

        right = tk.Frame(self.card, bg=THEME["card"])
        right.grid(row=0, column=1, sticky="ne")

        for subj in QUIZ_BANK:
            tk.Button(right, text=subj, width=20, height=2, font=("Segoe UI", 16), bd=0,
                      bg=THEME["btn_bg"], fg=THEME["btn_fg"], activebackground="#3e4c77",
                      command=lambda s=subj: self._start_quiz(s)).pack(pady=8, anchor="e")

    def _start_quiz(self, subj):
        self.subject = subj
        self.q_idx = 0
        self.score = 0
        self.choice.set("")
        self._clear_card()
        self._load_question()

    def _load_question(self):
        q = QUIZ_BANK[self.subject][self.q_idx]

        tk.Label(self.card, text=q["question"], font=("Segoe UI", 26, "bold"),
                 wraplength=900, justify="left", bg=THEME["card"], fg=THEME["title"]).pack(anchor="w", pady=(0, 30))

        for opt in q["options"]:
            tk.Radiobutton(self.card, text=opt, value=opt, variable=self.choice,
                           indicatoron=False, width=60, pady=12,
                           font=("Segoe UI", 16), bg=THEME["btn_bg"], fg=THEME["btn_fg"],
                           selectcolor="#505d83").pack(anchor="w", pady=6)

        tk.Button(self.card, text="Next", width=20, 
                  font=("Segoe UI", 16), bg="#4caf50", fg="white",
                  command=self._next).pack(pady=30)

    def _next(self):
        if self.choice.get() == "":
            return messagebox.showwarning("Hold on!", "Please select an option.")

        if self.choice.get() == QUIZ_BANK[self.subject][self.q_idx]["answer"]:
            self.score += 1

        self.q_idx += 1
        if self.q_idx < len(QUIZ_BANK[self.subject]):
            self._clear_card()
            self._load_question()
        else:
            self._show_result()

    def _show_result(self):
        self._clear_card()
        score_text = f"You scored {self.score} / {len(QUIZ_BANK[self.subject])}\n\nSubject: {self.subject}"

        tk.Label(self.card, text=score_text, font=("Segoe UI", 32, "bold"),
                 bg=THEME["card"], fg=THEME["title"]).pack(pady=60)
        tk.Button(self.card, text="Play Again", width=20, height=2,
                  font=("Segoe UI", 16), bg=THEME["btn_bg"], fg=THEME["btn_fg"],
                  command=self._show_welcome).pack(pady=12)
        tk.Button(self.card, text="Exit", width=400, height=2,
                  font=("Segoe UI", 16), bg="#c62828", fg="white",
                  command=self.root.destroy).pack()

    def _clear_card(self):
        for widget in self.card.winfo_children():
            widget.destroy()

# ── Main ────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
