from client.gui.log_view import LogView
from client.gui.seat_view import SeatView
import tkinter as tk


class RightSideView:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.seat_view = SeatView(self.master)
        self.log_view = LogView(self.master)
        self.frame.pack(side=tk.RIGHT)

    def get_seat_view(self):
        return self.seat_view

    def get_log_view(self):
        return self.log_view
