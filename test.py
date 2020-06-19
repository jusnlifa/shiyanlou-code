import pywifi
from pywifi import const # 引入一个常量
import time

#连接wifi

wifiname='-a22bdd'
wifipassword='26293024'
wifi = pywifi.PyWiFi()
ifaces = wifi.interfaces()[0]
ifaces.disconnect()# 断开连接
time.sleep(1)#0.5秒
print('开始执行')
if ifaces.status() == const.IFACE_DISCONNECTED:
    profile = pywifi.Profile()# 创建WiFi连接文件
    profile.ssid = wifiname# WiFi的ssid，即wifi的名称
    profile.key = wifipassword# WiFi密码
    profile.akm.append(const.AKM_TYPE_WPA2PSK)# WiFi的加密类型，现在一般的wifi都是wpa2psk
    profile.auth = const.AUTH_ALG_OPEN # 开放网卡
    profile.cipher = const.CIPHER_TYPE_CCMP# 加密单元
    ifaces.remove_all_network_profiles()# 删除所有的WiFi文件
    tep_profile = ifaces.add_network_profile(profile)# 设定新的连接文件
    ifaces.connect(tep_profile) # 连接WiFi
    time.sleep(2)#1.5秒
    if ifaces.status() == const.IFACE_CONNECTED:
        print("破解成功")
    else:
        print("破解失败")
else:
    print("莫名奇怪")