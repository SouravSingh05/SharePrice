import requests
from bs4 import BeautifulSoup
from TelegramBot import bot
from TelegramBot.bot import Telegram

bot = Telegram("config.cfg")


def make_reply(msg):
    reply = None
    flag = 0
    flag1 = 0
    flag2 = 0
    name = ""
    if msg == "/start":
        reply = "Welcome. I will help you in getting the current share prices of different companies"
    elif msg[0] == "/":
        try:
            msg1 = msg.upper()
            url1 = "https://in.finance.yahoo.com/quote{}.NS".format(msg1)
            share = requests.get(url1)
            if share.status_code == 200:
                soup = BeautifulSoup(share.text, "html.parser")
                title = soup.find(class_="D(ib) Fz(16px) Lh(18px)").getText().strip().split()
                del title[0:2]
                if len(title) > 0:
                    str1 = ""
                    for ele in title:
                        str1 = str1 + " " + ele
                    name = str1
                price = soup.find(class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")\
                    .getText().strip()
                search = soup.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"}, limit=13)
                bid = search[2].getText().strip()
                ask = search[3].getText().strip()
                dayrange = search[4].getText().strip()
                weekrange = search[5].getText().strip()
                volume = search[6].getText().strip()
                peratio = search[10].getText().strip()
                eps = search[11].getText().strip()
                earndate = search[12].getText().strip()
                reply1 = "NSE\n  Price: (Rs)"+str(price)+"\n"+"  Bid: "+str(bid)+"\n" +\
                         "  Ask: "+str(ask)+"\n"+"  Day's Range: "+str(dayrange)+"\n" +\
                         "  52-Week Range: "+str(weekrange)+"\n"+"  Volume: "+str(volume)+"\n" +\
                         "  PE Ratio: "+str(peratio)+"\n"+"  EPS: "+str(eps)+"\n" +\
                         "  Earnings Date: "+str(earndate)+"\n"
                flag = 1
        except:
            reply1 = ""
        try:
            msg2 = msg.upper()
            url2 = "https://in.finance.yahoo.com/quote{}.BO".format(msg2)
            share1 = requests.get(url2)
            if share1.status_code == 200:
                soup1 = BeautifulSoup(share1.text, "html.parser")
                if name == "":
                    title = soup1.find(class_="D(ib) Fz(16px) Lh(18px)").getText().strip().split()
                    del title[0:2]
                    if len(title)>0:
                        str1 = ""
                        for ele in title:
                            str1 = str1 + " " + ele
                        name = str1
                price1 = soup1.find(class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)") \
                    .getText().strip()
                search1 = soup1.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"}, limit=13)
                bid1 = search1[2].getText().strip()
                ask1 = search1[3].getText().strip()
                dayrange1 = search1[4].getText().strip()
                weekrange1 = search1[5].getText().strip()
                volume1 = search1[6].getText().strip()
                peratio1 = search1[10].getText().strip()
                eps1 = search1[11].getText().strip()
                earndate1 = search1[12].getText().strip()
                reply2 = "BSE\n  Price: (Rs)" + str(price1) + "\n" + "  Bid: " + str(bid1) + "\n" + \
                         "  Ask: " + str(ask1) + "\n" + "  Day's Range: " + str(dayrange1) + "\n" + \
                         "  52-Week Range: " + str(weekrange1) + "\n" + "  Volume: " + str(volume1) + "\n" + \
                         "  PE Ratio: " + str(peratio1) + "\n" + "  EPS: " + str(eps1) + "\n" + \
                         "  Earnings Date: " + str(earndate1) + "\n"
        except:
            reply2 = ""
        try:
            msg3 = msg.upper()
            url3 = "https://in.finance.yahoo.com/quote{}".format(msg3)
            share2 = requests.get(url3)
            if share2.status_code == 200:
                soup2 = BeautifulSoup(share2.text, "html.parser")
                if name == "":
                    title = soup2.find(class_="D(ib) Fz(16px) Lh(18px)").getText().strip().split()
                    del title[0:2]
                    if len(title) > 0:
                        str1 = ""
                        for ele in title:
                            str1 = str1 + " " + ele
                        name = str1
                price2 = soup2.find(class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)") \
                    .getText().strip()
                search2 = soup2.findAll("td", {"class": "Ta(end) Fw(600) Lh(14px)"}, limit=13)
                bid2 = search2[2].getText().strip()
                ask2 = search2[3].getText().strip()
                dayrange2 = search2[4].getText().strip()
                weekrange2 = search2[5].getText().strip()
                volume2 = search2[6].getText().strip()
                peratio2 = search2[10].getText().strip()
                eps2 = search2[11].getText().strip()
                earndate2 = search2[12].getText().strip()
                reply3 = "NASDAQ\n  Price: (USD)" + str(price2) + "\n" + "  Bid: " + str(bid2) + "\n" + \
                         "  Ask: " + str(ask2) + "\n" + "  Day's Range: " + str(dayrange2) + "\n" + \
                         "  52-Week Range: " + str(weekrange2) + "\n" + "  Volume: " + str(volume2) + "\n" + \
                         "  PE Ratio: " + str(peratio2) + "\n" + "  EPS: " + str(eps2) + "\n" + \
                         "  Earnings Date: " + str(earndate2) + "\n"
                flag2 = 1
        except:
            reply3 = ""
        if flag == 1 or flag1 == 1 or flag2 == 1:
            reply = name+"\n"+reply1+"\n"+reply2+"\n"+reply3
        else:
            reply = "Invalid Symbol! Check the symbol or press \n \"/start\" \n and try again"
    return reply


update_id = None

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = 1
            if message != 1:
                from_ = item["message"]["chat"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, from_)