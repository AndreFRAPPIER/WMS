import sqlite3 as sq
from tkinter import *
from tkinter import ttk, messagebox
from database_management import create_tab_alcool

class Alcool_management:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1350x700+220+130")
        self.root.title("Stock Management")
        self.root.config(bg = "#f0e9f7")
        self.root.focus_force()
        create_tab_alcool()

        #-----------------------------------------------------------------#

        self.search_by = StringVar()
        self.search_txt = StringVar()

        self.sort_by = StringVar()
        self.sort_by_ord = StringVar()

        self.var_bottle_name = StringVar()
        self.var_bottle_marque = StringVar()
        self.var_bottle_age = StringVar()
        self.var_bottle_quantity = StringVar()
        self.var_id_lot = StringVar()

        #-----------------------------------------------------------------#

        search_frame = LabelFrame(self.root, text = "Recherche", bg = "#f0e9f7")
        search_frame.place(x = 50, y = 20, width = 600, height = 70)

        sort_frame = LabelFrame(self.root, text = "Trier", bg = "#f0e9f7")
        sort_frame.place(x = 750, y = 20, width = 550, height = 70)

        cmb_search = ttk.Combobox(search_frame, textvariable = self.search_by, values = ("name", "marque", "age", "quantite"), state = "readonly", justify = CENTER, font = ("arial", 15))
        cmb_search.place(x = 10, y = 10, width = 180)
        cmb_search.current(0)

        txt_search = Entry(search_frame, textvariable = self.search_txt, font = ("arial", 15), bg = "white", borderwidth = 2, relief = SOLID)
        txt_search.place(x = 200, y = 10, width = 210)

        button_search = Button(search_frame, command = self.search, text = "Recherche", font = ("arial", 15), bg = "grey")
        button_search.place(x = 420, y = 10, height = 30)

        cmb_sort = ttk.Combobox(sort_frame, textvariable = self.sort_by, values = ("id_lot", "name", "marque", "age", "quantite"), state = "readonly", justify = CENTER, font = ("arial", 15))
        cmb_sort.place(x = 35, y = 10, width = 180)
        cmb_sort.current(0)

        cmb_sort_ord = ttk.Combobox(sort_frame, textvariable = self.sort_by_ord, values = ("croissant", "décroissant"), state = "readonly", justify = CENTER, font = ("arial", 15))
        cmb_sort_ord.place(x = 245, y = 10, width = 180)
        cmb_sort_ord.current(0)

        button_sort = Button(sort_frame, command = self.show, text = "Trier", font = ("arial", 15), bg = "grey")
        button_sort.place(x = 450, y = 10, height = 30)

        #-----------------------------------------------------------------#

        title = Label(self.root, text = "Gestion du stock", font = "arial", bg = "#b4a7d6")
        title.place(x = 50, y = 100, width = 1250)

        label_bottle_name = Label(self.root, text = "Type", font = "arial", bg = "#f0e9f7").place(x = 300, y = 150)
        label_bottle_marque = Label(self.root, text = "Marque", font = "arial", bg = "#f0e9f7").place(x = 650, y = 150)
        label_bottle_age = Label(self.root, text = "Age", font = "arial", bg = "#f0e9f7").place(x = 650, y = 200)

        txt_bottle_name = Entry(self.root, textvariable = self.var_bottle_name, font = "arial", bg = "white").place(x = 400, y = 150, width = 180)
        txt_bottle_marque = Entry(self.root, textvariable = self.var_bottle_marque, font = "arial", bg = "white").place(x = 750, y = 150, width = 180)
        txt_bottle_age = Entry(self.root, textvariable = self.var_bottle_age, font = "arial", bg = "white").place(x = 750, y = 200, width = 180)

        label_bottle_quantity = Label(self.root, text = "Quantité", font = "arial", bg = "#f0e9f7").place(x = 300, y = 200)

        txt_bottle_quantity = Entry(self.root, textvariable = self.var_bottle_quantity, font = "arial", bg = "white").place(x = 400, y = 200)

        label_id_lot = Label(self.root, text = "lot n°", font = "arial", bg = "#f0e9f7").place(x = 1000, y = 175)
        txt_id_lot = Entry(self.root, textvariable = self.var_id_lot, font = "arial", bg = "white", state = "readonly").place(x = 1050, y = 175)

        button_add = Button(self.root, command = self.add, text = "Ajouter", font = ("arial", 15), bg = "#4cd014", activebackground = "#c4f6ae", relief = FLAT).place(x = 330, y = 305)
        button_update = Button(self.root, text = "Mettre à jour", command = self.update, font = ("arial", 15), bg = "#e5b114", activebackground = "#ffeebd", relief = FLAT).place(x = 505, y = 305)
        button_delete = Button(self.root, text = "Supprimer", command = self.delete, font = ("arial", 15), bg = "#e54c4c", activebackground = "#ffa5a5", relief = FLAT).place(x = 730, y = 305)
        button_clear = Button(self.root, text = "Clear", command = self.clear, font = ("arial", 15), bg = "#7c48ff", activebackground = "#b293ff", relief = FLAT).place(x = 930, y = 305)
 
        #-----------------------------------------------------------------#

        stock_frame = Frame(self.root, bd = 3, relief = FLAT)
        stock_frame.place(x = 0, y = 350, relwidth = 1, height = 350)

        scrolly = Scrollbar(stock_frame, orient = VERTICAL)
        scrollx = Scrollbar(stock_frame, orient = HORIZONTAL)

        self.stock_table = ttk.Treeview(stock_frame, columns = ("name", "marque", "age", "quantite", "id_lot"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.stock_table.xview)
        scrolly.config(command = self.stock_table.yview)

        self.stock_table.heading("name", text = "Type")
        self.stock_table.heading("marque", text = "Marque")
        self.stock_table.heading("age", text = "Age")
        self.stock_table.heading("quantite", text = "Quantité")
        self.stock_table.heading("id_lot", text = "id lot")

        self.stock_table["show"] = "headings"

        self.stock_table.column("name", width = 100, )
        self.stock_table.column("marque", width = 100)
        self.stock_table.column("age", width = 10)
        self.stock_table.column("quantite", width = 10)
        self.stock_table.column("id_lot", width = 100)

        self.stock_table.pack(fill = BOTH, expand = 1)
        self.stock_table.bind("<ButtonRelease-1>", self.get_data)

        self.show()

        #-----------------------------------------------------------------#

    def add(self):
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            if self.var_bottle_name.get() == "":
                messagebox.showerror("Erreur", "vous devez nommer la bouteille.", parent =  self.root)
            else:
                cur.execute("Insert into alcool (name,marque,age,quantite) values(?,?,?,?)", (
                    self.var_bottle_name.get(),
                    self.var_bottle_marque.get(),
                    self.var_bottle_age.get(),
                    self.var_bottle_quantity.get()
                ))
                con.commit()
                messagebox.showinfo("Succeed", "La (les) bouteille(s) a (ont) été ajouté avec brio!", parent = self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()

    def show(self):
        order_by = self.sort_by.get()
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            if self.sort_by_ord.get() == "croissant":
                cur.execute(f"select * from alcool order by {order_by} asc")
            else:
                cur.execute(f"select * from alcool order by {order_by} desc")
            rows = cur.fetchall()
            self.stock_table.delete(*self.stock_table.get_children())
            for row in rows:
                self.stock_table.insert('', END, values = row)
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()

    def get_data(self, ev):
        f = self.stock_table.focus()
        content = (self.stock_table.item(f))
        row = content["values"]
        if len(row) > 0:
            self.var_bottle_name.set(row[0])
            self.var_bottle_marque.set(row[1])
            self.var_bottle_age.set(row[2])
            self.var_bottle_quantity.set(row[3])
            self.var_id_lot.set(row[4])

    def update(self):
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            if self.var_id_lot.get() == "":
                messagebox.showerror("Erreur", "Spécifiez le n° de lot.", parent =  self.root)
            else:
                cur.execute("Select * from alcool where id_lot=?", (self.var_id_lot.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "Bouteille(s) inconnue(s).", parent =  self.root)
                cur.execute("Update alcool set name=?,marque=?,age=?,quantite=? where id_lot=?", (
                    self.var_bottle_name.get(),
                    self.var_bottle_marque.get(),
                    self.var_bottle_age.get(),
                    self.var_bottle_quantity.get(),
                    self.var_id_lot.get()
                ))
                con.commit()
                messagebox.showinfo("Succeed", "La (les) bouteille(s) a (ont) été mise à jour avec brio!", parent = self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()

    def delete(self):
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            if self.var_id_lot.get() == "":
                messagebox.showerror("Erreur", "Spécifiez le n° de lot.", parent =  self.root)
            else:
                cur.execute("Select * from alcool where id_lot=?", (self.var_id_lot.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "Bouteille(s) inconnue(s).", parent =  self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Souhaitez vous vraiment supprimer la/les bouteille(s)?", parent = self.root)
                    if op == True:
                        cur.execute("delete from alcool where id_lot=?", (self.var_id_lot.get(),))
                        con.commit()
                        messagebox.showinfo("Succeed", "La (les) bouteille(s) a (ont) été supprimées avec brio!", parent = self.root)
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()

    def clear(self):
        self.var_bottle_name.set("")
        self.var_bottle_marque.set("")
        self.var_bottle_age.set("")
        self.var_bottle_quantity.set("")
        self.search_by.set("name")
        self.search_txt.set("")
        self.show()

    def search(self):
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            if self.search_by.get() == "Selectionner":
                messagebox.showerror("Erreur", "Précisez votre recherche", parent =  self.root)
            elif self.search_txt.get() == "":
                messagebox.showerror("Erreur", "Précisez votre recherche", parent =  self.root)
            else :
                cur.execute("select * from alcool where " + self.search_by.get() + " LIKE '%" + self.search_txt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.stock_table.delete(*self.stock_table.get_children())
                    for row in rows:
                        self.stock_table.insert('', END, values = row)
                else:
                    messagebox.showerror("Erreur", "Bouteille(s) inconnue(s).", parent =  self.root)
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()

class Print_alcool:
    def __init__(self, root) -> None:
        self.root = root
        self.root.geometry("1350x700+220+130")
        self.root.title("Stock Management")
        self.root.config(bg = "white")
        self.root.focus_force()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        self.sort_by = StringVar()
        self.sort_by_ord = StringVar()

        search_frame = LabelFrame(self.root, text = "Recherche", bg = "white")
        search_frame.place(x = 50, y = 20, width = 600, height = 70)

        sort_frame = LabelFrame(self.root, text = "Trier", bg = "white")
        sort_frame.place(x = 750, y = 20, width = 550, height = 70)

        cmb_search = ttk.Combobox(search_frame, textvariable = self.search_by, values = ("Selectionner", "name", "marque", "age"), state = "readonly", justify = CENTER, font = ("arial", 15))
        cmb_search.place(x = 35, y = 10, width = 180)
        cmb_search.current(0)

        txt_search = Entry(search_frame, textvariable = self.search_txt, font = ("arial", 15), bg = "white", borderwidth = 2, relief = SOLID)
        txt_search.place(x = 225, y = 10, width = 210)

        button_search = Button(search_frame, command = self.search, text = "Recherche", font = ("arial", 15), bg = "white", relief = FLAT)
        button_search.place(x = 445, y = 10, height = 30)

        cmb_sort = ttk.Combobox(sort_frame, textvariable = self.sort_by, values = ("id_lot", "name", "marque", "age", "quantite"), state = "readonly", justify = CENTER, font = ("arial", 15))
        cmb_sort.place(x = 35, y = 10, width = 180)
        cmb_sort.current(0)

        cmb_sort_ord = ttk.Combobox(sort_frame, textvariable = self.sort_by_ord, values = ("croissant", "décroissant"), state = "readonly", justify = CENTER, font = ("arial", 15))
        cmb_sort_ord.place(x = 245, y = 10, width = 180)
        cmb_sort_ord.current(0)

        button_sort = Button(sort_frame, command = self.show, text = "Trier", font = ("arial", 15), bg = "white", relief = FLAT)
        button_sort.place(x = 450, y = 10, height = 30)

        button_clear = Button(self.root, text = "Clear", command = self.clear, font = ("arial", 15), bg = "white", activebackground = "#b293ff", relief = FLAT).place(x = 660, y = 40)

        stock_frame = Frame(self.root, bd = 3, relief = FLAT)
        stock_frame.place(x = 0, y = 100, relwidth = 1, height = 600)

        scrolly = Scrollbar(stock_frame, orient = VERTICAL)
        scrollx = Scrollbar(stock_frame, orient = HORIZONTAL)

        self.stock_table = ttk.Treeview(stock_frame, columns = ("name", "marque", "age", "quantity", "id_lot"), yscrollcommand = scrolly.set, xscrollcommand = scrollx.set)
        scrollx.pack(side = BOTTOM, fill = X)
        scrolly.pack(side = RIGHT, fill = Y)
        scrollx.config(command = self.stock_table.xview)
        scrolly.config(command = self.stock_table.yview)

        self.stock_table.heading("name", text = "Nom")
        self.stock_table.heading("marque", text = "Marque")
        self.stock_table.heading("age", text = "Age")
        self.stock_table.heading("quantity", text = "Quantité")
        self.stock_table.heading("id_lot", text = "id lot")

        self.stock_table["show"] = "headings"

        self.stock_table.column("name", width = 100)
        self.stock_table.column("marque", width = 100)
        self.stock_table.column("age", width = 100)
        self.stock_table.column("quantity", width = 200)
        self.stock_table.column("id_lot", width = 100)
        self.stock_table.pack(fill = BOTH, expand = 1)

        self.show()

    def show(self):
        order_by = self.sort_by.get()
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            if self.sort_by_ord.get() == "croissant":
                cur.execute(f"select * from alcool order by {order_by} asc")
            else:
                cur.execute(f"select * from alcool order by {order_by} desc")
            rows = cur.fetchall()
            self.stock_table.delete(*self.stock_table.get_children())
            for row in rows:
                self.stock_table.insert('', END, values = row)
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()

    def search(self):
        con = sq.connect(database = r"wms.db")
        cur = con.cursor()
        try:
            if self.search_by.get() == "Selectionner":
                messagebox.showerror("Erreur", "Précisez votre recherche", parent =  self.root)
            elif self.search_txt.get() == "":
                messagebox.showerror("Erreur", "Précisez votre recherche", parent =  self.root)
            else :
                cur.execute("select * from alcool where " + self.search_by.get() + " LIKE '%" + self.search_txt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.stock_table.delete(*self.stock_table.get_children())
                    for row in rows:
                        self.stock_table.insert('', END, values = row)
                else:
                    messagebox.showerror("Erreur", "Bouteille(s) inconnue(s).", parent =  self.root)
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur due à : {str(ex)}.")
        con.close()
    
    def clear(self):
        self.search_by.set("Selectionner")
        self.search_txt.set("")
        self.show()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Print_alcool(root)
#     root.mainloop()
