import base64
import sys
import login_rc
from PyQt5.QtWidgets import QApplication, QDialog
import requests
def isConnected():
    try:
        html = requests.get("http://www.baidu.com", timeout=2)
        html = str(html.content)
        flag = html.find('www.hao123.com')
        # print(html, flag, '\n1')
        if flag >= 0:
            return 1
        else:
            return 0
    except:
        return False


def get_mac_address():
    '''
    @summary: return the MAC address of the computer
    '''
    import sys
    import os
    mac = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            # print(line)
            if line.lstrip().startswith("Physical Address"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if 'Ether' in line:
                mac = line.split()[4]
                break
    return mac


def jiami(password1):

    # 想将字符串转编码成base64,要先将字符串转换成二进制数据
    y_password = password1
    bytes_url = y_password.encode("utf-8")
    h_password = base64.b64encode(bytes_url)
    h_password = r'{B}'+str(h_password)[2:-1]  # 被编码的参数必须是二进制数据
    print('base64加密后:'+h_password)
    return h_password




class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = login_rc.Ui_Dialog()
        self.ui.setupUi(self)

    def connect(self):
        username = '301737'
        password1 = 'a13307023186'  # 更改为自己对应的卡号，密码。

        print('校园卡号' + username, '\n校园网密码' + password1)

        s = requests.session()

        res1 = s.post(
            url=r"http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
            headers={
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN",
                "Cache-Control": "no-cache",
                "Connection": "Keep-Alive",
                "Content-Length": "109",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Cookie": r"login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; NSC_tsvo_4l_TH=ffffffffaf160e3b45525d5f4f58455e445a4a423660",
                "Host": "172.30.16.34",
                "Referer": "http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
                "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)",
            },
            data={
                "ac_id": "64",
                "action": "login",
                "ajax": "1",
                "nas_ip": '',

                "password": password1,
                "save_me": "1",
                "user_ip": '',


                "username": username,
            },

        )
        # res1=res1[content]
        # abc = str(res1.json())
        abc=type(res1)
        print(abc)
        weatherMsg =abc
        self.ui.textEdit.setText('校园卡号' + username+'\n校园网密码' + password1+'\n'+weatherMsg)

    # def queryWeather(self):
    #     # cityName = self.ui.comboBox.currentText()
    #     # cityCode = self.getCode(cityName)
    #     # url = 'http://hn216.api.yesapi.cn/?s=App.Common_Weather.LiveWeather&return_data=0&city=%E6%AD%A6%E6%B1%89&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=319DECDD0D63B8E1CD3B8AABD7F2CC71'
    #     # s = requests.session()
    #
    #     # res1 = s.get(url).text
    #     r = requests.get("http://hn216.api.yesapi.cn/?s=App.Common_Weather.LiveWeather&return_data=0&city=%E6%AD%A6%E6%B1%89&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=319DECDD0D63B8E1CD3B8AABD7F2CC71")
    #     abc=str(r.json())
    #     print(abc)
    #     weatherMsg =abc
    #     self.ui.textEdit.setText(weatherMsg)


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
