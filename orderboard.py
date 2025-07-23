import tkinter, json, functions, time

tab = functions.Window("Order Board", "600x400")
tab.set_window()

tab.create_frame(rowspan=5, columnspan=5, row=0, column=0, isimage=True,
                 imageDir=r"Images\ORDERS.png", imagerow=0, imagecolumn=0,
                 imagerowspan=1, imagecolumnspan=5)


currentOrderFrames = {}

def check_for_new_orders():

    data = {}

    with open("data.json", "r") as file:

        newdata = json.load(file)

        if data != newdata:
            data = newdata

            for frame in currentOrderFrames.values():
                frame.destroy()
            currentOrderFrames.clear()

            for orderID in range(len(newdata['orders'])):
            
                frame = tab.create_frame(rowspan=1, columnspan=5, row=orderID+1, column=0,
                                isOrder=True,
                                labelText=f"Order ID: {newdata['orders'][orderID]}",
                                labelrow=2, labelcolumn=0, labelrowspan=1,
                                labelcolumnspan=1, labelfontsize=15, labelFont="Arial",
                                buttonText="Fulfill", buttonrow=2,
                                buttoncolumn=4)
                
                currentOrderFrames[orderID] = frame

        tab.window.after(5000, check_for_new_orders)


check_for_new_orders()



tab.window.mainloop()

