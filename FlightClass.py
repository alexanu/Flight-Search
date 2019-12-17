import Code


class Flight():
    FlightNumber = None
    AirlineName = None
    CraftTypeName = None
    Bcity = None
    Bairport = None
    BTN = None  # Begin-Terminal-name
    BTSN = None  # Begin-Terminal-short-name
    Acity = None
    Aairport = None
    ATN = None  # Arrive-Terminal-name
    ATSN = None  # Arrive-Terminal-short-name
    BTime = None
    ATime = None
    stopTime = None
    stopInfo = None
    Price = None

    def inputMSG(__name__, flightMSG, departureAirportInfoMSG,
                 arrivalAirportInfoMSG, timeMSG, priceMSG):
        __name__.FlightNumber = flightMSG.setdefault("航班编号")
        __name__.AirlineName = flightMSG.setdefault("航空公司")
        __name__.CraftTypeName = flightMSG.setdefault("飞机型号")

        __name__.Bcity = departureAirportInfoMSG.setdefault("起飞城市")
        __name__.Bairport = departureAirportInfoMSG.setdefault("起飞机场")
        __name__.BTN = departureAirportInfoMSG.setdefault(
            "Begin Terminal name")
        __name__.BTSN = departureAirportInfoMSG.setdefault(
            "Begin Terminal short-name")

        __name__.Acity = arrivalAirportInfoMSG.setdefault("到达城市")
        __name__.Aairport = arrivalAirportInfoMSG.setdefault("到达机场")
        __name__.ATN = arrivalAirportInfoMSG.setdefault("Arrive Terminal name")
        __name__.ATSN = arrivalAirportInfoMSG.setdefault(
            "Arrive Terminal short-name")

        __name__.BTime = timeMSG.setdefault("起飞时间")
        __name__.ATime = timeMSG.setdefault("到达时间")
        __name__.stopTime = timeMSG.setdefault("stopTime")
        __name__.stopInfo = timeMSG.setdefault("stopInfo")

        __name__.Price = priceMSG  # 字典组成的列表

    def printFlightMSG(__name__):
        print("================================================")
        print("|               Flight Message                 |")
        print("================================================\n")

        print("航班编号：" + str(__name__.FlightNumber))
        print("航空公司：" + str(__name__.AirlineName))
        print("飞机型号：" + str(__name__.CraftTypeName))

        print("起飞城市：" + str(__name__.Bcity))
        print("起飞机场：" + str(__name__.Bairport))
        print("Begin Terminal name：" + str(__name__.BTN))
        print("Begin Terminal short-name：" + str(__name__.BTSN))

        print("到达城市：" + str(__name__.Acity))
        print("到达机场：" + str(__name__.Aairport))
        print("Arrive Terminal name：" + str(__name__.ATN))
        print("Arrive Terminal short-name：" + str(__name__.ATSN))

        print("起飞时间：" + str(__name__.BTime))
        print("到达时间：" + str(__name__.ATime))
        print("stopTimes：" + str(__name__.stopTime))
        print("stopInfo：" + str(__name__.stopInfo))

        code_method = Code.Code()
        code = code_method.cabinCode()
        print("\n============PRICE============")
        for each_cabinPrice in __name__.Price:
            print(
                str(code.setdefault(each_cabinPrice[1])) + "\n" +
                str(each_cabinPrice[0]) + str(each_cabinPrice[1]) +
                str(each_cabinPrice[2]) + ":",
                str(each_cabinPrice[3]) + ":", str(each_cabinPrice[4]))
            print("-----------------------------")
        print("\n\n")

    def writeSendMail(__name__):
        file_SendMail = open("Mail.txt", "a")
        file_SendMail.write(
            "================================================\n")
        file_SendMail.write(
            "|               Flight Message                 |\n")
        file_SendMail.write(
            "================================================\n\n")

        file_SendMail.write("航班编号：" + str(__name__.FlightNumber) + "\n")
        file_SendMail.write("航空公司：" + str(__name__.AirlineName) + "\n")
        file_SendMail.write("飞机型号：" + str(__name__.CraftTypeName) + "\n")

        file_SendMail.write("起飞城市：" + str(__name__.Bcity) + "\n")
        file_SendMail.write("起飞机场：" + str(__name__.Bairport) + "\n")
        file_SendMail.write("Begin Terminal name：" + str(__name__.BTN) + "\n")
        file_SendMail.write("Begin Terminal short-name：" + str(__name__.BTSN) +
                            "\n")

        file_SendMail.write("到达城市：" + str(__name__.Acity) + "\n")
        file_SendMail.write("到达机场：" + str(__name__.Aairport) + "\n")
        file_SendMail.write("Arrive Terminal name：" + str(__name__.ATN) + "\n")
        file_SendMail.write("Arrive Terminal short-name：" +
                            str(__name__.ATSN) + "\n")

        file_SendMail.write("起飞时间：" + str(__name__.BTime) + "\n")
        file_SendMail.write("到达时间：" + str(__name__.ATime) + "\n")
        file_SendMail.write("stopTimes：" + str(__name__.stopTime) + "\n")
        file_SendMail.write("stopInfo：" + str(__name__.stopInfo) + "\n")

        code_method = Code.Code()
        code = code_method.cabinCode()
        file_SendMail.write("\n============PRICE============" + "\n")
        for each_cabinPrice in __name__.Price:
            file_SendMail.write(
                str(code.setdefault(each_cabinPrice[1])) + "\n" +
                str(each_cabinPrice[0]) + str(each_cabinPrice[1]) +
                str(each_cabinPrice[2]) + ": " + str(each_cabinPrice[3]) +
                ": " + str(each_cabinPrice[4]) + "\n")
            file_SendMail.write("-----------------------------" + "\n")
        file_SendMail.write("\n\n" + "\n")
        file_SendMail.close()

    def JudgePrint(__name__, Time, Price):
        pass
