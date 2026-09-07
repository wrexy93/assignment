import tkinter as tk
from tkinter import ttk


class LanguageExplorerApp(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Western Australian Country and Language Explorer")
		self.geometry("900x600")
		self.configure(bg="#f7f3eb")

		style = ttk.Style(self)
		style.configure("TNotebook", background="#f7f3eb", borderwidth=0)
		style.configure("TNotebook.Tab", padding=(22, 10), font=("Arial", 11))
		style.configure("Content.TFrame", background="#f7f3eb")

		header = tk.Frame(self, bg="#173f35", height=115)
		header.pack(fill="x")
		header.pack_propagate(False)
		tk.Label(
			header,
			text="Western Australian Country and Language Explorer",
			bg="#173f35",
			fg="white",
			font=("Arial", 24, "bold"),
		).pack(expand=True)

		self.tabs = ttk.Notebook(self)
		self.tabs.pack(fill="both", expand=True, padx=35, pady=(20, 30))

		self.home = ttk.Frame(self.tabs, style="Content.TFrame", padding=45)
		self.explore = ttk.Frame(self.tabs, style="Content.TFrame", padding=45)
		self.statistics = ttk.Frame(self.tabs, style="Content.TFrame", padding=45)
		self.quiz = ttk.Frame(self.tabs, style="Content.TFrame", padding=45)

		self.tabs.add(self.home, text="Home")
		self.tabs.add(self.explore, text="Explore")
		self.tabs.add(self.statistics, text="Statistics")
		self.tabs.add(self.quiz, text="Quiz")

		self._build_home()
		self._placeholder(self.explore, "Explore Languages")
		self._placeholder(self.statistics, "Language Statistics")
		self._placeholder(self.quiz, "Take Quiz")

	def _build_home(self):
		tk.Label(
			self.home,
			text="Discover Country and Language",
			bg="#f7f3eb",
			fg="#173f35",
			font=("Arial", 25, "bold"),
		).pack(pady=(40, 18))
		tk.Label(
			self.home,
			text="Explore publicly available information about Aboriginal languages\nand their relationship with Country in Western Australia.",
			bg="#f7f3eb",
			fg="#3e4b46",
			font=("Arial", 14),
			justify="center",
		).pack(pady=(0, 35))

		actions = tk.Frame(self.home, bg="#f7f3eb")
		actions.pack()
		self._button(actions, "Explore Languages", lambda: self.tabs.select(self.explore)).pack(side="left", padx=10)
		self._button(actions, "Take Quiz", lambda: self.tabs.select(self.quiz), secondary=True).pack(side="left", padx=10)

	def _button(self, parent, text, command, secondary=False):
		return tk.Button(
			parent,
			text=text,
			command=command,
			bg="#d27d4c" if not secondary else "#e4c48a",
			fg="white" if not secondary else "#173f35",
			activebackground="#b9653a",
			relief="flat",
			cursor="hand2",
			font=("Arial", 12, "bold"),
			padx=24,
			pady=12,
		)

	@staticmethod
	def _placeholder(frame, heading):
		tk.Label(frame, text=heading, bg="#f7f3eb", fg="#173f35", font=("Arial", 22, "bold")).pack(pady=80)


if __name__ == "__main__":
	LanguageExplorerApp().mainloop()
