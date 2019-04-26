import os
import textwrap

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

DISCORD_VOICE_CH_ID = "348823033005211652"

ACTIVE_CHANNEL_NAME = "honda-bot"

WIN_RATE = 0.5

HELLO_MESSAGE = textwrap.dedent("""\
    今日の本田ロイド、起動したで！
""")

HAND_R_KEYWORDS = [
    "ぐー",
    "グー",
    "gu",
    "rock",
    "Rock",
    "ROCK"
]
HAND_S_KEYWORDS = [
    "ちょき",
    "チョキ",
    "choki",
    "cyoki",
    "tyoki",
    "scissors",
    "Scissors",
    "SCISSORS"
]
HAND_P_KEYWORDS = [
    "ぱー",
    "パー",
    "pa",
    "paper",
    "Paper",
    "PAPER"
]