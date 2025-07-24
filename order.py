import tkinter, json, functions
from PIL import ImageTk, Image

tab = functions.Window("Order", "600x600")

tab.set_window()

tab.create_frame(rowspan=1, columnspan=5, row=0,
                 column=0, isimage=True,
                 imageDir=r"Images\Banner.png",
                 imagerow=0, imagecolumn=0, imagerowspan=1, imagecolumnspan=5)

tab.create_frame(rowspan=3, columnspan=2, row=1, column=3,
                 isimage=True, imageDir=r"Images\MAIN.png", imagerow=0, imagecolumn=0,
                 imagerowspan=3, imagecolumnspan=2)

tab.create_frame(rowspan=3, columnspan=3, row=1, column=0, ismenuitems=True,
                 menuitemamount=9)

tab.create_footer(row=4, column=0, rowspan=1, columnspan=5)


tab.window.mainloop()
