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
    X_size = stitches[0] / count
    Y_size = stitches[1] / count
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
    X_count = int((dimensions[0] / 2.54) * count)
    Y_count = int((dimensions[1] / 2.54) * count)
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
        return (
            f" (при вышивании через {lst[-2]} нит{'и' if lst[-2]=='2' else 'ь'} основы)"
        )

    empty_line = ""
    alsize_total = (
        float(alsize.get()) * 2
    )  # Seam allowanse dounled for calculating dimensions (allowance goes for both sides)

    # CASE 1: Checked radibuttons: know size in crosses, want size in cm
    if (r1_val.get() == 0) and (r2_val.get() == 1):
        stitches = (int(x_stitch.get()), int(y_stitch.get()))
        count = countlist2.get().split()

        if (
            len(count) > 2
        ):  # For cases when checkbox has value with brackets (counts from 25 to 56)
            ans = stitch_to_size(stitches, int(count[0]) / int(count[-2]))
            txt_add = long_line(count)
        else:  # For cases when checkbox has no brackets in value (counts from 6 to 24)
            ans = stitch_to_size(stitches, int(count[0]))
            txt_add = empty_line
        # For cases without or with seam allowance (based on checkbox)
        if check_var.get() == 0:
            answer = f"""Вышивка размером {stitches[0]} х {stitches[1]} крестиков занимает на ткани {count[0]} каунт{txt_add}:
В сантиметрах: {ans[0] * 2.54:.2f} х {ans[1] * 2.54:.2f} см.\
В дюймах: {ans[0]:.2f} х {ans[1]:.2f} дюймов."""
        elif check_var.get() == 1:
            answer = f"""Вышивка размером {stitches[0]} х {stitches[1]} крестиков занимает на ткани {count[0]} каунт{txt_add}:
В сантиметрах с припуском: {ans[0] * 2.54 + alsize_total:.2f} х {ans[1] * 2.54 + alsize_total:.2f} см.\
В дюймах с припуском: {ans[0] + (alsize_total / 2.54):.2f} х {ans[1] + (alsize_total / 2.54):.2f} дюймов."""

    # CASE 2: Checked radibuttons: know size in cm on count, want number of stitches
    elif (r1_val.get() == 1) and (r2_val.get() == 0):
        dimensions = (float(x_size.get()), float(y_size.get()))
        count = countlist1.get().split()
        if (
            len(count) > 2
        ):  # For cases when checkbox has value with brackets (counts from 25 to 56)
            ans = size_to_stitch(dimensions, int(count[0]) / int(count[-2]))
            txt_add = long_line(count)
        else:  # For cases when checkbox has no brackets in value (counts from 6 to 24)
            ans = size_to_stitch(dimensions, int(count[0]))
            txt_add = empty_line
        answer = f"""Вышивка размером {dimensions[0]} х {dimensions[1]} cм на ткани {count[0]} каунт{txt_add}:
состоит приблизительно из {ans[0]}x{ans[1]} крестиков."""

    # CASE 3: Checked radibuttons: know size in cm on count, want size in cm on another count
    elif (r1_val.get() == 1) and (r2_val.get() == 1):
        dimensions = (float(x_size.get()), float(y_size.get()))
        count_old = countlist1.get().split()
        count_new = countlist2.get().split()
        if (
            len(count_old) > 2
        ):  # For cases when checkbox of known count has value with brackets (counts from 25 to 56)
            pre = size_to_stitch(dimensions, int(count_old[0]) / int(count_old[-2]))
            txt_add_old = long_line(count_old)
        else:  # For cases when checkbox of known count has no brackets in value (counts from 6 to 24)
            pre = size_to_stitch(dimensions, int(count_old[0]))
            txt_add_old = empty_line
        if (
            len(count_new) > 2
        ):  # For cases when checkbox of wanted count has value with brackets (counts from 25 to 56)
            ans = stitch_to_size(pre, int(count_new[0]) / int(count_new[-2]))
            txt_add_new = long_line(count_new)
        else:
            ans = stitch_to_size(pre, int(count_new[0]))
            txt_add_new = empty_line
        # For cases without or with seam allowance (based on checkbox)
        if check_var.get() == 0:
            answer = f"""Вышивка размером {dimensions[0]} х {dimensions[1]} cм на ткани {count_old[0]} каунт{txt_add_old} занимает на ткани {count_new[0]} каунт{txt_add_new}:
В сантиметрах: {ans[0] * 2.54:.2f} х {ans[1] * 2.54:.2f} см.
В дюймах: {ans[0]:.2f} х {ans[1]:.2f} дюймов."""
        elif check_var.get() == 1:
            answer = f"""Вышивка размером {dimensions[0]} х {dimensions[1]} cм на ткани {count_old[0]} каунт{txt_add_old} занимает на ткани {count_new[0]} каунт{txt_add_new}:
В сантиметрах с припуском: {ans[0] * 2.54 + alsize_total:.2f} х {ans[1] * 2.54 + alsize_total:.2f} см.
В дюймах с припуском: {ans[0] + (alsize_total / 2.54):.2f} х {ans[1] + (alsize_total / 2.54):.2f} дюймов."""

    result.config(text=answer)


# Variable and function for entry fields validation (only integers available)
def validate_float(new_value):
    try:
        if new_value == "" or new_value == ".":
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
