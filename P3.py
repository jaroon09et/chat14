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
                
