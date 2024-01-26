import math
import tkinter as tk
from PIL import ImageTk, Image


class SeatView():
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master, bg="white")
        self.seat = Image.open("img/seat.png")
        self.back_seat = Image.open("img/back_seat_2.png")

        self.canvas = tk.Canvas(self.frame, width=600, height=350, bg="white")
        self.canvas.pack()

        # create the image related to the back seat
        self.back_seat = self.back_seat.resize((600, 300))
        self.back_seat_tk = ImageTk.PhotoImage(self.back_seat)
        self.canvas_back_seat = self.canvas.create_image(15, 350, anchor=tk.SW, image=self.back_seat_tk)
        self.actual_degree = 0

        # create the image related to the seat
        self.seat = self.seat.resize((150, 60))
        self.seat_tk = ImageTk.PhotoImage(self.seat)
        self.canvas.create_image(270, 315, anchor=tk.SW, image=self.seat_tk)

        # create the oval, which represent the seat back
        # x1, y1 = 170, 130
        # x2, y2 = 220, 270
        # self.oval = self.canvas.create_oval(x1, y1, x2, y2, outline="black", stipple="gray12")

        self.left_arrow_image = Image.open("img/left_arrow.jpg")
        self.right_arrow_image = Image.open("img/right_arrow.jpg")
        self.left_arrow_photo = ImageTk.PhotoImage(self.left_arrow_image)
        self.right_arrow_photo = ImageTk.PhotoImage(self.right_arrow_image)

        self.left_arrow_label = tk.Label(self.frame, image=self.left_arrow_photo, cursor="hand2")
        self.left_arrow_label.pack(side=tk.LEFT)
        self.left_arrow_label.bind("<Button-1>", self.left_arrow_handler)

        self.right_arrow_label = tk.Label(self.frame, image=self.right_arrow_photo, cursor="hand2")
        self.right_arrow_label.pack(side=tk.RIGHT)
        self.right_arrow_label.bind("<Button-1>", self.right_arrow_handler)

        self.frame.pack(side=tk.TOP)

    def left_arrow_handler(self, event):
        # TODO logica della gestione della freccia sinistra
        self.rotate_back_seat(10)
        pass

    def right_arrow_handler(self, event):
        # TODO logica della gestione della freccia destra
        self.rotate_back_seat(-10)
        pass

    def rotate_back_seat(self, degrees):
        self.actual_degree += degrees
        rotated_image = self.back_seat.rotate(self.actual_degree, resample=Image.BICUBIC, center=((self.back_seat.width // 2) - 27, self.back_seat.height - 72))
        rotated_image_tk = ImageTk.PhotoImage(rotated_image)
        self.canvas.itemconfig(self.canvas_back_seat, image=rotated_image_tk)
        #self.back_seat = rotated_image
        self.back_seat_tk = rotated_image_tk