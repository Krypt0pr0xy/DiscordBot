import discord
import serial
import time
import os

os.system("git init .")
os.system("git remote add originhttps://github.com/Krypt0pr0xy/DiscordBot.git")
os.system("git pull origin master")

class MyClient(discord.Client):
    async def on_ready(self):
         print("Bot is Online V2")
		  
    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        global messageauthor
        messageauthor = str(message.author)
        if message.author == client.user:
            return

        if message.content == "/help":
            await message.author.send("/help --> for help")
            await message.author.send("Hi Bot --> name repliay")


        if message.content.startswith("Hi Bot"):
            await message.channel.send('Hi ' + str(message.author))

        if message.content.startswith("led3On") and (Ranks.checkRanktoWriteSerial("user.txt",5)):
            Serial.write("Switch3ON")

        if message.content.startswith("led3Off") and (Ranks.checkRanktoWriteSerial("user.txt",5)):
            Serial.write("Switch3OFF")

        if message.content.startswith("send") and (Ranks.checkRanktoWriteSerial("user.txt", 5)):
            temp_author = str(message.author)
            temp2_author = temp_author.split("#",1)
            Serial.write("writel2 " + temp2_author[0] + "\n")
            temp_message = str(message.content)
            temp2_message = temp_message.split(" ",1)
            Serial.write("writel1 " + temp2_message[1] + "\n")

        print("message from " + str(message.author) + " contains " + str(message.content))



    #Wenn Nachricht gelöscht wird
    async def on_message_delete(self, message):
        await message.author.send("Why did you deleted this? " + message.content)
        print("Deleted message: " + message.content)



Port = '/dev/ttyUSB0'
serport = serial.Serial(Port, 9600)
serport.close()
class Serial():
    def write(data):
        try:
            serport.open()
            time.sleep(2)
        except Exception as e:
            print("Exception: Opening serial port: " + str(e))
        if serport.isOpen():
            if serport.inWaiting() > 0:
                serport.flush
            try:
                serport.flush()
                serport.write(str(data).encode('ascii'))
                serport.flush()
                print("write data: " + str(data))
                time.sleep(1)
               
            except Exception as e:
                print("Error communicating...: " + str(e))

class Ranks():
    def checkRanktoWriteSerial(path,rank):
        flag = 0;
        try:
            file = open(str(path))
            for line in file:
                if messageauthor == line.split(" ")[0] and int(line.split(" ")[1]) >= rank:
                    print("accepted")
                    flag = 1
                    break
                else:
                    print("not accepted")
            file.close()
        except Exception as e:
            print("Error reading File: " + str(path) + " " + str(e))
        return flag





hashfile = open("hash.txt")
hash = hashfile.read()
hashfile.close()


client = MyClient()
client.run(hash)
