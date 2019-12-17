import pickle
import filecmp
import checkEachDcit


class check():
    def check_flightMSG_dat(__name__):
        return filecmp.cmp("flightMSG.dat", "flightMSG_temp.dat")

    def check(__name__, Add, Delete, Change):
        Method = checkEachDcit.check()
        if Method.check_flightMSG_dat():
            pass
        else:
            file = open("flightMSG.dat", "rb")
            file_temp = open("flightMSG_temp.dat", "rb")
            Dict = pickle.load(file)
            Dict_temp = pickle.load(file_temp)

            file.close()
            file_temp.close()

            List = list(Dict)
            List_temp = list(Dict_temp)

            judgeList = [0, 0, 0]
            for each in List_temp:
                if each not in List:
                    Add.append(each)
                    judgeList[0] = 1
            for each in List:
                if each not in List_temp:
                    Delete.append(each)
                    judgeList[1] = 1

            for each in List:
                if each in List_temp:
                    file_c1 = open("check1.dat", "wb")
                    file_c2 = open("check2.dat", "wb")

                    pickle.dump(Dict.setdefault(each), file_c1)
                    pickle.dump(Dict_temp.setdefault(each), file_c2)

                    file_c1.close()
                    file_c2.close()

                    if filecmp.cmp("check1.dat", "check2.dat"):
                        pass
                    else:
                        Change.append(each)
                        judgeList[2] = 1
            """ file = open("flightMSG.dat", "wb")
            file_temp = open("flightMSG_temp.dat", "rb")
            Dir_temp = pickle.load(file_temp)
            pickle.dump(Dir_temp, file)
            file.close()
            file_temp.close() """

            return judgeList
