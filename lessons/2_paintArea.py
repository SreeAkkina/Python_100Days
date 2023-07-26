import math
def cans_needed(height, width, coverage):
    cans = math.ceil((height * width) / coverage)
    return cans

input_h = int(input("Enter the height of the wall >>> "))
input_w = int(input("Enter the width of the wall >>> "))
cover = 5
print(f"Number of cans needed >>> {cans_needed(height = input_h, width = input_w, coverage = cover)}")