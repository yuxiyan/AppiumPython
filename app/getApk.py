# -*- coding:utf-8 -*-
import requests
import os
import subprocess
from common.logger import Log
import time

filePath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(filePath)



def start_server():
    stop_server()
    cmd=f'appium -a 127.0.0.1 -p 4723 --log startlog.log --local-timezone  & '   #mac需要加&,不加后续程序无法运行
    os.system(cmd)
    print("启动成功")
    time.sleep(3)


def stop_server():

    p = os.popen(f'lsof -i tcp:4723')
    p0 = p.read()
    if p0.strip() != '':
        p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
        os.popen(f'kill {p1}')  # 结束进程
        print('appium server已结束')


def ci_apk():
    log=Log()
    url = r"*lastSuccessfulBuild/artifact/snowball/build/outputs/apk/beta/snowball-beta.apk"
    try:
        r = requests.get(url)
    except Execption as e:
        log.error(e)

    with open(filePath+"/app/xueqiu.apk","wb") as code:
        code.write(r.content)
    print('下载成功')


def replace_package():
    cmd = "adb install -r /Users/xueqiu/PycharmProjects/AppiumPython/app/xueqiu.apk"# -r 覆盖安装
    result = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    print("替换成功")


def set_up(self):
    self.d.unlock()
    self.base.watch_device('同意|继续安装|允许安装|始终允许|安装|重新安装|开启|允许|确认|好的|始终允许', self.d)
    self.d.push(self.currentPath + "/Maxim/monkey.jar", "/sdcard/")
    self.d.push(self.currentPath + "/Maxim/framework.jar", "/sdcard/")
    self.d.push(self.currentPath + "/Maxim/max.config", "/sdcard/")
    self.d.push(self.currentPath + "/Maxim/max.strings", "/sdcard/")

    # self.d.app_uninstall(self.package_name)

    # 更改apk安装方式为本地安装，防止网络下载apk过程中出现异常
    self.base.local_install(self.currentPath + '/apk/xueying.apk', self.device_info, self.d)
    t.sleep(2)
    self.d.app_start(self.package_name)
    self.login()

def download_apk(self):
    res = requests.get(
        'http:*lastSuccessfulBuild/artifact/snowball/build/outputs/apk/xueying.apk')

    try:
        res.raise_for_status()
    except Exception as exc:
        print(self.base.time_tag() + self.device_info + '下载文件出错: %s' % exc)
    play_file = open('apk/xueying.apk', 'wb')
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
    play_file.close()



if __name__ == '__main__':
    ci_apk()
    replace_package()
