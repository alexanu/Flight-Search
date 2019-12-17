import FlightClass
import pickle


class printMSG():
    def printStatusCode(__name__, judgeList):
        print("==============Judge Code==============")
        print("|{:^36}|".format(str(judgeList)))
        print("======================================\n")

    def printAroundTime(__name__, aroundTime):
        print("==============Around Time=============")
        print("|{:^36}|".format(str(aroundTime)))
        print("======================================\n")

    def printAddMSG(__name__, Add, FlightDict):
        Flight = FlightClass.Flight()
        if len(Add) != 0:
            print(
                "=======================================Add======================================="
            )
            for each in Add:
                Flight = FlightDict.setdefault(each)
                Flight.printFlightMSG()
            print(
                "================================================================================="
            )
        else:
            print("No Add.")

    def printDeleteMSG(__name__, Delete):
        Flight = FlightClass.Flight()
        if len(Delete) != 0:
            file = open("flightMSG.dat", "rb")
            FlightDict = pickle.load(file)
            file.close()
            print(
                "======================================Delete====================================="
            )
            for each in Delete:
                Flight = FlightDict.setdefault(each)
                print(FlightDict.setdefault(each))
                Flight.printFlightMSG()
            print(
                "================================================================================="
            )
        else:
            print("No Delete.")

    def printChangeMSG(__name__, Change, FlightDict):
        Flight = FlightClass.Flight()
        if len(Change) != 0:
            print(
                "======================================Change====================================="
            )
            for each in Change:
                Flight = FlightDict.setdefault(each)
                Flight.printFlightMSG()
            print(
                "================================================================================="
            )
        else:
            print("No Change.")

    def printFlightMSG(__name__, FlightDict):
        Flight = FlightClass.Flight()
        flightList = list(FlightDict)
        for each in flightList:
            Flight = FlightDict.setdefault(each)
            Flight.printFlightMSG()
