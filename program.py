print """Welcome to the Leaving Certificate Examination Point Converter Program 2018.
This is based on the point system introduced in the year 2017 by the CAO.
Please use your best 6 results.
If Mathematics is not one of your better subjects, 
please insert N/A into the Mathematics grade section,
if it is, insert N/A into one of the last slots.
Same applies for Irish. There are 8 slots in total.
Good Luck!!!

Developer: Conor Casey
v1.0
"""

def main():
    print """Program running..."""

    # Mathematics Grading System
    # Higher Level
    def mathematics(math_grade):
        if math_grade == "H1":
            return 125
        elif math_grade == "H2":
            return 113
        elif math_grade == "H3":
            return 102
        elif math_grade == "H4":
            return 91
        elif math_grade == "H5":
            return 81
        elif math_grade == "H6":
            return 71
        elif math_grade == "H7":
            return 33
    # Ordinary Level
        elif math_grade == "O1":
            return 56
        elif math_grade == "O2":
            return 46
        elif math_grade == "O3":
            return 37
        elif math_grade == "O4":
            return 28
        elif math_grade == "O5":
            return 20
        elif math_grade == "O6":
            return 13
    # Foundation Level
        elif math_grade == "F1":
            return 20
        elif math_grade == "F2":
            return 12       
    # Other Grades
        else:
            return 0

    # Irish Grading System
    # Higher Level
    def irish(irish_grade):
        if irish_grade == "H1":
            return 100
        elif irish_grade == "H2":
            return 88
        elif irish_grade == "H3":
            return 77
        elif irish_grade == "H4":
            return 66
        elif irish_grade == "H5":
            return 56
        elif irish_grade == "H6":
            return 46
        elif irish_grade == "H7":
            return 33
    # Ordinary Level
        elif irish_grade == "O1":
            return 56
        elif irish_grade == "O2":
            return 46
        elif irish_grade == "O3":
            return 37
        elif irish_grade == "O4":
            return 28
        elif irish_grade == "O5":
            return 20
        elif irish_grade == "O6":
            return 13
    # Foundation Level
        elif irish_grade == "F1":
            return 20
        elif irish_grade == "F2":
            return 12       
    # Other Grades
        else:
            return 0

    # Grading System for All Other Subjects
    # Higher Level
    def subjects(subject_grade):
        if subject_grade == "H1":
            return 100
        elif subject_grade == "H2":
            return 88
        elif subject_grade == "H3":
            return 77
        elif subject_grade == "H4":
            return 66
        elif subject_grade == "H5":
            return 56
        elif subject_grade == "H6":
            return 46
        elif subject_grade == "H7":
            return 33
        # Ordinary Level
        elif subject_grade == "O1":
            return 56
        elif subject_grade == "O2":
            return 46
        elif subject_grade == "O3":
            return 37
        elif subject_grade == "O4":
            return 28
        elif subject_grade == "O5":
            return 20
        elif subject_grade == "O6":
            return 13
        else:
            return 0

    # Mathematics
    mathematics_grade = raw_input("Please Insert Mathematics Grade:").upper()
    points_for_math = mathematics(mathematics_grade)

    # Irish
    gaeilge_grade = raw_input("Please Insert Irish Grade:").upper()
    points_for_irish = irish(gaeilge_grade)

    # Subject 3
    subject_3 = raw_input("Please Insert A Third Subject:")
    subject_3_grade = raw_input("Please Insert Grade:").upper()
    points_for_subject_3 = subjects(subject_3_grade)

    # Subject 4
    subject_4 = raw_input("Please Insert A Fourth Subject:")
    subject_4_grade = raw_input("Please Insert Grade:").upper()
    points_for_subject_4 = subjects(subject_4_grade)

    # Subject 5
    subject_5 = raw_input("Please Insert A Fifth Subject:")
    subject_5_grade = raw_input("Please Insert Grade:").upper()
    points_for_subject_5 = subjects(subject_5_grade)

    # Subject 6
    subject_6 = raw_input("Please Insert A Sixth Subject:")
    subject_6_grade = raw_input("Please Insert Grade:").upper()
    points_for_subject_6 = subjects(subject_6_grade)

    # Subject 7
    subject_7 = raw_input("Please Insert A Seventh Subject:")
    subject_7_grade = raw_input("Please Insert Grade:").upper()
    points_for_subject_7 = subjects(subject_7_grade)

    # Subject 8
    subject_8 = raw_input("Please Insert A Eigth Subject:")
    subject_8_grade = raw_input("Please Insert Grade:").upper()
    points_for_subject_8 = subjects(subject_8_grade)

    # Final Total
    print """
Mathematics = """ + str(points_for_math)
    print "Irish = " + str(points_for_irish)
    print subject_3 + " = " + str(points_for_subject_3)
    print subject_4 + " = " + str(points_for_subject_4)
    print subject_5 + " = " + str(points_for_subject_5)
    print subject_6 + " = " + str(points_for_subject_6)
    print subject_7 + " = " + str(points_for_subject_7)
    print subject_8 + " = " + str(points_for_subject_8)


    point_total = points_for_math + points_for_irish + points_for_subject_3 + points_for_subject_4 + points_for_subject_5 + points_for_subject_6 + points_for_subject_7 + points_for_subject_8


    print """Congradulations, you got """ + str(point_total) + """ points. The hard work paid off!"""

    # End of Program
    print """
Thank You for using this Leaving Certificate Examination Point Converter Program 2018"""

    restart = raw_input("Do You Want to Restart the Program:").lower()
    if restart == "yes":
        main()
    else:
        quit()

main()
