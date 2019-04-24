import discord
import env

import textwrap

async def respond_greeting(message):
    if message.content.startswith("おはよう"):
        m = "おはようございます" + message.author.name + "さん！"
        await message.channel.send(m)

def key_parser(message, keyword_list):
    has_keyword = False
    for key in keyword_list:
        if key in message.content:
            has_keyword = True
            break
    return has_keyword

def parse_hands(message):
    r = key_parser(message, env.HAND_R_KEYWORDS)
    p = key_parser(message, env.HAND_P_KEYWORDS)
    s = key_parser(message, env.HAND_S_KEYWORDS)
    return r, p, s

async def play_youtube(voice, url):
    player = await voice.create_ytdl_player(url)
    player.start()

async def respond_rps(client, message):
    r, p, s = parse_hands(message)
    if [r, p, s].count(True) == 0:
        return
    if [r, p, s].count(True) > 1:
        m = textwrap.dedent("""\
            手を複数同時に出すのは反則やで！
        """)
        await message.channel.send(m)
    else:
        assert [r, p, s].count(True) == 1, 'assert: [r, p, s].count(True) == 1 ... r:{0}, p:{1}, s:{2}'.format(r, p, s)
        voice = await client.join_voice_channel(client.get_channel(DISCORD_VOICE_CH_ID))
        if r is True:
            # m = "https://youtu.be/LhPJcvJLNEA"
            f = [
                discord.File("honda_p.png"),
                discord.File("honda_p.gif")
            ]
            m = textwrap.dedent("""\
                俺の勝ち！
                負けは次につながるチャンスです！
                ネバーギブアップ！
                ほな、いただきます！
            """)
            await message.channel.send(m, files=f)
            await play_youtube(voice, "https://youtu.be/LhPJcvJLNEA")
        elif s is True:
            # m = "https://youtu.be/SWNCYpeDTfo"
            f = [
                discord.File("honda_r.png"),
                discord.File("honda_r.gif")
            ]
            m = textwrap.dedent("""\
                俺の勝ち！
                たかがじゃんけん、そう思ってないですか？
                それやったら明日も、俺が勝ちますよ
                ほな、いただきます！
            """)
            await message.channel.send(m, files=f)
            await play_youtube(voice, "https://youtu.be/SWNCYpeDTfo")
        if p is True:
            # m = "https://youtu.be/28d78XP1TJs"
            f = [
                discord.File("honda_s.png"),
                discord.File("honda_s.gif")
            ]
            m = textwrap.dedent("""\
                俺の勝ち！
                なんで負けたか、明日まで考えといてください。
                そしたら何かが見えてくるはずです
                ほな、いただきます！
            """)
            await message.channel.send(m, files=f)
            await play_youtube(voice, "https://youtu.be/28d78XP1TJs")
