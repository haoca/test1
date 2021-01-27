# coding:utf-8

import sys
import wea
from PyQt5.QtWidgets import QApplication, QDialog
import requests
import json


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = wea.Ui_Dialog()
        self.ui.setupUi(self)

    def queryWeather(self):
        cityName = self.ui.comboBox.currentText()
        cityCode = self.getCode(cityName)

        # r = requests.get(
        #     "http://t.weather.sojson.com/api/weather/city/{}".format(cityCode))
        url = 'http://hn216.api.yesapi.cn/?s=App.Open_Baidu.LocationIP&return_data=0&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=E70E38BAB6CFE7B9C9C2D3299BDD5135'

        s = requests.session()
        # node = (node=uuid.getnode())
        # mac = str(uuid.UUID(int=node).hex[-12:])
        r = s.get(url)
        print(r.json())
        print(r.status_code)
        if r.status_code == 200:
            res1 = s.get(url).text
            weatherMsg = res1

            # weatherMsg = json.loads(res1)['data']
            # weatherMsg = '城市：{}\n日期：{}\n天气：{}\nPM 2.5：{} {}\n温度：{}\n湿度：{}\n风力：{}\n\n{}'.format(
            #     r.json()['cityInfo']['city'],
            #     r.json()['data']['forecast'][0]['ymd'],
            #     r.json()['data']['forecast'][0]['type'],
            #     int(r.json()['data']['pm25']),
            #     r.json()['data']['quality'],
            #     r.json()['data']['wendu'],
            #     r.json()['data']['shidu'],
            #     r.json()['data']['forecast'][0]['fl'],
            #     r.json()['data']['forecast'][0]['notice'],
            # )
        else:
            weatherMsg = '天气查询失败，请稍后再试！'

        self.ui.textEdit.setText(weatherMsg)

    def getCode(self, cityName):
        cityDict = {"北京": "101010100",
                    "上海": "101020100",
                    "天津": "101030100"}

        return cityDict.get(cityName, '101010100')

    def clearText(self):
        self.ui.textEdit.clear()


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
