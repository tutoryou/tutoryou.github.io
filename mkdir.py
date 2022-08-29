import os
a = [1511 , 1521 , 1531 , 2511 , 2521 , 3311 , 3121 , 3331, 2041]
b = [6080 , 6771 , 9021 , 9024 , 9101 , 9311 , 9313 , 9331 , 9418 , 9444 , 9517, 9044, 9814]
under_graduated = set(a)
post_graduated = set(b)
# comp_under_graduated = ["COMP" + str(i) for i in under_graduated]
# comp_post_graduated = ["COMP" + str(i) for i in post_graduated]
# print("Under Graduated Courses: " + str(comp_under_graduated))
# print("Post Graduated Courses: " + str(comp_post_graduated))
for i in under_graduated:
    # os.mkdir("COMP" + str(i))
    os.mkdir("COMP" + str(i) + "/lab")
    os.mkdir("COMP" + str(i) + "/test")
    os.mkdir("COMP" + str(i) + "/final")
    os.mkdir("COMP" + str(i) + "/quiz")
    os.mkdir("COMP" + str(i) + "/tutorial")
    os.mkdir("COMP" + str(i) + "/assignment")
    with open("COMP" + str(i) + "/README.md", "w") as f:
        f.write("# COMP" + str(i))
for i in post_graduated:
    os.mkdir("COMP" + str(i) + "/lab")
    os.mkdir("COMP" + str(i) + "/test")
    os.mkdir("COMP" + str(i) + "/final")
    os.mkdir("COMP" + str(i) + "/quiz")
    os.mkdir("COMP" + str(i) + "/tutorial")
    os.mkdir("COMP" + str(i) + "/assignment")
    with open("COMP" + str(i) + "/README.md", "w") as f:
        f.write("# COMP" + str(i))