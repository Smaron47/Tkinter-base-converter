from tkinter import *

class NumberConverter:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("500x600")
        self.win.title("Universal Number System Converter")
        self.win.resizable(0, 0)

        Label(self.win, text="Universal Number Converter",
              font=("Arial", 22, "bold")).pack(pady=20)

        Label(self.win, text="Enter Value:",
              font=("Arial", 16, "bold")).pack()

        self.input_var = StringVar()
        Entry(self.win, textvar=self.input_var,
              font=("Arial", 16), width=20).pack(pady=10)

        Label(self.win, text="Select Input Base:",
              font=("Arial", 16, "bold")).pack(pady=10)

        btn_frame = Frame(self.win)
        btn_frame.pack()

        Button(btn_frame, text="Decimal",
               command=self.from_decimal,
               font=("Arial", 14), width=10).grid(row=0, column=0, padx=5, pady=5)

        Button(btn_frame, text="Binary",
               command=self.from_binary,
               font=("Arial", 14), width=10).grid(row=0, column=1, padx=5, pady=5)

        Button(btn_frame, text="Octal",
               command=self.from_octal,
               font=("Arial", 14), width=10).grid(row=1, column=0, padx=5, pady=5)

        Button(btn_frame, text="Hex",
               command=self.from_hex,
               font=("Arial", 14), width=10).grid(row=1, column=1, padx=5, pady=5)

        self.result_labels = []
        self.win.mainloop()

    # -------------------------- UI CLEANER ----------------------------
    def clear_results(self):
        for lbl in self.result_labels:
            lbl.destroy()
        self.result_labels = []

    # -------------------------- RESULT DISPLAY ------------------------
    def show_results(self, dec, binv, octv, hexv):
        self.clear_results()

        answers = [
            f"Decimal : {dec}",
            f"Binary  : {binv}",
            f"Octal   : {octv}",
            f"Hex     : {hexv}",
        ]

        y = 350
        for text in answers:
            lbl = Label(self.win, text=text,
                        font=("Arial", 18, "bold"))
            lbl.place(x=100, y=y)
            self.result_labels.append(lbl)
            y += 40

    # -------------------------- CONVERTERS ----------------------------
    def from_decimal(self):
        try:
            value = int(self.input_var.get())
            dec = value
            binv = bin(value)[2:]
            octv = oct(value)[2:]
            hexv = hex(value)[2:].upper()
            self.show_results(dec, binv, octv, hexv)
        except:
            self.error()

    def from_binary(self):
        try:
            value = self.input_var.get()
            dec = int(value, 2)
            binv = value
            octv = oct(dec)[2:]
            hexv = hex(dec)[2:].upper()
            self.show_results(dec, binv, octv, hexv)
        except:
            self.error()

    def from_octal(self):
        try:
            value = self.input_var.get()
            dec = int(value, 8)
            binv = bin(dec)[2:]
            octv = value
            hexv = hex(dec)[2:].upper()
            self.show_results(dec, binv, octv, hexv)
        except:
            self.error()

    def from_hex(self):
        try:
            value = self.input_var.get()
            dec = int(value, 16)
            binv = bin(dec)[2:]
            octv = oct(dec)[2:]
            hexv = value.upper()
            self.show_results(dec, binv, octv, hexv)
        except:
            self.error()

    # -------------------------- ERROR HANDLER -------------------------
    def error(self):
        self.clear_results()
        lbl = Label(self.win, text="Invalid Input!",
                    fg="red", font=("Arial", 20, "bold"))
        lbl.place(x=160, y=350)
        self.result_labels.append(lbl)


# ---------------- RUN PROGRAM ----------------
NumberConverter()
