import asyncio
import discord
import time
from random import *
import os

client = discord.Client()

t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = t10 = t11 = 0
start = int(time.time())

@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("===============")
    await client.change_presence(status=discord.Status.online, activity=discord.Game('까바자보'))

@client.event
async def on_message(message):
    
    global t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11
    name = message.author.name
    now = time.time()
    cooldown = 30       #명령어 쿨타임(30초)

    if message.author.bot:
        return None

    if message.content == "!트위치":       #Command 1 : 트위치
        if now < t1 + cooldown :
            return None
        else:
            await message.channel.send("https://www.twitch.tv/sbjw123/")
            t1 = time.time()

    if message.content == "!트게더" or message.content == "!까게더":      #Command 2 : 트게더        
        if now < t2 + cooldown:
            return None
        else:
            await message.channel.send("https://tgd.kr/sbjw123")
            t2 = time.time()
    
    if message.content == "!유튜브" or message.content == "!까튜브":      #Command 3 : 유튜브
        if now < t3 + cooldown:
            return None
        else:
            await message.channel.send("https://www.youtube.com/channel/UCuFpKTh5zq9PESiwg0xV13A")
            t3 = time.time()

    if message.content == "!키":     #Command 4 : 키
        if now < t4 + cooldown:
            return None
        else:
            await message.channel.send("대사 주세요 ㅠㅠ")
            t4 = time.time()

    if message.content == "!까바자보":      #Command 5 : 까바자보
        if now < t5 + cooldown:
            return None
        else:
            await message.channel.send("대사!!!! ||!까바자보||")
            t5 = time.time()

    if message.content == "!까모닝":       #Command 6 : 까모닝
        if now < t6 + cooldown:
            return None
        else:
            await message.channel.send("대사아아아아ㅏㅏㅏㅏㅏㅏ!!!!!!!!")
            t6 = time.time()

    if message.content == "!까브닝":       #Command 7 : 까브닝
        if now < t7 + cooldown:
            return None
        else:
            msg_eve = randint(1, 3)
            if msg_eve == 1:
                await message.channel.send("대사아아ㅏㅏㅏㅏ!!!!(1)")
            elif msg_eve == 2:
                await message.channel.send("대사아아ㅏㅏㅏㅏ!!!!(2)")
            else:
                await message.channel.send("대사아아ㅏㅏㅏㅏ!!!!(3)")
            t7 = time.time()
            
    if message.content == "!까나잇":       #Command 8 : 까나잇
        if now < t8 + cooldown:
            return None
        else:
            await message.channel.send("대사....ㅠ")
            t8 = time.time()

    if message.content == "!오뱅알":       #Command 9 : 오뱅알
        if now < t9 + cooldown:
            return None
        else:
            await message.channel.send(name + " 대사 못만들겠다 ^^...")
            t9 = time.time()

    if message.content == "!선":     #Command 10 : 선
        if now < t10 + cooldown:
            return None
        else:
            await message.channel.send("---------------^^-이-거-슨-뇌-절-방-지-선-^^---------------")
            t10 = time.time()

    if message.content == "!명령어":       #Command 11 : 명령어
        if now < t11 + cooldown:
            return None
        else:
            embed = discord.Embed(title="까자봇 명령어", description="이거슨 명령어 목록이올시다.", color=0xaaf0d1)
            embed.set_footer(text = '누가 쿨타임 좀 짜주세요 ㅠㅠ')
            embed.add_field(name = '!트위치', value = '트위치 명령어 설명', inline=False)
            embed.add_field(name = '!유튜브/!까튜브', value = '유튜브 명령어 설명', inline=False)
            embed.add_field(name = '!트게더/!까게더', value = '트게더 명령어 설명', inline=False)
            embed.add_field(name = '!키', value = '키 명령어 설명', inline=False)
            embed.add_field(name = '!까바자보', value = '까바자보 명령어 설명', inline=False)
            embed.add_field(name = '!까모닝/!까브닝/!까나잇', value = '까모닝 명령어 설명', inline=False)
            embed.add_field(name = '!오뱅알', value = '오뱅알 명령어 설명', inline=False)
            embed.add_field(name = '!선', value = '선 명령어 설명', inline=False)
            await message.channel.send(embed = embed)
            t11 = time.time()
            
    if message.content == "!업타임": #Test Comman
        uptime = now - start
        await message.channel.send(str(uptime//86400) + "d " + str((uptime%86400)//3600) + "h " + str((uptime%3600)//60) + "min " + str(uptime%%60) + "sec")
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
