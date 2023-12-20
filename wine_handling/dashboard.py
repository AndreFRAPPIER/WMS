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

        self.lbl_tot_red_wine = Label(self.root, text = "Nombre de bouteille de \nBordeau:\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#79c6ff")
        self.lbl_tot_red_wine.place(x = 250, y = 300, height = 150, width = 300)

        self.lbl_tot_white_wine = Label(self.root, text = "Nombre de bouteille de \nBourgogne:\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#79c6ff")
        self.lbl_tot_white_wine.place(x = 600, y = 300, height = 150, width = 300)

        self.lbl_tot_rose_wine = Label(self.root, text = "Nombre de bouteille de \nl'Alsace:\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#79c6ff")
        self.lbl_tot_rose_wine.place(x = 950, y = 300, height = 150, width = 300)

        self.lbl_tot_white_white = Label(self.root, text = "Nombre de bouteille du \nLanguedoc\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#ffdd73")
        self.lbl_tot_white_white.place(x = 250, y = 500, height = 150, width = 300)

        self.lbl_tot_brut_champ = Label(self.root, text = "Nombre de bouteille de la\nVallée du Rhone\n0", font = ("times new roman", 20), bd = 5, relief = FLAT, bg = "#ffdd73")
        self.lbl_tot_brut_champ.place(x = 600, y = 500, height = 150, width = 300)

        self.update_content()

    def stock_management(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Stock_management(self.new_window)

    def print_stock(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = Print_stock(self.new_window)

    def update_content(self):
        #print("ok")
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            cur.execute("select quantity from stock")
            temp = cur.fetchall()
            qty = 0
            for i in range (len(temp)):
                qty = qty + int(temp[i][0])
            self.lbl_tot_bottle.config(text = f"Nombre total de bouteilles :\n{str(qty)}")

            cur.execute("select quantity from stock where type LIKE '%Vin%'")
            temp = cur.fetchall()
            tot_wine = 0
            for i in range (len(temp)):
                tot_wine = tot_wine + int(temp[i][0])
            self.lbl_tot_wine_bottle.config(text = f"Nombre total de \nbouteilles de Vin :\n{str(tot_wine)}")

            cur.execute("select quantity from stock where type LIKE '%Champagne%'")
            temp = cur.fetchall()
            tot_champ = 0
            for i in range (len(temp)):
                tot_champ = tot_champ + int(temp[i][0])
            self.lbl_tot_champ_bottle.config(text = f"Nombre total de \nbouteilles de Champagne :\n{str(tot_champ)}")

            cur.execute("select quantity from stock where appelation LIKE '%Bordeau%'")
            temp = cur.fetchall()
            tot_bord = 0
            for i in range (len(temp)):
                tot_bord = tot_bord + int(temp[i][0])
            self.lbl_tot_red_wine.config(text = f"Nombre de bouteille de \nBordeau:\n{str(tot_bord)}")

            cur.execute("select quantity from stock where appelation LIKE '%Bourgogne%'")
            temp = cur.fetchall()
            tot_bourg = 0
            for i in range (len(temp)):
                tot_bourg = tot_bourg + int(temp[i][0])
            self.lbl_tot_white_wine.config(text = f"Nombre de bouteille de \nBourgogne:\n{str(tot_bourg)}")

            cur.execute("select quantity from stock where appelation LIKE '%Alsace%'")
            temp = cur.fetchall()
            tot_als = 0
            for i in range (len(temp)):
                tot_als = tot_als + int(temp[i][0])
            self.lbl_tot_rose_wine.config(text = f"Nombre de bouteille de \nl'Alsace:\n{str(tot_als)}")

            cur.execute("select quantity from stock where appelation LIKE '%Languedoc%'")
            temp = cur.fetchall()
            tot_lang = 0
            for i in range (len(temp)):
                tot_lang = tot_lang + int(temp[i][0])
            self.lbl_tot_white_white.config(text = f"Nombre de bouteille du \nLanguedoc\n{str(tot_lang)}")

            cur.execute("select quantity from stock where appelation LIKE '%Rhone%'")
            temp = cur.fetchall()
            tot_rhone = 0
            for i in range (len(temp)):
                tot_rhone = tot_rhone + int(temp[i][0])
            self.lbl_tot_brut_champ.config(text = f"Nombre de bouteille de la\nVallée du Rhone\n{str(tot_rhone)}")

        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")

if __name__ == "__main__":
    root = Tk()
    obj = WMS(root)
    root.mainloop()
