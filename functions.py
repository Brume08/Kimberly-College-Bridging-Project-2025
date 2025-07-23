import json  # Imports both json and tkinter modules
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random


class Window:  # Define a class that creates windows
    def __init__(self, name, geometry):
        self.name = name  # Title of the window
        self.geometry = geometry  # Setting window geometry
        self.window = Tk()
        self.images = []
        self.menuitems = [r"Images\Cheese Burger.png",
                          r"Images\2 Chicken Wings.png",
                          r"Images\Small Pizza.png",
                          r"Images\Potato Fries.png",
                          r"Images\Baked Beans.png",
                          r"Images\Loaded Nachos.png",
                          r"Images\Coca-Cola.png",
                          r"Images\Choco Milkshake.png",
                          r"Images\Water.png"]
        self.namedItems = [3.9, 2.5, 4.5, 2.5, 2.0, 3.0, 1.5, 2.5, 1.0]
        self.price = 0.0

        self.footerFrame = Frame(self.window, bg="White", width=5 * 120, height=1 * 120)
        self.financialFrame = Frame(self.footerFrame, bg="grey75", width=5 * (4 / 5) * 120, height=1 * 120)
        self.cartFrame = Frame(self.financialFrame, bg="White", width=5 * (3 / 5) * 120, height=1 * (4 / 5) * 120)

        self.totalPriceLabel = Label(self.cartFrame, text=f"Total Price: £{self.price}0", font=("Arial", 8), fg="Black")
        self.currentItemsLabel = Label(self.cartFrame, text=f"Items: ", font=("Arial", 6), fg="Black")

        self.addedItems = []
        self.viewItems = ""
        self.characterCount = 1
        self.orderIDs = []

    def add_order_json_file(self, filename, orderID):
        with open(filename, "r") as file:
            data = json.load(file)

        data['orders'].append(orderID)

        data[f'{orderID}'] = []
        
        for item in self.addedItems:
            data[f'{orderID}'].append(item)

        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

        
    
    def add_item(self, name, price):
        message = Toplevel()
        text = Label(message, text=f"Added {name} \n Price:{price}0")
        text.grid(row=0, column=2, sticky="nsew")
        text.grid_propagate(False)
        close_button = Button(message, text="Close", command=message.destroy)
        close_button.grid(row=2, column=0, columnspan=5)
        close_button.grid_propagate(False)

    def remove_item(self, name, price):
        message = Toplevel()
        text = Label(message, text=f"Removed {name} from cart")
        text.grid(row=0, column=2, sticky="nsew")
        text.grid_propagate(False)
        close_button = Button(message, text="Close", command=message.destroy)
        close_button.grid(row=2, column=0, columnspan=5)
        close_button.grid_propagate(False)

    def increase_price(self, price, label, itemname):
        self.price += price
        label.config(text=f"Total Price: £{self.price}0")
        self.addedItems.append(itemname)
        self.add_item(itemname, price)

        if self.viewItems == "":
            self.viewItems += "  " + itemname
        elif len(self.viewItems) > 25 * self.characterCount:
            self.viewItems += " \n" + itemname
            self.characterCount += 1
        else:
            self.viewItems += ", " + itemname

        self.currentItemsLabel.config(text=f"Items: {self.viewItems}")

    def decrease_price(self, price, label, itemname):
        if itemname in self.addedItems:
            self.price -= price
            label.config(text=f"Total Price: £{self.price}0")
            self.addedItems.remove(itemname)
            self.remove_item(itemname, price)
            self.viewItems = self.viewItems[:-len(itemname)-1]
            self.currentItemsLabel.config(text=f"Items: {self.viewItems}")
        else:
            message = Toplevel()
            text = Label(message, text="Item is not in cart.")
            text.grid(row=0, column=2, sticky="nsew")
            text.grid_propagate(False)
            close_button = Button(message, text="Close", command=message.destroy)
            close_button.grid(row=2, column=0, columnspan=5)
            close_button.grid_propagate(False)

    def complete_order(self):
        if len(self.addedItems) > 0:
            completedOrder = Toplevel()
            orderID = random.randint(1111, 9999)
            self.orderIDs.append(orderID)
            completedOrderLabel = Label(completedOrder,
                                        text=f"Order ID: {orderID} \n Price: £{self.price}0")
            completedOrderLabel.grid(row=0, column=0, sticky="nsew", padx=(50, 50), pady=(50, 50))
            self.add_order_json_file("data.json", orderID)
            self.viewItems = ""
            self.currentItemsLabel.config(text=f"Items: {self.viewItems}")
            self.price = 0.0
            self.totalPriceLabel.config(text=f"Total Price: £{self.price}0")
            self.addedItems.clear()
            
        else:
            message = Toplevel()
            text = Label(message, text="No items ordered.")
            text.grid(row=0, column=2, sticky="nsew")
            text.grid_propagate(False)
            close_button = Button(message, text="Close", command=message.destroy)
            close_button.grid(row=2, column=0, columnspan=5)
            close_button.grid_propagate(False)

    def set_window(self):
        self.window.title(self.name)

    def create_frame(self, rowspan=1, columnspan=1,
                     bgcolour="white", borderwidth=0, row=0, column=0,
                     isimage=False, imageDir="", imagerow=0, imagecolumn=0,
                     imagerowspan=1, imagecolumnspan=1, ismenuitems=False,
                     menuitemamount=1, ismenufooter=False, isOrder=False,
                     labelText="", labelrow=0, labelcolumn=0, labelrowspan=1,
                     labelcolumnspan=1, labelfontsize=10, labelFont="Arial",
                     buttonText="Fulfill", buttonrow=0, buttoncolumn=0,
                     buttonrowspan=1, buttoncolumnspan=1, isProgress=False):

        newFrame = Frame(self.window, bg=bgcolour,
                         width=columnspan * 120, height=rowspan * 120)
        newFrame.grid_propagate(False)
        newFrame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)


        if isimage and not ismenuitems:
            newImage = ImageTk.PhotoImage(Image.open(imageDir))
            self.images.append(newImage)
            imageLabel = Label(newFrame, image=newImage, width=imagecolumnspan * 120, height=imagerowspan * 120)
            imageLabel.grid(row=imagerow, column=imagecolumn)
            imageLabel.grid_propagate(False)

    
        elif isOrder and not (isimage or ismenuitems or isProgress):


            newFrame.config(height=rowspan*40)


            newLabel = Label(newFrame, text=labelText, font=("Arial", 18))
            newLabel.grid(row=labelrow, column=labelcolumn, rowspan=labelrowspan,
                          columnspan=labelcolumnspan, padx=(0, 10))
            newLabel.grid_propagate(False)


            
            fulfillButton = Button(newFrame, text=buttonText, font=("Arial", 18))
            fulfillButton.grid(row=buttonrow, column=buttoncolumn,
                                rowspan=buttonrowspan,
                                columnspan=buttoncolumnspan, sticky="nse",
                               padx=300)
            fulfillButton.grid_propagate(False)

            return newFrame
                
        elif ismenuitems and not isimage:
            for i in range(0, rowspan):
                for j in range(0, columnspan):
                    gridItem = self.menuitems[3 * i + j]
                    gridItemPrice = self.namedItems[3 * i + j]
                    nameOfItem = gridItem[7:-4].capitalize()

                    menuFrame = Frame(newFrame, bg=bgcolour, width=(columnspan / 3) * 120, height=(rowspan / 3) * 120)
                    menuFrame.grid(row=i, column=j)
                    menuFrame.grid_propagate(False)

                    currentImage = ImageTk.PhotoImage(Image.open(gridItem))
                    self.images.append(currentImage)
                    menuImage = Label(menuFrame, image=currentImage)
                    menuImage.grid(row=0, column=0)
                    menuImage.grid_propagate(False)

                    imageLabel = Label(menuFrame, text=nameOfItem, width=int(columnspan / 18) * 120,
                                       height=int(rowspan / 15) * 120, bg="Black", fg="White", font=("Arial", 8))
                    imageLabel.grid(row=0, column=0, sticky="sw", padx=5, pady=5)
                    imageLabel.lift()
                    imageLabel.grid_propagate(False)

                    imageButtonAdd = Button(menuFrame, text="+", width=int(columnspan / 15) * 120,
                                            height=int(rowspan / 15) * 120, bg="Black", fg="White", font=("Arial", 10),
                                            command=lambda p=gridItemPrice, l=self.totalPriceLabel, n=nameOfItem:
                                            self.increase_price(p, l, n))
                    imageButtonAdd.grid(row=0, column=0, sticky="nw", padx=1, pady=1)
                    imageButtonAdd.lift()
                    imageButtonAdd.grid_propagate(False)

                    imageButtonMinus = Button(menuFrame, text="-", width=int(columnspan / 15) * 120,
                                              height=int(rowspan / 15) * 120, bg="Black", fg="White", font=("Arial", 10),
                                              command=lambda p=gridItemPrice, l=self.totalPriceLabel, n=nameOfItem:
                                              self.decrease_price(p, l, n))
                    imageButtonMinus.grid(row=0, column=0, sticky="ne", padx=1, pady=1)
                    imageButtonMinus.lift()
                    imageButtonMinus.grid_propagate(False)

                    imagePrice = Label(menuFrame, text=f"{gridItemPrice}0", width=int(column / 15) * 120,
                                       height=int(rowspan / 15) * 120, bg="Black", fg="White", font=("Arial", 8))
                    imagePrice.grid(row=0, column=0, sticky="se", padx=1, pady=1)
                    imagePrice.lift()
                    imagePrice.grid_propagate(False)

        elif ismenuitems and isimage:
            print("Only image or menu items can be true, not both.")

    def create_footer(self, row=0, column=0, rowspan=1, columnspan=1,
                      backgroundcolour="White"):
        self.footerFrame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan)
        self.footerFrame.grid_propagate(False)

        self.financialFrame.grid(row=0, column=0, columnspan=columnspan - 1, rowspan=rowspan)
        self.financialFrame.grid_propagate(False)

        self.cartFrame.grid(row=0, column=0, pady=(15, 25), columnspan=2)
        self.cartFrame.grid_propagate(False)

        cartTitle = Label(self.cartFrame, text="Cart", font=("Arial", 14, "bold"), fg="Black", bg=backgroundcolour)
        cartTitle.grid(row=0, column=2)
        cartTitle.grid_propagate(False)

        self.currentItemsLabel.grid(row=3, column=0)
        self.currentItemsLabel.grid_propagate(False)

        self.totalPriceLabel.grid(row=3, column=4)
        self.totalPriceLabel.grid_propagate(False)

        completeButton = Button(self.footerFrame, text="Complete Order", bg="Green", fg="White",
                                width=int(columnspan / 10) * 120, height=int(rowspan / 10) * 120,
                                font=("Arial", 10, "bold"), command=self.complete_order)
        completeButton.grid(row=0, column=4, padx=5)
        completeButton.grid_propagate(False)

