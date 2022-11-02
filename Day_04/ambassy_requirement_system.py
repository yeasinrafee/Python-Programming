know_python = False
know_finnish = True

if know_python and know_finnish:
    print("You can go finland")
elif (not know_python) and (not know_finnish):
    print("You have to know python and finnish must")
elif know_python and (not know_finnish):
    print("You have to know finnish as well")
else:
    print("You have to learn python must")