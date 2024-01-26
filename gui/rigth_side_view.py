from gui.log_view import LogView
from gui.seat_view import SeatView
import tkinter as tk


class RightSideView:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.seat_view = SeatView(self.master)
        self.log_view = LogView(self.master)
        self.frame.pack(side=tk.RIGHT)