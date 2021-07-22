subj_dict = {}
with open("academic_subjects.txt", "r", encoding="UTF-8") as subj_schedule:
    for line in subj_schedule:
        one_subj = line.split()
        subj = one_subj[0]
        subj_ind = subj.index(":")
        subj = subj[0:subj_ind]
        lect = one_subj[1]
        lect = lect.split("(")[0]
        pract = one_subj[2]
        pract = pract.split("(")[0]
        lab = one_subj[3]
        lab = lab.split("(")[0]
        try:
            lect = int(lect)
        except ValueError:
            lect = int(0)
        try:
            pract = int(pract)
        except ValueError:
            pract = int(0)
        try:
            lab = int(lab)
        except ValueError:
            lab = int(0)
        sum_hour = lect + pract + lab
        subj_dict.update({subj: sum_hour})
print(subj_dict)
