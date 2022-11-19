from tkinter import *
from tkinter import ttk

# Create window
window = Tk()
window.geometry('600x380')
window.minsize(600, 380)
window.maxsize(600, 380)
window.title("Калькулятор канвы")

# Variable and function for entry fields validation (only integers available)
def validate_float(new_value):
    try: 
        if new_value == "" or new_value ==".":
            return True
        _str = str(float(new_value))
        return True
    except:
        return False 

def validate_int(new_value):
    try: 
        if new_value == "":
            return True
        _str = str(float(new_value))
        return True
    except:
        return False 

vcmd_float = (window.register(validate_float),'%P')
vcmd_int = (window.register(validate_int),'%P')

# Functions for enabling/diabling fields with radiobuttons and checkboxes
def entry_status_cross():
        x_stitch.configure(state="normal")
        x_stitch.update()
        y_stitch.configure(state="normal")
        y_stitch.update()
        x_size.configure(state="disabled")
        x_size.update()
        y_size.configure(state="disabled")
        y_size.update()
        countlist1.configure(state="disabled")
        countlist1.update()
        sizeinstitches2.configure(state="disabled")
        sizeinstitches2.update()


def entry_status_cm():
        x_stitch.configure(state="disabled")
        x_stitch.update()
        y_stitch.configure(state="disabled")
        y_stitch.update()
        x_size.configure(state="normal")
        x_size.update()
        y_size.configure(state="normal")
        y_size.update()
        countlist1.configure(state="normal")
        countlist1.update()
        sizeinstitches2.configure(state="normal")
        sizeinstitches2.update()


def entry_status_allow_off():
        allow.configure(state="disable")
        allow.update()
        allow_size.configure(state="disable")
        allow_size.update()
        countlist2.configure(state="disable")
        countlist2.update()


def entry_status_allow_on():
        allow.configure(state="normal")
        allow.update()
        allow_size.configure(state="normal")
        allow_size.update()
        countlist2.configure(state="normal")
        countlist2.update()


def stitch_to_size(stitches, count) -> tuple:
    """
    Converts numbers of stitches on X and Y axis on count to inches

    Args:
    stitches: list(float, float): -- stitches[0] - number of stitches on x axis; stitches[1] - number of stitches on y axis
    count: int -- count size

    Return:
    tuple(float, float) -- result[0] - inches on x axis; result[1] - inches on y axis
    """
    X_size = (stitches[0]/count)
    Y_size = (stitches[1]/count)
    result = (X_size, Y_size)
    return result


def size_to_stitch(dimensions, count) -> tuple:
    """
    Converts dimension  on X and Y axis in centimeters on count to number of stitches

    Args:
    dimensions: list(float, float) -- dimensions[0] - size in cm on x axis; dimensions[1] size in cm on y axis
    count: int -- count size

    Return:
    result: tuple(int, int) -- result[0] - number of stitches on x axis; result[1] - number of stitches on y axis
    """
    X_count = int((dimensions[0]/2.54)*count)
    Y_count = int((dimensions[1]/2.54)*count)
    result = (X_count, Y_count)
    return result



def calculate():
    """
    Calculate results when user presses 'Calculate' button. Uses funcions size_to_stitch and stitch_to_size
    Answer depends of what checkboxes, radiobuttons, and values from comboboxes were chosen.
    Generates f-string with an answer and sends it to Label 'result'.
    """
    global answer

    def long_line(lst):
        # For modifying answer string when count value has brackets (counts from 25 to 56)
        return f" (при вышивании через {lst[-2]} нит{'и' if lst[-2]=='2' else 'ь'} основы)"

    empty_line = ""
    alsize_total = float(alsize.get())*2 # Seam allowanse dounled for calculating dimensions (allowance goes for both sides)

    # CASE 1: Checked radibuttons: know size in crosses, want size in cm
    if (r1_val.get() == 0) and (r2_val.get() == 1): 
        stitches = (int(x_stitch.get()), int(y_stitch.get()))
        count = countlist2.get().split()
 
        if len(count) > 2: # For cases when checkbox has value with brackets (counts from 25 to 56)
            ans = stitch_to_size(stitches, int(count[0])/int(count[-2]))
            txt_add = long_line(count)
        else: # For cases when checkbox has no brackets in value (counts from 6 to 24)
            ans = stitch_to_size(stitches, int(count[0]))
            txt_add = empty_line
        # For cases without or with seam allowance (based on checkbox)
        if check_var.get() == 0:
            answer = f"Вышивка размером {stitches[0]} х {stitches[1]} крестиков занимает на ткани {count[0]} каунт{txt_add}:\
            \nВ сантиметрах: {ans[0] * 2.54:.2f} х {ans[1] * 2.54:.2f} см.\
            \nВ дюймах: {ans[0]:.2f} х {ans[1]:.2f} дюймов."
        elif check_var.get() == 1:
            answer = f"Вышивка размером {stitches[0]} х {stitches[1]} крестиков занимает на ткани {count[0]} каунт{txt_add}:\
            \nВ сантиметрах с припуском: {ans[0] * 2.54 + alsize_total:.2f} х {ans[1] * 2.54 + alsize_total:.2f} см.\
            \nВ дюймах с припуском: {ans[0] + (alsize_total / 2.54):.2f} х {ans[1] + (alsize_total / 2.54):.2f} дюймов."

    # CASE 2: Checked radibuttons: know size in cm on count, want number of stitches
    elif (r1_val.get() == 1) and (r2_val.get() == 0):
        dimensions = (float(x_size.get()), float(y_size.get()))
        count = countlist1.get().split()
        if len(count) > 2: # For cases when checkbox has value with brackets (counts from 25 to 56)
            ans = size_to_stitch(dimensions, int(count[0])/int(count[-2]))
            txt_add = long_line(count)
        else: # For cases when checkbox has no brackets in value (counts from 6 to 24)
            ans = size_to_stitch(dimensions, int(count[0]))
            txt_add = empty_line
        answer = f"Вышивка размером {dimensions[0]} х {dimensions[1]} cм на ткани {count[0]} каунт{txt_add}:\
        \nсостоит приблизительно из {ans[0]}x{ans[1]} крестиков."

    # CASE 3: Checked radibuttons: know size in cm on count, want size in cm on another count
    elif (r1_val.get() == 1) and (r2_val.get() == 1):
        dimensions = (float(x_size.get()), float(y_size.get()))
        count_old = countlist1.get().split() 
        count_new = countlist2.get().split()
        if len(count_old) > 2: # For cases when checkbox of known count has value with brackets (counts from 25 to 56)
            pre = size_to_stitch(dimensions, int(count_old[0])/int(count_old[-2]))
            txt_add_old = long_line(count_old)
        else: # For cases when checkbox of known count has no brackets in value (counts from 6 to 24)
            pre = size_to_stitch(dimensions, int(count_old[0]))
            txt_add_old = empty_line
        if len(count_new) > 2: # For cases when checkbox of wanted count has value with brackets (counts from 25 to 56)
            ans = stitch_to_size(pre, int(count_new[0])/int(count_new[-2]))
            txt_add_new = long_line(count_new)
        else:
            ans = stitch_to_size(pre, int(count_new[0]))
            txt_add_new = empty_line
        # For cases without or with seam allowance (based on checkbox)
        if check_var.get() == 0:
            answer = f"Вышивка размером {dimensions[0]} х {dimensions[1]} cм на ткани {count_old[0]} каунт{txt_add_old} занимает на ткани {count_new[0]} каунт{txt_add_new}:\
            \nВ сантиметрах: {ans[0] * 2.54:.2f} х {ans[1] * 2.54:.2f} см.\
            \nВ дюймах: {ans[0]:.2f} х {ans[1]:.2f} дюймов."
        elif check_var.get() == 1:
            answer = f"Вышивка размером {dimensions[0]} х {dimensions[1]} cм на ткани {count_old[0]} каунт{txt_add_old} занимает на ткани {count_new[0]} каунт{txt_add_new}:\
            \nВ сантиметрах с припуском: {ans[0] * 2.54 + alsize_total:.2f} х {ans[1] * 2.54 + alsize_total:.2f} см.\
            \nВ дюймах с припуском: {ans[0] + (alsize_total / 2.54):.2f} х {ans[1] + (alsize_total / 2.54):.2f} дюймов."
          
    result.config(text=answer)


# Define text, buttons, entries etc.:
# LABELS
youknow = Label(window, text="Вы знаете:", font=('Calibri', 12, "bold"))
oncount = Label(window, text="на канве",)
wanttoknow = Label(window, text="Вы хотите узнать:", font=("Calibri", 12, "bold"))

# 'x' labels between entries with sizes (for input values) -> size *x* size
x_mark1 = Label(window, text="x",)
x_mark2 = Label(window, text="x",)
x_mark3 = Label(window, text="x",)

# Field with final result
result = Label(window, text = '', font=("Calibri", 12), wraplength=600, justify='left')

# RADIOBUTTONS
# Set variables and default values for Radiobuttons
r1_val = BooleanVar(value=1)
r2_val = BooleanVar(value=1)

sizeinstitches = Radiobutton(window, text="Размер вышивки в крестиках:", variable=r1_val, value=0, command=entry_status_cross)
sizeincm = Radiobutton(window, text="Размер вышивки в сантиметрах:", variable=r1_val, value=1, command=entry_status_cm)
sizeinstitches2 = Radiobutton(window, text="Размер вышивки в крестиках", variable=r2_val, value=0, comman=entry_status_allow_off)
sizeoncount = Radiobutton(window, text="Размер вышивки в сантиметрах на канве", variable=r2_val, value=1, comman=entry_status_allow_on)

# COMBOBOXES and their default values
# Values
counts = [
    '6 каунт',
    '8 каунт',
    '10 каунт',
    '11 каунт',
    '14 каунт',
    '16 каунт',
    '18 каунт',
    '20 каунт',
    '22 каунт',
    '24 каунт',
    '25 каунт (через 1 нить)',
    '25 каунт (через 2 нити)',
    '27 каунт (через 1 нить)',
    '27 каунт (через 2 нити)',
    '28 каунт (через 1 нить)',
    '28 каунт (через 2 нити)',
    '30 каунт (через 1 нить)',
    '30 каунт (через 2 нити)',
    '32 каунт (через 1 нить)',
    '32 каунт (через 2 нити)',
    '36 каунт (через 1 нить)',
    '36 каунт (через 2 нити)',
    '40 каунт (через 1 нить)',
    '40 каунт (через 2 нити)',
    '46 каунт (через 1 нить)',
    '46 каунт (через 2 нити)',
    '56 каунт (через 1 нить)',
    '56 каунт (через 2 нити)',
]
counts2 = counts[:]

#Boxes
countlist1 = ttk.Combobox(window, values = counts, width=22)
countlist1.current(0)
countlist2 = ttk.Combobox(window, values = counts2, width=22)
countlist2.current(0)

# 'CALCULATE' button
showresult = Button(window, width='20', text="Посчитать", font=("Calibri", 12, "bold"), command=calculate) 

# ENTRIES
# Define fields and initial values for entering x and y numbers of stitches
xstitch = IntVar(value=0)
ystitch = IntVar(value=0)
x_stitch = Entry(window, state='disabled', width=10, borderwidth=2, textvariable=xstitch, validate ='key', validatecommand=vcmd_int)
y_stitch = Entry(window, state='disabled', width=10, borderwidth=2, textvariable=ystitch, validate ='key', validatecommand=vcmd_int)
# Define fields and initial values for entering x and y for cm on fabric
xsize = IntVar(value=0)
ysize = IntVar(value=0)
alsize = IntVar(value=0)
x_size = Entry(window, width=10, borderwidth=2, textvariable=xsize, validate ='key', validatecommand=vcmd_float)
y_size = Entry(window, width=10, borderwidth=2, textvariable=ysize, validate ='key', validatecommand=vcmd_float)
allow_size = Entry(window, width=10, borderwidth=2, textvariable=alsize, validate ='key', validatecommand=vcmd_float)

# Seam allowance checkbutton
check_var = IntVar()
allow = Checkbutton(window, text = 'Припуск в сантиметрах', variable=check_var)

# Put text, buttons, entries etc. on a screen ordering from top to bottom, left to right:
youknow.place(x = 10, y = 0)
sizeinstitches.place(x = 10, y = 30)
x_stitch.place(x = 220, y = 30)
x_mark1.place(x = 290, y = 30)
y_stitch.place(x = 308, y = 30)
sizeincm.place(x = 10, y = 60)
x_size.place(x = 220, y = 60)
x_mark2.place(x = 290, y = 60)
y_size.place(x = 308, y = 60)
oncount.place(x = 378, y = 60)
countlist1.place (x = 430, y = 60)
wanttoknow.place(x = 10, y = 90)
sizeinstitches2.place(x = 10, y = 120)
sizeoncount.place(x = 10, y = 150)
countlist2.place (x = 265, y = 150)
allow.place(x = 10, y = 180)
allow_size.place(x = 170, y = 180)
showresult.place(x = 10, y = 220)
result.place(x = 10, y = 250)


# Start program window
window.mainloop()

# TODO multilanguage? modules?
