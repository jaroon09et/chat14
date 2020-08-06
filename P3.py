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


╔══════════════┓
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
คำสั่งพูดMp3ภาษาต่างๆ
  ────┅═ই۝ई═┅────
╔══════════════┓
╠❂➣ af : แอฟริกัน
╠❂➣ sq : อัลเบเนีย
╠❂➣ hy : อาเมเนีย
╠❂➣ bn : เบนจาลี
╠❂➣ zh-cn : จีน
╠❂➣ zh-tw : ใต้หวัน
╠❂➣ cs : เช็ก
╠❂➣ nl : ดัช
╠❂➣ en : อังกฤษ
╠❂➣ en-us : สหรัฐ
╠❂➣ el : กรีก
╠❂➣ id : อินโดนีเซีย
╠❂➣ it : อิตาลี
╠❂➣ ja : ญี่ปุ่น
╠❂➣ ko : เกาหลี
╠❂➣ la : ลาติน
╠❂➣ ro : โรมาเนีย
╠❂➣ ru : รัสเซีย
╠❂➣ sr : เซอเบียร์
╠❂➣ th : ไทย
╠❂➣ vi : เวียดนาม
╰═✰™❍✯͜͡RED™SAMURAI✯͜͡❂➣

「วิธีใช้ : say-th ผมชื่อเรดนะครับ」"""
    return helpTextToSpeech
    
def helplanguange():
    helpLanguange =    """╔══════════════┓
    คำสั่งตั้งขอความ
    ✌✌✌✌✌
💜 เปิด/ปิดรับแขก
💛 เปิด/ปิดส่งแขก
💛 เปิด/ปิดทักเตะ
💚 เปิด/ปิดพูด
💛 เปิด/ปิดตรวจสอบ
╠❂➣ทักเข้า:
╠❂➣ ทักออก:
╠❂➣ ทักเตะ:
╠❂➣ ตั้งแทค:
╠❂➣ ตั้งแอด:
╠❂➣ คอมเม้น:
หมายเหตุ กรุณาไส่ . หน้าคำสั่งเสมอ"""
    return helpLanguange
#==============================================================================#
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoBlock"] == True:
                line.blockContact(op.param1)
            if settings['autoAdd'] == True:
                line.findAndAddContactsByMid(op.param1)
                line.sendMessageWithMention(op.param1)
#                line.sendMessage(op.param1,"สวัสดีครับ","\nมีอะไรให้ผมรับใช้ครับ\n\n{}".format(str(settings["comment"])))
#                line.sendMessage(op.param1,(str(settings["comment1"])))
#                line.sendMessage(op.param1,str(settings["message"]))
                if (settings["messageadd"] in [""," ","\n",None]):
                    pass
                else:
                    line.sendMessage(op.param1,str(settings["messageadd"]))
                                
                
        if op.type == 13:
            if lineMID in op.param3:
                G = line.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    if settings["autoCancel"]["on"] == True:
                        if len(G.members) <= settings["autoCancel"]["members"]:
                            line.rejectGroupInvitation(op.param1)
                        else:
                            line.acceptGroupInvitation(op.param1)
                    else:
                        line.acceptGroupInvitation(op.param1)
                elif settings["autoCancel"]["on"] == True:
                    if len(G.members) <= settings["autoCancel"]["members"]:
                        line.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in settings["blacklist"]:
                    matched_list+=[str for str in InviterX if str == tag]
                if matched_list == []:
                    pass
                else:
                    line.cancelGroupInvitation(op.param1, matched_list)				
#        if op.type == 13:
#            group = line.getGroup(op.param1)
#            if settings["autoJoin"] == True:
#                line.acceptGroupInvitation(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                line.leaveRoom(op.param1)
                                     
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if settings["winvite"] == True:
                     if msg._from in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = line.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 line.sendText(msg.to,"-> " + _name + " \nทำการเชิญสำเร็จ")
                                 break
                             elif invite in settings["blacklist"]:
                                 line.sendText(msg.to,"ขออภัย, " + _name + " บุคคนนี้อยู่ในรายการบัญชีดำ")
                                 line.sendText(msg.to,"ใช้คำสั่ง!, \n➡ล้างดำ➡ดึง" )
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     line.findAndAddContactsByMid(target)
                                     line.inviteIntoGroup(msg.to,[target])
                                     line.sendText(msg.to,"เชิญคนนี้สำเร็จแล้ว : \n➡" + _name)
                                     settings["winvite"] = False
                                     break
                                 except:
                                     try:
                                         line.findAndAddContactsByMid(invite)
                                         line.inviteIntoGroup(op.param1,[invite])
                                         settings["winvite"] = False
                                     except:
                                         line.sendText(msg.to,"😧ตรวจพบข้อผิดพลาดที่ไม่ทราบสาเหตุ😩อาจเป็นได้ว่าบัญชีของคุณถูกแบนเชิญ😨")
                                         settings["winvite"] = False
                                         break
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if settings["wblack"] == True:
                    if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        line.sendText(msg.to,"รับทราบ")
                        settings["wblack"] = False
                    else:
                        settings["commentBlack"][msg.contentMetadata["mid"]] = True
                        settings["wblack"] = False
                        line.sendText(msg.to,"decided not to comment")

               elif settings["dblack"] == True:
                   if msg.contentMetadata["mid"] in settings["commentBlack"]:
                        del settings["commentBlack"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"ลบจากรายการที่ถูกแบนแล้ว")
                        settings["dblack"] = False

                   else:
                        settings["dblack"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif settings["wblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        line.sendText(msg.to,"Sudah Ada")
                        settings["wblacklist"] = False
                   else:
                        settings["blacklist"][msg.contentMetadata["mid"]] = True
                        settings["wblacklist"] = False
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีดำเรียบร้อยแล้ว")

               elif settings["dblacklist"] == True:
                 if msg._from in admin: 
                   if msg.contentMetadata["mid"] in settings["blacklist"]:
                        del settings["blacklist"][msg.contentMetadata["mid"]]
                        line.sendText(msg.to,"เพิ่มบัญชีนี้ในรายการสีขาวเรียบร้อยแล้ว")
                        settings["dblacklist"] = False

                   else:
                        settings["dblacklist"] = False
                        line.sendText(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
                               
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != line.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
#==============================================================================#
             
if ".พูด " in msg.text.lower():
                    spl = re.split(".พูด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        mts = spl[1]
                        mtsl = mts.split()
                        mtsTimeArg = len(mtsl) - 1
                        mtsTime = mtsl[mtsTimeArg]
                        del mtsl[mtsTimeArg]
                        mtosay = " ".join(mtsl)
                        global Rapid1To
                        Rapid1To = msg.to
                        RapidTime = mtsTime
                        rmtosay = []
                        for count in range(0,int(RapidTime)):
                            rmtosay.insert(count,mtosay)
                        p = Pool(20)
                        p.map(Rapid1Say,rmtosay)
                        p.close()
                if text.lower() == 'help':
                    myHelp = myhelp()
                    line.sendMessage(to, str(myHelp))  
                elif text.lower() == 'คำสั่ง1':
                    helpSet = helpset()
                    line.sendMessage(to, str(helpSet))
                    sendMessageWithMention(to, lineMID)
                elif text.lower() == 'คำสั่ง2':
                    listGrup = listgrup()
                    line.sendMessage(to, str(listGrup))
                elif text.lower() == 'คำสั่ง3':
                    helpSetting = helpsetting()
                    line.sendMessage(to, str(helpSetting))
                elif text.lower() == 'คำสั่ง4':
                    socMedia = socmedia()
                    line.sendMessage(to, str(socMedia))
                elif text.lower() == 'คำสั่ง5':
                    helpTextToSpeech = helptexttospeech()
                    line.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == '.sett':
                    helpLanguange = helplanguange()
                    line.sendMessage(to, str(helpLanguange))
#==============================================================================#
                elif text.lower() == '.sp':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == 'sp':
                    start = time.time()
                    line.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    line.sendMessage(msg.to, "[ %s Seconds ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ms ]")
                elif text.lower() == '.เริ่มใหม่':
                    line.sendMessage(to, "กำลังเริ่มต้นใหม่ ... โปรดรอสักครู่ ..")
                    line.sendMessage(to, "Success Restarting.")
                    restartBot()
                elif text.lower() == '.ออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    line.sendMessage(to, "ระยะเวลาการทำงานของบอท {}".format(str(runtime)))
                elif text.lower() == '.ข้อมูล':
                    try:
                        arr = []
                        owner = "ufad8bc98e4811b51115039219b8f8faf"
                        creator = line.getContact(owner)
                        contact = line.getContact(lineMID)
                        grouplist = line.getGroupIdsJoined()
                        contactlist = line.getAllContactIds()
                        blockedlist = line.getBlockedContactIds()
                        ret_ = "╔══[BY.มินทีมทดลองบอท]"
                        ret_ += "\n╠۝ ชื่อ ═ {}".format(contact.displayName)
                        ret_ += "\n╠۝ กลุ่ม ═ {}".format(str(len(grouplist)))
                        ret_ += "\n╠۝ เพื่อน ═ {}".format(str(len(contactlist)))
                        ret_ += "\n╠۝ บล็อค ═ {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[สถานะ] ═ {}".format(contact.statusMessage)
                        ret_ += "\n╠۝ ผู้สร้าง ═ {}".format(creator.displayName)
                        ret_ += "\n╚══[BY.มินทีมทดลองบอท]"
                        line.sendContact(to, owner)
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
#==============================================================================#
                elif text.lower() == '.เช็ค':
                    try:
                        ret_ = "╔════[ Status ]═════┓"
                        if settings["autoBlock"] == True: ret_ += "\n╠ ออโต้บล็อค✔"
                        else: ret_ += "\n╠ ออโต้บล็อค   ✘ "
                        if settings["autoAdd"] == True: ret_ += "\n╠ ออโต้แอด✔"
                        else: ret_ += "\n╠ ออโต้แอด   ✘ "
                        if settings["autoJoinTicket"] == True: ret_ += "\n╠ มุดลิ้ง✔"
                        else: ret_ += "\n╠ มุดลิ้ง   ✘ "
                        if settings["autoJoin"] == True: ret_ += "\n╠ เข้าห้องออโต้ ✔"
                        else: ret_ += "\n╠ เข้าห้องออโต้    ✘ "
                        if settings["Api"] == True: ret_ += "\n╠ บอทApi✔"
                        else: ret_ += "\n╠ บอทApi   ✘ "
                        if settings["Aip"] == True: ret_ += "\n╠ แสกนคำพูด+คำสั่งบิน✔"
                        else: ret_ += "\n╠ แสกนคำพูด+คำสั่งบิน   ✘ "
                        if settings["Wc"] == True: ret_ += "\n╠ ข้อความต้อนรับสมาชิก ✔"
                        else: ret_ += "\n╠ ข้อความต้อนรับสมาชิก    ✘ "
                        if settings["Lv"] == True: ret_ += "\n╠ ข้อความอำลาสมาชิก ✔"
                        else: ret_ += "\n╠ ข้อความอำลาสมาชิก    ✘ "
                        if settings["Nk"] == True: ret_ += "\n╠ ข้อความแจ้งเตือนคนลบ ✔"
                        else: ret_ += "\n╠ ข้อความแจ้งเตือนคนลบ    ✘ "
                        if settings["autoCancel"]["on"] == True:ret_+="\n╠ ปฏิเสธกลุ่มเชิญที่มีสมาชิกต่ำกว่า: " + str(settings["autoCancel"]["members"]) + " → ✔"
                        else: ret_ += "\n╠ ปฏิเสธกลุ่มเชิญ    ✘ "						
                        if settings["autoLeave"] == True: ret_ += "\n╠ ออกแชทรวม ✔"
                        else: ret_ += "\n╠ ออกแชทรวม ✘ "
                        if settings["autoRead"] == True: ret_ += "\n╠ อ่านออโต้ ✔"
                        else: ret_ += "\n╠ อ่านออโต้   ✘ "				
                        if settings["checkContact"] == True: ret_ += "\n╠ อ่านคท ✔"
                        else: ret_ += "\n╠ อ่านคท        ✘ "
                        if settings["checkPost"] == True: ret_ += "\n╠ เช็คโพส ✔"
                        else: ret_ += "\n╠ เช็คโพส        ✘ "
                        if settings["checkSticker"] == True: ret_ += "\n╠ Sticker ✔"
                        else: ret_ += "\n╠ Sticker        ✘ "
                        if settings["detectMention"] == True: ret_ += "\n╠ ตอบกลับคนแทค ✔"
                        else: ret_ += "\n╠ ตอบกลับคนแทค ✘ "
                        if settings["potoMention"] == True: ret_ += "\n╠ แสดงภาพคนแทค ✔"
                        else: ret_ += "\n╠ แสดงภาพคนแทค ✘ "
                        if settings["kickMention"] == True: ret_ += "\n╠ เตะคนแทค ✔"
                        else: ret_ += "\n╠ เตะคนแทค ✘ "
                        if settings["delayMention"] == True: ret_ += "\n╠ แทคกลับคนแทค ✔"
                        else: ret_ += "\n╠ แทคกลับคนแทค ✘ "
                        if RfuProtect["inviteprotect"] == True: ret_ += "\n╠ กันเชิญ ✔"
                        else: ret_ += "\n╠ กันเชิญ ✘ "
                        if RfuProtect["cancelprotect"] == True: ret_ += "\n╠ กันยกเชิญ ✔"
                        else: ret_ += "\n╠ กันยกเชิญ ✘ "
                        if RfuProtect["protect"] == True: ret_ += "\n╠ ป้องกัน ✔"
                        else: ret_ += "\n╠ ป้องกัน ✘ "
                        if RfuProtect["linkprotect"] == True: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✔"
                        else: ret_ += "\n╠ ป้องกันเปิดลิ้ง ✘ "
                        if RfuProtect["Protectguest"] == True: ret_ += "\n╠ ป้องกันสมาชิก ✔"
                        else: ret_ += "\n╠ ป้องกันสมาชิก ✘ "
                        if RfuProtect["Protectjoin"] == True: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✔"
                        else: ret_ += "\n╠ ป้องกันเข้ากลุ่ม ✘ "						
                        ret_ += "\n[BY.มินทีมทดลองบอท]"
                        line.sendMessage(to, str(ret_))
                    except Exception as e:
                        line.sendMessage(msg.to, str(e))
                elif text.lower() == '.เปิดบล็อค':
                    settings["autoBlock"] = True
                    line.sendMessage(to, "Autoblock enabled.")
                elif text.lower() == '.ปิดบล็อค':
                    settings["autoBlock"] = False
                    line.sendMessage(to, "Autoblock disabled.")
                elif text.lower() == '.เปิดแอด':
                    settings["autoAdd"] = True
                    line.sendMessage(to, "ออโต้แอดทำงาน enabled.")
                elif text.lower() == '.ปิดแอด':
                    settings["autoAdd"] = False
                    line.sendMessage(to, "ออโต้แอดปิดทำงาน disabled.")                                        
                elif text.lower() == '.เปิดเข้า':
                    settings["autoJoin"] = True
                    line.sendMessage(to, "Autojoin enabled.")
                elif text.lower() == '.ปิดเข้า':
                    settings["autoJoin"] = False
                    line.sendMessage(to, "Auto Join disabled.")
                elif "gcancel:" in msg.text:
                    try:
                        strnum = msg.text.replace("gcancel:","")
                        if strnum == "off":
                                settings["autoCancel"]["on"] = False
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to,str(settings["eror"]))
                                else:
                                    line.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                        else:
                                num =  int(strnum)
                                settings["autoCancel"]["on"] = True
                                if settings["lang"] == "JP":
                                    line.sendText(msg.to, " สมาชิกในกลุ่มที่ไม่ถึง" + strnum + "จะถูกปฏิเสธคำเชิญโดยอัตโนมัติ")
                                else:
                                    line.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                    except:
                        if settings["lang"] == "JP":
                                line.sendText(msg.to,str(settings["eror"]))
                        else:
                                line.sendText(msg.to,"Bizarre ratings")					
                elif text.lower() == '.เปิดออก':
                    settings["autoLeave"] = True
                    line.sendMessage(to, "เปิดระบบออกแชทรวมอัตโนมัติ")
                elif text.lower() == '.ปิดออก':
                    settings["autoLeave"] = False
                    line.sendMessage(to, "Autoleave disabled.")
                elif text.lower() == '.เปิดอ่าน':
                    settings["autoRead"] = True
                    line.sendMessage(to, "Autoread message enabled.")
                elif text.lower() == '.ปิดอ่าน':
                    settings["autoRead"] = False
                    line.sendMessage(to, "Autoread message disabled.")
                elif text.lower() == '.เปิดติ๊ก':
                    settings["checkSticker"] = True
                    line.sendMessage(to, "Check sticker enabled.")
                elif text.lower() == '.ปิดติ๊ก':
                    settings["checkSticker"] = False
                    line.sendMessage(to, "Check sticker disabled.")
                elif text.lower() == '.เปิดมุด':
                    settings["autoJoinTicket"] = True
                    line.sendMessage(to, "Autojoin byTicket  enabled.")
                elif text.lower() == '.ปิดมุด':
                    settings["autoJoinTicket"] = False
                    line.sendMessage(to, "Autojoin byTicket  disabled.")
                elif text.lower() == '.เปิดเผือก':
                    settings["unsendMessage"] = True
                    line.sendMessage(to, "unsendMessage  enabled.")
                elif text.lower() == '.ปิดเผือก':
                    settings["unsendMessage"] = False
                    line.sendMessage(to, "unsendMessage disabled.")           
#==============================================================================#
                elif msg.text.lower() == "ผม":
                me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[👇ชื่อของพี่👇]")
                    sendMessageWithMention(to, lineMID)
                    line.sendMessage(msg.to,"[สเตตัส]\n" + me.statusMessage)
                    line.sendContact(to, lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                    cover = line.getProfileCoverURL(lineMID)
                    line.sendImageWithURL(msg.to, cover)
                    line.sendMessage(msg.to,str(settings["comment"]))
                elif text.lower() == '.me':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, lineMID)
                elif text.lower() == '.ผส':
                    sendMessageWithMention(to, lineMID)
                    line.sendContact(to, "ufad8bc98e4811b51115039219b8f8faf")
                elif text.lower() == '.ไอดี':
                    line.sendMessage(msg.to,"[MID]\n" +  lineMID)
                elif text.lower() == '.ชื่อ':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[DisplayName]\n" + me.displayName)
                elif text.lower() == '.ตัส':
                    me = line.getContact(lineMID)
                    line.sendMessage(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif text.lower() == '.รูปโปร':
                    me = line.getContact(lineMID)
                    line.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == '.วีดีโอโปร':
                    me = line.getContact(lineMID)
                    line.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == '.รูปปก':
                    me = line.getContact(lineMID)
                    cover = line.getProfileCoverURL(lineMID)    
                    line.sendImageWithURL(msg.to, cover)
                elif text.lower() == '.คอมเม้น':
                    line.sendMessage(msg.to,str(settings["comment"]))
                elif text.lower() == '.ทักเข้า':
                    line.sendMessage(msg.to, str(settings["welcome"]))
                elif text.lower() == '.ทักออก':
                    line.sendMessage(msg.to, str(settings["bye"]))
                elif text.lower() == '.ทักเตะ':
                    line.sendMessage(msg.to, str(settings["kick"]))
                elif text.lower() == '.ข้อความแอด':
                    line.sendMessage(msg.to, str(settings["message"]))
                elif text.lower() == '.ข้อความแทค':
                    line.sendMessage(msg.to, str(settings["Respontag"]))
                elif text.lower() == '.แทคล่อง':
                    gs = line.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        line.sendMessage(to, "ม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        line.sendMessage(to, mc)
                elif text.lower() == '.ไอดีล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีmidคนใส่ร่องหน🤗")
                    else:
                        mc = ""
                        for mi_d in lists:
                            mc += "->" + mi_d + "\n"
                        line.sendMessage(to,mc)
                elif text.lower() == '.คทล่อง':
                    gs = line.getGroup(to)
                    lists = []
                    for g in gs.members:
                        if g.displayName in "":
                            lists.append(g.mid)
                    if lists == []:
                        line.sendMessage(to, "ไม่มีคนใส่ร่องหนในกลุ่มนี้😂")
                    else:
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(to, mi_d)
                elif msg.text.lower().startswith(".คท "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            mi_d = contact.mid
                            line.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith(".ไอดี "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n{}" + ls
                        line.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith(".ชื่อ "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Display Name ]\n" + contact.displayName)
                elif msg.text.lower().startswith(".ตัส "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = line.getContact(ls)
                            line.sendMessage(msg.to, "[ Status Message ]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith(".รูป "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith(".วีดีโอโปร "):
                    if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + line.getContact(ls).pictureStatus + "/vp"
                            line.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith(".ปก "):
                    if line != None:
                        if 'MENTION' in list(msg.contentMetadata.keys())!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = line.getProfileCoverURL(ls)
                                line.sendImageWithURL(msg.to, str(path))
                elif ".โพส " in msg.text:
                    tl_text = msg.text.replace(".โพส ","")
                    line.sendText(msg.to,"line://home/post?userMid="+lineMID+"&postId="+line.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
                elif ".ก๊อป " in msg.text:
                  if msg._from in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                    for target in targets:
                        try:
                            contact = line.getContact(target)
                            X = contact.displayName
                            profile = line.getProfile()
                            profile.displayName = X
                            line.updateProfile(profile)
                            line.sendMessage(msg.to, "Success...")
                        #---------------------------------------
                            Y = contact.statusMessage
                            lol = line.getProfile()
                            lol.statusMessage = Y
                            line.updateProfile(lol)
                        #---------------------------------------
                            P = contact.pictureStatus
                            hun = line.getProfile()
                            hun.pictureStatus = P
                            line.updateProfile(hun)
                        except Exception as e:
                            line.sendMessage(msg.to, "Failed!")
                            print (e)

                elif msg.text in [".คืนร่าง"]:
                    try:
                        line.updateProfile.pictureStatus(backup.pictureStatus)
                        line.updateProfile.statusMessage(backup.statusMessage)
                        line.updateProfile.displayName(backup.displayName)
                        line.sendMessage(msg.to, "กลับร่างเดิมแล้ว")
                    except Exception as e:
                        line.sendText(msg.to, str (e))
                        
                elif msg.text in ["Allprotect on",".เปิดกทม"]:
                        settings["kickMention"] = True
                        settings["Aip"] = False
                        RfuProtect["protect"] = True
                        RfuProtect["cancelprotect"] = True
                        RfuProtect["inviteprotect"] = True 
                        RfuProtect["linkprotect"] = True 
                        RfuProtect["Protectguest"] = True
                        RfuProtect["Protectjoin"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด เปิด👌")
						
                elif msg.text in ["Allprotect off",".ปิดกทม"]:
                        settings["kickMention"] = False
                        settings["Aip"] = False
                        RfuProtect["protect"] = False
                        RfuProtect["cancelprotect"] = False
                        RfuProtect["inviteprotect"] = False 
                        RfuProtect["linkprotect"] = False 
                        RfuProtect["Protectguest"] = False
                        RfuProtect["Protectjoin"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดรักษาความปลอดภัยทั้งหมด ปิด👌")
                        
                elif msg.text in ["Allmsg on",".เปิดข้อความ"]:
                        settings["Wc"] = True
                        settings["Lv"] = True
                        settings["Nk"] = True
                        settings["autoRead"] = True
                        settings["checkSticker"] = True 
                        settings["checkContact"] = True 
                        settings["checkPost"] = True
                        settings["potoMention"] = True
                        settings["detectMention"] = True
                        settings["delayMention"] = True
                        settings["Api"] = True
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด เปิด👌")
						
                elif msg.text in ["Allmsg off",".ปิดข้อความ"]:
                        settings["Wc"] = False
                        settings["Lv"] = False
                        settings["Nk"] = False
                        settings["autoRead"] = True
                        settings["checkSticker"] = False 
                        settings["checkContact"] = False 
                        settings["checkPost"] = False
                        settings["detectMention"] = False
                        settings["potoMention"] = False
                        settings["delayMention"] = False
                        settings["Api"] = False
                        line.sendText(msg.to,"การตั้งค่าชุดข้อความทั้งหมด ปิด👌")
#==============================================================================#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            line.sendMessage(msg.to,"Mimic has been added as")
                            break
                        except:
                            line.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            line.sendMessage(msg.to,"Mimic deleting succes...")
                            break
                        except:
                            line.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        line.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+line.getContact(mi_d).displayName
                        line.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            line.sendMessage(msg.to,"Mimic enabled.")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            line.sendMessage(msg.to,"Mimic disabled.")

                elif "Spam " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               line.sendMessage(msg.to, teks)
                        else:
                           line.sendMessage(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            line.sendMessage(msg.to, tulisan)
                        else:
                            line.sendMessage(msg.to, "Out Of Range!")
#==============================================================================#
                elif text.lower() == '.แอด':
                    group = line.getGroup(to)
                    GS = group.creator.mid
                    line.sendContact(to, GS)
                    line.sendMessage(to, "☝คนนี้แหล่ะคนสร้างกลุ่มนี้")
                elif text.lower() == '.ไอดีกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ไอดีกลุ่ม \n" + gid.id)
                elif text.lower() == '.รูปกลุ่ม':
                    group = line.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    line.sendImageWithURL(to, path)
                elif text.lower() == '.ชื่อกลุ่ม':
                    gid = line.getGroup(to)
                    line.sendMessage(to, "ชื่อกลุ่ม -> \n" + gid.name)
                elif text.lower() == '.ลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = line.reissueGroupTicket(to)
                            line.sendMessage(to, "ลิ้งของกลุ่ม\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif text.lower() == '.เปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = False
                            line.updateGroup(group)
                            line.sendMessage(to, "เปิดลิ้งเรียบร้อย")
                elif text.lower() == '.ปิดลิ้ง':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                        else:
                            group.preventedJoinByTicket = True
                            line.updateGroup(group)
                            line.sendMessage(to, "ปิดลิ้งเรียบร้อย")
                elif text.lower() == '.ข้อมูลกลุ่ม':
                    group = line.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "คนนี้คือผู้สร้างกลุ่มนี้"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิด"
                        gTicket = "ไม่สมารถแสดงลิ้งได้"
                    else:
                        gQr = "เปิด"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ ข้อมูลของกลุ่มนี้ ]"
                    ret_ += "\n╠ ชื่อของกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีของกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ ผู้สร้างกลุ่ม : {}".format(str(gCreator))
                    ret_ += "\n╠ จำนวนสมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ จำนวนค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ ลิ้งของกลุ่ม : {}".format(gQr)
                    ret_ += "\n╠ ลิ้งกลุ่ม👉 : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    line.sendMessage(to, str(ret_))
                    line.sendImageWithURL(to, path)
                elif text.lower() == '.สมาชิกกลุ่ม':
                    if msg.toType == 2:
                        group = line.getGroup(to)
                        ret_ = "╔══[ Member List ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} ]".format(str(len(group.members)))
                        line.sendMessage(to, str(ret_))
                elif text.lower() == '.เช็คกลุ่ม':
                        groups = line.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = line.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[ จำนวน {} Groups ]".format(str(len(groups)))
                        line.sendMessage(to, str(ret_))				
                elif ".เชิญคลอ" == msg.text.lower():
                    line.inviteIntoGroupCall(msg.to,[uid.mid for uid in line.getGroup(msg.to).members if uid.mid != line.getProfile().mid])
                    line.sendMessage(msg.to,"เชิญเข้าร่วมการโทรสำเร็จ(｀・ω・´)")
                elif ".sh " in msg.text.lower():
                    spl = re.split(".sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass
                elif msg.text.lower() == '.เชิญแอด':
                	if msg.toType == 2:                
                           ginfo = line.getGroup(receiver)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if settings["lang"] == "JP":
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "พิมพ์คำเชิญกลุ่มแล้ว")
                           else:
                               line.inviteIntoGroup(receiver,[gcmid])
                               line.sendMessage(receiver, "ผู้สร้างกลุ่มอยู่ในแล้ว")
                               
                elif msg.text.lower() == "getjoined":
                    line.sendText(msg.to,"กรุณารอสักครู่ ใจเย็นๆ")
                    all = line.getGroupIdsJoined()
                    text = ""
                    cnt = 0
                    for i in all:
                        text += line.getGroup(i).name + "\n" + i + "\n\n"
                        cnt += 1
                        if cnt == 10:
                            line.sendText(msg.to,text[:-2])
                            text = ""
                            cnt = 0
                    line.sendText(msg.to,text[:-2])
                    cnt = 0				
                elif ".ข้อมูล " in msg.text.lower():
                    spl = re.split(".ข้อมูล ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = line.getContact(uid)
                            try:
                                line.sendImageWithUrl(msg.to,"http://dl.profile.line-cdn.net{}".format(userData.picturePath))
                            except:
                                pass
                            line.sendText(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            line.sendText(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            line.sendText(msg.to,"ไอดีบัญชี: "+userData.mid)
                
                elif "รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\n💝ราคาดูที่หน้างาน💝\n👉มีบริการให้เช่าบอทSAMURAI\nราคา300บาทต่อเดือน💖\n#เพิ่มคิกเกอร์ตัวละ100👌\n🎀สนใจรีบทัก..บอทpython3ฟังชั่นล้นหลาม🎁กำลังรอให้คุณเป็นเจ้าของ\n(ผมจะอยู่ที่ห้องนี้แค่15นาทีนะจ๊ะ)\nselfbot by:\n╔══════════════┓\n[BY.มินทีมทดลองบอท] \n╚══════════════┛" in msg.text:
                    spl = msg.text.split("รับแก้ไฟล์+เพิ่มไฟล์+แก้ภาษา\n💝ราคาดูที่หน้างาน💝\n👉มีบริการให้เช่าบอทSAMURAI\nราคา300บาทต่อเดือน💖\n#เพิ่มคิกเกอร์ตัวละ100👌\n🎀สนใจรีบทัก..บอทpython3ฟังชั่นล้นหลาม🎁กำลังรอให้คุณเป็นเจ้าของ\n(ผมจะอยู่ที่ห้องนี้แค่15นาทีนะจ๊ะ)\nselfbot by:\n╔══════════════┓\n[BY.มินทีมทดลองบอท]➣ \n╚══════════════┛")
                    if spl[len(spl)-1] == "":
                        line.sendText(msg.to,"กดที่นี่เพื่อเขย่าข้อความด้านบน:\nline://nv/chatMsg?chatId="+msg.to+"&messageId="+msg.id) ### CMD COVER
                elif ".รันแชท @" in msg.text:
                    _name = msg.text.replace(".รันแชท @","")
                    _nametarget = _name.rstrip(' ')
                    gs = line.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(g.mid,"[Line://ti/g2/OXNFJ5K4P9]")
                           line.sendText(msg.to, "Done")
                           print (" Spammed !")
                elif ".สำรองห้อง" in msg.text:
                    thisgroup = line.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    line.createGroup("MIN HACK SELFBOT", mi_d)
                    line.sendText(msg.to,"MIN HACK BOT")
                    line.createGroup("MIN HACK SELFBOT", mi_d)
                    line.sendText(msg.to,"MIN HACK BOT")
                elif ".รัน: " in msg.text.lower():
                        key = msg.text[-33:]
                        line.findAndAddContactsByMid(key)                   
                        contact = cl.getContact(key)
                        line.createGroup("MIN HACK SELFBOT Group",[key])
                        line.sendText(msg,to,"MIN HACK SELFBOT")
                elif ".ไม่รับเชิญ " in msg.text.lower():
                    spl = re.split(".ไม่รับเชิญ ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = line.getGroupIdsInvited()
                        txt = "กำลังยกเลิกค้างเชิญจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        line.sendText(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                line.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    line.sendText(gr,spl[1])
                                line.leaveGroup(gr)
                            except:
                                pass
                        line.sendText(msg.to,"สำเร็จแล้ว")	
                elif ".whois " in msg.text.lower():
                    spl = re.split(".whois ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        msg.contentType = 13
                        msg.text = None
                        msg.contentMetadata = {"mid":spl[1]}
                        line.sendMessage(msg)
                elif ".หวด" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            random.choice(Exc).kickoutFromGroup(msg.to,[prov[i]["M"]])
                elif ".ปลิว" in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            line.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        line.findAndAddContactsByMids(allmid)
                        line.inviteIntoGroup(msg.to,allmid)
                        line.cancelGroupInvitation(msg.to,allmid)

                elif msg.text.lower() == "mid":
                    line.sendText(msg.to,user1)
                
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = spl[1]
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".nmx " in msg.text.lower():
                    spl = re.split(".nmx ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = line.getProfile()
                        prof.displayName = line.nmxstring(spl[1])
                        line.updateProfile(prof)
                        line.sendText(msg.to,"สำเร็จแล้ว")
                elif ".มุด " in msg.text.lower():
                    spl = re.split(".มุด ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            gid = spl[1].split(" ")[0]
                            ticket = spl[1].split(" ")[1].replace("line://ti/g/","") if "line://ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1].replace("http://line.me/R/ti/g/","") if "http://line.me/R/ti/g/" in spl[1].split(" ")[1] else spl[1].split(" ")[1]
                            line.acceptGroupInvitationByTicket(gid,ticket)
                        except Exception as e:
                            line.sendText(msg.to,str(e))	
                						
                elif msg.text.lower().startswith(".ส่งข้อความ "):
                    pnum = re.split(".ส่งข้อความ ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                line.sendText(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                line.sendText(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                line.sendText(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                line.sendText(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                line.sendText(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == ".groupurl":
                    if msg.toType == 2:
                        line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(msg.to)))
                    else:
                        line.sendText(msg.to,"คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้น")
                elif ".groupurl " in msg.text.lower():
                    spl = re.split(".groupurl ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            line.sendText(msg.to,"http://line.me/R/ti/g/"+str(line.reissueGroupTicket(spl[1])))
                        except Exception as e:
                            line.sendText(msg.to,"พบข้อผิดพลาด (เหตุผล \""+e.reason+"\")")
                if "gift " in msg.text.lower():
                    red = re.compile(re.escape('gift '),re.IGNORECASE)
                    themeid = red.sub('',msg.text)
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': themeid,
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '1'}
                    msg.text = None
                    line.sendMessage(msg)
#==============================================================================#
                elif text.lower() == '.แจ๊ะ':
             group = line.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = ''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += '@Alin \n'
                        line.sendMessage(to, text=txt, contentMetadata={'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        line.sendMessage(to, "จำนวนแจ๊ะทั้งหมด {} คน".format(str(len(nama))))  
                elif text.lower() == '.จับ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                line.sendMessage(msg.to,"Lurking enabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            line.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == '.เลิกจับ':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        line.sendMessage(msg.to,"Lurking disabled")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        line.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == '.จับใหม่':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        line.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        line.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == '.อ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["วันอาทิตย์", "วันจันทร์", "วันอังคาร", "วันพุธ", "วันพฤหัสบดี", "วันศุกร์", "วันเสาร์"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if list(read["ROM"][receiver].items()) == []:
                            line.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in list(read["ROM"][receiver].items()):
                                chiya.append(rom[1])
                            cmem = line.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ *** LurkDetector *** ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            line.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        line.sendMessage(receiver,"Lurking has not been set.")
#==============================================================================#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    line.sendAudio(msg.to,"hasil.mp3")
#==============================================================================# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    line.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    line.sendMessage(msg.to, A)

