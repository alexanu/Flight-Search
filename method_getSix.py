import method_getSix


class getSix():
    def get_flight(__name__, legs_dict):
        flight = legs_dict.setdefault("flight")  # 航班信息（航班编号，机型，公司）//字典
        return flight

    def getFlightMSG(__name__, flight, flightMsg):
        flightNumber = flight.setdefault("flightNumber")  # 航班编号
        airlineName = flight.setdefault("airlineName")  # 航班公司
        craftTypeName = flight.setdefault("craftTypeName")  # 飞机型号
        flightMsg["航班编号"] = flightNumber
        flightMsg["航空公司"] = airlineName
        flightMsg["飞机型号"] = craftTypeName

    def get_departureAirportInfo(__name__, flight):
        departureAirportInfo = flight.setdefault(
            "departureAirportInfo")  # 起飞机场、城市//字典
        return departureAirportInfo

    def getDepartureAirportInfoMsg(__name__, departureAirportInfo,
                                   departureAirportInfoMSG):
        BcityName = departureAirportInfo.setdefault("cityName")  # 起飞城市
        BairportName = departureAirportInfo.setdefault("airportName")  # 起飞机场
        # ====  是不是候机楼？？？
        Bterminal = departureAirportInfo.setdefault("terminal")  # dir
        Bname = Bterminal.setdefault("name")
        BshortName = Bterminal.setdefault("shortName")

        departureAirportInfoMSG["起飞城市"] = BcityName
        departureAirportInfoMSG["起飞机场"] = BairportName
        departureAirportInfoMSG["Begin Terminal name"] = Bname
        departureAirportInfoMSG["Begin Terminal short-name"] = BshortName

    def get_arrivalAirportInfo(__name__, flight):
        arrivalAirportInfo = flight.setdefault(
            "arrivalAirportInfo")  # 到达机场、城市//字典
        return arrivalAirportInfo

    def getArrivalAirportInfoMSG(__name__, arrivalAirportInfo,
                                 arrivalAirportInfoMSG):
        EcityName = arrivalAirportInfo.setdefault("cityName")  # 到达城市
        EairportName = arrivalAirportInfo.setdefault("airportName")  # 到达机场
        # ====  是不是到达机场楼？？？
        Eterminal = arrivalAirportInfo.setdefault("terminal")
        Ename = Eterminal.setdefault("name")
        EshortName = Eterminal.setdefault("shortName")

        arrivalAirportInfoMSG["到达城市"] = EcityName
        arrivalAirportInfoMSG["到达机场"] = EairportName
        arrivalAirportInfoMSG["Arrive Terminal name"] = Ename
        arrivalAirportInfoMSG["Arrive Terminal short-name"] = EshortName

    def getTime(__name__, flight, timeMSG):
        departureDate = flight.setdefault("departureDate")  # 起飞时间
        arrivalDate = flight.setdefault("arrivalDate")  # 到达时间
        punctualityRate = flight.setdefault("punctualityRate")  # 守时率
        stopTimes = flight.setdefault("stopTimes")
        stopInfo = flight.setdefault("stopInfo")

        timeMSG["起飞时间"] = departureDate
        timeMSG["到达时间"] = arrivalDate
        timeMSG["守时率"] = punctualityRate
        timeMSG["stopTimes"] = str(stopTimes)
        timeMSG["stopInfo"] = str(stopInfo)

    def get_cabins(__name__, legs_dict):
        cabins = legs_dict.setdefault("cabins")  # 仓位！！！！//价格在这里 list
        return cabins

    def getPriceMSG(__name__, cabins, priceMSG):
        temp_flightPrice = []
        for each_cabin in cabins:
            cabinClass = str(each_cabin.setdefault("cabinClass"))
            priceClass = str(each_cabin.setdefault("priceClass"))
            classAreaCode = str(each_cabin.setdefault("classAreaCode"))
            seatCount = str(each_cabin.setdefault("seatCount"))
            tempPriceBlock = each_cabin.setdefault("price")
            price = str(tempPriceBlock.setdefault("price"))

            temp_flightPrice.append(cabinClass)
            temp_flightPrice.append(priceClass)
            temp_flightPrice.append(classAreaCode)
            temp_flightPrice.append(seatCount)
            temp_flightPrice.append(price)
            priceMSG.append(temp_flightPrice)
            temp_flightPrice = []

    def getSix(__name__, legs_dict, flightMSG, departureAirportInfoMSG,
               arrivalAirportInfoMSG, timeMSG, priceMSG):
        Method = method_getSix.getSix()
        flight = Method.get_flight(legs_dict)
        Method.getFlightMSG(flight, flightMSG)
        departureAirportInfo = Method.get_arrivalAirportInfo(flight)
        Method.getDepartureAirportInfoMsg(departureAirportInfo,
                                          departureAirportInfoMSG)
        arrivalAirportInfo = Method.get_arrivalAirportInfo(flight)
        Method.getArrivalAirportInfoMSG(arrivalAirportInfo,
                                        arrivalAirportInfoMSG)
        Method.getTime(flight, timeMSG)
        cabins = Method.get_cabins(legs_dict)
        Method.getPriceMSG(cabins, priceMSG)
