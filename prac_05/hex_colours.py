

HEX_COLOUR = {"absolutezero": "0048ba", "acidgreen": "b0bf1a", "aliceblue": "f0f8ff", "alizarincrimson": "e32636",
                "amaranth": "e52b50", "amber": "ffbf00", "amethyst": "9966cc", "antiquewhite": "faebd7"}
# print(HEX_COLOUR)
try:
    hex_name = input("Colour name: ").lower()
except KeyError:
    print("Enter valid colour name")
    hex_name = input("Colour name: ").lower()
while hex_name != "":
    if hex_name in HEX_COLOUR:
        print(hex_name, "is", HEX_COLOUR[hex_name])
    else:
        print("Invalid colour")
    hex_name = input("Colour name: ")
# for key, value in HEX_COLOUR.items():
#     print(f"{key:5}: {value:3}")
