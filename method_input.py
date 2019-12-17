import method_judgeTime


class Input():
    def inputSleepTime(__name__):
        while (1):
            sleep_time = input(
                "[input]Please input sleep time(s)[suggest:1200]:")
            if sleep_time.isnumeric:
                return sleep_time
            else:
                print("Please input a number!!")

    def inputCityName(__name__):
        cityName = input("[input]Please input city-name[中文]:")
        return cityName

    def inputTime(__name__):
        Judge = method_judgeTime.judgeTime()

        while (1):
            time = input("[input]Please input departure-time[xxxx-xx-xx]")
            judgeNum = Judge.judgeTime(time)

            if judgeNum == 0:
                return time
            elif judgeNum == -1:
                print("Error! You're not input number!!")
            elif judgeNum == -2:
                print("Error! It's not [xxxx-xx-xx]!!")
            elif judgeNum == -3:
                print("Error! Please check the number!!")
