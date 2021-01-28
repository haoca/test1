import sys
import weather
from PyQt5.QtWidgets import QApplication, QDialog
import requests
import json


class MainDialog(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = weather.Ui_Dialog()
        self.ui.setupUi(self)

    def queryWeather(self):
        # cityName = self.ui.comboBox.currentText()
        # cityCode = self.getCode(cityName)
        # url = 'http://hn216.api.yesapi.cn/?s=App.Common_Weather.LiveWeather&return_data=0&city=%E6%AD%A6%E6%B1%89&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=319DECDD0D63B8E1CD3B8AABD7F2CC71'
        # s = requests.session()

        # res1 = s.get(url).text
        r = requests.get(
            "http://hn216.api.yesapi.cn/?s=App.Common_Weather.LiveWeather&return_data=0&city=%E6%AD%A6%E6%B1%89&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=319DECDD0D63B8E1CD3B8AABD7F2CC71")
        abc = str(r.json())
        print(abc)
        weatherMsg = abc
        self.ui.textEdit.setText(weatherMsg)


'''  if r.json().get('status') == 200:     
     weatherMsg = '城市：{}\n日期：{}\n天气：{}\nPM 2.5：{} {}\n温度：{}\n湿度：{}\n风力：{}\n\n{}'.format(
                r.json()['cityInfo']['city'],
                r.json()['data']['forecast'][0]['ymd'],
                r.json()['data']['forecast'][0]['type'],
                int(r.json()['data']['pm25']),
                r.json()['data']['quality'],
                r.json()['data']['wendu'],
                r.json()['data']['shidu'],
                r.json()['data']['forecast'][0]['fl'],
                r.json()['data']['forecast'][0]['notice'],
            )
     else:                               
      weatherMsg = '天气查询失败，请稍后再试！'    

 '''

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainDialog()
    myDlg.show()
    sys.exit(myapp.exec_())
