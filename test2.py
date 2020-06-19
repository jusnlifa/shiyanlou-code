import pywifi
from pywifi import const # 引入一个常量
import time

#获取wifi列表
AKNS = {
	0:'AKM_TYPE_NONE',
	1:'AKM_TYPE_WPA',
	2:'AKM_TYPE_WPAPSK',
	3:'AKM_TYPE_WPA2',
	4:'AKM_TYPE_WPA2PSK',
	5:'AKM_TYPE_UNKNOWN'
}


wifi=pywifi.PyWiFi()
iface = wifi.interfaces()[0]
wifilist = iface.scan_results()
for data in wifilist:
	print(data.ssid)
	print(AKNS[data.akm[0]])
