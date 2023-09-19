from pyDOE import *
from freeCAD.my_API import get_displacement_magnitude

Ym_min = 60000
Ym_max = 500000

Pr_min = 0.1
Pr_max = 0.45

L_min = 8000
L_max = 10000

W_min = 1000
W_max = 2000

F1_min = 1000000
F1_max = 10000000

F2_min = 1000000
F2_max = 5000000

F3_min = 1000000
F3_max = 10000000

F4_min = 1000000
F4_max = 5000000

samples = lhs(8, 2000)

with open("testdata_2000.csv", "w") as f:
    f.write("Ym, Pr, L, W, F1, F2, F3, F4, Displacement\n")
    count = 0
    for sample in samples:
        samp_ym = Ym_min + (Ym_max - Ym_min) * sample[0]
        samp_pr = Pr_min + (Pr_max - Pr_min) * sample[1]
        samp_l = L_min + (L_max - L_min) * sample[2]
        samp_w = W_min + (W_max - W_min) * sample[3]
        samp_f1 = F1_min + (F1_max - F1_min) * sample[4]
        samp_f2 = F2_min + (F2_max - F2_min) * sample[5]
        samp_f3 = F3_min + (F3_max - F3_min) * sample[6]
        samp_f4 = F4_min + (F4_max - F4_min) * sample[7]

        samp_displacement = get_displacement_magnitude(samp_l, samp_w, samp_f1, samp_f2, samp_f3, samp_f4, f"{samp_ym} MPa", str(samp_pr))
        f.write(str(samp_ym) + "," + str(samp_pr) + "," + str(samp_l) + "," + str(samp_w) + "," + str(samp_f1) + "," + str(samp_f2) + "," + str(samp_f3) + "," + str(samp_f4) + "," + str(samp_displacement) + "\n")
        count = count +1
        print(count)