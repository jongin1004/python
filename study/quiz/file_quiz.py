for i in range(1, 6):
    text = "- {} 주차 중간보고 -".format(i)
    text += "\n부서 : "
    text += "\n이름 : "
    text += "\n업무 요약 : "

    with open("{}주차.txt".format(i), "w", encoding="utf8") as report_file:
        report_file.write(text)
