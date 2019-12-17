class judgeTime():
    def judgeTime(__name__, time):
        temp = time.split("-")
        # print(temp)
        # print(len(temp))
        if len(temp) == 3:
            if temp[0].isnumeric() and temp[0].isnumeric(
            ) and temp[0].isnumeric():
                if 1945 < int(temp[0]) and 0 < int(temp[1]) <= 12 and 0 < int(
                        temp[2]) <= 31:
                    return 0
                else:
                    return -3
            else:
                return -2
        else:
            return -1
