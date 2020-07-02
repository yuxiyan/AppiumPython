import requests,json,datetime,time


def send_message(content):
    url= "  "   #钉钉hook地址
    para={
        "msgtype":"text",
          "text":{
              "content":content
          },
          "isAtAll":True
    }
    headers={'Content-Type':'application/json'}
    f=requests.post(url,data=json.dumps(para),headers=headers)
