"""def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name("SREE", "akkINa"))"""

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first Name? "), input("What is your last name? ")))