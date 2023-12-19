import sqlite3 as sq
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from Stock_class import Stock_management, Print_stock

class WMS:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Wine Management System")

        self.icon_title = PhotoImage(file = "assets/icon_title.png")
        title = Label(self.root, text = "Wine Management System", image = self.icon_title, compound = LEFT, font = ("times new roman", 40, "bold"), bg = "#ba5390", fg = "white", anchor = "w", padx = 20).place(x = 0, y = 0, relwidth = 1, height = 70 )

        self.menu_logo = Image.open("assets/inventory_management.png")
        self.menu_logo = self.menu_logo.resize((200, 200))
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        left_menu = Frame(self.root, bd = 2, relief = FLAT, bg = "white")
        left_menu.place(x = 0, y = 102, width = 200, height = 565)

        lbl_menu_logo = Label(left_menu, image = self.menu_logo)
        lbl_menu_logo.pack(side = TOP, fill = X)

        lbl_menu = Label(left_menu, text = "Menu", font = ("times new roman", 20), bg = "#d9c5f2").pack(side = TOP, fill = X)
        button_stock = Button(left_menu, text = "Afficher le Stock", command = self.print_stock, font = ("times new roman", 20, "bold"), bg = "white", bd = 3)
        button_stock.pack(side = TOP, fill = X)
        button_manage_stock = Button(left_menu, text = "Gérer le Stock", command = self.stock_management, font = ("times new roman", 20, "bold"), bg = "white", bd = 3)
        button_manage_stock.pack(side = TOP, fill = X)

        self.lbl_tot_bottle = Label(self.root, text = "Nombre total de bouteilles :\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#9fec7d")
        self.lbl_tot_bottle.place(x = 250, y = 100, height = 150, width = 300)

        self.lbl_tot_wine_bottle = Label(self.root, text = "Nombre total de \nbouteilles de Vin :\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#9fec7d")
        self.lbl_tot_wine_bottle.place(x = 600, y = 100, height = 150, width = 300)

        self.lbl_tot_champ_bottle = Label(self.root, text = "Nombre total de \nbouteilles de Champagne :\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#9fec7d")
        self.lbl_tot_champ_bottle.place(x = 950, y = 100, height = 150, width = 300)

        self.lbl_tot_red_wine = Label(self.root, text = "Nombre de bouteille de \nvin rouge:\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#79c6ff")
        self.lbl_tot_red_wine.place(x = 250, y = 300, height = 150, width = 300)

        self.lbl_tot_white_wine = Label(self.root, text = "Nombre de bouteille de \nvin blanc:\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#79c6ff")
        self.lbl_tot_white_wine.place(x = 600, y = 300, height = 150, width = 300)

        self.lbl_tot_rose_wine = Label(self.root, text = "Nombre de bouteille de \nvin rosé:\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#79c6ff")
        self.lbl_tot_rose_wine.place(x = 950, y = 300, height = 150, width = 300)

        self.lbl_tot_white_white = Label(self.root, text = "Nombre de bouteille de \nChampagne blanc de blanc\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#ffdd73")
        self.lbl_tot_white_white.place(x = 250, y = 500, height = 150, width = 300)

        self.lbl_tot_brut_champ = Label(self.root, text = "Nombre de bouteille de \nChampagne brut\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#ffdd73")
        self.lbl_tot_brut_champ.place(x = 600, y = 500, height = 150, width = 300)

        self.lbl_tot_sec_champ = Label(self.root, text = "Nombre de bouteille de \nChampagne sec/demi-sec\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#ffdd73")
        self.lbl_tot_sec_champ.place(x = 950, y = 500, height = 150, width = 300)

        self.update_content()

    def stock_management(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Stock_management(self.new_window)

    def print_stock(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Print_stock(self.new_window)

    def update_content(self):
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from stock")
            tot_bottle = cur.fetchall()
            self.lbl_tot_bottle.config(text = f"Nombre total de bouteilles :\n{str(len(tot_bottle))}")

            cur.execute("select * from stock where type LIKE '%Vin%'")
            tot_wine_bottle = cur.fetchall()
            self.lbl_tot_wine_bottle.config(text = f"Nombre total de \nbouteilles de Vin :\n{str(len(tot_wine_bottle))}")

            cur.execute("select * from stock where type LIKE '%Champagne%'")
            tot_champ_bottle = cur.fetchall()
            self.lbl_tot_champ_bottle.config(text = f"Nombre total de \nbouteilles de Champagne :\n{str(len(tot_champ_bottle))}")

            cur.execute("select * from stock where color LIKE '%Rouge%'")
            tot_red_wine = cur.fetchall()
            self.lbl_tot_red_wine.config(text = f"Nombre de bouteille de \nvin rouge:\n{str(len(tot_red_wine))}")

            cur.execute("select * from stock where color LIKE '%Blanc%'")
            tot_white_wine = cur.fetchall()
            self.lbl_tot_white_wine.config(text = f"Nombre de bouteille de \nvin blanc:\n{str(len(tot_white_wine))}")

            cur.execute("select * from stock where color LIKE '%Rosé%'")
            tot_rose_wine = cur.fetchall()
            self.lbl_tot_rose_wine.config(text = f"Nombre de bouteille de \nvin rosé:\n{str(len(tot_rose_wine))}")

            cur.execute("select * from stock where type LIKE '%Blanc de blanc%'")
            tot_white_white = cur.fetchall()
            self.lbl_tot_white_white.config(text = f"Nombre de bouteille de \nChampagne blanc de blanc\n{str(len(tot_white_white))}")

            cur.execute("select * from stock where type LIKE '%Brute%'")
            tot_brut = cur.fetchall()
            self.lbl_tot_brut_champ.config(text = f"Nombre de bouteille de \nChampagne brut\n{str(len(tot_brut))}")

            cur.execute("select * from stock where type LIKE '%Sec%'")
            tot_sec = cur.fetchall()
            self.lbl_tot_sec_champ.config(text = f"Nombre de bouteille de \nChampagne sec/demi-sec\n{str(len(tot_sec))}")
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()

if __name__ == "__main__":
    root = Tk()
    obj = WMS(root)
    root.mainloop()
