# -*- coding: utf-8 -*-
from MGET import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib.request, urllib.parse, urllib.error, urllib.parse,antolib,subprocess,unicodedata,GACSender
from gtts import gTTS
from googletrans import Translator
#==============================================================================#
botStart = time.time()
#==============================================================================#
line = LINE()
#line = LINE("เมล","พาส")
#line = LINE('EulkVm03YPzIy1y9cjb3.TAVOkm2wqPizxdXz1JiGmW.8S00JCP4DRsRTBGHcgh3JJRnGxUeoUlXI2iRelhqwrY=')
line.log("Auth Token : " + str(line.authToken))
line.log("Timeline Token : " + str(line.tl.channelAccessToken))

print ("Login Succes")

lineMID = line.profile.mid
lineProfile = line.getProfile()
lineSettings = line.getSettings()

oepoll = OEPoll(line)
#call = Call(line)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
Rfu = [line]
Exc = [line]
lineMID = line.getProfile().mid
bot1 = line.getProfile().mid
RfuBot=[lineMID]
Family=["ufad8bc98e4811b51115039219b8f8faf",lineMID]
admin=['ufad8bc98e4811b51115039219b8f8faf',lineMID]
RfuFamily = RfuBot + Family

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
#==============================================================================#
msg_dict = {}

settings = {
    "autoBlock": False,
    "autoAdd": True,
    "autoJoin": True,
    'autoCancel':{"on":True,"members":10},	
    "autoLeave": True,
    "autoRead": True,
    "leaveRoom": False,
    "detectMention": True,
    "checkSticker": False,
    "checkContact": False,
    "checkPost": False,
    "kickMention": False,
    "potoMention": True,
    "delayMention": False,
    "lang":"JP",
    "Wc": True,
    "Lv": True,
    "Nk": True,
    "Api": True,
    "Aip": True,
    "blacklist":{},
    "winvite": False,
    "wblacklist": False,
    "dblacklist": False,
    "gift":False,
    "likeOn":True,
    "timeline":True,
    "commentOn":True,
    "commentBlack":{},
    "wblack": False,
    "dblack": False,
    "clock": False,
    "cName":"",
    "cNames":"",
    "changeGroupPicture": [],
    "changePictureProfile":False,
    "unsendMessage": False,
    "autoJoinTicket": False,
    "welcome":"[Line://ti/g2/OXNFJ5K4P9]",
    "kick":"เอาหวะใจแม่งได้หวะ",
    "bye":"นายทำดีแล้วเพื่อน ลาก่อน",
    "Respontag":"💗",
    "eror":"",
    "spam":{},
    "invite": {},
    "winvite": False,
    "pnharfbot": {},
    "pname": {},
    "pro_name": {},
    "message1":"",
    "messageadd":"",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}

RfuProtect = {
    "protect": False,
    "cancelprotect": False,
    "inviteprotect": False,
    "linkprotect": False,
    "Protectguest": False,
    "Protectjoin": False,
    "autoBlock": True,
}

Setmain = {
    "foto": {},
}

read = {
    "readPoint": {},
    "readMember": {},
    "readTime": {},
    "setTime":{},
    "ROM": {}
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
RfuCctv={
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

rfuSet = {
    'setTime':{},
    'ricoinvite':{},
    'winvite':{},
    }

user1 = lineMID
user2 = ""
	
setTime = {}
setTime = rfuSet['setTime']

contact = line.getProfile() 
backup = line.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

mulai = time.time() 

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")

myProfile["displayName"] = lineProfile.displayName
myProfile["statusMessage"] = lineProfile.statusMessage
myProfile["pictureStatus"] = lineProfile.pictureStatus
#==============================================================================#
#==============================================================================#            
def Rapid1Say(mtosay):
    line.sendText(Rapid1To,mtosay)

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("TAG ALL")
    try:
       line.sendMessage(msg)
    except Exception as error:
       print(error)

def restartBot():
    print ("RESTART SERVER")
    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    line.log("[ แจ้งเตือน ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))

def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
        
def sendMessageWithMention(to, lineMID):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(lineMID)+'}'
        text_ = '@x '
        line.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
  
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                line.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "╔══[Mention {} User]\n╠ ".format(str(len(mid)))
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠ "
            else:
                try:
                    textx += "╚══[ {} ]".format(str(line.getGroup(to).name))
                except:
                    pass
        line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        line.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def myhelp():
    myHelp = """꧁มินทีมทดลองบอท꧂
 SELF BOT MIN HACK
꧁ชุดคำสั่ง ภาษาไทย꧂
╔═══════════════════┓
╔══════════╗
╠✰ เช็ค [เช็คการตั้งค่า]
╚══════════╝
╔══════════╗
╠✰ ผส [คท.ผู้สร้าง]
╚══════════╝
╔══════════╗
╠✰ ข้อมูล [ข้อมูลตัวเอง]
╚══════════╝
╔══════════╗
╠✰ ข้อมูล @ [คนที่แทค]
╚══════════╝
╔══════════╗
╠✰ คำสั่ง1 [เซลบอท]
╚══════════╝
╔══════════╗
╠✰ คำสั่ง2 [คำสั่งกลุ่ม]
╚══════════╝
╔══════════╗
╠✰ คำสั่ง3 [คำสั่งตั้งค่า]
╚══════════╝
╔══════════╗
╠✰ คำสั่ง4 [คำสั่งโซเชล]
╚══════════╝
╔══════════╗
╠✰ คำสั่ง5 [คำสั่งพูดเสียง]
╚══════════╝
╔══════════╗
╠✰ ไอดี @ [ไอดีคนแทค]
╚══════════╝
╔══════════╗
╠✰ ชื่อ @ [ชื่อคนแทค]
╚══════════╝
╔══════════╗
╠✰ ตัส @ [สเตตัสคนแทค]
╚══════════╝
╔══════════╗
╠✰ รูป @ [ดึงรูป]
╚══════════╝
╔══════════╗
╠✰ ปก @ [ดึงปก]
╚══════════╝
╔══════════╗
╠✰ คท @ [คอนแทคคนแท็ก]
╚══════════╝
╔══════════╗
╠✰ วีดีโอโปร @ [วีดีโอคนแทค]
╚══════════╝
╔══════════╗
╠✰ ไอดีล่อง [ไอดีล่องหน]
╚══════════╝
╔══════════╗
╠✰ คทล่อง [คอนแทคล่องหน]
╚══════════╝
╔══════════╗
╠✰ แทคล่อง [ร่องหน]
╚══════════╝
╔══════════╗
╠✰ ปฏิทิน [เช็ควันเวลา]
╚══════════╝
╔══════════╗
╠✰ ส่งเสียงกลุ่ม [ข้อความ]
╚══════════╝
╔══════════╗
╠✰ ส่งเสียงแชท [ข้อความ]
╚══════════╝
╔══════════╗
╠✰ ประกาศกลุ่ม [ข้อความ]
╚══════════╝
╔══════════╗
╠✰ ประแชท [ข้อความ]
╚══════════╝
╔══════════╗
╠✰ ส่งรูปภาพตามกลุ่ม [ลิ้งรูป]
╚══════════╝
╔══════════╗
╠✰ ส่งรูปภาพตามแชท [ลิ้งรูป]
╚══════════╝
╔══════════╗
╠✰ เริ่มใหม่ [รีบูสระบบใหม่]
╚══════════╝
╔══════════╗
╠✰ เวลออน [เช็คเวลาออน]
╚══════════╝
 *หมายเหตุ*  คำสั่งที่เป็นภาษาไทย
 ให้ใส่ . นำหน้าคำสั่งเวลาใช้ด้วยเด้อ"""
    return myHelp

def listgrup():
    listGrup = """꧁มินทีมทดลองบอท꧂
 SELF BOT MIN HACK
꧁ชุดคำสั่ง ภาษาไทย꧂
 ────┅═ই۝ई═┅────
             คำสั่งในกลุ่ม
 ────┅═ই۝ई═┅────
╔══════════════┓
💓 แอด
💔ชื่อกลุ่ม
💖 ไอดีกลุ่ม
💚 เปิดลิ้ง
💛 ปิดลิ้ง
💜 ลิ้ง
💓ลิ้งกลุ่ม
💖 รายการกลุ่ม
💗 สมาชิกกลุ่ม
💘 ข้อมูลกลุ่ม
💝 รูปกลุ่ม
💞 แจ๊ะ
💟เช็คไอดี
💟 ไอดีล่อง
💞คทล่อง
💝 แทคล่อง
💘 จับ
💗 เลิกจับ
💖 จับใหม่
💕 อ่าน
💔 .เปลี่ยนรูปกลุ่ม
💓 เปิด/ปิดแสกน
💜 เปิด/ปิดรับแขก
💛 เปิด/ปิดส่งแขก
💛 เปิด/ปิดทักเตะ
💚 เปิด/ปิดพูด
💛 เปิด/ปิดตรวจสอบ
💜 สำรองห้อง
💜 เช็คดำ
💛 ลงดำ
💛 ล้างดำ
💜 ไล่ดำ
💚 ปวดตับ (Kickall)
*หมายเหตุ*  คำสั่งที่เป็นภาษาไทย
 ให้ใส่ . นำหน้าคำสั่งด้วยครับ"""
    return listGrup

def socmedia():
    socMedia = """꧁มินทีมทดลองบอท꧂
 SELF BOT MIN HACK
꧁ชุดคำสั่ง ภาษาไทย꧂



╠❂➣ ปฏิทิน
╠❂➣ รูปภาพ [ชื่อรูปภาพ]
╠❂➣ ค้นหารูปภาพ [ชื่อรูปภาพ]
╠❂➣ ยูทูป [ข้อความ]
╠❂➣ เพลง [ชื่อเพลง]
╠❂➣ Lyric
╠❂➣ ScreenshootWebsite
╠❂➣ หนัง [ชื่อหนัง]
╠❂➣ วีดีโอ [ชื่อวีดีโอ]
╠❂➣ รูปการ์ตูน [ชื่อรูป]
╠❂➣ ไอจี [ชื่อยูส]
╠❂➣ Urban
╠❂➣ กูเกิ้ล [ข้อความ]
*หมายเหตุ*  คำสั่งที่เป็นภาษาไทย
 ให้ใส่ . นำหน้าคำสั่งด้วยครับ"""
    return socMedia

def helpset():
    helpSet = """꧁มินทีมทดลองบอท꧂
 SELF BOT MIN HACK
꧁ชุดคำสั่ง ภาษาไทย꧂
╔══════════════┓
╠❂➣ โย่ว
╠❂➣ ไอดี
╠❂➣ ชื่อ
╠❂➣ ตัส
╠❂➣ รูปโปร
╠❂➣ รูปปก
╠❂➣ วัดรอบ
╠❂➣ Sp
╠❂➣ ทักเข้า
╠❂➣ ทักออก
╠❂➣ ทักเตะ
╠❂➣ คอมเม้น
╠❂➣ ข้อความแทค
╠❂➣ ข้อความแอด
╠❂➣ ชื่อ:
╠❂➣ ตัส:
╠❂➣ ทักเข้า:
╠❂➣ ทักออก:
╠❂➣ ทักเตะ:
╠❂➣ ตั้งแทค:
╠❂➣ ตั้งแอด:
╠❂➣ คอมเม้น:
╠❂➣ เวลออน
╠❂➣ ดำ
╠❂➣ ขาว
╠❂➣ คทแบน
╠❂➣ แบน @
╠❂➣ ลบแบน @
╠❂➣ บล็อค @
╠❂➣ ลบรัน
╠❂➣ ดึง
╠❂➣ หวด @
╠❂➣ สอย @
╠❂➣ ลาก่อย @
╠❂➣ ปลิว @
╠❂➣ ดับไฟ
╠❂➣ แปลงโฉม
╠❂➣ เพื่อน
╠❂➣ ไอดีเพื่อน
╠❂➣ Gcancel:(จำนวนสมาชิก)
*หมายเหตุ*  คำสั่งที่เป็นภาษาไทย
 ให้ใส่ . นำหน้าคำสั่งด้วยครับ"""
    return helpSet

def helpsetting():
    helpSetting = """꧁มินทีมทดลองบอท꧂
 SELF BOT MIN HACK
꧁ชุดคำสั่ง ภาษาไทย꧂
╔══════════════┓
╠❂➣ เปิดกัน/ปิดกัน
╠❂➣ กันยก/ปิดกันยก
╠❂➣ กันเชิญ/ปิดกันเชิญ
╠❂➣ กันลิ้ง/ปิดกันลิ้ง
╠❂➣ กันเข้า/ปิดกันเข้า
╠❂➣ เปิดหมด/ปิดหมด
╠❂➣ เปิดกทม/ปิดกทม
╠❂➣ เปิดเข้า/ปิดเข้า
╠❂➣ เปิดออก/ปิดออก
╠❂➣ เปิดติ๊ก/ปิดติ๊ก
╠❂➣ เปิดบล็อค/ปิดบล็อค
╠❂➣ เปิดแอด/ปิดแอด
╠❂➣ เปิดมุด/ปิดมุด
╠❂➣ เปิดเผือก/ปิดเผือก
╠❂➣ เปิดอ่าน/ปิดอ่าน
╠❂➣ เปิดพูด/ปิดพูด
╠❂➣ เปิดแทค/ปิดแทค
╠❂➣ เปิดแทค2/ปิดแทค2
╠❂➣ เปิดแทค3/ปิดแทค3
╠❂➣ เปิดแทคเจ็บ/ปิดแทคเจ็บ
╠❂➣ เปิดคท/ปิดคท
╠❂➣ เปิดตรวจสอบ/ปิดตรวจสอบ
╠❂➣ เปิดเช็คโพส/ปิดเช็คโพส
╠❂➣ เปิดแสกน/ปิดแสกน
╠❂➣ เปิดรับแขก/ปิดรับแขก
╠❂➣ เปิดส่งแขก/ปิดส่งแขก
╠❂➣ เปิดทักเตะ/ปิดทักเตะ
╠❂➣ เปิดข้อความ/ปิดข้อความ
*หมายเหตุ*  คำสั่งที่เป็นภาษาไทย
 ให้ใส่ . นำหน้าคำสั่งด้วยครับ"""
    return helpSetting

def helptexttospeech():
    helpTextToSpeech =   """╔══════════════┓
╠™❍✯͜͡RED™SAMURI✯͜͡❂➣ 
╚══════════════┛
 ────┅═ই۝ई═┅────
