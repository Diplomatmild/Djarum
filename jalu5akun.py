# -*- coding: utf-8 -*-

import BASYIR
from BASYIR.lib.curve.ttypes import *
from BASYIR.lib.curve.ttypes import Message
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile,glob
import requests
import urllib
import urllib2
import subprocess
import profile
import wikipedia
import requests
import os
from gtts import gTTS
from bs4 import BeautifulSoup
from threading import Thread

cl = BASYIR.LINE() #Self
cl.login(token="TOKENMU")
cl.loginResult()

ki = BASYIR.LINE() #Jembut1
ki.login(token="TOKENMU")
ki.loginResult()

ki2 = BASYIR.LINE() #Jembut2
ki2.login(token="TOKENMU")
ki2.loginResult()

ki3 = BASYIR.LINE() #Jembot3
ki3.login(token="TOK3NMU")
ki3.loginResult()

ki4 = BASYIR.LINE() #Jembot4
ki4.login(token="TOKENMU")
ki4.loginResult()

ki5 = BASYIR.LINE() #Jembot5
ki5.login(token="TOKENMU")
ki5.loginResult()

print u"Running Succes Mbott"
reload(sys)
sys.setdefaultencoding('utf-8')

selfMessage ="""
Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠７⃠

❥ .Idline: 「Text」
❥ .Image:「Text」
❥ .Smule:「Text」
❥ .Musik:「Text」
❥ .Music:「Text」
❥ .Lyric:「Text」
❥ .Youtubelink「Text」
❥ .Youtubesearch「Text」
❥ .Gift
❥ .Gift 「1-10」
❥ .All gift
❥ .Apakah 「Text」
❥ .Salam
❥ .Jawab salam
"""


mediaMessage ="""
Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠６⃠

❥ .Sider 「 On/Off 」
❥ .Share 「 On/Off 」
❥ .Sticker 「 On/Off 」
❥ .Simisimi 「 On/Off 」
❥ .Link 「 On/Off 」
❥ .Welcome 「 On/Off 」
❥ .Always read 「 On/Off 」
❥ .Comment 「 On/Off 」
❥ .Like 「 On/Off 」
❥ .Contact 「 On/Off 」
❥ .Autoadd 「 On/Off 」
❥ .Autojoin 「 On/Off 」
❥ .Autoleave 「 On/Off 」
❥ .Autocancel 「 On/Off 」
❥ .Respon1 「 On/Off 」
❥ .Respon2 「 On/Off 」
❥ .Pbrespon 「 On/Off 」
❥ .Respon4 「 On/Off 」
❥ .Responkick 「 On/Off 」
❥ .Reject 「 On/Off 」

"""

groupMessage ="""
Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠５⃠

❥ .Spam: 「Text」
❥ .Spamchange: 「Text」
❥ .Spamadd: 「Text」
❥ .Spamtag 「@」
❥ .Spamcontact 「@」
❥ .Spam uni 「@」
❥ .Broadcast「Text」
❥ .Cbroadcast 「Text」
❥ .Mbroadcast 「Text」
"""

setMessage ="""
「 Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠４⃠ 」

❥ .「 Mayhem 」
❥ .「 Fuck @」
❥ .「 Kick @」
❥ .「 Nk:  @」 
❥ .「 Vkick @」 
❥ .「 Nuke 」
❥ .「 Kickall 」
"""

admin2Message ="""
「 Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠３⃠ 」

❥ .Ban 「@」
❥ .Unban 「@」
❥ .Talkban 「@」
❥ .Ban Repeat 「@」
❥ .Ban 「Send」
❥ .Unban 「Send」
❥ .Talkdel「@」
❥ .Conban
❥ .Mid Ban
❥ .Talklist
❥ .Banlist
❥ .Kill
❥ .Mid 「@」
❥ .Invite 「Send」
❥ .Invite:「Mid」
❥ .Clear Ban

"""

adminMessage ="""
「 Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠２⃠ 」

❥ .Friendlist
❥ .Memlist
❥ .Myname
❥ .Mymid
❥ .Glist
❥ .Group
❥ .Tag/Ats
❥ .Tagall
❥ .Cctv/Cyduk
❥ .Ginfo
❥ .List group
❥ .Gurl
❥ .Welcome
❥ .Gcreator
❥ .Cancel
❥ .Runtime
❥ .Bio: 「Text」
❥ .Mycopy 「@」
❥ .Mybackup
❥ .Pict Group
❥ .Gn: 「Text」
"""

helpMessage ="""
「 Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠ 」

༇❥﴾ᎻᎬᏞᎮ ¹﴿
༇❥﴾ᎻᎬᏞᎮ ²﴿
༇❥﴾ᎻᎬᏞᎮ ³﴿
༇❥﴾ᎻᎬᏞᎮ ⁴﴿
༇❥﴾ᎻᎬᏞᎮ ⁵﴿
༇❥﴾ᎻᎬᏞᎮ ⁶﴿
༇❥﴾ᎻᎬᏞᎮ ⁷⁨⁨⁠⁠⁢⁡﴿
"""

protectMessage ="""
「 Ꮋ⃠Ꭼ⃠Ꮮ⃠Ꭾ⃠１⃠ 」

❥ .AllProtect 「 On/Off 」
❥ .Protect 「 On/Off 」
❥ .Cancelprotect 「 On/Off 」
❥ .Linkprotect 「 On/Off 」
❥ .Inviteprotect 「 On/Off 」
❥ .Namelock 「 On/Off 」
❥ .Member 「 On/Off 」
"""


KAC=[cl,ki,ki2,ki3,ki4,ki5]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
Bots = [mid,kimid,ki2mid,ki3mid,ki4mid,ki5mid]
admsa = "uaf602c7210b2abc5227d7e66a102f0d9"
admin = "uaf602c7210b2abc5227d7e66a102f0d9"


mulai = time.time()

wait = {
    "likeOn":True,
    "alwaysRead":False,
    'detectMention2':False,
    'detectMention1':False,
    'detectMention4':False,
    "checkContact":False,
    "checkPost":False,
    'sticker':False,
    "Sambutan":False,
    "kickMention":False,
    "steal":True,
    'pap':{},
    "Reject":{},
    'invite':{},
    "spam":{},
    "sider":{},
    "tag1":"Kamvlet lu njing.... \n Gk usah tag napa.... \n Kurang desahan lu pake tag segala...",
    "tag2":"Gosah Tag Gua.. \n Gw Tupes Lo Mau Apa !!",
    "members":1,
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":50},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':True,
    'alwayRead':False,
    "stickerMention":False,
    'point':False,
    'sidermem':False,
    'message':"꧁❥͜͡❂ོ⟬「 Auto Add 」⟭❂ོ͜͡❥꧂ \n\n ❥ http://line.me/ti/p/~my.name.is.jalu \n ❥ http://line.me/ti/p/~atamu-icek \n ╔═══════════════ \n ║❥ ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽ༵  \n ╚═══════════════",
    "lang":"JP",
    "comment1":"꧁❥͜͡❂ོ⟬「 Auto Like 」⟭❂ོ͜͡❥꧂ \n\n ❥ http://line.me/ti/p/~my.name.is.jalu \n ❥ http://line.me/ti/p/~atamu-icek \n\n╔═══════════════ \n║❥ ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽ༵  \n╚═══════════════",
    "commentOn":True,
    "comment":"Waya waya",
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "winvite":False,
    "cyduk":False,
    "clock":False,
    "cNames":"",
    "cNames":"",
    "displayname":{},
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "mid":{},
    'copy':{},
    'steal':{},
    'gift':{},
    "Simi":{},
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "MProtection":False,
    "protect":False,
    "sendMessage":True,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "welcome":False,
    "re":False
    
    
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{},
    }
    
settings = {
    "simiSimi":{}
    }
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    
cctv2 = {
    "cyduk2":{},
    "point2":{},
    "sidermem2":{}
}    
res = {
    'num':{},
    'us':{},
    'au':{},
    }
    
setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def tagall(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "✮ @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
      cl.sendMessage(msg)
    except Exception as error:
      print error
      
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
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
    
      
  #Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"    
            
def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()      
      
def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': objectId,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudio(self, to_, path):
        M = Message(to=to_,contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True
        
def sendAudioWithURL(self, to_, url):
        path = 'pythonLiness.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e


def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
#------------------------✖ BASYIR ✖-----------------------------#
dangerMessage = ["Cleanse","Group cleansed.","Mulai","!down",".kickall","Mayhem","Kick on","Makasih :d","!kickall","Nuke"]
#------------------------✖ BASYIR ✖-----------------------------#


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 5:
           if wait["autoAdd"] == True:
              cl.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                cl.sendText(op.param1,str(wait["message"]))

        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#-----------------------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = ki2.getGroup(op.param1)
                            except:
                                pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                ki2.updateGroup(G)
                            except:
                                pass
                    if op.param2 in Bots:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                            cl.sendText(op.param1,"Groupname Lock on")
                            c = Message(to=op.param1, from_=None, text=None, contentType=13)
                            c.contentMetadata={'mid':op.param2}
                            cl.sendMessage(c)
#------------------------✖ BASYIR ✖-----------------------------#        
#------------------------✖ BASYIR ✖-----------
#----MemberProtection------#
        if op.type == 19:
            if wait["MProtection"] == True:
                if op.param2 not in Bots and amin:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
#------------------------✖ BASYIR ✖-----------------------------#         
 #------------------------------------
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            Np = cl.getContact(op.param2).pictureStatus
              #              Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nCie cie yang jones ngintip aja cie . . .\nSini napa nes  (-__-)   ")
                                        cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nBisulan tujuh turunan cctv telus . . .\nChat Napa (-__-)   ")
                                        cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nKak ngapain ngintip ? \nSini Dong ih..   ")
                                    cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass   
#------------------------------------
        if op.type == 55:
                try:
                    if cctv2['cyduk2'][op.param1]==True:
                        if op.param1 in cctv2['point2']:
                            Name = cl.getContact(op.param2).displayName
                  #          Np = cl.getContact(op.param2).pictureStatus
              #              Name = summon(op.param2)
                            if Name in cctv2['sidermem2'][op.param1]:
                                pass
                            else:
                                cctv2['sidermem2'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Halo mblo " + "☞ " + Name + " ☜" + "\nNgintip aja cie . . .")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        cl.sendText(op.param1, "Ngintip Mblo " + "☞ " + Name + " ☜" + "\nAwas Tu Mata Bisulan Kebanyakan Ngintip 😠😠 . . .")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    cl.sendText(op.param1, "Anda Tercyduk " + "☞ " + Name + " ☜" + "\nNgapain ngintip ? \nKeliatan Banget Nah Jomblonya..   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass   
#------------------------------------            
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))     
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention1"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + "\n" + str(wait["tag1"]) , cName + "\n" + str(wait["tag2"])]
                     ret_ = "  【ᵃᵘᵗᵒ rᵉˢᵖᵒⁿˢ】 \n"+ random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '3234393',
                                                            'STKTXT': '[]',
                                                            'STKVER': '1',
                                                            'STKID':'35532562'
                                                        }
                                  cl.sendMessage(msg)
                                  break
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["stickerMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy"]
                     ret_ = "     「 AUTO NDESAH 」 \n "  + cName + "\n"+ random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '1395389',
                                                            'STKTXT': '[]',
                                                            'STKVER': '1',
                                                            'STKID':'15356462'
                                                        }
                                  cl.sendMessage(msg)
                                  break
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention4"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Nih Gift !!\n Buat Jones Yang Suka Tag !! "]
                     ret_ = "       【ᵃᵘᵗᵒ rᵉˢᵖᵒⁿˢ】 \n" + cName+ " \n" + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  msg.contentType = 9
                                  msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                                                
                                  cl.sendMessage(msg)                                           
                                  break
#------------------------✖ BASYIR ✖-----------------------------#                                                      
                                  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = cl.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Woii " + cName + ", Dasar Jones Ngetag Mulu!"]
                    balas1 = "Ini Foto Sii Jones Yang Suka Ngetag. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.sendText(msg.to,balas1)
                                  cl.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  cl.sendMessage(msg)                                
                                  break  
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = cl.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["",cName + " Ngapain Ngetag?, ", cName + " Kenapa Tag saya?,  " + cName + "?", "Ada Perlu apa, " + cName + "?","Tag doang tidak perlu., ", "Tersummon -_-, "]
                     ret_ = "**Auto Respond** " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  cl.sendText(msg.to,ret_)
                                  cl.kickoutFromGroup(msg.to,[msg.from_])
                                  break    
                              
#------------------------✖ BASYIR ✖-----------------------------# 
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
                ki.like(url[25:58], url[66:], likeType=1001)
                ki2.like(url[25:58], url[66:], likeType=1001)
                ki3.like(url[25:58], url[66:], likeType=1001)
                ki4.like(url[25:58], url[66:], likeType=1001)
                ki5.like(url[25:58], url[66:], likeType=1001)
                cl.comment(url[25:58], url[66:], wait["comment1"])
                ki.comment(url[25:58], url[66:], wait["comment1"])
                ki2.comment(url[25:58], url[66:], wait["comment1"])
                ki3.comment(url[25:58], url[66:], wait["comment1"])
                ki4.comment(url[25:58], url[66:], wait["comment1"])
                ki5.comment(url[25:58], url[66:], wait["comment1"])
#--------------------------------        
            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)      
            if msg.contentType == 13:
                  if msg.from_ in admin:
                    if wait["wblacklist"] == True:
                       if msg.contentMetadata["mid"] in wait["blacklist"]:
                         cl.sendText(msg.to,"Is already banned")
                       wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"has been banned by :")

            elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                       del wait["blacklist"][msg.contentMetadata["mid"]]
                       cl.sendText(msg.to,"Has been Unbanned deleted by :")
                       wait["dblacklist"] = False

                    else:
                       wait["dblacklist"] = False
                       kk.sendText(msg.to,"is not in banned!")
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)        
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            cl.sendText(op.param1,"Hallo " + cl.getContact(op.param2).displayName + "\nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            cl.sendMessage(c)  
            cl.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            cl.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            cl.sendText(op.param1,"Good Bye " + cl.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1329191",
                                    "STKVER": "1" }                
            cl.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
#------------------------✖ BASYIR ✖-----------------------------#
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "uaf602c7210b2abc5227d7e66a102f0d9":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
                           
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         cl.findAndAddContactsByMid(invite)
                                         cl.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "POST URL: \n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

 #---------------------------------------------------------
#--------------------------------------------------------------------     
            elif msg.text in ["Key 3","help 3","Help 3"]:
                cl.sendText(msg.to,admin2Message+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Key 5","help 5","Help 5"]:
                cl.sendText(msg.to,groupMessage+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Key","help","Help"]:
                cl.sendText(msg.to,helpMessage+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Key 7","help 7","Help 7"]:
                cl.sendText(msg.to,selfMessage+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Key 4","help 4","Help 4"]:
                cl.sendText(msg.to,setMessage+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Key 6","help 6","Help 6"]:
                cl.sendText(msg.to,mediaMessage+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#                
            elif msg.text in ["Key 2","help 2","Help 2"]:
                cl.sendText(msg.to,adminMessage+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#                
            elif msg.text in ["Key 1","help 1","Help 1"]:
                cl.sendText(msg.to,protectMessage+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
 #---------------------------------------------------------
        
                
 #---------------------------------------------------------
            elif "Mbut on" in msg.text:
                try:
                    del cctv2['point2'][msg.to]
                    del cctv2['sidermem2'][msg.to]
                    del cctv2['cyduk2'][msg.to]
                except:
                    pass
                cctv2['point2'][msg.to] = msg.id
                cctv2['sidermem2'][msg.to] = ""
                cctv2['cyduk2'][msg.to]=True
                wait["Mbut"] = True
                cl.sendText(msg.to,"「 Detect Sider 」\nType: Sider Cek \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif "Mbut off" in msg.text:
                if msg.to in cctv2['point2']:
                    cctv2['cyduk2'][msg.to]=False
                    wait["Mbut"] = False
                    cl.sendText(msg.to,"「 Detect Sider 」\nType: Sider Cek \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to, "Cek dulu mbut guoblok si 😇")    
         
 #--------------------------------------------------------
 #---------------------------------------------------------         
            elif msg.text in ["Pp","pp"]:
                    h = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
         
            elif msg.text in ["Cover"]:
                    h = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)          
                    path = str(cu)
                    cl.sendImageWithURL(msg.to, path)
                    
            elif msg.text in ["Mybio"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Myvid"]:
                    h = cl.getContact(mid)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = cl.getContact(mid)
                    cl.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
 
            elif msg.text in ["Invite:on"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
#---------------------------------------------------------
            elif ("Gn:" in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn:","")
                    ki.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok👈")
 #---------------------------------------------------------
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.name = msg.text.replace("Gn ","")
                    cl.updateGroup(group)
                else:
                    cl.sendText(msg.to,"Can not be used for groups other than")
                    
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
                
            elif "Pp group" in msg.text:
                group = cl.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                cl.sendImageWithURL(msg.to,path)
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = cl.getGroup(msg.to)
                cl.sendText(msg.to, "[ID Grup : ]\n" + gid.id)   
#---------------------------------------------------------
#------------------------✖ BASYIR ✖-----------------------------#                    
            elif msg.text in ["Friendlist"]:    
                contactlist = cl.getAllContactIds()
                kontak = cl.getContacts(contactlist)
                num=1
                msgs="══════List Friend══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n══════List Friend══════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Memlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="══════List Member══════"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n══════List Member══════\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Friendlistmid"]: 
                gruplist = cl.getAllContactIds()
                kontak = cl.getContacts(gruplist)
                num=1
                msgs="══════List FriendMid══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n══════List FriendMid══════\n\nTotal Friend : %i" % len(kontak)
                cl.sendText(msg.to, msgs+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            
 #---------------------------------------------------------
 #------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Conban","Blc","Contact ban"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "═══════List Blacklist══════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n══════List Blacklist══════\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
#------------------------✖ BASYIR ✖-----------------------------#
#---------------------------------------------------------
            elif "Kick:" in msg.text:
                midd = msg.text.replace("Kick:","")
                cl.kickoutFromGroup(msg.to,[midd])
#---------------------------------------------------------
            elif "Invite:" in msg.text:
                midd = msg.text.replace("Invite:","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#---------------------------------------------------------          
            elif msg.text.lower() == 'mybot':
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                cl.sendMessage(msg)
                
            
            elif "Bot1" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif "Bot2" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)
            elif "Bot3" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki3mid}
                ki3.sendMessage(msg)
            elif "Bot4" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki4mid}
                ki4.sendMessage(msg)
            elif "Bot5" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': ki5mid}
                ki5.sendMessage(msg)
            
#---------------------------------------------------------
            
            elif msg.text in ["Bot1 Gift","Bot1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                cl.sendMessage(msg)

            elif msg.text in ["Bot2 Gift","Bot2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)
                
            elif msg.text in ["Bot3 Gift","Bot3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki3.sendMessage(msg)
                
            elif msg.text in ["Bot4 Gift","Bot4 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki4.sendMessage(msg)
                
            elif msg.text in ["Bot5 Gift","Bot5 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki5.sendMessage(msg)
                
                
            elif msg.text.lower() == 'allgift':
            	msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki2.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki3.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki4.sendMessage(msg)
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                ki5.sendMessage(msg)
                

            elif msg.text in ["B Cancel","Cancel dong","B cancel"]:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
#---------------------------------------------------------

            elif msg.text in ["Cancel","cancel"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No invites👈")
                        else:
                            cl.sendText(msg.to,"Invite people inside not👈")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada undangan👈")
                    else:
                        cl.sendText(msg.to,"invitan tidak ada")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
    #---------------------------------------------------------            
            elif msg.text in ["Link on"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL open")
                    else:
                        cl.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            elif msg.text in ["Link off"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"URL close")
                    else:
                        cl.sendText(msg.to,"URL close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
 #---------------------------------------------------------
 
            elif "Ginfo" == msg.text:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[Nama]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nAnggota:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
               
 #---------------------------------------------------------        
            elif "Contact" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.to}
                cl.sendMessage(msg)
            elif "Mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif "Bot1 mid" == msg.text:
                ki.sendText(msg.to,kimid)
            elif "Bot2 mid" == msg.text:
                ki2.sendText(msg.to,ki2mid)
            elif "Bot3 mid" == msg.text:
                ki3.sendText(msg.to,ki3mid)
            elif "Bot4 mid" == msg.text:
                ki4.sendText(msg.to,ki4mid)
            elif "Bot5 mid" == msg.text:
                ki5.sendText(msg.to,ki5mid)
             
            elif "All mid" == msg.text:
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                ki3.sendText(msg.to,ki3mid)
                ki4.sendText(msg.to,ki4mid)
                ki5.sendText(msg.to,ki5mid)
                
 #---------------------------------------------------------
 
            elif "Reboot" in msg.text:
                print "[Command]Reboot"
                try:
                 cl.sendText(msg.to,"Please waiting...")
                 cl.sendText(msg.to,"Restarted done !!")
                 restart_program()
                except:
                 cl.sendText(msg.to,"Please wait")
                restart_program()
                pass
 
            elif "TL:" in msg.text:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "All:" in msg.text:
                string = msg.text.replace("All:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
              #---------------------------------------------------------
            elif "Allbio:" in msg.text:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
#---------------------------------------------------------       
            elif "Myname:" in msg.text:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to," Done Update Name " + string + "👈")

#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag","Ats","Hem","Muach"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                      tagall(msg.to, nama)
                  if jml > 100 and jml < 500:
                      for i in range(0,99):
                          nm1 += [nama[i]]
                      tagall(msg.to, nm1)
                      for j in range(100, len(nama)-1):
                          nm2 += [nama[j]]
                      tagall(msg.to, nm2)
                      for k in range(200, len(nama)-1):
                          nm3 += [nama[k]]
                      tagall(msg.to, nm3)
                      for l in range(300, len(nama)-1):
                          nm4 += [nama[l]]
                      tagall(msg.to, nm4)
                      for m in range(400, len(nama)-1):
                          nm5 += [nama[m]]
                      tagall(msg.to, nm5)
                  cnt = Message()
                  cnt.text = "AUTO TAG BY : ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽཽ༵༵"
                  cnt.to = msg.to
                  cl.sendMessage(cnt)
                  if jml > 500:
                      cnt = Message()
                      cnt.text = "AUTO TAG BY : ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽཽ༵"
                      cnt.to = msg.to
                      cl.sendMessage(cnt)
                      
#-------------Fungsi Tagall User Start---------------#
            elif msg.text in ["Dor","Crot"]:
                group = ki.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    ki.sendMessage(msg)
                except Exception as error:
                    print error
#-------------------------------------------------------------
            elif "tagall" == msg.text.lower():
                 group = cl.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1): 
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)                 
                 if jml > 200 and jml < 300:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, len(nama)-1):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                 if jml > 300  and jml < 400:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, len(nama)-1):
                    	nm4 += [nama[l]]
                    summon(msg.to, nm4)
                 if jml > 400  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members" +"\n\nRead time: " + datetime.today().strftime('%H:%M:%S')
                 cnt.to = msg.to
                 cl.sendMessage(cnt)                 

#-------------Fungsi Tag All Finish--------------#
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        cl.sendText(msg.to, str(njer))
#---------------------------------------------------------
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass           

#------------------------✖ BASYIR ✖-----------------------------#
            elif "Broadcast: " in msg.text:
		bc = msg.text.replace("Broadcast: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
			cl.sendText(i,"「 BROADCAST 」\n"+bc+msg)
			msg.contentType = 13
		    msg.contentMetadata = {"mid":admin}
		    cl.sendText(msg.to,"Success BC BosQ"+"\n\n"+ datetime.today().strftime('%H:%M:%S'))
		else:
		    cl.sendText(msg.to,"Khusus Admin")
#------------------------✖ BASYIR ✖-----------------------------#
            elif "Cbroadcast: " in msg.text:
                bc = msg.text.replace("Cbroadcast: ","")
                gid = cl.getAllContactIds()
                for i in gid:
                    cl.sendText(i, bc)
#------------------------✖ BASYIR ✖-----------------------------#
#-----------------------------------------
            elif "Mbroadcast: " in msg.text:
		bc = msg.text.replace("Mbroadcast: ","")
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		for i in mi_d:
		    cl.sendText(i,bc+"\n"+ datetime.today().strftime('%H:%M:%S'))
		cl.sendText(msg.to,"Success BC to: "+str(len(mi_d))+" members Boss")
#---------------------------------------------------------
#---------------------------------------------------------
            
            elif "1name:" in msg.text:
                string = msg.text.replace("1name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to," Done update names " + string + "👈")

            elif "2name:" in msg.text:
                string = msg.text.replace("2name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki2.getProfile()
                    profile.displayName = string
                    ki2.updateProfile(profile)
                    ki2.sendText(msg.to," Done update names " + string + "👈")
                    
            elif "3name:" in msg.text:
                string = msg.text.replace("3name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki3.getProfile()
                    profile.displayName = string
                    ki3.updateProfile(profile)
                    ki3.sendText(msg.to," Done update names " + string + "👈")
                    
            elif "4name:" in msg.text:
                string = msg.text.replace("4name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki4.getProfile()
                    profile.displayName = string
                    ki4.updateProfile(profile)
                    ki4.sendText(msg.to," Done update names " + string + "👈")
                   
            elif "5name:" in msg.text:
                string = msg.text.replace("5name:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki5.getProfile()
                    profile.displayName = string
                    ki5.updateProfile(profile)
                    ki5.sendText(msg.to," Done update names " + string + "👈")
                    
                    
#---------------------------------------------------------
            elif "Mid:" in msg.text:
                mmid = msg.text.replace("Mid:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
#---------------------------------------------------------
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Contact 」\nType: Cek Contact \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'linkprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                    	cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'autojoin on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock on" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"「 Name Lock  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"「 Name Lock  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock off" in msg.text:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"「 Name Lock  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"「 Name Lock  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Member on"]:
                if msg.from_ in admin:
                    if wait["MProtection"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                        else:
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wait["MProtection"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                        else:
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Member off"]:
                if msg.from_ in admin:
                    if wait["MProtection"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                        else:
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        wait["MProtection"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                        else:
                            cl.sendText(msg.to,"「 Protect Member 」\nType: Protect Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
 #---------------------------------------------------------
            elif msg.text.lower() == 'blocklist':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait !!")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["Protect Hight","Mode on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                    else:
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                    else:
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                if wait["MProtection"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Member Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                    else:
                        cl.sendText(msg.to,"「 Member Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                else:
                    wait["MProtection"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Member Protect  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
            elif msg.text in ["Allprotect off","Mode Off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Invite Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))  
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                    	cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'autojoin off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Join 」\nType: Join Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                        
#------------------------✖ BASYIR ✖-----------------------------#
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Welcome on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sambutan Di Aktifkanヾ(*´���｀*)ﾉ"+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Sambutan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Onヽ(´▽｀)/"+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Welcome off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Welcome  」\nType: Welcome Group\nStatus: ♛ᶱᶰ  \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Welcome  」\nType: Welcome Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                  
 #---------------------------------------------------------
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
              	 	cl.sendText(msg.to,"「 Protect  」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Linkprotect off","linkprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr  」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                        
            elif msg.text in ["Inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                     	cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Block Qr 」\nType: Protect Group\nStatus: ♛ᶱᶠᶠ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect 」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
       	     		cl.sendText(msg.to,"「 Cancel Protect 」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Cancel Protect 」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Cancel Protect 」\nType: Protect Group\nStatus: ♛ᶱᶰ \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Group cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Autoleave on","Autoleave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Autoleave off","Autoleave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Leave 」\nType: Leave Group \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Detect Share 」\nType: Share Group \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                        
            #------------------------✖ BASYIR ✖-----------------------------#
            elif "Set" == msg.text:
                md = ""
                if wait["contact"] == True: md+="༇❥ Contact : On\n"       
                else: md+="༇❥ Contact : Off\n"      
                if wait["autoJoin"] == True: md+="༇❥ Auto join : On\n" 
                else: md +="༇❥ Auto join : Off\n"
                if wait["autoCancel"]["on"] == True:md+="༇❥ Group Cancel : " + str(wait["autoCancel"]["members"]) + " \n"     
                else: md+= "༇❥ Group Cancel : Off\n"  
                if wait["leaveRoom"] == True: md+="༇❥ Auto leave : On\n"   
                else: md+="༇❥ Auto leave : Off\n"
                if wait["timeline"] == True: md+="༇❥ Auto Share : On\n"  
                else:md+="༇❥ Auto Share : Off\n" 
                if wait["commentOn"] == True: md+="༇❥ Comment : On\n"   
                else:md+="༇❥ Comment : Off\n"    
                if wait["autoAdd"] == True: md+="༇❥ Auto add : On\n"  
                else:md+="༇❥ Auto add : Off\n"   
                if wait["likeOn"] == True: md+="༇❥ Auto like : On\n"
                else:md+="༇❥ Auto like : Off\n" 
                if wait["Sambutan"] == True: md+="༇❥ Welcome message : On\n"  
                else:md+="༇❥ Welcome message : Off\n"   
                if wait["detectMention1"] == True: md+="༇❥ Respon1 : On\n"
                else:md+="༇❥ Respon1 : Off\n" 
                if mimic["status"] == True: md+="༇❥ Mimic : On\n"
                else:md+="༇❥ Mimic : Off\n" 
                if wait["stickerMention"] == True: md+="༇❥ Sticker mention : On\n"   
                else: md+="༇❥ Sticker mention : Off\n"
                if wait["detectMention2"] == True: md+="༇❥ Respon2 : On\n"  
                else:md+="༇❥ Respon2 : Off\n" 
                if wait["kickMention"] == True: md+="༇❥ Kick Mention : On\n"  
                else:md+="༇❥ Kick Mention : Off\n" 
                if wait["detectMention4"] == True: md+="༇❥ Gift mention : On\n"   
                else: md+="༇❥ Gift mention : Off\n"
                ma = ""
                if wait["protect"] == True: ma+="༇❥ Protect : On\n"       
                else: ma+="༇❥ Protect : Off\n"      
                if wait["cancelprotect"] == True: ma+="༇❥ Cancel protect : On\n" 
                else: ma +="༇❥ Cancel protect : Off\n"
                if wait["inviteprotect"] == True: ma+="༇❥ Invite protect : On\n"   
                else: ma+="༇❥ Invite protect : Off\n"
                if wait["linkprotect"] == True: ma+="༇❥  Qr protect : On\n"  
                else:ma+="༇❥ Qr protect : Off\n" 
                if wait["MProtection"] == True: ma+="༇❥ MProtection : On\n"  
                else:ma+="༇❥ MProtection : Off\n" 
                if wait["pname"]: ma+="༇❥ Namelock : On" 
                else: ma +="༇❥ Namelock : Off"
                cl.sendText(msg.to,"[✧] Selfbot Status:\n\n"+md+"\n[✧] Group Status:\n\n"+ma + "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
 #------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text.lower() == 'runtime':
                cl.sendText(msg.to,"「Please wait..」")
                eltime = time.time() - mulai
                van = "Type : Bot \nStatus : Aktif \nMybot Aktif Seconds\n"+waktu(eltime)
                cl.sendText(msg.to,van+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
#-----------------------------------------------
            elif "Center @bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye😘 "  +  str(ginfo.name)  + "")
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------
#---------------------------------------------------------
 
            elif "/removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        ki.removeAllMessages(op.param2)
                        ki2.removeAllMessages(op.param2)
                        ki3.removeAllMessages(op.param2)
                        ki4.removeAllMessages(op.param2)
                        ki5.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error")      
#------------------------✖ BASYIR ✖-----------------------------#                
#---------------------------------------------------------
#---------------------------------------------------------
            elif "Me" == msg.text:
                       msg.contentType = 13
                       msg.contentMetadata = {'mid': msg.from_}
                       cl.sendMessage(msg)
                       eltime = time.time() - mulai
                       van = "Bot has been active "+waktu(eltime)
                       cl.sendText(msg.to,van+"\n\n"+ datetime.today().strftime('%H:%M:%S')) 
#------------------------✖ BASYIR ✖-----------------------------#
                
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid':"uaed33f60ed0b0d5ee5b33cc5c979d770"}
                msg.contentMetadata = {'mid':"ucb633967bafc99fc34771c7515a1c908"}
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendText(msg.to,"⏫⏫⏫⏫⏫⏫⏫⏫")
      #---------------------------------------------------------          
            elif msg.text in ["Cancelall"]:
                if msg.from_ in admin:
                  gid = cl.getGroupIdsInvited()
                  for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to," 😈😈😈😈")	
#---------------------------------------------------------          
      
            elif msg.text in ["Salam"]:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Jawab salam"]:
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam perdamaian" in msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Assalamu'alaikum")
                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                cl.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam3","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"maaf kalo gak sopan")
                    cl.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                    cl.sendText(msg.to,"hehehhehe")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                cl.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                cl.sendText(msg.to,"Nah salamnya jawab sendiri dah")                    
            elif "Set album:" in msg.text:
                gid = msg.text.replace("Set album:","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album??")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak👈")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "æžš\n"
                        else:
                            mg += str(y["title"]) + ":0 Pieces\n"
                    cl.sendText(msg.to,mg)
            elif msg.text in ["Bye Allgroup"]:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                gid = ki3.getGroupIdsJoined()
                gid = ki4.getGroupIdsJoined()
                gid = ki5.getGroupIdsJoined()
                for i in gid:
                    ki.leaveGroup(i)
                    ki2.leaveGroup(i)
                    ki3.leaveGroup(i)   
                    ki4.leaveGroup(i)   
                    ki5.leaveGroup(i)   
                    
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Bot Sudah Keluar Di semua grup")
                else:
                    cl.sendText(msg.to,"He declined all invitations")
   #------------------------✖ BASYIR ✖-----------------------------#
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"「 Detect Sider 」\nType: Read Sider \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to,"「 Detect Sider 」\nType: Read Sider \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to, "Cek dulu kak set nya 😇")    
         
#------------------------✖ BASYIR ✖-----------------------------#
            elif "Album" in msg.text:
                gid = msg.text.replace("Album","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tidak ada album")
                    else:
                        cl.sendText(msg.to,"Dalam album tidak")
                else:
                    if wait["lang"] == "JP":
                        mg = "Berikut ini adalah album dari target"
                    else:
                        mg = "Berikut ini adalah subjek dari album"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "\n"
                        else:
                            mg += str(y["title"]) + ":0 pieces\n"
            elif "Hapus album " in msg.text:
                gid = msg.text.replace("Hapus album ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["gid"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album🛡")
            elif msg.text.lower() == 'group id':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Clear ban","Clearban"]:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Removed banlist user target succes."+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))       
                ki.sendText(msg.to,"Removed banlist user target succes."+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))       
                ki2.sendText(msg.to,"Removed banlist user target succes."+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
   #     		ki3.sendText(msg.to,"Removed banlist user target succes."+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))       
        	#	ki4.sendText(msg.to,"Removed banlist user target succes."+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
			#	ki5.sendText(msg.to,"Removed banlist user target succes."+ "\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))              
                    
            elif "Album deleted:" in msg.text:
                gid = msg.text.replace("Album deleted:","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Soal album telah dihapus👈")
                else:
                    cl.sendText(msg.to,str(i) + "Hapus kesulitan album👈")
#------------------------✖ BASYIR ���-----------------------------#
            elif msg.text in ["Autoadd on","Autoadd:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Autoadd off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"「 Auto Add 」\nType: Add Friends\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
#----------------------------------------------------------
            elif "Tag1 set: " in msg.text:
                wait["tag1"] = msg.text.replace("Tag1 set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Tag changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Tag1 cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Tag1 change to\n\n" + wait["tag1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Tag1 saat ini:\n\n" + wait["tag1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#            
            elif "Tag2 set: " in msg.text:
                wait["tag2"] = msg.text.replace("Tag2 set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Tag2 changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Tag2 cek","è‡ªå‹•è¿½åŠ å•å€™èªžç��ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Tag2 change to\n\n" + wait["tag2"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Tag2 saat ini:\n\n" + wait["tag2"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#           
            elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                cl.sendText(msg.to,"We changed the message"+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#    
            elif "Com1 set: " in msg.text:
                wait["comment1"] = msg.text.replace("Com1 set: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Comment1 changed\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Com1 cek","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Comment1 saat ini:\n\n" + wait["comment1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"Comment1 saat ini:\n\n" + wait["comment1"]+"\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#        
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"「 Read Chat 」\nType: Always Read Chat \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"「 Read Chat 」\nType: Always Read Chat \nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))         
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Glist1","Groups1","Group1"]:
                gid = ki.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠○⏩ %s\n" % (ki.getGroup(i).name +"➡["+str(len(ki.getGroup(i).members))+"]")
                ki.sendText(msg.to,"╠══════════════════\n╠ 👑👑👑 My Group 👑👑👑\n╠══════════════════\n"+ h +"\n👑 Total Group 👑 = " +""+str(len(gid))+"")

            elif "Bot1 gurl" in msg.text:
                if msg.toType == 1:
                    gid = msg.text.replace("gurl","")
                    gurl = ki.reissueGroupTicket(gid)
                    ki.sendText(msg.to,"line://ti/g" + gurl)
                else:
                    ki.sendText(msg.to,"error")
			
            elif "gurl" in msg.text:
                if msg.toType == 2:
                    gid = msg.text.replace("gurl","")
                    gurl = cl.reissueGroupTicket(gid)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the blacklistô€œô€…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the blacklistô€œô€…”👈")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Already onn")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"👉Jam on👈")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Already off...")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Adalah Off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Ini telah diubah🛡\n\n" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui👈")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Nama")

            elif "Nk " in msg.text:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki5.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki5.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
#------------------------✖ BASYIR ✖---------
            elif "Idline: " in msg.text:
                msgg = msg.text.replace('Idline: ','')
                conn = cl.findContactsByUserid(msgg)
                if True:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': conn.mid}
                    cl.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                    cl.sendMessage(msg)
#-----------------------------------------------------------
#-----------------------------------------------------------
            elif cms(msg.text,["Add"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'uaed33f60ed0b0d5ee5b33cc5c979d770'}
                cl.sendText(msg.to,"❂•••••••••✧••••••••••❂")
                cl.sendMessage(msg)
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ucb633967bafc99fc34771c7515a1c908'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"❂••••••••✰•✰••••••••❂")
#---------------------------------------------

            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                cl.sendText(msg.to,"「 Detect Cctv 」\nType: Cek Cctv \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
                print "Setview"

            elif msg.text in ["Glist","Groups","Group"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠○⏩ %s\n" % (cl.getGroup(i).name +"➡["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"╠══════════════════\n╠ 👑👑👑 My Group 👑👑👑\n╠══════════════════\n"+ h +"\n👑 Total Group 👑 = " +""+str(len(gid))+"")
			
            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔══════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠══════════════════════\n╠➩"
                        grp = '\n╠➩ '.join(str(f) for f in dataResult)
                        total = '\n╠══════════════════════\n╠➩ Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚══════════════════════"
                        cl.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        cl.sendText(msg.to,"「 Auto Check 」\nType: Auto Check Cctv \nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))                        
                    else:
                        cl.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"
                        
#-----------------------[Add Staff Section]------------------------
            elif "Add staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)

                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Add Staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Add Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove Staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove Staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Remove staff @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Remove staff @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Stafflist","stafflist"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "=>" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"								
#-----------------------------------------------------------

            elif ("Fuck " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           ki2.kickoutFromGroup(msg.to,[target])
                       except:
                           ki2.sendText(msg.to,"Error")
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)

            elif "Vk " in msg.text:                  
                       nk0 = msg.text.replace("Beb ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ki.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Good Bye")

#----------------------------------------------------------------
            elif "InviteMeTo: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("InviteMeTo: ","")
                    if gid == "":
                        cl.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ki.findAndAddContactsByMid(msg.from_)
                            ki.inviteIntoGroup(gid,[msg.from_])
                        except:
                            ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#-----------------------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
#-----------------------------------------------
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        print "Spamtag Berhasil."

#==============================================
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam') 
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam') 
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam') 
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam') 
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam') 
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam') 
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(g.mid,'spam')
                       cl.sendText(msg.to, "Done"+"\n\n"+ datetime.today().strftime('%H:%M:%S'))
                       print " Spammed !"

#-----------------------------------
                        
#========================== FOR COMMAND BOT FINISHED =============================#                        
            elif 'Say' in msg.text:
                 psn = msg.text.replace("Say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')          
                        
            elif ("Mimic add " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Mimic del " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        cl.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Mimic list"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"Reply Message on")
                    else:
                        cl.sendText(msg.to,"Already on 🎵")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"Reply Message off")
                    else:
                        cl.sendText(msg.to,"Sudah off")
            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,"Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,"Your Account Has Been Spammed !")  
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"

            elif "Hallo " in msg.text:
                midd = msg.text.replace("Hallo ","")
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ki.sendText(g.mid,[miid] + "Your Account Has Been Spammed !")
                       ki2.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki3.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       ki4.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")
                       ki5.sendText(g.mid,[midd] + "Your Account Has Been Spammed !")  
                       cl.sendText(msg.to, "Done")
                       print " Spammed !"
#-----------------------------------------------------------)
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Bosque")
                   except:
                      pass
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Target Unlocked")
                            except:
                                cl.sendText(msg.to,"Error")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									wait["blacklist"][target] = True
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Locked")
                                except:
                                    kk.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
									del wait["blacklist"][target]
									f=codecs.open('st2__b.json','w','utf-8')
									json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
									cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    kk.sendText(msg.to,"Error")
#-----------------------------------------------------------

            elif "Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
                                    
#-----------------------------------------------------------

            elif "B1copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki.sendText(msg.to, "Succes Copy profile")
                                except Exception as e:
                                    print e
                                    

            elif msg.text in ["Mybackup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "backup done")
                except Exception as e:
                    cl.sendText(msg.to, str (e))
                    
            elif msg.text in ["Backup"]:
                try:
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    ki2.updateDisplayPicture(backup.pictureStatus)
                    ki2.updateProfile(backup)
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#-----------------------------------------------------------
            elif "Mban:" in msg.text:
                midd = msg.text.replace("Mban:","")
                wait["blacklist"][midd] = True
		cl.sendText(msg.to,"Target Lock")
#-----------------------------------------------------<------
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------

            
            elif msg.text in ["Dsp","Sp","Speed",".speed"]:
                cl.sendText(msg.to, "「 Debug Speed 」\n☼Type: speed\n☼Testing....")
                start = time.time()
                for i in range(3000):
                    1+1 
                elsp = time.time() - start
                cl.sendText(msg.to, "「 Debug Speed」\nType: speed\nTime taken: %s" % (elsp))   
                ki.sendText(msg.to, "「 Debug Speed」\nType: speed\nTime taken: %s" % (elsp))   
                ki2.sendText(msg.to, "「 Debug Speed」\nType: speed\nTime taken: %s" % (elsp))   
               # cl.sendText(msg.to, "「Please wait..」")
                elapsed_time = time.time() - start
  #              cl.sendText(msg.to, "♬「Speed : 0.04 - 0.07」\n♬「Speed is : %sseconds" % (elapsed_time))
 #               ki.sendText(msg.to, "♬「Speed : 0.04 - 0.07」\n♬「Speed is : %sseconds" % (elapsed_time))
#                ag.sendText(msg.to, "♬「Speed : 0.04 - 0.07」\n♬「Speed is : %sseconds" % (elapsed_time))

            elif msg.text in ["Sp set"]:
                cl.sendText(msg.to, "「 Debug Speed 」\n☼Type: Speed Setting\n☼Testing....")
              #  cl.sendText(msg.to, "=====「Speed Setting」=====")
                start = time.time()
                start2 = time.time()
                start3 = time.time()
                start4 = time.time()             
                start5 = time.time()             
                start6 = time.time()             
                start7 = time.time()    
                start8 = time.time()             
                start9 = time.time()             
                start10 = time.time()                         
                for i in range(3000):
                    1+1
                elsp = time.time() - start          
                elsp2 = time.time() - start2
                elsp3 = time.time() - start3
                elsp4 = time.time() - start4
                elsp5 = time.time() - start5
                elsp6 = time.time() - start6
                elsp7 = time.time() - start7
                elsp8 = time.time() - start8
                elsp9 = time.time() - start9
                elsp10 = time.time() - start10    
                cl.sendText(msg.to, "「 Debug Speed」\nType: Contact\nTime taken: %s" % (elsp))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: AutoJoin\nTime taken: %s" % (elsp2))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: AutoCancel\nTime taken: %s" % (elsp3))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: LeaveRoom\nTime taken: %s" % (elsp4))   
                cl.sendText(msg.to, "「 Debug Speed」\nType: Timeline\nTime taken: %s" % (elsp5))                
                cl.sendText(msg.to, "「 Debug Speed」\nType: AutoAdd\nTime taken: %s" % (elsp6))                
                cl.sendText(msg.to, "「 Debug Speed」\nType: Protect\nTime taken: %s" % (elsp7))    
                cl.sendText(msg.to, "「 Debug Speed」\nType: Linkprotect\nTime taken: %s" % (elsp8))        
                cl.sendText(msg.to, "「 Debug Speed」\nType: Inviteprotect\nTime taken: %s" % (elsp9))      
                cl.sendText(msg.to, "「 Debug Speed」\nType: Cancelprotect\nTime taken: %s" % (elsp10))     
                                                     
#-----------------------------------------------------------
            elif msg.text.lower() == 'respons':
                profile = ki.getProfile()
                text = profile.displayName + " WE ARE ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽ༵ "
                ki.sendText(msg.to, text)
                profile = ki2.getProfile()
                text = profile.displayName + " WE ARE ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽ༵"
                ki2.sendText(msg.to, text)
                profile = ki3.getProfile()
                text = profile.displayName + " WE ARE ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽ༵"
                ki3.sendText(msg.to, text)
                profile = ki4.getProfile()
                text = profile.displayName + " WE ARE ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽ༵"
                ki4.sendText(msg.to, text)
                profile = ki5.getProfile()
                text = profile.displayName + " WE ARE ༆࿋ོ༙P̶̶̷̺̟͎͎͓͓͆̽̽o̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽t̶̶̷̺̟͎͎͓͓͆̽̽e̶̶̷̺̟͎͎͓͓͆̽̽r̶̶̷̺̟͎͎͓͓͆̽̽ᴮᵒᵗ྄࿐ཽ༵"
                ki5.sendText(msg.to, text)
#-------------------------------------------------------------------

#------------------------------------------------------------------	
            elif "Cover @" in msg.text:            
                print "[Command]Cover executing"
                _name = msg.text.replace("Cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]Cover executed"			
#------------------------------------------------------------------
            elif "Pic @" in msg.text:            
                print "[Command]Pic executing"
                _name = msg.text.replace("Pic @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]Pic executed"
			

            elif "Getbio " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage+"\n\n"+ datetime.today().strftime('%H:%M:%S'))
                except:
                    cl.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage+"\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Getname " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName+"\n\n"+ datetime.today().strftime('%H:%M:%S'))
                except:
                    cl.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName+"\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Getprofile " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    cl.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    cl.sendText(msg.to,"Profile Picture " + contact.displayName)
                    cl.sendImageWithURL(msg.to,image)
                    cl.sendText(msg.to,"Cover " + contact.displayName)
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact " in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
 #------------------------------------------------------------------
 #------------------------------------------------------------------
            elif msg.text in ["Gcreator:inv"]:
              if msg.toType == 2:
                 ginfo = cl.getGroup(msg.to)
                 gCreator = ginfo.creator.mid
                 try:
                    cl.findAndAddContactsByMid(gCreator)
                    cl.inviteIntoGroup(msg.to,[gCreator])
                    print "success inv gCreator"
                 except:
                    pass
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif msg.text in ["Bans:on"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unbans:on"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'mcheck':
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 Nothing in the blacklist")
                else:
                    cl.sendText(msg.to,"􀜁􀇔􏿿 following is a blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "➡" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'banlist':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += "➡" +cl.getContact(mm).displayName + "\n"
                    cl.sendText(msg.to,cocoa + "Daftar Hitam")
            elif msg.text.lower() == 'kill':
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        ki.sendText(msg.to,"Daftar hitam pengguna tidak memiliki")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            ki.kickoutFromGroup(msg.to,[jj])
                            ki2.kickoutFromGroup(msg.to,[jj])
                            ki3.kickoutFromGroup(msg.to,[jj])
                            ki4.kickoutFromGroup(msg.to,[jj])
                            ki5.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuke" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuke","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"Just some casual cleansing ")
                    ki2.sendText(msg.to,"Group cleansed.")
                    ki3.sendText(msg.to,"Fuck you !")
                    ki4.sendText(msg.to,"Fuck you !")
                    ki5.sendText(msg.to,"Fuck you !")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found.")
                        ki2.sendText(msg.to,"Not found.")
                        ki3.sendText(msg.to,"Not found.")
                        ki4.sendText(msg.to,"Not found.")
                        ki5.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[ki,ki2,ki3,ki4,ki5]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                ki2.sendText(msg,to,"Group cleanse")
                                ki3.sendText(msg,to,"Group cleanse")
                                ki4.sendText(msg,to,"Group cleanse")
                                ki5.sendText(msg,to,"Group cleanse")
#=====================================
                    
            elif "Mayhem" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mayhem","")
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    ki.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n' abort' to abort♪")
                    ki.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\n/ˌhələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not Found")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[ki,ki2,ki3,ki4,ki5]
                               	   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done \n"+ datetime.today().strftime('%H:%M:%S'))

#-----------------------------------------------------------

            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled👈")
    
            elif msg.text in ["Mangat","B"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
                    cl.sendText(msg.to,"B")
            elif "Album" in msg.text:
                try:
                    albumtags = msg.text.replace("Album","")
                    gid = albumtags[:33]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "We created an album👈")
                except:
                    cl.sendText(msg.to,"Error")
                    
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    amid = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbumF(msg.to,name,amid)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass			

#-----------------------------------------------
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Autorespon:on","Respon1 on","Respon:on"]:
                wait["detectMention1"] = True
                cl.sendText(msg.to,"「 Detect Mention1 」\nType: Respon Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
              
            elif msg.text in ["Autorespon:off","Respon1 off","Respon:off"]:
                wait["detectMention1"] = False
                cl.sendText(msg.to,"「 Detect Mention1 」\nType: Respon Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Respon2 on"]:
                    wait["detectMention2"] = True
                    cl.sendText(msg.to,"「 Detect Mention2 」\nType: Respon Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Pbrespon on"]:
                wait["stickerMention"] = True
                cl.sendText(msg.to,"「 Sticker Mention 」\nType: Respon Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
              
            elif msg.text in ["Pbrespon off"]:
                wait["stickerMention"] = False
                cl.sendText(msg.to,"「 Sticker Mention 」\nType: Respon Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Respon4 on"]:
                wait['detectMention4'] = True
                cl.sendText(msg.to,"「 Gift Mention」\nType: Respon Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Respon4 off"]:
                wait['detectMention4'] = False
                cl.sendText(msg.to,"「 Gift Mention 」\nType: Respon Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Respon2 off"]:
                    wait["detectMention2"] = False
                    cl.sendText(msg.to,"「 Detect Mention2 」\nType: Respon Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Autoread off","Read:off"]:
               if wait["cyduk"] ==False:
               	if wait["lang"] == "JP":
                      cl.sendText(msg.to,"「 Always Read 」\nType: Read Chat Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
               else:
                 if wait["cyduk"] == False:
                	if wait["lang"] == "JP":
                          cl.sendText(msg.to,"Auto read Off")
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Notag on"]:
                wait["kickMention"] = True
                cl.sendText(msg.to,"「 Kick Mention 」\nType: Respon Group\nStatus: On \n\n"+ datetime.today().strftime('%H:%M:%S'))
              
            elif msg.text in ["Notag off"]:
                wait["kickMention"] = False
                cl.sendText(msg.to,"「 Kick Mention 」\nType: Respon Group\nStatus: Off \n\n"+ datetime.today().strftime('%H:%M:%S'))
#-----------------------------------------------
            elif msg.text in ["Masuk","Asist @join"]:
                if msg.from_ in admsa:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        time.sleep(0.2)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        time.sleep(0.2),
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        time.sleep(0.2),
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        time.sleep(0.2),
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        time.sleep(0.2),
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text.lower() == 'Sp come':
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Asist1 @join" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
#-----------------------------------------------
            elif "Asist2 @join" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki2.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki2.updateGroup(G)
#---------------------------------------------
	
#-----------------------------------------------
            elif "Asist4 @join" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki4.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki3.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki3.updateGroup(G)
#-----------------------------------------------
            elif "Asist5 @join" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ki5.sendText(msg.to,"Haloo 😘 "  +  str(ginfo.name)  + "")
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                        print "kicker ok"
                        G.preventJoinByTicket(G)
                        ki5.updateGroup(G)
#---------------------------------------------
#-----------------------------------------------
            elif msg.text in ["Pulang","Asist @bye"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        ki2.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki2.leaveGroup(msg.to)
                        ki3.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki3.leaveGroup(msg.to)
                        ki4.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki4.leaveGroup(msg.to)
                        ki5.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Asist1 @bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	ki.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Asist2 @bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	ki2.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki2.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Asist3 @bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	ki3.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki3.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Asist4 @bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	ki4.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki4.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif "Asist5 @bye" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                    	ki5.sendText(msg.to,"Bye Bye😘 "  +  str(ginfo.name)  + "")
                        ki5.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
#-----------------------------------------------
#------------------------✖ BASYIR ✖-----------------------------#
            elif msg.text in ["Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like already On。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Like already Off。\n\nRead time: " + datetime.today().strftime('%H:%M:%S'))
#----------------------------------------------- 

            elif msg.text in ["Welcome","wc","welcome","Wc"]:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            elif "Sayang say " in msg.text:
				bctxt = msg.text.replace("Sayang say ","")
				ki2.sendText(msg.to,(bctxt))
            elif "say" in msg.text:
              if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				ki.sendText(msg.to,(bctxt))
				ki2.sendText(msg.to,(bctxt))
				
				
            elif msg.text.lower() == 'ping':
                ki.sendText(msg.to,"Jebret Matamu 🤣")
                ki2.sendText(msg.to,"Jebret Matamu 🤣")
                ki4.sendText(msg.to,"Jebret Matamu 🤣")
                ki5.sendText(msg.to,"Jebret Matamu 🤣")
#----------------------------------------------- 
#-----------------------------------------------
        if op.type == 19:
            try:
                if op.param3 in mid:
                    if op.param2 in kimid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)

                            
                        
                        
                        ki.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        ki.updateGroup(G)
                        wait["blacklist"][op.param2] = True

                       
                        
                elif op.param3 in kimid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = ki2.getGroup(op.param1)

                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)


                elif op.param3 in ki1mid:
                    if op.param2 in ki2mid:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki2mid:
                    if op.param2 in ki1mid:
                        G = ki1.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ticket = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = cl.getGroup(op.param1)

                        
                        ki2.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ticket = ki2.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki2.updateGroup(G)
                        
                elif op.param3 in ki4mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki5mid:
                    if op.param2 in ki4mid:
                        G = ki4.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)
                    else:
                        G = ki4.getGroup(op.param1)

                        
                        ki4.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki4.updateGroup(G)
                        Ticket = ki4.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki4.updateGroup(G)

                elif op.param3 in ki6mid:
                    if op.param2 in ki5mid:
                        G = ki5.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)
                    else:
                        G = ki5.getGroup(op.param1)

                        
                        ki5.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki5.updateGroup(G)
                        Ticket = ki5.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki5.updateGroup(G)

                elif op.param3 in ki7mid:
                    if op.param2 in ki6mid:
                        G = ki6.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki6.updateGroup(G)
                    else:
                        G = ki6.getGroup(op.param1)

                        
                        ki6.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki6.updateGroup(G)
                        Ticket = ki6.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)

                elif op.param3 in ki8mid:
                    if op.param2 in ki7mid:
                        G = ki9.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki9.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
                    else:
                        G = ki9.getGroup(op.param1)

                        
                        ki9.kickoutFromGroup(op.param1,[op.param2])

                        G.preventJoinByTicket = False
                        ki9.updateGroup(G)
                        Ticket = ki7.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki10.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki9.updateGroup(G)
            except:
                pass

	if op.type == 17:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
	    if wait["protect"] == True:
		if wait["blacklist"][op.param2] == True:
		   try:
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			G = random.choice(KAC).getGroup(op.param1)
			G.preventJoinByTicket = True
			ki4.updateGroup(G)
#			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		   except:
#			pass
			try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    G = random.choice(KAC).getGroup(op.param1)
			    G.preventJoinByTicket = True
			    random.choice(KAC).updateGroup(G)
#			    random.choice(KAK).kickoutFromGroup(op.param1,[op.param2])
			except:
			    pass
		elif op.param2 not in admin + Bots:
		    random.choice(KAC).sendText(op.param1,"Welcome. Don't Play Bots. I can kick you!")
	    else:
		pass
	if op.type == 19:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["protect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = ki.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    ki.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n-> " + Nama
                        wait2['ROM'][op.param1][op.param2] = "-> " + Nama
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    cl.sendText
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()



while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)