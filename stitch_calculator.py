from tkinter import *
from tkinter import ttk
from func import (
    entry_status_cross,
    entry_status_cm,
    entry_status_allow_off,
    entry_status_allow_on,
    stitch_to_size,
    size_to_stitch,
    calculate,
    validate_float,
    validate_int
)

if __name__ == "__main__":
    # Create window
    window = Tk()
    window.geometry("640x380")
    window.minsize(640, 380)
    window.maxsize(640, 380)
    window.title("Калькулятор канвы")

    vcmd_float = (window.register(validate_float), "%P")
    vcmd_int = (window.register(validate_int), "%P")


    # Define text, buttons, entries etc.:
    # LABELS
    youknow = Label(window, text="Вы знаете размер вышивки:", font=("Calibri", 12, "bold"))
    oncount = Label(
        window,
        text="на канве",
    )
    wanttoknow = Label(
        window, text="Вы хотите узнать размер вышивки:", font=("Calibri", 12, "bold")
    )

    # 'x' labels between entries with sizes (for input values) -> size *x* size
    x_mark1 = Label(
        window,
        text="x",
    )
    x_mark2 = Label(
        window,
        text="x",
    )
    x_mark3 = Label(
        window,
        text="x",
    )

    # Field with final result
    result = Label(window, text="", font=("Calibri", 12), wraplength=600, justify="left")

    # RADIOBUTTONS
    # Set variables and default values for Radiobuttons
    r1_val = BooleanVar(value=1)
    r2_val = BooleanVar(value=1)

    sizeinstitches = Radiobutton(
        window,
        text="в крестиках:",
        variable=r1_val,
        value=0,
        command=entry_status_cross,
    )
    sizeincm = Radiobutton(
        window,
        text="в сантиметрах:",
        variable=r1_val,
        value=1,
        command=entry_status_cm,
    )
    sizeinstitches2 = Radiobutton(
        window,
        text="в крестиках",
        variable=r2_val,
        value=0,
        comman=entry_status_allow_off,
    )
    sizeoncount = Radiobutton(
        window,
        text="в сантиметрах на канве",
        variable=r2_val,
        value=1,
        comman=entry_status_allow_on,
    )

    # COMBOBOXES and their default values
    # Values
    counts = [
        "6 каунт",
        "8 каунт",
        "10 каунт",
        "11 каунт",
        "14 каунт",
        "16 каунт",
        "18 каунт",
        "20 каунт",
        "22 каунт",
        "24 каунт",
        "25 каунт (через 1 нить)",
        "25 каунт (через 2 нити)",
        "27 каунт (через 1 нить)",
        "27 каунт (через 2 нити)",
        "28 каунт (через 1 нить)",
        "28 каунт (через 2 нити)",
        "30 каунт (через 1 нить)",
        "30 каунт (через 2 нити)",
        "32 каунт (через 1 нить)",
        "32 каунт (через 2 нити)",
        "36 каунт (через 1 нить)",
        "36 каунт (через 2 нити)",
        "40 каунт (через 1 нить)",
        "40 каунт (через 2 нити)",
        "46 каунт (через 1 нить)",
        "46 каунт (через 2 нити)",
        "56 каунт (через 1 нить)",
        "56 каунт (через 2 нити)",
    ]
    counts2 = counts[:]

    # Boxes
    countlist1 = ttk.Combobox(window, values=counts, width=22)
    countlist1.current(0)
    countlist2 = ttk.Combobox(window, values=counts2, width=22)
    countlist2.current(0)

    # 'CALCULATE' button
    showresult = Button(
        window,
        width="20",
        text="Посчитать",
        font=("Calibri", 12, "bold"),
        command=calculate,
    )

    # ENTRIES
    # Define fields and initial values for entering x and y numbers of stitches
    xstitch = IntVar(value=0)
    ystitch = IntVar(value=0)
    x_stitch = Entry(
        window,
        state="disabled",
        width=10,
        borderwidth=2,
        textvariable=xstitch,
        validate="key",
        validatecommand=vcmd_int,
    )
    y_stitch = Entry(
        window,
        state="disabled",
        width=10,
        borderwidth=2,
        textvariable=ystitch,
        validate="key",
        validatecommand=vcmd_int,
    )
    # Define fields and initial values for entering x and y for cm on fabric
    xsize = IntVar(value=0)
    ysize = IntVar(value=0)
    alsize = IntVar(value=0)
    x_size = Entry(
        window,
        width=10,
        borderwidth=2,
        textvariable=xsize,
        validate="key",
        validatecommand=vcmd_float,
    )
    y_size = Entry(
        window,
        width=10,
        borderwidth=2,
        textvariable=ysize,
        validate="key",
        validatecommand=vcmd_float,
    )
    allow_size = Entry(
        window,
        width=10,
        borderwidth=2,
        textvariable=alsize,
        validate="key",
        validatecommand=vcmd_float,
    )

    # Seam allowance checkbutton
    check_var = IntVar()
    allow = Checkbutton(window, text="Припуск в сантиметрах", variable=check_var)

    # Put text, buttons, entries etc. on a screen ordering from top to bottom, left to right:
    youknow.place(x=10, y=0)
    sizeinstitches.place(x=10, y=30)
    x_stitch.place(x=160, y=30)
    x_mark1.place(x=250, y=30)
    y_stitch.place(x=265, y=30)
    sizeincm.place(x=10, y=60)
    x_size.place(x=160, y=60)
    x_mark2.place(x=250, y=60)
    y_size.place(x=265, y=60)
    oncount.place(x=355, y=60)
    countlist1.place(x=425, y=60)
    wanttoknow.place(x=10, y=90)
    sizeinstitches2.place(x=10, y=120)
    sizeoncount.place(x=10, y=150)
    countlist2.place(x=220, y=150)
    allow.place(x=10, y=180)
    allow_size.place(x=220, y=180)
    showresult.place(x=10, y=220)
    result.place(x=10, y=250)


    # Start program window
    window.mainloop()

# TODO multilanguage?
