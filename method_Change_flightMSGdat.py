import pickle


class changeFile():
    def changeFile(__name__):
        file = open("flightMSG.dat", "wb")
        file_temp = open("flightMSG_temp.dat", "rb")
        Dir_temp = pickle.load(file_temp)
        pickle.dump(Dir_temp, file)
        file.close()
        file_temp.close()