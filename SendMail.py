from email.mime.text import MIMEText
import smtplib


class Mail():
    def Mail(__name__, mailMSG):
        msg = MIMEText(mailMSG)
        msg["Subject"] = "航班查询邮件"
        # 寄件者
        msg["From"] = '航班查询'
        # 收件者
        msg["To"] = ''

        from_addr = '' # 发送邮箱
        password = ''  # 邮箱的密码或者授权码
        # smtp服务器地址
        smtp_server = ''  # 邮箱服务器
        # 收件人地址
        to_addr_list = ['']  # 收件人列表，可以填写多个

        for to_addr in to_addr_list:
            try:
                # smtp协议的默认端口是25，QQ邮箱smtp服务器端口是465,第一个参数是smtp服务器地址，第二个参数是端口，第三个参数是超时设置,这里必须使用ssl证书，要不链接不上服务器
                server = smtplib.SMTP_SSL(smtp_server, 465, timeout=2)
                # 登录邮箱
                server.login(from_addr, password)
                # 发送邮件，第一个参数是发送方地址，第二个参数是接收方列表，列表中可以有多个接收方地址，表示发送给多个邮箱，msg.as_string()将MIMEText对象转化成文本
                server.sendmail(from_addr, [to_addr], msg.as_string())
                server.quit()
                print('success')
            except (Exception):
                print('Faild')
