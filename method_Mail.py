import FlightClass
import pickle
from email.mime.text import MIMEText
import smtplib


class Mail():
    def writeMail(__name__, Add, Delete, Change, FlightDict):
        file = open("Mail.txt", "a")
        Flight = FlightClass.Flight()
        if len(Add) != 0:
            file.write(
                "=======================================Add=======================================\n"
            )
            file.close()
            for each in Add:
                Flight = FlightDict.setdefault(each)
                Flight.writeSendMail()
            file = open("Mail.txt", "a")
            file.write(
                "=================================================================================\n"
            )
            file.close()
        else:
            file = open("Mail.txt", "a")
            file.write("No Add.\n")
            file.close()

        if len(Delete) != 0:
            file = open("Mail.txt", "a")
            file.write(
                "======================================Delete=====================================\n"
            )
            file.close()
            file_old = open("flightMSG.dat", "rb")
            FlightDict_old = pickle.load(file_old)
            file_old.close()
            for each in Delete:
                Flight = FlightDict_old.setdefault(each)
                Flight.writeSendMail()
            file = open("Mail.txt", "a")
            file.write(
                "=================================================================================\n"
            )
            file.close()
        else:
            file = open("Mail.txt", "a")
            file.write("No Delete.\n")
            file.close()

        if len(Change) != 0:
            file = open("Mail.txt", "a")
            file.write(
                "======================================Change=====================================\n"
            )
            file.close()
            for each in Change:
                Flight = FlightDict.setdefault(each)
                Flight.writeSendMail()
            file = open("Mail.txt", "a")
            file.write(
                "=================================================================================\n"
            )
            file.close()
        else:
            file = open("Mail.txt", "a")
            file.write("No Change.\n")
            file.close()

    def SendMail(__name__, judgeList):
        if 1 in judgeList:
            file = open("Mail.txt", "r")
            mailMSG = file.read()
            file.close()
            msg = MIMEText(mailMSG)
            msg["Subject"] = "航班查询邮件"
            # 寄件者
            msg["From"] = '航班查询'
            # 收件者
            msg["To"] = '739386753@qq.com'

            from_addr = '739386753@qq.com'
            password = 'aonwonrchkusbcgg'
            # smtp服务器地址
            smtp_server = 'smtp.qq.com'
            # 收件人地址
            to_addr_list = ['739386753@qq.com']

            for to_addr in to_addr_list:
                try:
                    # smtp协议的默认端口是25，QQ邮箱smtp服务器端口是465,第一个参数是smtp服务器地址，第二个参数是端口，第三个参数是超时设置,这里必须使用ssl证书，要不链接不上服务器
                    server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)
                    # 登录邮箱
                    server.login(from_addr, password)
                    # 发送邮件，第一个参数是发送方地址，第二个参数是接收方列表，列表中可以有多个接收方地址，表示发送给多个邮箱，msg.as_string()将MIMEText对象转化成文本
                    server.sendmail(from_addr, [to_addr], msg.as_string())
                    server.quit()
                    print("================================")
                    print("|    Success to send a mail.   |")
                    print("================================")
                except (Exception):
                    print("================================")
                    print("|       Send mail error!       |")
                    print("================================")
        else:
            print("================================")
            print("| No change, didn't send mail. |")
            print("================================")

            # ==================
            # ==================
            # ==================
            # ==================
