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

Dis_min = 0.7452444949255465
Dis_max = 347.5282604374643
def nor_x(line):
    new_line = []
    new_line.append((line[0]-Ym_min) / (Ym_max - Ym_min))
    new_line.append((line[1]-Pr_min) / (Pr_max - Pr_min))
    new_line.append((line[2]-L_min) / (L_max - L_min))
    new_line.append((line[3]-W_min) / (W_max - W_min))
    new_line.append((line[4]-F1_min) / (F1_max - F1_min))
    new_line.append((line[5]-F2_min) / (F2_max - F2_min))
    new_line.append((line[6]-F3_min) / (F3_max - F3_min))
    new_line.append((line[7]-F4_min) / (F4_max - F4_min))
    return(new_line)

def nor_y(dis):
    new_dis = (dis - Dis_min) / (Dis_max - Dis_min)
    return(new_dis)

def un_nor_x(line):
    new_line = []
    new_line.append(Ym_min + (Ym_max - Ym_min) * line[0])
    new_line.append(Pr_min + (Pr_max - Pr_min) * line[1])
    new_line.append(L_min + (L_max - L_min) * line[2])
    new_line.append(W_min + (W_max - W_min) * line[3])
    new_line.append(F1_min + (F1_max - F1_min) * line[4])
    new_line.append(F2_min + (F2_max - F2_min) * line[5])
    new_line.append(F3_min + (F3_max - F3_min) * line[6])
    new_line.append(F4_min + (F4_max - F4_min) * line[7])
    return(new_line)

def un_nor_y(dis):
    new_dis = Dis_min + (Dis_max - Dis_min) * dis
    return(new_dis)

# line=[70000, 0.33, 9000, 1500, 1900000, 1933333, 2500000, 3500000]
# dis=390
#
# nor_line = nor_x(line)
# nor_dis = nor_y(dis)
# a = un_nor_x(nor_line)
# b = un_nor_y(nor_dis)
#
# print(nor_line,nor_dis,a,b)