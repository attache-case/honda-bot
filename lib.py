import discord
import env

import textwrap
import random

# rps_done_member_list = []

def key_parser(message, keyword_list):
    has_keyword = False
    for key in keyword_list:
        if key in message.content:
            has_keyword = True
            break
    return has_keyword

class GameRPS:
    __rps_done_member_list = []
    __msg_daily_limit_exceeded = textwrap.dedent("""\
        じゃんけんは1日1回まで！
        ほな、また明日！
    """)
    __msg_too_many_hands = textwrap.dedent("""\
        手を複数同時に出すのは反則やで！
    """)
    __msg_win = textwrap.dedent("""\
        やるやん。
        明日は俺にリベンジさせて。
        では、どうぞ。
    """)
    __msg_lose_r = textwrap.dedent("""\
        俺の勝ち！
        負けは次につながるチャンスです！
        ネバーギブアップ！
        ほな、いただきます！
    """)
    __msg_lose_s = textwrap.dedent("""\
        俺の勝ち！
        たかがじゃんけん、そう思ってないですか？
        それやったら明日も、俺が勝ちますよ
        ほな、いただきます！
    """)
    __msg_lose_p = textwrap.dedent("""\
        俺の勝ち！
        なんで負けたか、明日まで考えといてください。
        そしたら何かが見えてくるはずです
        ほな、いただきます！
    """)
    __file_win = [
        discord.File("honda_win.png")
    ]
    __file_lose_r = [
        # discord.File("honda_p.png"),
        discord.File("honda_p.gif")
    ]
    __file_lose_s = [
        # discord.File("honda_r.png"),
        discord.File("honda_r.gif")
    ]
    __file_lose_p = [
        # discord.File("honda_s.png"),
        discord.File("honda_s.gif")
    ]

    __youtube_lose_r = "https://youtu.be/LhPJcvJLNEA"
    __youtube_lose_s = "https://youtu.be/SWNCYpeDTfo"
    __youtube_lose_p = "https://youtu.be/28d78XP1TJs"

    def __init__(self):
        pass

    def __parse_hands(self, message):
        r = key_parser(message, env.HAND_R_KEYWORDS)
        p = key_parser(message, env.HAND_P_KEYWORDS)
        s = key_parser(message, env.HAND_S_KEYWORDS)
        return [r, p, s]

    async def __play_youtube(self, voice, url):
        player = await voice.create_ytdl_player(url)
        player.start()

    def __create_rps_battle_string(self, player, hands, result='L'): # result: win->'W' lose->'L'
        player_hand = None
        honda_hand = None
        r, p, s = hands
        if result == 'W':
            if r is True:
                player_hand = env.EMOJI_R
                honda_hand = env.EMOJI_S
            elif s is True:
                player_hand = env.EMOJI_S
                honda_hand = env.EMOJI_P
            elif p is True:
                player_hand = env.EMOJI_P
                honda_hand = env.EMOJI_R
        elif result == 'L':
            if r is True:
                player_hand = env.EMOJI_R
                honda_hand = env.EMOJI_P
            elif s is True:
                player_hand = env.EMOJI_S
                honda_hand = env.EMOJI_R
            elif p is True:
                player_hand = env.EMOJI_P
                honda_hand = env.EMOJI_S
        if player_hand is not None and honda_hand is not None:
            return "(YOU) " + player_hand + " VS " + honda_hand + " (HONDA)\n"
        else:
            return ""


    def __play_rps(self, ch, player, hands, m_prefix=""):
        r, p, s = hands
        rnd = random.random()

        if rnd < env.WIN_RATE:
            m_prefix = self.__create_rps_battle_string(player, hands, 'W') + m_prefix
            f = self.__file_win
            m = self.__msg_win
        else:
            m_prefix = self.__create_rps_battle_string(player, hands, 'L') + m_prefix
            if r is True:
                f = self.__file_lose_r
                m = self.__msg_lose_r
            elif s is True:
                f = self.__file_lose_s
                m = self.__msg_lose_s
            elif p is True:
                f = self.__file_lose_p
                m = self.__msg_lose_p

        self.__rps_done_member_list.append(player) # add user to done list when rps is done
        await ch.send(m_prefix + m, files=f)
        return

    async def process_message(self, client, message):
        player = message.author
        hands = self.__parse_hands(message)
        ch = message.channel

        if hands.count(True) == 0:
            return

        m_prefix = player.mention + "\n"

        # judge rights
        if player in self.__rps_done_member_list:
            m = self.__msg_daily_limit_exceeded
            await ch.send(m_prefix + m)
            return

        if hands.count(True) > 1:
            m = self.__msg_too_many_hands
            await ch.send(m_prefix + m)
        else:
            assert hands.count(True) == 1, 'assert: [r, p, s].count(True) == 1 ... r:{0}, p:{1}, s:{2}'.format(r, p, s)

            self.__play_rps(ch, player, hands, m_prefix)


async def respond_greeting(message):
    if message.content.startswith("おはよう"):
        m = "おはようございます" + message.author.name + "さん！"
        await message.channel.send(m)
    if message.content.startswith("こんにちは"):
        m = "ちーっす、" + message.author.name + "さん！"
        await message.channel.send(m)
    if message.content.startswith("こんばんは"):
        m = "こんばんは、" + message.author.name + "さん！"
        await message.channel.send(m)
