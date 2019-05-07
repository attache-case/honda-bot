import os
import textwrap
import datetime

DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

DATABASE_URL = os.environ['DATABASE_URL']

DISCORD_VOICE_CH_ID = "348823033005211652"

ACTIVE_CHANNEL_NAME = "honda-bot"

WIN_RATE = 0.1

REFRESH_TIME_HOUR = 5

def get_dt_now_and_dt_prev_next_refresh():
    dt_now = datetime.datetime.now()
    dt_refresh_base = dt_now.replace(hour=REFRESH_TIME_HOUR, minute=0, second=0, microsecond=0)
    if dt_refresh_base < dt_now:
        dt_prev_refresh = dt_refresh_base
        dt_next_refresh = dt_refresh_base + datetime.timedelta(hours=24)
    else:
        dt_prev_refresh = dt_refresh_base - datetime.timedelta(hours=24)
        dt_next_refresh = dt_refresh_base
    return dt_now, dt_prev_refresh, dt_next_refresh

HELLO_MESSAGE_BASE = textwrap.dedent("""\
    本田ロイド、再起動したで！
""")

def get_hello_message():
    _, _, dt_next_refresh = get_dt_now_and_dt_prev_next_refresh()
    s = ""
    s = s + HELLO_MESSAGE_BASE + "\n"
    s = s + "（次回のじゃんけん回数リセットは" + dt_next_refresh.strftime('%Y-%m-%d %H:%M:%S') + "）"
    return s

EMOJI_R = ":fist:"
EMOJI_S = ":v:"
EMOJI_P = ":hand_splayed:"

HAND_R_KEYWORDS = [
    "ぐー",
    "グー",
    "gu",
    "rock",
    "Rock",
    "ROCK",
    EMOJI_R,
    "✊"
]
HAND_S_KEYWORDS = [
    "ちょき",
    "チョキ",
    "choki",
    "cyoki",
    "tyoki",
    "scissors",
    "Scissors",
    "SCISSORS",
    EMOJI_S,
    "✌"
]
HAND_P_KEYWORDS = [
    "ぱー",
    "パー",
    "pa",
    "paper",
    "Paper",
    "PAPER",
    EMOJI_P,
    "🖐"
]