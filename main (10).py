import ccxt
import pandas as pd
import numpy as np
import ta
import requests
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import re
# -----------------------------
# تنظیمات API و ربات
API_KEY = "sEdZ3rjkls0BHCVYyDmyalNrwDu6VHdcxxedngayFqIFfyfiH5TQq7Mua0ds3Sv7"
EXCHANGE_NAME = "toobit"
# -----------------------------
# لیست SYMBOL ها
SYMBOLS = [
        "1000PEPE/USDT:USDT",
    "BTC/USDT:USDT",
    "ETH/USDT:USDT",
    "SOL/USDT:USDT",
    "DOGE/USDT:USDT",
    "XRP/USDT:USDT",
    "TON/USDT:USDT",
    "SUI/USDT:USDT",
    "ZEC/USDT:USDT",
    "BNB/USDT:USDT",
    "ALICE/USDT:USDT",
    "PAXG/USDT:USDT",
    "ADA/USDT:USDT",
    "HYPE/USDT:USDT",
    "ASTER/USDT:USDT",
    "COAI/USDT:USDT",
    "XPLUS/USDT:USDT",
    "AAVE/USDT:USDT",
    "ZORA/USDT:USDT",
    "LTC/USDT:USDT",
    "FORM/USDT:USDT",
    "PUMP/USDT:USDT",
    "DASH/USDT:USDT",
    "AIA/USDT:USDT",
    "1000PEPE/USDT:USDT",
    "SQD/USDT:USDT",
    "ENA/USDT:USDT",
    "MERL/USDT:USDT",
    "BAT/USDT:USDT",
    "OKB/USDT:USDT",
    "PENGU/USDT:USDT",
    "CAKE/USDT:USDT",
    "LDO/USDT:USDT",
    "GIGGLE/USDT:USDT",
    "1000CHEEMS/USDT:USDT",
    "UNI/USDT:USDT",
    "FIL/USDT:USDT",
    "WLD/USDT:USDT",
    "WLFI/USDT:USDT",
    "STO/USDT:USDT",
    "WIF/USDT:USDT",
    "ZEN/USDT:USDT",
    "XAUT/USDT:USDT",
    "LINK/USDT:USDT",
    "AVAX/USDT:USDT",
    "APT/USDT:USDT",
    "STBL/USDT:USDT",
    "TWT/USDT:USDT",
    "USELESS/USDT:USDT",
    "MIRA/USDT:USDT",
    "ETC/USDT:USDT",
    "FET/USDT:USDT",
    "TLM/USDT:USDT",
    "FF/USDT:USDT",
    "AXS/USDT:USDT",
    "KGEN/USDT:USDT",
    "NEAR/USDT:USDT",
    "OPEN/USDT:USDT",
    "KOMA/USDT:USDT",
    "EDEN/USDT:USDT",
    "AVNT/USDT:USDT",
    "2Z/USDT:USDT",
    "1000BONK/USDT:USDT",
    "DOT/USDT:USDT",
    "SOON/USDT:USDT",
    "PLUME/USDT:USDT",
    "DOOD/USDT:USDT",
    "OG/USDT:USDT",
    "HBAR/USDT:USDT",
    "LISTA/USDT:USDT",
    "1000SHIB/USDT:USDT",
    "TRX/USDT:USDT",
    "SNX/USDT:USDT",
    "MYX/USDT:USDT",
    "TAO/USDT:USDT",
    "ETHFI/USDT:USDT",
    "NMR/USDT:USDT",
    "LYN/USDT:USDT",
    "SPX/USDT:USDT",
    "ONDO/USDT:USDT",
    "BLESS/USDT:USDT",
    "EIGEN/USDT:USDT",
    "BANK/USDT:USDT",
    "CRV/USDT:USDT",
    "MAGIC/USDT:USDT",
    "AR/USDT:USDT",
    "LINEA/USDT:USDT",
    "XMR/USDT:USDT",
    "ATOM/USDT:USDT",
    "INJ/USDT:USDT",
    "AKE/USDT:USDT",
    "TRUMP/USDT:USDT",
    "IN/USDT:USDT",
    "XAN/USDT:USDT",
    "HANA/USDT:USDT",
    "TAKE/USDT:USDT",
    "SOMI/USDT:USDT",
    "CELO/USDT:USDT",
    "ATH/USDT:USDT",
    "HEMI/USDT:USDT",
    "BROCCOLI714/USDT:USDT",
    "VFY/USDT:USDT",
    "STRK/USDT:USDT",
    "1000FLOKI/USDT:USDT",
    "NOT/USDT:USDT",
    "EDU/USDT:USDT",
    "BCH/USDT:USDT",
    "MOCA/USDT:USDT",
    "W/USDT:USDT",
    "ORDI/USDT:USDT",
    "RENDER/USDT:USDT",
    "RED/USDT:USDT",
    "DOLO/USDT:USDT",
    "TRADOOR/USDT:USDT",
    "EUR/USDT:USDT",
    "Q/USDT:USDT",
    "TOSHI/USDT:USDT",
    "ZRO/USDT:USDT",
    "CRO/USDT:USDT",
    "MOODENG/USDT:USDT",
    "VIRTUAL/USDT:USDT",
    "QTUM/USDT:USDT",
    "DYDX/USDT:USDT",
    "EPIC/USDT:USDT",
    "QNT/USDT:USDT",
    "HOOK/USDT:USDT",
    "TIA/USDT:USDT",
    "BARD/USDT:USDT",
    "OP/USDT:USDT",
    "1000WHY/USDT:USDT",
    "REZ/USDT:USDT",
    "PIXEL/USDT:USDT",
    "ENJ/USDT:USDT",
    "MUBARAK/USDT:USDT",
    "HFT/USDT:USDT",
    "WAL/USDT:USDT",
    "SEI/USDT:USDT",
    "BRETT/USDT:USDT",
    "PNUT/USDT:USDT",
    "SSV/USDT:USDT",
    "AUCTION/USDT:USDT",
    "LIGHT/USDT:USDT",
    "ICP/USDT:USDT",
    "PYTH/USDT:USDT",
    "S/USDT:USDT",
    "MORPHO/USDT:USDT",
    "VIC/USDT:USDT",
    "PENDLE/USDT:USDT",
    "TUT/USDT:USDT",
    "MUS/USDT:USDT",
    "RDNT/USDT:USDT",
    "PI/USDT:USDT",
    "EVAA/USDT:USDT",
    "XPIN/USDT:USDT",
    "AI16Z/USDT:USDT",
    "H/USDT:USDT",
    "GALA/USDT:USDT",
    "JUP/USDT:USDT",
    "POL/USDT:USDT",
    "DEEP/USDT:USDT",
    "SPK/USDT:USDT",
    "BOME/USDT:USDT",
    "B2/USDT:USDT",
    "MEME/USDT:USDT",
    "CFX/USDT:USDT",
    "1000SATS/USDT:USDT",
    "KSM/USDT:USDT",
    "JELLYJELLY/USDT:USDT",
    "TRUTH/USDT:USDT",
    "NAORIS/USDT:USDT",
    "BERA/USDT:USDT",
    "MASK/USDT:USDT",
    "SAND/USDT:USDT",
    "UB/USDT:USDT",
    "PROMPT/USDT:USDT",
    "IO/USDT:USDT",
    "ILV/USDT:USDT",
    "EGLD/USDT:USDT",
    "COW/USDT:USDT",
    "ALPINE/USDT:USDT",
    "SAPIEN/USDT:USDT",
    "1000LUNC/USDT:USDT",
    "MANA/USDT:USDT",
    "CELR/USDT:USDT",
    "KAITO/USDT:USDT",
    "RSR/USDT:USDT",
    "WOO/USDT:USDT",
    "SFP/USDT:USDT",
    "UMA/USDT:USDT",
    "XLM/USDT:USDT",
    "FLOCK/USDT:USDT",
    "BIO/USDT:USDT",
    "STG/USDT:USDT",
    "PROM/USDT:USDT",
    "ARIA/USDT:USDT",
    "AIXB/USDT:USDT",
    "ORDER/USDT:USDT",
    "LPT/USDT:USDT",
    "BB/USDT:USDT",
    "BANANA/USDT:USDT",
    "ZKC/USDT:USDT",
    "ONT/USDT:USDT",
    "KERNEL/USDT:USDT",
    "SUSHI/USDT:USDT",
    "MAV/USDT:USDT",
    "LA/USDT:USDT",
    "PTB/USDT:USDT",
    "BAS/USDT:USDT",
    "ARKM/USDT:USDT",
    "RLC/USDT:USDT",
    "GTC/USDT:USDT",
    "ID/USDT:USDT",
    "APE/USDT:USDT",
    "LQTY/USDT:USDT",
    "MBOX/USDT:USDT",
    "NOM/USDT:USDT",
    "USUAL/USDT:USDT",
    "YGG/USDT:USDT",
    "ALCH/USDT:USDT",
    "HOLO/USDT:USDT",
    "KAVA/USDT:USDT",
    "SYRUP/USDT:USDT",
    "TREE/USDT:USDT",
    "OM/USDT:USDT",
    "FLOW/USDT:USDT",
    "AERO/USDT:USDT",
    "POPCAT/USDT:USDT",
    "TR/USDT:USDT",
    "SLP/USDT:USDT",
    "THE/USDT:USDT",
    "DENT/USDT:USDT",
    "COTI/USDT:USDT",
    "MITO/USDT:USDT",
    "STX/USDT:USDT",
    "IMX/USDT:USDT",
    "PUMPBTC/USDT:USDT",
    "SCRT/USDT:USDT",
    "ZK/USDT:USDT",
    "PROVE/USDT:USDT",
    "NEO/USDT:USDT",
    "PORT3/USDT:USDT",
    "GAS/USDT:USDT",
    "HOT/USDT:USDT",
    "RUNE/USDT:USDT",
    "ACH/USDT:USDT",
    "ALGO/USDT:USDT",
    "SOPH/USDT:USDT",
    "IP/USDT:USDT",
    "1000CAT/USDT:USDT",
    "XAI/USDT:USDT",
    "FLUID/USDT:USDT",
    "VINE/USDT:USDT",
    "PARTI/USDT:USDT",
    "TURBO/USDT:USDT",
    "DUSK/USDT:USDT",
    "1INCH/USDT:USDT",
    "VET/USDT:USDT",
    "1MBABYDOGE/USDT:USDT",
    "THETA/USDT:USDT",
    "DODOX/USDT:USDT",
    "SAGA/USDT:USDT",
    "BMT/USDT:USDT",
    "ROSE/USDT:USDT",
    "JTO/USDT:USDT",
    "PUFFER/USDT:USDT",
    "C98/USDT:USDT",
    "A2Z/USDT:USDT",
    "TST/USDT:USDT",
    "ANIME/USDT:USDT",
    "KAIA/USDT:USDT",
    "NIL/USDT:USDT",
    "GRT/USDT:USDT",
    "ENS/USDT:USDT",
    "SXT/USDT:USDT",
    "RARE/USDT:USDT",
    "PORTAL/USDT:USDT",
    "ARPA/USDT:USDT",
    "CKB/USDT:USDT",
    "ONE/USDT:USDT",
    "API3/USDT:USDT",
    "IOTA/USDT:USDT",
    "EPT/USDT:USDT",
    "SPELL/USDT:USDT",
    "KNC/USDT:USDT",
    "SYS/USDT:USDT",
    "KAS/USDT:USDT",
    "XTZ/USDT:USDT",
    "CHZ/USDT:USDT",
    "PERP/USDT:USDT",
    "ASR/USDT:USDT",
    "GOAT/USDT:USDT",
    "ICX/USDT:USDT",
    "PHA/USDT:USDT",
    "DEXE/USDT:USDT",
    "VOXEL/USDT:USDT",
    "AEVO/USDT:USDT",
    "CTSI/USDT:USDT",
    "GRASS/USDT:USDT",
    "CHILLGUY/USDT:USDT",
    "DRIFT/USDT:USDT",
    "BICO/USDT:USDT",
    "BANANAS31/USDT:USDT",
    "ARK/USDT:USDT",
    "POWR/USDT:USDT",
    "WCT/USDT:USDT",
    "SKATE/USDT:USDT",
    "RVN/USDT:USDT",
    "AVAAI/USDT:USDT",
    "JOE/USDT:USDT",
    "TA/USDT:USDT",
    "FUN/USDT:USDT",
    "SUPER/USDT:USDT",
    "RPLUS/USDT:USDT",
    "BEAMX/USDT:USDT",
    "ASTR/USDT:USDT",
    "GPS/USDT:USDT",
    "SKL/USDT:USDT",
    "XVS/USDT:USDT",
    "SCR/USDT:USDT",
    "JASMY/USDT:USDT",
    "OXT/USDT:USDT",
    "HYPER/USDT:USDT",
    "GMX/USDT:USDT",
    "1000000MOG/USDT:USDT",
    "YALA/USDT:USDT",
    "C/USDT:USDT",
    "GMT/USDT:USDT",
    "A/USDT:USDT",
    "CVX/USDT:USDT",
    "SWELL/USDT:USDT",
    "STEEM/USDT:USDT",
    "XNY/USDT:USDT",
    "LUNA2/USDT:USDT",
    "AGT/USDT:USDT",
    "QUICK/USDT:USDT",
    "LRC/USDT:USDT",
    "KDA/USDT:USDT",
    "AWE/USDT:USDT",
    "ACT/USDT:USDT",
    "SKY/USDT:USDT",
    "TOWNS/USDT:USDT",
    "VVV/USDT:USDT",
    "NTRN/USDT:USDT",
    "ZRX/USDT:USDT",
    "MINA/USDT:USDT",
    "MTL/USDT:USDT",
    "1000XEC/USDT:USDT",
    "OGN/USDT:USDT",
    "NXPC/USDT:USDT",
    "DOGS/USDT:USDT",
    "AKT/USDT:USDT",
    "KMNO/USDT:USDT",
    "VANA/USDT:USDT",
    "ONG/USDT:USDT",
    "TRU/USDT:USDT",
    "BAND/USDT:USDT",
    "FIO/USDT:USDT",
    "CUDIS/USDT:USDT",
    "HUMA/USDT:USDT",
    "ZIL/USDT:USDT",
    "DAM/USDT:USDT",
    "INIT/USDT:USDT",
    "FORTH/USDT:USDT",
    "GRIFFAIN/USDT:USDT",
    "PEOPLE/USDT:USDT",
    "IOST/USDT:USDT",
    "WAXP/USDT:USDT",
    "DUS/USDT:USDT",
    "RAY/USDT:USDT",
    "BSV/USDT:USDT",
    "SLERF/USDT:USDT",
    "AGLD/USDT:USDT",
    "MEW/USDT:USDT",
    "BTR/USDT:USDT",
    "COMP/USDT:USDT",
    "AIN/USDT:USDT",
    "BLUR/USDT:USDT",
    "FXS/USDT:USDT",
    "PHB/USDT:USDT",
    "VELVET/USDT:USDT",
    "RONIN/USDT:USDT",
    "ORCA/USDT:USDT",
    "ZETA/USDT:USDT",
    "AXL/USDT:USDT",
    "METIS/USDT:USDT",
    "B3/USDT:USDT",
    "MANTA/USDT:USDT",
    "SIGN/USDT:USDT",
    "BIGTIME/USDT:USDT",
    "YFI/USDT:USDT",
    "NEWT/USDT:USDT",
    "ERA/USDT:USDT",
    "SAHARA/USDT:USDT",
    "MILK/USDT:USDT",
    "DYM/USDT:USDT",
    "ZEREBRO/USDT:USDT",
    "IDOL/USDT:USDT",
    "GUN/USDT:USDT",
    "GLM/USDT:USDT",
    "VANRY/USDT:USDT",
    "HIPPO/USDT:USDT",
    "CETUS/USDT:USDT",
    "STORJ/USDT:USDT",
    "RESOLV/USDT:USDT",
    "F/USDT:USDT",
    "CHESS/USDT:USDT",
    "AI/USDT:USDT",
    "BABY/USDT:USDT",
    "HOME/USDT:USDT",
    "FIDA/USDT:USDT",
    "BID/USDT:USDT",
    "CATI/USDT:USDT",
    "HIGH/USDT:USDT",
    "PLAY/USDT:USDT",
    "TAC/USDT:USDT",
    "G/USDT:USDT",
    "SHELL/USDT:USDT",
    "MOVR/USDT:USDT",
    "SXP/USDT:USDT",
    "ESPORTS/USDT:USDT",
    "BAN/USDT:USDT",
    "HAEDAL/USDT:USDT",
    "ANKR/USDT:USDT",
    "CROSS/USDT:USDT",
    "TNSR/USDT:USDT",
    "IOTX/USDT:USDT",
    "ICNT/USDT:USDT",
    "1000RATS/USDT:USDT",
    "LSK/USDT:USDT",
    "MYRO/USDT:USDT",
    "DEGO/USDT:USDT",
    "MELANIA/USDT:USDT",
    "T/USDT:USDT",
    "NFP/USDT:USDT",
    "FHE/USDT:USDT",
    "SKYAI/USDT:USDT",
    "ZKJ/USDT:USDT",
    "TAG/USDT:USDT",
    "XCN/USDT:USDT",
    "SIREN/USDT:USDT",
    "MLN/USDT:USDT",
    "NKN/USDT:USDT",
    "GHST/USDT:USDT",
    "B/USDT:USDT",
    "LAYER/USDT:USDT",
    "HMSTR/USDT:USDT",
    "POLY/USDT:USDT",
    "AERGO/USDT:USDT",
    "AVA/USDT:USDT",
    "JST/USDT:USDT",
    "DEGEN/USDT:USDT",
    "COOKIE/USDT:USDT",
    "CARV/USDT:USDT",
    "OBOL/USDT:USDT",
    "DIA/USDT:USDT",
    "BDXN/USDT:USDT",
    "USTC/USDT:USDT",
    "CVC/USDT:USDT",
    "LUMIA/USDT:USDT",
    "COS/USDT:USDT",
    "CGPT/USDT:USDT",
    "BNT/USDT:USDT",
    "ETHW/USDT:USDT",
    "TANSSI/USDT:USDT",
    "1000X/USDT:USDT",
    "MAVIA/USDT:USDT",
    "VELODROME/USDT:USDT",
    "PUNDIX/USDT:USDT",
    "DF/USDT:USDT",
    "BULLA/USDT:USDT",
    "SOLV/USDT:USDT",
    "PONKE/USDT:USDT",
    "ACX/USDT:USDT",
    "SAFE/USDT:USDT",
    "CYBER/USDT:USDT",
    "DMC/USDT:USDT",
    "BR/USDT:USDT",
    "FIS/USDT:USDT",
    "FLUX/USDT:USDT",
    "TAIKO/USDT:USDT",
    "ZRC/USDT:USDT",
    "RIF/USDT:USDT",
    "SIN/USDT:USDT",
    "REI/USDT:USDT",
    "SWARMS/USDT:USDT",
    "CTK/USDT:USDT",
    "VTH/USDT:USDT",
    "HEI/USDT:USDT",
    "SYN/USDT:USDT",
    "SONIC/USDT:USDT",
    "OL/USDT:USDT",
    "PIPPIN/USDT:USDT",
    "MKR/USDT:USDT"
]
# -----------------------------
# 🔄 تنظیمات چند تایم‌فریمی (MULTI-TIMEFRAME)
TIMEFRAME_TREND_4H = "4h"
TIMEFRAME_TREND_1H = "1h"
TIMEFRAME_ANALYSIS = "30m"
TIMEFRAME_SIGNAL = "15m"
EMA_PERIOD = 50 # تغییر از 20 به 50
MIN_CANDLES_REQUIRED = 50
LOOKBACK_SWING = 20
VOLUME_PERIOD = 20
# 🆕 تنظیمات مانیجمنت و وین ریت
MAX_RISK_PER_TRADE = 0.02 # حداکثر ریسک 2% در هر معامله
MAX_DAILY_RISK = 0.05 # حداکثر ریسک 5% در روز
MAX_WEEKLY_RISK = 0.10 # حداکثر ریسک 10% در هفته
MIN_VOLATILITY_THRESHOLD = 0.006 # کاهش از 0.008 به 0.006 برای کمتر سخت‌گیری
WIN_RATE_LOOKBACK = 100 # تعداد معاملات گذشته برای محاسبه وین ریت
TRAILING_STOP_ACTIVATION = 0.008 # نرم‌تر از 0.01
TRAILING_STOP_DISTANCE = 0.004 # نرم‌تر از 0.005
# 🆕🆕 تنظیمات جدید برای فیلتر کردن سیگنال‌های پرریسک
MAX_ACCEPTABLE_RISK_PCT = 0.08 # نرم‌تر از 0.06 به 0.08
MAX_RR_RATIO = 4.0 # حداکثر نسبت ریسک به ریوارد (1:4)
TARGET_RR_MULTIPLIER = 2.0 # کاهش از 2.5 به 2.0 برای تارگت‌های واقعی‌تر
MIN_PROFIT_MARGIN_PCT = 2.0 # کاهش از 2.5 به 2.0 برای اجازه بیشتر سیگنال‌ها
MIN_STOP_DISTANCE_PCT = 0.005 # حداقل فاصله استاپ از ورود برای جلوگیری از استاپ نزدیک (0.5%)
VOLUME_CONFIRM_THRESHOLD = 1.1 # کاهش از 1.2 به 1.1 برای تایید حجم کمتر سخت‌گیر
ADX_MIN_FOR_BREAKOUT = 20 # کاهش از 25 به 20 برای اجازه breakout با روند ضعیف‌تر
FAKE_BREAKOUT_VOLUME_THRESHOLD = 1.3 # حداقل حجم برای تایید breakout واقعی (کاهش از 1.5)
FAKE_BREAKOUT_CANDLE_CONFIRM = True # نیاز به کندل تایید پس از breakout

# 🆕 تنظیمات RSI حرفه‌ای
RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
RSI_DIVERGENCE_LOOKBACK = 20  # برای تشخیص واگرایی

# 🆕 تنظیمات فیبوناچی
FIB_LEVELS = [0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0, 1.272, 1.618, 2.0, 2.618, 3.0, 4.236]  # سطوح استاندارد + اکستنشن‌ها
FIB_LOOKBACK = 50  # برای پیدا کردن سوئینگ‌های فیبو

# 🆕 تنظیمات R:R داینامیک (از 1 تا 10 بر اساس بازار)
MAX_RR_LEVELS = 10  # حداکثر R:R تا 10

exchange = getattr(ccxt, EXCHANGE_NAME)({
    'apiKey': API_KEY,
    'options': {
        'defaultType': 'future' # این خط کلیدی است برای اتصال به فیوچرز
    }
})
# -----------------------------
# 🆕 تابع تعیین رژیم کلی بازار
def get_market_regime(benchmark_symbol="BTC/USDT"):
    """
    تعیین رژیم کلی بازار با تحلیل یک جفت‌ارز مرجع (مانند BTC/USDT)
    """
    try:
        # تحلیل روی بالاترین تایم‌فریم برای دید بلندمدت
        df_benchmark = fetch_data(benchmark_symbol, TIMEFRAME_TREND_4H, limit=100)
        if df_benchmark is None or len(df_benchmark) < MIN_CANDLES_REQUIRED:
            return "UNKNOWN", 0
        df_benchmark = calculate_ema(df_benchmark)
        structure, _ = determine_market_structure(df_benchmark)
        current_price = df_benchmark['close'].iloc[-1]
        ema50 = df_benchmark['ema50'].iloc[-1]
        # محاسبه قدرت روند (مثلاً با فاصله از EMA50)
        trend_strength = 0
        if structure == "UP":
            trend_strength = ((current_price - ema50) / ema50) * 100
        elif structure == "DOWN":
            trend_strength = ((ema50 - current_price) / ema50) * 100
        # تعیین رژیم قطعی
        if structure == "UP" and trend_strength > 2: # مثلاً 2% بالاتر از EMA50
            return "STRONG_BULL", trend_strength
        elif structure == "DOWN" and trend_strength > 2: # مثلاً 2% پایین‌تر از EMA50
            return "STRONG_BEAR", trend_strength
        elif structure == "UP":
            return "BULLISH", trend_strength
        elif structure == "DOWN":
            return "BEARISH", trend_strength
        else:
            return "RANGE", trend_strength
    except Exception as e:
        return "UNKNOWN", 0
# -----------------------------
# 🆕 Decision Engine بهبودیافته
def decision_engine(analysis_result):
    """
    موتور تصمیم‌گیری نهایی برای سیگنال‌های معاملاتی بهبودیافته
    با ترکیب تمام شاخص‌ها و الگوها، تصمیم نهایی را اتخاذ می‌کند
    """
    signal = analysis_result['signal']
    buy_score = analysis_result['buy_score']
    sell_score = analysis_result['sell_score']
    volatility = analysis_result['volatility']
    win_rate = analysis_result['win_rate']
    # استخراج اطلاعات الگوها
    patterns = analysis_result.get('patterns', {})
    bullish_breakout = analysis_result.get('bullish_breakout')
    bearish_breakout = analysis_result.get('bearish_breakout')
    bullish_reversal = analysis_result.get('bullish_reversal')
    bearish_reversal = analysis_result.get('bearish_reversal')
    structure = analysis_result.get('structure') # اضافه شده برای فیلتر رنج
    risk_pct = analysis_result.get('risk_pct', 0) # ریسک درصدی
  
    # تصمیم اولیه بر اساس امتیاز
    decision = {
        'action': signal,
        'confidence': 0,
        'reason': [],
        'risk_level': 'MEDIUM'
    }
  
    # 🆕 کاهش سخت‌گیری: فقط اگر RANGE باشد و volatility کم، WAIT کن (نه همیشه)
    if structure == "RANGE" and volatility < MIN_VOLATILITY_THRESHOLD:
        decision['action'] = "WAIT"
        decision['reason'].append("Market in RANGE with low volatility - avoiding signals")
        decision['confidence'] = 0
        return decision
  
    # محاسبه اطمینان اولیه
    if signal == "BUY":
        decision['confidence'] = min(95, buy_score)
    elif signal == "SELL":
        decision['confidence'] = min(95, sell_score)
    else:
        decision['confidence'] = 30
        decision['reason'].append("No clear signal")
        return decision
  
    # بهبود: بررسی نوسان با آستانه‌های دینامیک (نرم‌تر)
    volatility_threshold = MIN_VOLATILITY_THRESHOLD * 0.8 # کاهش آستانه برای اجازه بیشتر سیگنال‌ها
    if signal == "BUY" and bullish_breakout is not None:
        volatility_threshold *= 0.7 # حتی نرم‌تر برای breakout
    elif signal == "SELL" and bearish_breakout is not None:
        volatility_threshold *= 0.7
  
    # 🆕🆕 فیلتر نوسان نرم‌تر: فقط اگر خیلی کم باشد WAIT کن
    if volatility < volatility_threshold:
        decision['action'] = "WAIT"
        decision['reason'].append(f"Low volatility ({volatility*100:.2f}% < {volatility_threshold*100:.2f}%) - avoiding range market")
        decision['confidence'] = 0
        return decision
  
    # بهبود: بررسی وین ریت با وزن‌دهی کمتر (نرم‌تر)
    if win_rate < 40: # نرم‌تر
        decision['confidence'] -= 5 # پنالتی کمتر
        decision['reason'].append(f"Low win rate: {win_rate:.1f}%")
    elif win_rate > 55: # کاهش آستانه از 60 به 55
        decision['confidence'] += 10 # بونوس کمتر برای تعادل
        decision['reason'].append(f"High win rate: {win_rate:.1f}%")
  
    # بررسی الگوهای قوی با وزن‌دهی بهبودیافته
    if bullish_breakout is not None and signal == "BUY":
        breakout_weight = 0.3 if bullish_breakout['confidence'] > 60 else 0.2 # کاهش آستانه از 70 به 60
        decision['confidence'] += bullish_breakout['confidence'] * breakout_weight
        decision['reason'].append(f"Bullish breakout with {bullish_breakout['confidence']}% confidence")
  
    if bearish_breakout is not None and signal == "SELL":
        breakout_weight = 0.3 if bearish_breakout['confidence'] > 60 else 0.2
        decision['confidence'] += bearish_breakout['confidence'] * breakout_weight
        decision['reason'].append(f"Bearish breakout with {bearish_breakout['confidence']}% confidence")
  
    if bullish_reversal is not None and signal == "BUY":
        reversal_weight = 0.4 if bullish_reversal['confidence'] > 60 else 0.3
        decision['confidence'] += bullish_reversal['confidence'] * reversal_weight
        decision['reason'].append(f"Bullish reversal with {bullish_reversal['confidence']}% confidence")
  
    if bearish_reversal is not None and signal == "SELL":
        reversal_weight = 0.4 if bearish_reversal['confidence'] > 60 else 0.3
        decision['confidence'] += bearish_reversal['confidence'] * reversal_weight
        decision['reason'].append(f"Bearish reversal with {bearish_reversal['confidence']}% confidence")
  
    # بررسی الگوهای تکنیکال با وزن‌دهی بهبودیافته
    if patterns is not None and len(patterns) > 0:
        if patterns.get('flag') is not None and patterns['flag']['type'] == 'bullish_flag' and signal == "BUY":
            flag_strength = min(20, 10 + patterns['flag']['pole_change'] * 100) # کاهش حداکثر از 25 به 20
            decision['confidence'] += flag_strength
            decision['reason'].append(f"Bullish flag pattern detected (strength: {flag_strength:.1f})")
 
        if patterns.get('flag') is not None and patterns['flag']['type'] == 'bearish_flag' and signal == "SELL":
            flag_strength = min(20, 10 + abs(patterns['flag']['pole_change']) * 100)
            decision['confidence'] += flag_strength
            decision['reason'].append(f"Bearish flag pattern detected (strength: {flag_strength:.1f})")
 
        if patterns.get('wedge') is not None and patterns['wedge']['type'] == 'falling_wedge' and signal == "BUY":
            wedge_strength = min(25, 15 + patterns['wedge']['convergence'] * 100) # کاهش حداکثر از 30 به 25
            decision['confidence'] += wedge_strength
            decision['reason'].append(f"Falling wedge pattern (bullish reversal) with {wedge_strength:.1f} strength")
 
        if patterns.get('wedge') is not None and patterns['wedge']['type'] == 'rising_wedge' and signal == "SELL":
            wedge_strength = min(25, 15 + patterns['wedge']['convergence'] * 100)
            decision['confidence'] += wedge_strength
            decision['reason'].append(f"Rising wedge pattern (bearish reversal) with {wedge_strength:.1f} strength")
 
        if patterns.get('ascending_triangle') is not None and signal == "BUY":
            triangle_strength = min(30, 18 + patterns['ascending_triangle']['convergence'] * 100) # کاهش از 35 به 30
            decision['confidence'] += triangle_strength
            decision['reason'].append(f"Ascending triangle pattern (bullish breakout) with {triangle_strength:.1f} strength")
 
        if patterns.get('descending_triangle') is not None and signal == "SELL":
            triangle_strength = min(30, 18 + patterns['descending_triangle']['convergence'] * 100)
            decision['confidence'] += triangle_strength
            decision['reason'].append(f"Descending triangle pattern (bearish breakdown) with {triangle_strength:.1f} strength")
  
    # بهبود: تعیین سطح ریسک با در نظر گرفتن وین ریت (نرم‌تر)
    if decision['confidence'] >= 70 and win_rate >= 55: # کاهش آستانه از 80/60 به 70/55
        decision['risk_level'] = 'LOW'
    elif decision['confidence'] >= 50 and win_rate >= 45: # کاهش از 60/50 به 50/45
        decision['risk_level'] = 'MEDIUM'
    else:
        decision['risk_level'] = 'HIGH'
  
    # 🆕🆕 فیلتر ریسک: اگر ریسک بیش از حداکثر باشد، WAIT کن
    if risk_pct > MAX_ACCEPTABLE_RISK_PCT:
        decision['action'] = "WAIT"
        decision['reason'].append(f"High risk: {risk_pct*100:.2f}% > {MAX_ACCEPTABLE_RISK_PCT*100:.1f}%")
  
    # تصمیم نهایی بر اساس اطمینان با آستانه دینامیک (نرم‌تر شده)
    confidence_threshold = 35 # کاهش از 40 به 35
    if win_rate >= 60:
        confidence_threshold = 30 # کاهش از 35 به 30
    elif win_rate <= 45:
        confidence_threshold = 40 # کاهش از 45 به 40
  
    if decision['confidence'] < confidence_threshold:
        decision['action'] = "WAIT"
        decision['reason'].append(f"Low confidence: {decision['confidence']:.1f}% < {confidence_threshold}%")
  
    # محدود کردن اطمینان در محدوده 0-100
    decision['confidence'] = max(0, min(100, decision['confidence']))
    return decision
# -----------------------------
# 🆕 محاسبه نوسان (Volatility) بهبودیافته - نسخه اصلاح شده
def calculate_volatility(df, period=14):
    """
    محاسبه نوسان با استفاده از ATR (Average True Range) بهبودیافته
    """
    if len(df) < period + 1:
        return 0
  
    # استفاده از .copy() برای اطمینان از کار روی یک کپی مستقل
    df_calc = df.copy()
  
    df_calc.loc[:, 'high_low'] = df_calc['high'] - df_calc['low']
    df_calc.loc[:, 'high_close'] = abs(df_calc['high'] - df_calc['close'].shift())
    df_calc.loc[:, 'low_close'] = abs(df_calc['low'] - df_calc['close'].shift())
    df_calc.loc[:, 'tr'] = df_calc[['high_low', 'high_close', 'low_close']].max(axis=1)
    df_calc.loc[:, 'atr'] = df_calc['tr'].rolling(window=period).mean()
  
    # بهبود: محاسبه نوسان نسبی به میانگین متحرک
    df_calc.loc[:, 'sma'] = df_calc['close'].rolling(window=period).mean()
    atr_relative_to_sma = df_calc['atr'].iloc[-1] / df_calc['sma'].iloc[-1] if df_calc['sma'].iloc[-1] > 0 else 0
  
    # بازگشت نوسان به صورت درصدی از قیمت
    atr_percent = df_calc['atr'].iloc[-1] / df_calc['close'].iloc[-1] if df_calc['close'].iloc[-1] > 0 else 0
  
    # ترکیب دو معیار برای نتیجه دقیق‌تر
    return (atr_percent + atr_relative_to_sma) / 2
# -----------------------------
# 🆕 محاسبه وین ریت بهبودیافته
def calculate_win_rate(symbol, signal_type, lookback=WIN_RATE_LOOKBACK):
    """
    محاسبه وین ریت تاریخی برای سیگنال‌های مشابه با در نظر گرفتن شرایط بازار
    """
    try:
        # دریافت داده‌های تاریخی برای تحلیل وین ریت
        df_historical = fetch_data(symbol, TIMEFRAME_SIGNAL, limit=lookback * 2)
 
        if df_historical is None or len(df_historical) < lookback:
            return 50.0 # مقدار پیش‌فرض اگر داده کافی نباشد
 
        # محاسبه نوسان تاریخی برای فیلتر کردن سیگنال‌ها
        historical_volatility = calculate_volatility(df_historical)
        current_volatility = calculate_volatility(df_historical.tail(lookback)) # Use recent data for current volatility
      
        # شبیه‌سازی معاملات گذشته بر اساس شرایط مشابه
        wins = 0
        total_trades = 0
 
        # تحلیل ساختار بازار
        structure, _ = determine_market_structure(df_historical)
      
        # بهبود: محاسبه شاخص قدرت روند (ADX)
        df_historical['adx'] = ta.trend.ADXIndicator(df_historical['high'], df_historical['low'], df_historical['close'], window=14).adx()
        avg_adx = df_historical['adx'].mean()
 
        # شبیه‌سازی سیگنال‌های خرید
        if signal_type == "BUY":
            for i in range(lookback, len(df_historical)):
                # شرایط مشابه سیگنال خرید فعلی با فیلترهای نرم‌تر
                volume_ok = df_historical['volume'].iloc[i-1] > df_historical['volume'].rolling(VOLUME_PERIOD).mean().iloc[i-1] * VOLUME_CONFIRM_THRESHOLD
                adx_ok = df_historical['adx'].iloc[i-1] > ADX_MIN_FOR_BREAKOUT # نرم‌تر
                volatility_ok = abs(historical_volatility - current_volatility) < 0.006 # نرم‌تر از 0.005
              
                if volume_ok and adx_ok and volatility_ok and structure in ["UP", "RANGE"]:
                    entry_price = df_historical['close'].iloc[i-1]
                    stop_loss = df_historical['low'].iloc[i-5:i].min() * 0.996 # شبیه‌سازی استاپ لاس
                    target1 = entry_price + (entry_price - stop_loss) * 1.5 # نرم‌تر از 2
                  
                    # بررسی نتیجه معامله در 7 کندل بعدی (افزایش از 5 به 7 برای واقعی‌تر)
                    for j in range(i, min(i+7, len(df_historical))):
                        if df_historical['high'].iloc[j] >= target1:
                            wins += 1
                            total_trades += 1
                            break
                        elif df_historical['low'].iloc[j] <= stop_loss:
                            total_trades += 1
                            break
 
        # شبیه‌سازی سیگنال‌های فروش
        elif signal_type == "SELL":
            for i in range(lookback, len(df_historical)):
                # شرایط مشابه سیگنال فروش فعلی با فیلترهای نرم‌تر
                volume_ok = df_historical['volume'].iloc[i-1] > df_historical['volume'].rolling(VOLUME_PERIOD).mean().iloc[i-1] * VOLUME_CONFIRM_THRESHOLD
                adx_ok = df_historical['adx'].iloc[i-1] > ADX_MIN_FOR_BREAKOUT # نرم‌تر
                volatility_ok = abs(historical_volatility - current_volatility) < 0.006 # نرم‌تر
              
                if volume_ok and adx_ok and volatility_ok and structure in ["DOWN", "RANGE"]:
                    entry_price = df_historical['close'].iloc[i-1]
                    stop_loss = df_historical['high'].iloc[i-5:i].max() * 1.004 # شبیه‌سازی استاپ لاس
                    target1 = entry_price - (stop_loss - entry_price) * 1.5 # نرم‌تر از 2
                  
                    # بررسی نتیجه معامله در 7 کندل بعدی
                    for j in range(i, min(i+7, len(df_historical))):
                        if df_historical['low'].iloc[j] <= target1:
                            wins += 1
                            total_trades += 1
                            break
                        elif df_historical['high'].iloc[j] >= stop_loss:
                            total_trades += 1
                            break
 
        # محاسبه وین ریت
        win_rate = (wins / total_trades * 100) if total_trades > 0 else 50.0
 
        # بهبود: تنظیم وین ریت بر اساس قدرت روند (نرم‌تر)
        if avg_adx > 35: # کاهش از 40 به 35
            win_rate = min(85.0, win_rate + 8) # بونوس کمتر
        elif avg_adx < 25: # افزایش از 20 به 25 برای پنالتی کمتر
            win_rate = max(35.0, win_rate - 8) # پنالتی کمتر
      
        # اطمینان از اینکه وین ریت در محدوده معقول است
        win_rate = max(35.0, min(85.0, win_rate))
 
        return win_rate
    except Exception as e:
        return 50.0 # مقدار پیش‌فرض در صورت خطا
# -----------------------------
# 🆕 محاسبه حجم معامله بهبودیافته
def calculate_position_size(entry_price, stop_loss, account_balance, risk_percentage=MAX_RISK_PER_TRADE, volatility=None, win_rate=None):
    """
    محاسبه حجم معامله بر اساس مدیریت ریسک بهبودیافته
    با در نظر گرفتن نوسان و وین ریت
    """
    if entry_price <= 0 or stop_loss <= 0 or account_balance <= 0:
        return 0
  
    # محاسبه مقدار ریسک در هر واحد از ارز
    risk_per_unit = abs(entry_price - stop_loss)
  
    # بهبود: تنظیم ریسک بر اساس نوسان و وین ریت (نرم‌تر)
    adjusted_risk_percentage = risk_percentage
  
    if volatility is not None:
        # کاهش ریسک در بازارهای پرنوسان (آستانه بالاتر)
        if volatility > 0.04: # افزایش از 0.03 به 0.04
            adjusted_risk_percentage *= 0.8 # پنالتی کمتر
        elif volatility < 0.012: # افزایش از 0.01 به 0.012
            adjusted_risk_percentage *= 1.1 # بونوس کمتر
  
    if win_rate is not None:
        # افزایش ریسک برای سیگنال‌های با وین ریت بالا (آستانه پایین‌تر)
        if win_rate > 60: # کاهش از 65 به 60
            adjusted_risk_percentage *= 1.15 # افزایش کمتر
        elif win_rate < 50: # افزایش از 45 به 50 برای پنالتی کمتر
            adjusted_risk_percentage *= 0.85 # پنالتی کمتر
  
    # محاسبه مقدار ریسک کل مجاز
    risk_amount = account_balance * adjusted_risk_percentage
  
    # محاسبه حجم معامله
    position_size = risk_amount / risk_per_unit if risk_per_unit > 0 else 0
  
    return position_size
# -----------------------------
# 🆕 محاسبه تریلینگ استاپ
def calculate_trailing_stop(df, entry_price, current_price, initial_stop_loss, is_buy_signal):
    """
    محاسبه تریلینگ استاپ برای محافظت از سود
    """
    if is_buy_signal:
        # برای سیگنال خرید
        profit_pct = (current_price - entry_price) / entry_price
 
        # فعال شدن تریلینگ استاپ پس از رسیدن به سود مشخص
        if profit_pct >= TRAILING_STOP_ACTIVATION:
            # محاسبه تریلینگ استاپ
            trailing_stop = current_price * (1 - TRAILING_STOP_DISTANCE)
     
            # تریلینگ استاپ نباید کمتر از استاپ لاس اولیه باشد
            return max(trailing_stop, initial_stop_loss)
 
        return initial_stop_loss
    else:
        # برای سیگنال فروش
        profit_pct = (entry_price - current_price) / entry_price
 
        # فعال شدن تریلینگ استاپ پس از رسیدن به سود مشخص
        if profit_pct >= TRAILING_STOP_ACTIVATION:
            # محاسبه تریلینگ استاپ
            trailing_stop = current_price * (1 + TRAILING_STOP_DISTANCE)
     
            # تریلینگ استاپ نباید بیشتر از استاپ لاس اولیه باشد
            return min(trailing_stop, initial_stop_loss)
 
        return initial_stop_loss
# -----------------------------
# 🆕🔄 تشخیص Bullish Breakout (شکست صعودی) بهبودیافته - نسخه اصلاح شده
def detect_bullish_breakout(df, lookback=50):
    """
    تشخیص شکست صعودی (Bullish Breakout) بهبودیافته
    - شکست سطح مقاومت کلیدی با حجم بالا
    - قیمت از محدوده رنج خارج می‌شود
    """
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy()
  
    # بهبود: محاسبه شاخص قدرت روند (ADX)
    recent.loc[:, 'adx'] = ta.trend.ADXIndicator(recent['high'], recent['low'], recent['close'], window=14).adx()
  
    # یافتن سطح مقاومت (بالاترین قیمت‌های اخیر)
    resistance = recent['high'].quantile(0.95)
  
    # قیمت فعلی و حجم
    current_price = recent['close'].iloc[-1]
    current_volume = recent['volume'].iloc[-1]
    avg_volume = recent['volume'].mean()
    current_adx = recent['adx'].iloc[-1]
  
    # شرایط Bullish Breakout بهبودیافته:
    # 1. قیمت بالای مقاومت
    # 2. حجم بالاتر از میانگین (حداقل 1.3x کاهش از 1.5)
    # 3. کندل صعودی قوی
    # 4. قدرت روند کافی (ADX > 20 کاهش از 25)
    last_candle_bullish = recent['close'].iloc[-1] > recent['open'].iloc[-1]
    candle_body = abs(recent['close'].iloc[-1] - recent['open'].iloc[-1])
    candle_range = recent['high'].iloc[-1] - recent['low'].iloc[-1]
    strong_body = candle_body > (candle_range * 0.5) if candle_range > 0 else False # نرم‌تر از 0.6
  
    # 🆕 فیلتر fake breakout: چک حجم و ADX، و کندل تایید
    is_fake = False
    if current_volume < avg_volume * FAKE_BREAKOUT_VOLUME_THRESHOLD or current_adx < ADX_MIN_FOR_BREAKOUT:
        is_fake = True
    if FAKE_BREAKOUT_CANDLE_CONFIRM and not (last_candle_bullish and strong_body):
        is_fake = True
  
    if current_price > resistance and not is_fake:
        # محاسبه قدرت شکست
        breakout_strength = ((current_price - resistance) / resistance) * 100
        volume_strength = current_volume / avg_volume
      
        # بهبود: محاسبه اطمینان با در نظر گرفتن ADX
        base_confidence = min(100, int(breakout_strength * 10 + volume_strength * 20))
        adx_bonus = min(20, int((current_adx - ADX_MIN_FOR_BREAKOUT) * 1.5)) if current_adx > ADX_MIN_FOR_BREAKOUT else 0 # بونوس کمتر سخت‌گیر
        confidence = base_confidence + adx_bonus
      
        return {
            'type': 'bullish_breakout',
            'resistance_level': resistance,
            'breakout_strength': breakout_strength,
            'volume_ratio': volume_strength,
            'adx': current_adx,
            'confidence': confidence
        }
    return None
# -----------------------------
# 🆕🔄 تشخیص Bearish Breakout (شکست نزولی) بهبودیافته - نسخه اصلاح شده
def detect_bearish_breakout(df, lookback=50):
    """
    تشخیص شکست نزولی (Bearish Breakout/Breakdown) بهبودیافته
    - شکست سطح حمایت کلیدی با حجم بالا
    - قیمت از محدوده رنج خارج می‌شود
    """
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy()
  
    # بهبود: محاسبه شاخص قدرت روند (ADX)
    recent.loc[:, 'adx'] = ta.trend.ADXIndicator(recent['high'], recent['low'], recent['close'], window=14).adx()
  
    # یافتن سطح حمایت (پایین‌ترین قیمت‌های اخیر)
    support = recent['low'].quantile(0.05)
  
    # قیمت فعلی و حجم
    current_price = recent['close'].iloc[-1]
    current_volume = recent['volume'].iloc[-1]
    avg_volume = recent['volume'].mean()
    current_adx = recent['adx'].iloc[-1]
  
    # شرایط Bearish Breakout بهبودیافته:
    # 1. قیمت زیر حمایت
    # 2. حجم بالاتر از میانگین (حداقل 1.3x کاهش از 1.5)
    # 3. کندل نزولی قوی
    # 4. قدرت روند کافی (ADX > 20 کاهش از 25)
    last_candle_bearish = recent['close'].iloc[-1] < recent['open'].iloc[-1]
    candle_body = abs(recent['close'].iloc[-1] - recent['open'].iloc[-1])
    candle_range = recent['high'].iloc[-1] - recent['low'].iloc[-1]
    strong_body = candle_body > (candle_range * 0.5) if candle_range > 0 else False # نرم‌تر
  
    # 🆕 فیلتر fake breakout: چک حجم و ADX، و کندل تایید
    is_fake = False
    if current_volume < avg_volume * FAKE_BREAKOUT_VOLUME_THRESHOLD or current_adx < ADX_MIN_FOR_BREAKOUT:
        is_fake = True
    if FAKE_BREAKOUT_CANDLE_CONFIRM and not (last_candle_bearish and strong_body):
        is_fake = True
  
    if current_price < support and not is_fake:
        # محاسبه قدرت شکست
        breakout_strength = ((support - current_price) / support) * 100
        volume_strength = current_volume / avg_volume
      
        # بهبود: محاسبه اطمینان با در نظر گرفتن ADX
        base_confidence = min(100, int(breakout_strength * 10 + volume_strength * 20))
        adx_bonus = min(20, int((current_adx - ADX_MIN_FOR_BREAKOUT) * 1.5)) if current_adx > ADX_MIN_FOR_BREAKOUT else 0
        confidence = base_confidence + adx_bonus
      
        return {
            'type': 'bearish_breakout',
            'support_level': support,
            'breakout_strength': breakout_strength,
            'volume_ratio': volume_strength,
            'adx': current_adx,
            'confidence': confidence
        }
    return None
# -----------------------------
# 🆕 تشخیص Major Trend Reversal صعودی
def detect_bullish_trend_reversal(df, lookback=100):
    """
    تشخیص بازگشت روند به صعودی (Bullish Major Trend Reversal)
    - تغییر از روند نزولی به صعودی
    - سری سوئینگ‌های Higher Lows و Higher Highs
    - تایید با حجم
    """
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy()
    # محاسبه EMA50 به جای EMA20
    recent['ema_50'] = ta.trend.EMAIndicator(recent['close'], 50).ema_indicator()
    # شرایط Bullish Reversal:
    # 1. قیمت از زیر EMA50 به بالای آن رسیده
    # 2. حجم معاملات افزایش یافته
    current_price = recent['close'].iloc[-1]
    prev_price = recent['close'].iloc[-20]
    ema50_current = recent['ema_50'].iloc[-1]
    ema50_prev = recent['ema_50'].iloc[-5]
    # قیمت بالای EMA50
    price_above_ema50 = current_price > ema50_current
    # روند قیمت صعودی شده (20 کندل اخیر)
    price_trend_up = current_price > prev_price
    # بررسی افزایش حجم
    volume_first_half = recent['volume'].iloc[:len(recent)//2].mean()
    volume_second_half = recent['volume'].iloc[len(recent)//2:].mean()
    volume_increasing = volume_second_half > volume_first_half * 1.1 # نرم‌تر از 1.2
    # امتیازدهی (نرم‌تر: حداقل 45 امتیاز برای تایید)
    score = 0
    if price_above_ema50:
        score += 35 # کاهش از 40 به 35
    if price_trend_up:
        score += 25 # کاهش از 30 به 25
    if volume_increasing:
        score += 25 # کاهش از 30 به 25
    if score >= 45: # کاهش از 50 به 45
        return {
            'type': 'bullish_major_reversal',
            'price_above_ema50': price_above_ema50,
            'volume_increasing': volume_increasing,
            'confidence': score,
            'price_change': ((current_price - prev_price) / prev_price) * 100
        }
    return None
# -----------------------------
# 🆕 تشخیص Major Trend Reversal نزولی
def detect_bearish_trend_reversal(df, lookback=100):
    """
    تشخیص بازگشت روند به نزولی (Bearish Major Trend Reversal)
    - تغییر از روند صعودی به نزولی
    - سری سوئینگ‌های Lower Highs و Lower Lows
    - تایید با حجم
    """
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy()
    # محاسبه EMA50 به جای EMA20
    recent['ema_50'] = ta.trend.EMAIndicator(recent['close'], 50).ema_indicator()
    # شرایط Bearish Reversal:
    # 1. قیمت از بالای EMA50 به زیر آن رسیده
    # 2. حجم معاملات افزایش یافته
    current_price = recent['close'].iloc[-1]
    prev_price = recent['close'].iloc[-20]
    ema50_current = recent['ema_50'].iloc[-1]
    ema50_prev = recent['ema_50'].iloc[-5]
    # قیمت زیر EMA50
    price_below_ema50 = current_price < ema50_current
    # روند قیمت نزولی شده (20 کندل اخیر)
    price_trend_down = current_price < prev_price
    # بررسی افزایش حجم
    volume_first_half = recent['volume'].iloc[:len(recent)//2].mean()
    volume_second_half = recent['volume'].iloc[len(recent)//2:].mean()
    volume_increasing = volume_second_half > volume_first_half * 1.1 # نرم‌تر
    # امتیازدهی (نرم‌تر)
    score = 0
    if price_below_ema50:
        score += 35
    if price_trend_down:
        score += 25
    if volume_increasing:
        score += 25
    if score >= 45: # کاهش آستانه
        return {
            'type': 'bearish_major_reversal',
            'price_below_ema50': price_below_ema50,
            'volume_increasing': volume_increasing,
            'confidence': score,
            'price_change': ((current_price - prev_price) / prev_price) * 100
        }
    return None
# -----------------------------
# 🆕 تشخیص Signal Bar و Key Bar
def detect_signal_and_key_bars(df, lookback=10):
    """
    تشخیص Signal Bar و Key Bar برای تعیین نقاط ورود به بهتر
    Signal Bar: کندلی که سیگنال اولیه را می‌دهد (معمولاً کندل برگشتی قوی)
    Key Bar: کندل کلیدی که تایید نهایی را می‌دهد (شکست سطح مهم با حجم)
    """
    if len(df) < lookback:
        return None
    result = {
        'signal_bar': None,
        'key_bar': None,
        'entry_quality': 0
    }
    recent = df.tail(lookback).copy()
    # محاسبه اندازه بدنه و سایه‌ها
    recent['body'] = abs(recent['close'] - recent['open'])
    recent['lower_shadow'] = recent[['open', 'close']].min(axis=1) - recent['low']
    recent['upper_shadow'] = recent['high'] - recent[['open', 'close']].max(axis=1)
    recent['total_range'] = recent['high'] - recent['low']
    # میانگین حجم
    avg_volume = recent['volume'].mean()
    # جستجو برای Signal Bar (کندل با ویژگی‌های خاص)
    for i in range(len(recent)-2, -1, -1):
        candle = recent.iloc[i]
        next_candle = recent.iloc[i+1] if i+1 < len(recent) else None
        # شرایط Bullish Signal Bar (نرم‌تر)
        if candle['close'] > candle['open']: # کندل صعودی
            body_ratio = candle['body'] / candle['total_range'] if candle['total_range'] > 0 else 0
            lower_shadow_ratio = candle['lower_shadow'] / candle['total_range'] if candle['total_range'] > 0 else 0
    
            # Signal Bar باید بدنه قوی (>50% کاهش از 60%) یا سایه پایین بلند (>40% کاهش از 50%) داشته باشد
            if (body_ratio > 0.5 and candle['volume'] > avg_volume * 1.1) or \
               (lower_shadow_ratio > 0.4 and candle['volume'] > avg_volume * 0.9): # حجم کمتر سخت‌گیر
                result['signal_bar'] = {
                    'index': i,
                    'type': 'bullish',
                    'price': candle['close'],
                    'body_ratio': body_ratio,
                    'volume_ratio': candle['volume'] / avg_volume
                }
                break
        # شرایط Bearish Signal Bar (نرم‌تر)
        elif candle['close'] < candle['open']: # کندل نزولی
            body_ratio = candle['body'] / candle['total_range'] if candle['total_range'] > 0 else 0
            upper_shadow_ratio = candle['upper_shadow'] / candle['total_range'] if candle['total_range'] > 0 else 0
    
            if (body_ratio > 0.5 and candle['volume'] > avg_volume * 1.1) or \
               (upper_shadow_ratio > 0.4 and candle['volume'] > avg_volume * 0.9):
                result['signal_bar'] = {
                    'index': i,
                    'type': 'bearish',
                    'price': candle['close'],
                    'body_ratio': body_ratio,
                    'volume_ratio': candle['volume'] / avg_volume
                }
                break
    # جستجو برای Key Bar (کندل تایید کننده) با شرایط نرم‌تر
    if result['signal_bar'] is not None:
        signal_idx = result['signal_bar']['index']
        signal_type = result['signal_bar']['type']
        # بررسی کندل‌های بعد از Signal Bar
        for i in range(signal_idx + 1, len(recent)):
            candle = recent.iloc[i]
    
            if signal_type == 'bullish':
                # Key Bar صعودی: شکست بالای Signal Bar با حجم بالا (نرم‌تر 1.3 کاهش از 1.5)
                if candle['close'] > result['signal_bar']['price'] and \
                   candle['volume'] > avg_volume * 1.3:
                    result['key_bar'] = {
                        'index': i,
                        'type': 'bullish',
                        'price': candle['close'],
                        'volume_ratio': candle['volume'] / avg_volume,
                        'breakout_strength': (candle['close'] - result['signal_bar']['price']) / result['signal_bar']['price']
                    }
                    break
    
            elif signal_type == 'bearish':
                # Key Bar نزولی: شکست پایین Signal Bar با حجم بالا
                if candle['close'] < result['signal_bar']['price'] and \
                   candle['volume'] > avg_volume * 1.3:
                    result['key_bar'] = {
                        'index': i,
                        'type': 'bearish',
                        'price': candle['close'],
                        'volume_ratio': candle['volume'] / avg_volume,
                        'breakout_strength': (result['signal_bar']['price'] - candle['close']) / result['signal_bar']['price']
                    }
                    break
    # محاسبه کیفیت نقطه ورود بر اساس Signal Bar و Key Bar (نرم‌تر)
    if result['signal_bar'] is not None and result['key_bar'] is not None:
        entry_quality = 0
        # امتیاز حجم Signal Bar (آستانه پایین‌تر)
        if result['signal_bar']['volume_ratio'] > 1.3:
            entry_quality += 12 # کاهش از 15
        elif result['signal_bar']['volume_ratio'] > 1.0:
            entry_quality += 8 # کاهش از 10
        # امتیاز حجم Key Bar
        if result['key_bar']['volume_ratio'] > 1.8:
            entry_quality += 18 # کاهش از 20
        elif result['key_bar']['volume_ratio'] > 1.3:
            entry_quality += 12 # کاهش از 15
        # امتیاز قدرت شکست (آستانه پایین‌تر)
        if result['key_bar']['breakout_strength'] > 0.015: # 1.5% کاهش از 2%
            entry_quality += 12 # کاهش از 15
        elif result['key_bar']['breakout_strength'] > 0.008: # 0.8% کاهش از 1%
            entry_quality += 8 # کاهش از 10
        # امتیاز بدنه Signal Bar (آستانه پایین‌تر)
        if result['signal_bar']['body_ratio'] > 0.6:
            entry_quality += 8 # کاهش از 10
        elif result['signal_bar']['body_ratio'] > 0.5:
            entry_quality += 4 # کاهش از 5
        result['entry_quality'] = entry_quality
    elif result['signal_bar'] is not None:
        # فقط Signal Bar موجود است
        result['entry_quality'] = 5
    return result if result['signal_bar'] is not None or result['key_bar'] is not None else None
# -----------------------------
# الگوهای تکنیکال جدید
def detect_flag_pattern(df, lookback=30):
    """تشخیص الگوی Flag (پرچم) صعودی و نزولی"""
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy()
    # محاسبه میانگین حجم
    avg_volume = recent['volume'].mean()
    # بررسی وجود pole (میله پرچم) - حرکت قوی با حجم بالا
    pole_start = lookback - 20
    pole_end = lookback - 10
    pole_data = recent.iloc[pole_start:pole_end]
    if len(pole_data) < 5:
        return None
    pole_change = (pole_data['close'].iloc[-1] - pole_data['close'].iloc[0]) / pole_data['close'].iloc[0]
    pole_volume = pole_data['volume'].mean()
    # Flag باید pole قوی داشته باشد (حداقل 2.5% تغییر کاهش از 3%)
    if abs(pole_change) < 0.025:
        return None
    # بررسی flag (پرچم) - consolidation با حجم کم
    flag_data = recent.iloc[pole_end:]
    if len(flag_data) < 5:
        return None
    flag_high = flag_data['high'].max()
    flag_low = flag_data['low'].min()
    flag_range = (flag_high - flag_low) / flag_low
    flag_volume = flag_data['volume'].mean()
    # Flag باید consolidation کوچک باشد (کمتر از 6% افزایش از 5%)
    if flag_range > 0.06:
        return None
    # حجم در flag باید کمتر از pole باشد (آستانه نرم‌تر)
    if flag_volume >= pole_volume * 0.9: # افزایش از 0.8 به 0.9
        return None
    # تشخیص جهت
    if pole_change > 0:
        # Bullish flag
        flag_trend_line = np.polyfit(range(len(flag_data)), flag_data['high'], 1)
        if flag_trend_line[0] < 0: # خط بالای flag نزولی یا صاف باشد
            return {'type': 'bullish_flag', 'pole_change': pole_change, 'flag_range': flag_range}
    else:
        # Bearish flag
        flag_trend_line = np.polyfit(range(len(flag_data)), flag_data['low'], 1)
        if flag_trend_line[0] > 0: # خط پایین flag صعودی یا صاف باشد
            return {'type': 'bearish_flag', 'pole_change': pole_change, 'flag_range': flag_range}
    return None
def detect_wedge_pattern(df, lookback=50):
    """تشخیص الگوهای Wedge (گوه)"""
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy().reset_index(drop=True)
    # محاسبه خطوط روند برای highs و lows
    x = np.arange(len(recent))
    try:
        upper_trend = np.polyfit(x, recent['high'], 1)
        lower_trend = np.polyfit(x, recent['low'], 1)
    except:
        return None
    upper_slope = upper_trend[0]
    lower_slope = lower_trend[0]
    # محاسبه همگرایی خطوط
    start_distance = abs((upper_trend[1]) - (lower_trend[1]))
    end_distance = abs((upper_trend[0] * len(recent) + upper_trend[1]) -
                      (lower_trend[0] * len(recent) + lower_trend[1]))
    convergence = (start_distance - end_distance) / start_distance if start_distance > 0 else 0
    # Wedge باید همگرا باشد (حداقل 15% کاهش از 20%)
    if convergence < 0.15:
        return None
    # تشخیص نوع Wedge
    price_trend = (recent['close'].iloc[-1] - recent['close'].iloc[0]) / recent['close'].iloc[0]
    # Rising Wedge (نزولی) - هر دو خط صعودی
    if upper_slope > 0 and lower_slope > 0:
        if upper_slope < lower_slope: # خط پایین شیب تندتر
            return {'type': 'rising_wedge', 'direction': 'bearish', 'convergence': convergence}
    # Falling Wedge (صعودی) - هر دو خط نزولی
    elif upper_slope < 0 and lower_slope < 0:
        if abs(lower_slope) > abs(upper_slope): # خط پایین شیب تندتر
            return {'type': 'falling_wedge', 'direction': 'bullish', 'convergence': convergence}
    return None
def detect_rectangle_pattern(df, lookback=50):
    """تشخیص الگوی Rectangle (مستطیل)"""
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy()
    # یافتن سطوح مقاومت و حمایت
    resistance = recent['high'].quantile(0.95)
    support = recent['low'].quantile(0.05)
    range_size = (resistance - support) / support
    # Rectangle باید محدوده مشخص داشته باشد (2-10% افزایش از 8%)
    if range_size < 0.02 or range_size > 0.10:
        return None
    # بررسی تعداد دفعاتی که قیمت به سطوح رسیده (حداقل 2 بار کاهش از 3)
    touches_resistance = ((recent['high'] >= resistance * 0.98).sum())
    touches_support = ((recent['low'] <= support * 1.02).sum())
    if touches_resistance < 2 or touches_support < 2:
        return None
    # بررسی روند قبلی برای تعیین جهت احتمالی شکست
    pre_pattern = df.iloc[-lookback-20:-lookback] if len(df) > lookback+20 else None
    if pre_pattern is not None and len(pre_pattern) > 10:
        pre_trend = (pre_pattern['close'].iloc[-1] - pre_pattern['close'].iloc[0]) / pre_pattern['close'].iloc[0]
        if pre_trend > 0.04: # کاهش از 0.05 به 0.04
            # روند صعودی قبلی - احتمال شکست صعودی
            return {'type': 'rectangle', 'direction': 'bullish_continuation',
                   'resistance': resistance, 'support': support, 'range': range_size}
        elif pre_trend < -0.04:
            # روند نزولی قبلی - احتمال شکست نزولی
            return {'type': 'rectangle', 'direction': 'bearish_continuation',
                   'resistance': resistance, 'support': support, 'range': range_size}
    return {'type': 'rectangle', 'direction': 'neutral',
           'resistance': resistance, 'support': support, 'range': range_size}
def detect_symmetrical_triangle(df, lookback=50):
    """تشخیص الگوی Symmetrical Triangle"""
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy().reset_index(drop=True)
    # محاسبه خطوط روند
    x = np.arange(len(recent))
    try:
        upper_trend = np.polyfit(x, recent['high'], 1)
        lower_trend = np.polyfit(x, recent['low'], 1)
    except:
        return None
    upper_slope = upper_trend[0]
    lower_slope = lower_trend[0]
    # در Symmetrical Triangle، خط بالا نزولی و خط پایین صعودی است
    if upper_slope >= 0 or lower_slope <= 0:
        return None
    # بررسی همگرایی (حداقل 25% کاهش از 30%)
    start_distance = abs(upper_trend[1] - lower_trend[1])
    end_distance = abs((upper_trend[0] * len(recent) + upper_trend[1]) -
                      (lower_trend[0] * len(recent) + lower_trend[1]))
    convergence = (start_distance - end_distance) / start_distance if start_distance > 0 else 0
    if convergence < 0.25:
        return None
    # بررسی تقارن شیب‌ها (باید تقریباً برابر باشند) (نرم‌تر 0.4 تا 2.5)
    slope_ratio = abs(upper_slope / lower_slope) if lower_slope != 0 else 0
    if slope_ratio < 0.4 or slope_ratio > 2.5:
        return None
    # بررسی حجم (باید در انتها کاهش یابد)
    volume_first_half = recent['volume'].iloc[:len(recent)//2].mean()
    volume_second_half = recent['volume'].iloc[len(recent)//2:].mean()
    volume_decline = (volume_first_half - volume_second_half) / volume_first_half if volume_first_half > 0 else 0
    # تعیین جهت احتمالی بر اساس روند قبلی
    pre_pattern = df.iloc[-lookback-20:-lookback] if len(df) > lookback+20 else None
    direction = 'neutral'
    if pre_pattern is not None and len(pre_pattern) > 10:
        pre_trend = (pre_pattern['close'].iloc[-1] - pre_pattern['close'].iloc[0]) / pre_pattern['close'].iloc[0]
        if pre_trend > 0.025: # کاهش از 0.03 به 0.025
            direction = 'bullish_continuation'
        elif pre_trend < -0.025:
            direction = 'bearish_continuation'
    return {
        'type': 'symmetrical_triangle',
        'direction': direction,
        'convergence': convergence,
        'upper_slope': upper_slope,
        'lower_slope': lower_slope,
        'volume_decline': volume_decline
    }
def detect_ascending_triangle(df, lookback=50):
    """تشخیص الگوی Ascending Triangle (صعودی)"""
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy().reset_index(drop=True)
    x = np.arange(len(recent))
    try:
        upper_trend = np.polyfit(x, recent['high'], 1)
        lower_trend = np.polyfit(x, recent['low'], 1)
    except:
        return None
    upper_slope = upper_trend[0]
    lower_slope = lower_trend[0]
    # در Ascending Triangle:
    # - خط بالا افقی یا تقریباً افقی (مقاومت)
    # - خط پایین صعودی (حمایت صعودی)
    # بررسی خط بالا افقی باشد (شیب نزدیک به صفر) (نرم‌تر)
    if abs(upper_slope) > 0.0008: # افزایش از 0.0005 به 0.0008
        return None
    # بررسی خط پایین صعودی باشد
    if lower_slope <= 0:
        return None
    # محاسبه همگرایی (حداقل 15% کاهش از 20%)
    start_distance = abs(upper_trend[1] - lower_trend[1])
    end_distance = abs((upper_trend[0] * len(recent) + upper_trend[1]) -
                      (lower_trend[0] * len(recent) + lower_trend[1]))
    convergence = (start_distance - end_distance) / start_distance if start_distance > 0 else 0
    if convergence < 0.15:
        return None
    # بررسی تعداد برخورد به خط مقاومت (حداقل 1 کاهش از 2)
    resistance_level = upper_trend[1]
    touches_resistance = (recent['high'] >= resistance_level * 0.98).sum()
    if touches_resistance < 1:
        return None
    # Ascending Triangle معمولاً الگوی ادامه‌دهنده صعودی است
    return {
        'type': 'ascending_triangle',
        'direction': 'bullish',
        'convergence': convergence,
        'resistance_level': resistance_level,
        'lower_slope': lower_slope,
        'touches_resistance': touches_resistance
    }
def detect_descending_triangle(df, lookback=50):
    """تشخیص الگوی Descending Triangle (نزولی)"""
    if len(df) < lookback:
        return None
    recent = df.tail(lookback).copy().reset_index(drop=True)
    x = np.arange(len(recent))
    try:
        upper_trend = np.polyfit(x, recent['high'], 1)
        lower_trend = np.polyfit(x, recent['low'], 1)
    except:
        return None
    upper_slope = upper_trend[0]
    lower_slope = lower_trend[0]
    # در Descending Triangle:
    # - خط پایین افقی یا تقریباً افقی (حمایت)
    # - خط بالا نزولی (مقاومت نزولی)
    # بررسی خط پایین افقی باشد (شیب نزدیک به صفر)
    if abs(lower_slope) > 0.0008: # نرم‌تر
        return None
    # بررسی خط بالا نزولی باشد
    if upper_slope >= 0:
        return None
    # محاسبه همگرایی (نرم‌تر)
    start_distance = abs(upper_trend[1] - lower_trend[1])
    end_distance = abs((upper_trend[0] * len(recent) + upper_trend[1]) -
                      (lower_trend[0] * len(recent) + lower_trend[1]))
    convergence = (start_distance - end_distance) / start_distance if start_distance > 0 else 0
    if convergence < 0.15:
        return None
    # بررسی تعداد برخورد به خط حمایت (نرم‌تر)
    support_level = lower_trend[1]
    touches_support = (recent['low'] <= support_level * 1.02).sum()
    if touches_support < 1:
        return None
    # Descending Triangle معمولاً الگوی ادامه‌دهنده نزولی است
    return {
        'type': 'descending_triangle',
        'direction': 'bearish',
        'convergence': convergence,
        'support_level': support_level,
        'upper_slope': upper_slope,
        'touches_support': touches_support
    }
# -----------------------------
# 🆕🆕 تابع جدید برای محاسبه سطوح فیبوناچی بر اساس سوئینگ‌های اخیر
def calculate_fib_levels(df, lookback=FIB_LOOKBACK):
    """
    محاسبه سطوح فیبوناچی retracement و extension بر اساس آخرین سوئینگ high/low
    """
    if len(df) < lookback:
        return None
    recent = df.tail(lookback)
    swing_lows, swing_highs = swing_points(recent, n=5)
    
    if len(swing_highs) < 1 or len(swing_lows) < 1:
        return None
    
    # آخرین سوئینگ high و low
    last_high = swing_highs['high'].max()
    last_low = swing_lows['low'].min()
    fib_diff = last_high - last_low
    
    fib_levels = {}
    for level in FIB_LEVELS:
        if level <= 1.0:
            fib_levels[level] = last_high - fib_diff * level  # retracement
        else:
            fib_levels[level] = last_high + fib_diff * (level - 1.0)  # extension
    
    return {
        'fib_high': last_high,
        'fib_low': last_low,
        'levels': fib_levels
    }

# 🆕🆕 تابع محاسبه RSI و واگرایی
def detect_rsi_signals(df, period=RSI_PERIOD, lookback_div=RSI_DIVERGENCE_LOOKBACK):
    """
    محاسبه RSI و تشخیص سیگنال‌های overbought/oversold و واگرایی
    """
    if len(df) < period + 1:
        return {'rsi': None, 'divergence': None}
    
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=period).rsi()
    current_rsi = df['rsi'].iloc[-1]
    
    # سیگنال overbought/oversold
    rsi_signal = "NEUTRAL"
    if current_rsi < RSI_OVERSOLD:
        rsi_signal = "OVERSOLD"  # سیگنال خرید احتمالی
    elif current_rsi > RSI_OVERBOUGHT:
        rsi_signal = "OVERBOUGHT"  # سیگنال فروش احتمالی
    
    # تشخیص واگرایی (divergence)
    recent = df.tail(lookback_div)
    swing_lows, swing_highs = swing_points(recent, n=5)
    
    divergence = None
    if len(swing_highs) >= 2:
        last_two_highs = swing_highs.tail(2)
        high1_price = last_two_highs['high'].iloc[0]
        high2_price = last_two_highs['high'].iloc[1]
        high1_rsi = recent['rsi'].loc[last_two_highs.index[0]]
        high2_rsi = recent['rsi'].loc[last_two_highs.index[1]]
        
        if high2_price > high1_price and high2_rsi < high1_rsi:
            divergence = "BEARISH_DIVERGENCE"  # سیگنال فروش
        elif high2_price < high1_price and high2_rsi > high1_rsi:
            divergence = "BULLISH_DIVERGENCE"  # سیگنال خرید
    
    if len(swing_lows) >= 2:
        last_two_lows = swing_lows.tail(2)
        low1_price = last_two_lows['low'].iloc[0]
        low2_price = last_two_lows['low'].iloc[1]
        low1_rsi = recent['rsi'].loc[last_two_lows.index[0]]
        low2_rsi = recent['rsi'].loc[last_two_lows.index[1]]
        
        if low2_price < low1_price and low2_rsi > low1_rsi:
            divergence = "BULLISH_DIVERGENCE"  # سیگنال خرید
        elif low2_price > low1_price and low2_rsi < low1_rsi:
            divergence = "BEARISH_DIVERGENCE"  # سیگنال فروش
    
    return {
        'rsi_value': current_rsi,
        'rsi_signal': rsi_signal,
        'divergence': divergence
    }
# -----------------------------
# 🆕🆕🆕 تابع محاسبه R:R واقعی بازار بر اساس فیبوناچی و volatility
def calculate_dynamic_rr(df, signal_type, entry, stop_loss, fib_levels, volatility):
    """
    محاسبه R:R داینامیک از 1 تا 10 بر اساس سطوح فیبو و نوسان بازار
    """
    risk = abs(entry - stop_loss)
    if risk <= 0:
        return [1.0, 2.0, 3.0]  # پیش‌فرض اگر ریسک صفر باشد
    
    rr_levels = []
    max_rr = min(10, int(volatility * 1000))  # داینامیک بر اساس volatility (مثلاً volatility 0.01 → max_rr=10)
    if max_rr < 1:
        max_rr = 1
    
    for i in range(1, max_rr + 1):
        rr_levels.append(i)
    
    # تنظیم بر اساس فیبو: نزدیک‌ترین سطح فیبو برای هر R
    adjusted_rr = []
    for rr in rr_levels:
        target_candidate = entry + risk * rr if signal_type == "BUY" else entry - risk * rr
        # پیدا کردن نزدیک‌ترین سطح فیبو
        closest_fib_level = min(fib_levels['levels'].values(), key=lambda x: abs(x - target_candidate))
        adjusted_rr.append(abs(closest_fib_level - entry) / risk)  # R:R جدید بر اساس فیبو
    
    return sorted(adjusted_rr[:MAX_RR_LEVELS])  # حداکثر 10 سطح

# -----------------------------
# -----------------------------
# تابع جدید: محاسبه استاپ لاس بر اساس آخرین سوئینگ + ATR(14)
def calculate_atr_based_stoploss(df, signal_type, entry_price, atr_multiplier=0.6, min_risk_pct=0.004, max_risk_pct=0.07):
    """
    محاسبه استاپ لاس حرفه‌ای با ترکیب آخرین سوئینگ و ATR(14)
    """
    if len(df) < 50:
        return None, None

    df = df.copy()

    # محاسبه ATR(14)
    df['tr'] = pd.DataFrame({
        'high_low': df['high'] - df['low'],
        'high_close': abs(df['high'] - df['close'].shift()),
        'low_close': abs(df['low'] - df['close'].shift())
    }).max(axis=1)
    df['atr_14'] = df['tr'].rolling(window=14).mean()
    current_atr = df['atr_14'].iloc[-1]

    if pd.isna(current_atr) or current_atr <= 0:
        return None, None

    # پیدا کردن آخرین Swing High و Swing Low
    swing_lows, swing_highs = swing_points(df, n=5)

    if signal_type == "BUY":
        if len(swing_lows) == 0:
            return None, None
        last_swing_low = swing_lows['low'].iloc[-1]
        stop_loss = last_swing_low - (current_atr * atr_multiplier)
        risk_pct = (entry_price - stop_loss) / entry_price

        # فیلتر فاصله استاپ
        if risk_pct < min_risk_pct:
            stop_loss = entry_price * (1 - min_risk_pct)  # حداقل 0.4%
            risk_pct = min_risk_pct
        elif risk_pct > max_risk_pct:
            return None, None  # ریسک بیش از حد → سیگنال نامعتبر

    elif signal_type == "SELL":
        if len(swing_highs) == 0:
            return None, None
        last_swing_high = swing_highs['high'].iloc[-1]
        stop_loss = last_swing_high + (current_atr * atr_multiplier)
        risk_pct = (stop_loss - entry_price) / entry_price

        if risk_pct < min_risk_pct:
            stop_loss = entry_price * (1 + min_risk_pct)
            risk_pct = min_risk_pct
        elif risk_pct > max_risk_pct:
            return None, None  # ریسک بیش از حد

    else:
        return None, None

    return stop_loss, risk_pct
    # -----------------------------
# 1. استاپ لاس بر اساس ATR + آخرین سوئینگ (هوشمند و ایمن)
def calculate_atr_based_stoploss(df, signal_type, entry_price, atr_period=14, atr_mult=0.8):
    """
    استاپ لاس: آخرین سوئینگ ± ATR × 0.6~1.0
    خیلی ایمن و حرفه‌ای — استاپ هانت نمی‌شه
    """
    if len(df) < 50:
        return None, None

    recent = df.tail(50).copy()

    # محاسبه ATR
    high_low = recent['high'] - recent['low']
    high_close = abs(recent['high'] - recent['close'].shift())
    low_close = abs(recent['low'] - recent['close'].shift())
    tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
    atr = tr.rolling(window=atr_period).mean().iloc[-1]

    if pd.isna(atr) or atr <= 0:
        atr = (recent['high'] - recent['low']).mean() * 0.8

    buffer = atr * atr_mult  # 0.6 تا 1.0

    if signal_type == "BUY":
        swing_low = recent['low'].min()
        stop_loss = swing_low - buffer
        # حداقل فاصله 0.4%
        if (entry_price - stop_loss) / entry_price < 0.004:
            stop_loss = entry_price * (1 - 0.004)
    else:  # SELL
        swing_high = recent['high'].max()
        stop_loss = swing_high + buffer
        if (stop_loss - entry_price) / entry_price < 0.004:
            stop_loss = entry_price * (1 + 0.004)

    risk_pct = abs(entry_price - stop_loss) / entry_price
    return round(stop_loss, 8), round(risk_pct, 5)


# -----------------------------
# 2. محاسبه سطوح فیبوناچی از آخرین سوئینگ بزرگ
def calculate_fib_levels(df, lookback=100):
    """
    فیبوناچی از آخرین سوئینگ High به Low (یا برعکس)
    """
    if len(df) < lookback:
        lookback = len(df) - 10

    recent = df.tail(lookback)
    high = recent['high'].max()
    low = recent['low'].min()
    diff = high - low

    if diff <= 0:
        return None

    levels = {
        '0.0%': high,
        '23.6%': high - diff * 0.236,
        '38.2%': high - diff * 0.382,
        '50.0%': high - diff * 0.5,
        '61.8%': high - diff * 0.618,
        '78.6%': high - diff * 0.786,
        '100%': low,
        '127.2%': low - diff * 0.272,
        '161.8%': low - diff * 0.618,
        '200%': low - diff * 1.0,
    }
    return {'high': high, 'low': low, 'levels': levels}


# -----------------------------
# 3. R:R داینامیک بر اساس نوسان و ساختار بازار
def calculate_dynamic_rr(df, signal_type, entry, stop_loss, fib_levels, volatility):
    """
    R:R داینامیک: در بازار پرنوسان → R:R بالاتر
    """
    risk = abs(entry - stop_loss)
    base_rr = [1.5, 2.5, 4.0, 6.0, 8.0, 10.0]  # تا 1:10

    # تنظیم بر اساس نوسان
    if volatility > 0.02:  # بازار خیلی پرنوسان
        ratios = [2.0, 3.5, 5.5, 8.0, 10.0, 12.0]
    elif volatility > 0.012:
        ratios = base_rr
    else:
        ratios = [1.3, 2.0, 3.0, 4.5, 6.0, 8.0]

    # اگر نزدیک سطح فیبو قوی باشیم → R:R بالاتر
    near_618 = any(abs(entry - lvl) / entry < 0.008 for lvl in fib_levels['levels'].values())
    if near_618:
        ratios = [r * 1.2 for r in ratios]

    return ratios[:6]  # حداکثر 6 تارگت


# -----------------------------
# حالا تابع اصلی که نوشتی (کمی بهینه‌تر شده)
def calculate_price_action_targets(entry, signal_type, df, structure):
    """
    نسخه نهایی: استاپ هوشمند + فیبو + R:R داینامیک
    """
    if len(df) < 50:
        return None, None

    # 1. استاپ لاس هوشمند
    stop_loss, risk_pct = calculate_atr_based_stoploss(df, signal_type, entry, atr_mult=0.8)
    if stop_loss is None:
        return None, None

    # 2. فیبوناچی
    fib = calculate_fib_levels(df)
    if fib is None:
        return None, None

    # 3. نوسان
    vol = calculate_volatility(df)

    # 4. R:R داینامیک
    rr_ratios = calculate_dynamic_rr(df, signal_type, entry, stop_loss, fib, vol)

    risk = abs(entry - stop_loss)
    targets = {}

    for i, rr in enumerate(rr_ratios, 1):
        if signal_type == "BUY":
            tp = entry + risk * rr
        else:
            tp = entry - risk * rr

        # تنظیم تارگت روی نزدیک‌ترین فیبو
        fib_values = list(fib['levels'].values())
        if signal_type == "BUY":
            candidates = [x for x in fib_values if x > entry]
        else:
            candidates = [x for x in fib_values if x < entry]

        if candidates:
            closest = min(candidates, key=lambda x: abs(x - tp))
            # فقط اگر خیلی نزدیک باشه جایگزین کن
            if abs(closest - tp) / entry < 0.015:
                tp = closest

        targets[f'tp{i}'] = round(tp, 8)

    return stop_loss, targets
# -----------------------------
# بازنویسی کامل تابع calculate_price_action_targets با روش جدید
def calculate_price_action_targets(entry, signal_type, df, structure):
    """
    محاسبه استاپ لاس و تارگت‌ها با روش جدید:
    - استاپ لاس: آخرین سوئینگ ± ATR(14) × 0.6
    - تارگت‌ها: بر اساس فیبوناچی + R:R داینامیک
    """
    if len(df) < 50:
        return None, None

    # محاسبه استاپ لاس با روش جدید
    stop_loss, risk_pct = calculate_atr_based_stoploss(df, signal_type, entry)
    if stop_loss is None:
        return None, None

    # محاسبه سطوح فیبوناچی
    fib_levels = calculate_fib_levels(df)
    if fib_levels is None:
        return None, None

    # تنظیم استاپ لاس با نزدیک‌ترین سطح فیبو (اختیاری، برای بهبود)
    buffer = 0.0005  # 0.05%
    if signal_type == "BUY":
        fib_candidates = [lvl for lvl in fib_levels['levels'].values() if lvl < entry - (entry * 0.005)]
        if fib_candidates:
            closest_fib = max(fib_candidates)
            stop_loss = min(stop_loss, closest_fib * (1 - buffer))
    else:
        fib_candidates = [lvl for lvl in fib_levels['levels'].values() if lvl > entry + (entry * 0.005)]
        if fib_candidates:
            closest_fib = min(fib_candidates)
            stop_loss = max(stop_loss, closest_fib * (1 + buffer))

    risk = abs(entry - stop_loss)
    if risk <= 0:
        return None, None

    # محاسبه R:R داینامیک
    volatility = calculate_volatility(df)
    rr_ratios = calculate_dynamic_rr(df, signal_type, entry, stop_loss, fib_levels, volatility)

    targets = {}
    for i, rr in enumerate(rr_ratios[:6], 1):  # حداکثر 6 تارگت
        if signal_type == "BUY":
            target = entry + risk * rr
        else:
            target = entry - risk * rr

        # تنظیم تارگت به نزدیک‌ترین سطح فیبو
        if signal_type == "BUY":
            fib_above = [lvl for lvl in fib_levels['levels'].values() if lvl > entry]
            if fib_above:
                closest = min(fib_above, key=lambda x: abs(x - target))
                target = closest
        else:
            fib_below = [lvl for lvl in fib_levels['levels'].values() if lvl < entry]
            if fib_below:
                closest = max(fib_below, key=lambda x: abs(x - target))
                target = closest

        targets[f'tp{i}'] = round(target, 8)

    return stop_loss, targets
# -----------------------------
def fetch_data(symbol, timeframe, limit=300):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        return None
# -----------------------------
def swing_points(df, n=5):
    lows = df['low']
    highs = df['high']
    swing_lows = df[(lows.shift(n) > lows) & (lows.shift(-n) > lows)]
    swing_highs = df[(highs.shift(n) < highs) & (highs.shift(-n) < highs)]
    return swing_lows, swing_highs
# -----------------------------
def price_action_patterns(df):
    body = abs(df['close'] - df['open'])
    lower_shadow = df[['open','close']].min(axis=1) - df['low']
    upper_shadow = df['high'] - df[['open','close']].max(axis=1)
    bullish_pin = (lower_shadow >= 2*body) & (upper_shadow <= body)
    bearish_pin = (upper_shadow >= 2*body) & (lower_shadow <= body)
    bullish_eng = (df['close'] > df['open']) & (df['open'].shift(1) > df['close'].shift(1)) & (df['close'] > df['open'].shift(1))
    bearish_eng = (df['close'] < df['open']) & (df['open'].shift(1) < df['close'].shift(1)) & (df['close'] < df['open'].shift(1))
    inside = (df['high'] < df['high'].shift(1)) & (df['low'] > df['low'].shift(1))
    doji = body <= (df['high'] - df['low']) * 0.1
    spinning_top = (body <= (df['high'] - df['low']) * 0.3) & (~doji)
    return bullish_pin, bearish_pin, bullish_eng, bearish_eng, inside, doji, spinning_top
# -----------------------------
def trendlines(df, n=20):
    highs = df['high'].rolling(n).max()
    lows = df['low'].rolling(n).min()
    return highs, lows
# -----------------------------
def detect_channel_levels(df, lookback=50):
    if len(df) < lookback:
        return []
    recent_df = df.tail(lookback).reset_index(drop=True)
    highs = recent_df['high'].values
    lows = recent_df['low'].values
    channels = []
    x = np.arange(len(lows))
    z = np.polyfit(x, lows, 1)
    if z[0] > 0:
        channels.append({'type': 'ascending_support', 'slope': z[0], 'intercept': z[1]})
    z = np.polyfit(x, highs, 1)
    if z[0] < 0:
        channels.append({'type': 'descending_resistance', 'slope': z[0], 'intercept': z[1]})
    return channels
# -----------------------------
def detect_horizontal_levels(df, lookback=100, threshold=0.02):
    if len(df) < lookback:
        return []
    recent_df = df.tail(lookback)
    levels = []
    swing_lows, swing_highs = swing_points(recent_df, n=5)
    if len(swing_lows) > 0:
        support_prices = swing_lows['low'].values
        for price in support_prices:
            levels.append({'type': 'horizontal_support', 'price': price})
    if len(swing_highs) > 0:
        resistance_prices = swing_highs['high'].values
        for price in resistance_prices:
            levels.append({'type': 'horizontal_resistance', 'price': price})
    return levels
# -----------------------------
def detect_trend_levels(df):
    swing_lows, swing_highs = swing_points(df, n=LOOKBACK_SWING)
    trend_levels = []
    if len(swing_lows) >= 2:
        last_two_lows = swing_lows.tail(2)
        if len(last_two_lows) == 2:
            idx = list(last_two_lows.index)
            prices = list(last_two_lows['low'])
            slope = (prices[1] - prices[0]) / (idx[1] - idx[0]) if idx[1] != idx[0] else 0
            trend_levels.append({'type': 'uptrend_line', 'slope': slope, 'points': list(zip(idx, prices))})
    if len(swing_highs) >= 2:
        last_two_highs = swing_highs.tail(2)
        if len(last_two_highs) == 2:
            idx = list(last_two_highs.index)
            prices = list(last_two_highs['high'])
            slope = (prices[1] - prices[0]) / (idx[1] - idx[0]) if idx[1] != idx[0] else 0
            trend_levels.append({'type': 'downtrend_line', 'slope': slope, 'points': list(zip(idx, prices))})
    return trend_levels
# -----------------------------
def detect_previous_day_levels(df):
    try:
        df_copy = df.copy()
        df_copy['date'] = df_copy['timestamp'].dt.date
        daily = df_copy.groupby('date').agg({'high': 'max', 'low': 'min'})
        if len(daily) >= 2:
            prev_day = daily.iloc[-2]
            return {
                'prev_day_high': prev_day['high'],
                'prev_day_low': prev_day['low']
            }
    except:
        pass
    return None
# -----------------------------
def calculate_ema(df):
    df['ema50'] = ta.trend.EMAIndicator(df['close'], EMA_PERIOD).ema_indicator()
    return df
# -----------------------------
def get_weekly_map(df):
    try:
        df_copy = df.copy()
        df_copy['week'] = df_copy['timestamp'].dt.isocalendar().week
        df_copy['year'] = df_copy['timestamp'].dt.year
        weekly = df_copy.groupby(['year', 'week']).agg({'high': 'max', 'low': 'min'})
        if len(weekly) >= 2:
            current_week = weekly.iloc[-1]
            prev_week = weekly.iloc[-2]
    
            return {
                'current_week_high': current_week['high'],
                'current_week_low': current_week['low'],
                'prev_week_high': prev_week['high'],
                'prev_week_low': prev_week['low']
            }
    except:
        pass
    return None
# -----------------------------
def get_swings_sequence(df, lookback=LOOKBACK_SWING):
    swing_lows, swing_highs = swing_points(df, n=lookback//4 if lookback>=4 else 1)
    seq = []
    highs = [(int(i), 'H', float(row['high'])) for i, row in swing_highs.iterrows()]
    lows = [(int(i), 'L', float(row['low'])) for i, row in swing_lows.iterrows()]
    combined = highs + lows
    combined_sorted = sorted(combined, key=lambda x: x[0])
    return combined_sorted[-12:]
def determine_market_structure(df):
    seq = get_swings_sequence(df)
    if len(seq) < 4:
        return "RANGE", seq
    highs_all = [x for x in seq if x[1]=='H']
    lows_all = [x for x in seq if x[1]=='L']
    if len(highs_all) >= 2 and len(lows_all) >= 2:
        last_high = highs_all[-1][2]
        prev_high = highs_all[-2][2]
        last_low = lows_all[-1][2]
        prev_low = lows_all[-2][2]
        if (last_high > prev_high) and (last_low > prev_low):
            return "UP", seq
        elif (last_high < prev_high) and (last_low < prev_low):
            return "DOWN", seq
        else:
            return "RANGE", seq
    else:
        return "RANGE", seq
# -----------------------------
def compute_trendline_from_structure(df, seq, structure):
    result = {'slope': None, 'intercept': None, 'points': [], 'type': None}
    if structure == "UP":
        lows = [x for x in seq if x[1]=='L']
        if len(lows) >= 2:
            p1 = lows[-2]
            p2 = lows[-1]
            idx1, _, price1 = p1
            idx2, _, price2 = p2
            x1 = float(idx1)
            x2 = float(idx2)
            if x2 != x1:
                slope = (price2 - price1) / (x2 - x1)
                intercept = price1 - slope * x1
                result.update({'slope': slope, 'intercept': intercept, 'points': [(idx1, price1), (idx2, price2)], 'type': 'up'})
    elif structure == "DOWN":
        highs = [x for x in seq if x[1]=='H']
        if len(highs) >= 2:
            p1 = highs[-2]
            p2 = highs[-1]
            idx1, _, price1 = p1
            idx2, _, price2 = p2
            x1 = float(idx1)
            x2 = float(idx2)
            if x2 != x1:
                slope = (price2 - price1) / (x2 - x1)
                intercept = price1 - slope * x1
                result.update({'slope': slope, 'intercept': intercept, 'points': [(idx1, price1), (idx2, price2)], 'type': 'down'})
    return result
def price_on_trendline(trend, idx):
    if trend['slope'] is None:
        return None
    x = float(idx)
    return trend['slope'] * x + trend['intercept']
# -----------------------------
def detect_breakout(df, seq, trend, structure):
    res = {'breakout': False, 'type': None, 'reason': None}
    if df is None or len(df) < 2:
        return res
    last_close = float(df['close'].iloc[-1])
    prev_close = float(df['close'].iloc[-2])
    last_volume = float(df['volume'].iloc[-1])
    volume_ma = float(df['volume'].rolling(VOLUME_PERIOD).mean().iloc[-1]) if len(df) >= VOLUME_PERIOD else 0
    highs = [x for x in seq if x[1]=='H']
    lows = [x for x in seq if x[1]=='L']
    if len(highs) > 0:
        last_swing_high = highs[-1][2]
    else:
        last_swing_high = None
    if len(lows) > 0:
        last_swing_low = lows[-1][2]
    else:
        last_swing_low = None
    vol_confirm = last_volume >= max(volume_ma, 1e-9) * FAKE_BREAKOUT_VOLUME_THRESHOLD # نرم‌تر با آستانه پایین‌تر
    if structure == "UP":
        if last_swing_high is not None and last_close > last_swing_high and vol_confirm:
            res.update({'breakout': True, 'type': 'up', 'reason': 'close_above_swing_high_with_volume'})
            return res
        if trend and trend.get('type')=='up' and trend.get('slope') is not None:
            price_on_line = price_on_trendline(trend, df.index[-1])
            if price_on_line is not None and last_close > price_on_line and prev_close <= price_on_line and vol_confirm:
                res.update({'breakout': True, 'type': 'up', 'reason': 'break_trendline_with_volume'})
                return res
    if structure == "DOWN":
        if last_swing_low is not None and last_close < last_swing_low and vol_confirm:
            res.update({'breakout': True, 'type': 'down', 'reason': 'close_below_swing_low_with_volume'})
            return res
        if trend and trend.get('type')=='down' and trend.get('slope') is not None:
            price_on_line = price_on_trendline(trend, df.index[-1])
            if price_on_line is not None and last_close < price_on_line and prev_close >= price_on_line and vol_confirm:
                res.update({'breakout': True, 'type': 'down', 'reason': 'break_trendline_with_volume'})
                return res
    return res
# -----------------------------
# ✅ تابع تحلیل فاندامنتال جدید (مبتنی بر RSS)
def analyze_fundamental(symbol):
    """
    تحلیل فاندامنتال با استفاده از فیدهای RSS خبری
    این تابع به هیچ API کلیدی نیاز ندارد و اخبار عمومی بازار را تحلیل می‌کند.
    """
    try:
        # استخراج نام ارز از symbol (مثل BTC از BTC/USDT)
        coin = symbol.split('/')[0].lower()
        # لیست فیدهای RSS معتبر برای اخبار کریپتوکارنسی
        rss_feeds = [
            'https://cointelegraph.com/rss', # Cointelegraph RSS
            'https://www.coindesk.com/arc/outboundfeeds/rss/', # CoinDesk RSS
            'https://decrypt.co/feed' # Decrypt RSS
        ]
        # کلمات کلیدی برای تحلیل احساسات (همان کلمات قبلی برای حفظ ثبات منطق)
        bullish_keywords = [
            'surge', 'rally', 'bullish', 'gains', 'up', 'rise', 'pump', 'moon', 'breakout',
            'adoption', 'partnership', 'listing', 'launch', 'upgrade', 'support', 'buy',
            'long', 'bull', 'integration', 'mainnet', 'staking', 'airdrop', 'etf', 'approval'
        ]
        bearish_keywords = [
            'crash', 'drop', 'bearish', 'fall', 'down', 'dump', 'plunge', 'collapse',
            'hack', 'ban', 'regulation', 'delisting', 'scam', 'fud', 'resistance', 'sell',
            'short', 'bear', 'vulnerability', 'exploit', 'sec', 'lawsuit', 'delay', 'rejection'
        ]
        bullish_count = 0
        bearish_count = 0
        neutral_count = 0
        total_articles_analyzed = 0
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        for feed_url in rss_feeds:
            try:
                response = requests.get(feed_url, headers=headers, timeout=10)
                response.raise_for_status() # برای بررسی خطاهای HTTP
                # تجزیه فید RSS با استفاده از کتابخانه استاندارد xml
                root = ET.fromstring(response.content)
                # RSS feeds می‌توانند ساختارهای متفاوتی داشته باشند
                # ما هر دو حالت standard RSS و Atom را پوشش می‌دهیم
                items = root.findall('.//item') or root.findall('.//{http://www.w3.org/2005/Atom}entry')
                for item in items[:15]: # تحلیل ۱۵ عنوان اخیر از هر فید
                    title_element = item.find('title')
                    if title_element is None:
                        title_element = item.find('{http://www.w3.org/2005/Atom}title')
                    if title_element is not None and title_element.text:
                        title = title_element.text.lower().strip()
                        # فقط اخبار مرتبط با symbol را در نظر بگیر
                        if coin in title:
                            total_articles_analyzed += 1
                            is_bullish = any(word in title for word in bullish_keywords)
                            is_bearish = any(word in title for word in bearish_keywords)
                            if is_bullish and not is_bearish:
                                bullish_count += 1
                            elif is_bearish and not is_bullish:
                                bearish_count += 1
                            else:
                                neutral_count += 1
            except requests.exceptions.RequestException as e:
                # اگر یک فید در دسترس نبود، به سراغ بقیه برو
                continue
            except ET.ParseError:
                # اگر محتوای RSS نامعتبر بود، از آن صرف نظر کن
                continue
        # اگر هیچ مقاله‌ای تحلیل نشد، احساسات را خنثی در نظر بگیر
        if total_articles_analyzed == 0:
            return "خنثی", 0
        # محاسبه احساسات نهایی
        if bullish_count > bearish_count:
            strength = min((bullish_count - bearish_count) * 2, 10) # قدرت سیگنال
            return "صعودی", strength
        elif bearish_count > bullish_count:
            strength = min((bearish_count - bullish_count) * 2, 10) # قدرت سیگنال
            return "نزولی", strength
        else:
            return "خنثی", 0
    except Exception as e:
        # در صورت بروز هر خطای پیش‌بینی نشده، حالت خنثی را برگردان
        return "خنثی", 0
# -----------------------------
def calculate_trading_score(df, structure, seq, trend, breakout_info, fundamental_sentiment, fund_strength, support_resistance_info, patterns, signal_key_bars, bullish_breakout, bearish_breakout, bullish_reversal, bearish_reversal):
    if df is None or len(df) < MIN_CANDLES_REQUIRED:
        return 0, 0, {}
    buy_score = 0
    sell_score = 0
    details = {}
    current_price = df['close'].iloc[-1]
    if structure == "UP":
        buy_score += 18 # کاهش از 20 برای تعادل
        details['market_structure'] = '+18 (UP trend)'
    elif structure == "DOWN":
        sell_score += 18
        details['market_structure'] = '+18 (DOWN trend)'
    else:
        details['market_structure'] = '0 (RANGE)'
    # 🆕 امتیازدهی Bullish Breakout
    if bullish_breakout is not None:
        breakout_score = min(25, int(bullish_breakout['confidence'] * 0.25)) # کاهش وزن از 0.3 به 0.25
        buy_score += breakout_score
        details['bullish_breakout'] = f'+{breakout_score} (Bullish Breakout detected - strength: {bullish_breakout["breakout_strength"]:.2f}%, volume: {bullish_breakout["volume_ratio"]:.2f}x)'
    # 🆕 امتیازدهی Bearish Breakout
    if bearish_breakout is not None:
        breakout_score = min(25, int(bearish_breakout['confidence'] * 0.25))
        sell_score += breakout_score
        details['bearish_breakout'] = f'+{breakout_score} (Bearish Breakout detected - strength: {bearish_breakout["breakout_strength"]:.2f}%, volume: {bearish_breakout["volume_ratio"]:.2f}x)'
    # 🆕 امتیازدهی Bullish Major Trend Reversal
    if bullish_reversal is not None:
        reversal_score = min(30, int(bullish_reversal['confidence'] * 0.3)) # کاهش از 0.35
        buy_score += reversal_score
        reversal_details = f'+{reversal_score} (Bullish Trend Reversal'
        reversal_details += f', Price change: {bullish_reversal["price_change"]:.2f}%)'
        details['bullish_major_reversal'] = reversal_details
    # 🆕 امتیازدهی Bearish Major Trend Reversal
    if bearish_reversal is not None:
        reversal_score = min(30, int(bearish_reversal['confidence'] * 0.3))
        sell_score += reversal_score
        reversal_details = f'+{reversal_score} (Bearish Trend Reversal'
        reversal_details += f', Price change: {bearish_reversal["price_change"]:.2f}%)'
        details['bearish_major_reversal'] = reversal_details
    # امتیازدهی Signal Bar و Key Bar
    if signal_key_bars is not None:
        entry_quality = signal_key_bars.get('entry_quality', 0)
        if entry_quality > 0:
            if signal_key_bars.get('signal_bar') is not None and signal_key_bars.get('key_bar') is not None:
                if signal_key_bars['signal_bar']['type'] == 'bullish' and signal_key_bars['key_bar']['type'] == 'bullish':
                    buy_score += entry_quality
                    details['signal_key_bars'] = f'+{entry_quality} (Strong bullish setup: Signal Bar + Key Bar confirmed)'
                elif signal_key_bars['signal_bar']['type'] == 'bearish' and signal_key_bars['key_bar']['type'] == 'bearish':
                    sell_score += entry_quality
                    details['signal_key_bars'] = f'+{entry_quality} (Strong bearish setup: Signal Bar + Key Bar confirmed)'
            elif signal_key_bars.get('signal_bar') is not None:
                signal_type = signal_key_bars['signal_bar']['type']
                if signal_type == 'bullish':
                    buy_score += entry_quality
                    details['signal_key_bars'] = f'+{entry_quality} (Signal Bar detected - awaiting Key Bar)'
                elif signal_type == 'bearish':
                    sell_score += entry_quality
                    details['signal_key_bars'] = f'+{entry_quality} (Signal Bar detected - awaiting Key Bar)'
    # امتیازدهی الگوهای تکنیکال
    if patterns is not None and len(patterns) > 0:
        if patterns.get('flag') is not None:
            flag = patterns['flag']
            if flag['type'] == 'bullish_flag':
                buy_score += 12 # کاهش از 15
                details['pattern_flag'] = f'+12 (Bullish Flag detected, pole: {flag["pole_change"]*100:.1f}%)'
            elif flag['type'] == 'bearish_flag':
                sell_score += 12
                details['pattern_flag'] = f'+12 (Bearish Flag detected, pole: {flag["pole_change"]*100:.1f}%)'
        if patterns.get('wedge') is not None:
            wedge = patterns['wedge']
            if wedge['type'] == 'falling_wedge' and wedge['direction'] == 'bullish':
                if structure == "DOWN":
                    buy_score += 18 # کاهش از 20
                    details['pattern_wedge'] = f'+18 (Falling Wedge in downtrend - reversal signal)'
                else:
                    buy_score += 10 # کاهش از 12
                    details['pattern_wedge'] = f'+10 (Falling Wedge detected)'
            elif wedge['type'] == 'rising_wedge' and wedge['direction'] == 'bearish':
                if structure == "UP":
                    sell_score += 18
                    details['pattern_wedge'] = f'+18 (Rising Wedge in uptrend - reversal signal)'
                else:
                    sell_score += 10
                    details['pattern_wedge'] = f'+10 (Rising Wedge detected)'
        if patterns.get('rectangle') is not None:
            rect = patterns['rectangle']
            if rect['direction'] == 'bullish_continuation':
                buy_score += 10 # کاهش از 12
                details['pattern_rectangle'] = f'+10 (Rectangle in uptrend - continuation expected)'
            elif rect['direction'] == 'bearish_continuation':
                sell_score += 10
                details['pattern_rectangle'] = f'+10 (Rectangle in downtrend - continuation expected)'
            else:
                details['pattern_rectangle'] = f'0 (Rectangle neutral - range: {rect["range"]*100:.1f}%)'
        if patterns.get('symmetrical_triangle') is not None:
            sym_tri = patterns['symmetrical_triangle']
            if sym_tri['direction'] == 'bullish_continuation':
                buy_score += 15 # کاهش از 18
                details['pattern_symmetrical_triangle'] = f'+15 (Symmetrical Triangle - bullish continuation, convergence: {sym_tri["convergence"]*100:.1f}%)'
            elif sym_tri['direction'] == 'bearish_continuation':
                sell_score += 15
                details['pattern_symmetrical_triangle'] = f'+15 (Symmetrical Triangle - bearish continuation, convergence: {sym_tri["convergence"]*100:.1f}%)'
            else:
                details['pattern_symmetrical_triangle'] = f'0 (Symmetrical Triangle neutral - convergence: {sym_tri["convergence"]*100:.1f}%)'
        if patterns.get('ascending_triangle') is not None:
            asc_tri = patterns['ascending_triangle']
            buy_score += 20 # کاهش از 22
            details['pattern_ascending_triangle'] = f'+20 (Ascending Triangle - bullish breakout expected, convergence: {asc_tri["convergence"]*100:.1f}%)'
        if patterns.get('descending_triangle') is not None:
            desc_tri = patterns['descending_triangle']
            sell_score += 20
            details['pattern_descending_triangle'] = f'+20 (Descending Triangle - bearish breakdown expected, convergence: {desc_tri["convergence"]*100:.1f}%)'
    bullish_pin, bearish_pin, bullish_eng, bearish_eng, inside, doji, spinning_top = price_action_patterns(df)
    candle_buy = 0
    candle_sell = 0
    if bullish_pin.iloc[-1] == True:
        candle_buy += 7 # کاهش از 8
        details['candle_bullish_pin'] = '+7'
    if bullish_eng.iloc[-1] == True:
        candle_buy += 8 # کاهش از 10
        details['candle_bullish_eng'] = '+8'
    if bearish_pin.iloc[-1] == True:
        candle_sell += 7
        details['candle_bearish_pin'] = '+7'
    if bearish_eng.iloc[-1] == True:
        candle_sell += 8
        details['candle_bearish_eng'] = '+8'
    buy_score += min(candle_buy, 12) # کاهش حداکثر از 15 به 12
    sell_score += min(candle_sell, 12)
    df['volume_ma'] = df['volume'].rolling(VOLUME_PERIOD).mean()
    current_volume = df['volume'].iloc[-1]
    volume_ma = df['volume_ma'].iloc[-1]
    if current_volume >= volume_ma * 1.8: # کاهش آستانه از 2.0 به 1.8
        buy_score += 18
        sell_score += 18
        details['volume'] = f'+18 (very strong volume: {(current_volume/volume_ma):.2f}x avg)'
    elif current_volume >= volume_ma * 1.3: # کاهش از 1.5
        buy_score += 12
        sell_score += 12
        details['volume'] = f'+12 (strong volume: {(current_volume/volume_ma):.2f}x avg)'
    elif current_volume >= volume_ma * 1.0: # کاهش از 1.2
        buy_score += 8
        sell_score += 8
        details['volume'] = f'+8 (good volume: {(current_volume/volume_ma):.2f}x avg)'
    elif current_volume >= volume_ma * 0.8: # جدید برای اجازه حجم متوسط
        buy_score += 4
        sell_score += 4
        details['volume'] = f'+4 (normal volume)'
    else:
        details['volume'] = f'0 (weak volume: {(current_volume/volume_ma):.2f}x avg)'
    if breakout_info.get('breakout') == True:
        if breakout_info.get('type') == 'up':
            buy_score += 18 # کاهش از 20
            details['breakout'] = f'+18 (bullish breakout: {breakout_info.get("reason")})'
        elif breakout_info.get('type') == 'down':
            sell_score += 18
            details['breakout'] = f'+18 (bearish breakout: {breakout_info.get("reason")})'
    else:
        details['breakout'] = '0 (no breakout detected)'
    swing_lows, swing_highs = swing_points(df, n=LOOKBACK_SWING)
    if len(swing_highs) > 0 and len(swing_lows) > 0:
        last_high = swing_highs['high'].iloc[-1]
        last_low = swing_lows['low'].iloc[-1]
        distance_to_high = ((last_high - current_price) / current_price) * 100
        distance_to_low = ((current_price - last_low) / current_price) * 100
        if distance_to_low > 1.5 and distance_to_high > 4: # نرم‌تر از 2/5
            buy_score += 8 # کاهش از 10
            details['swing_position'] = f'+8 (away from resistance, above support)'
        elif distance_to_low < 0.8: # نرم‌تر از 1
            buy_score += 6 # کاهش از 8
            details['swing_position'] = f'+6 (near support level)'
        if distance_to_high < 0.8:
            sell_score += 6
            details['swing_position'] = f'+6 (near resistance level)'
        elif distance_to_high > 1.5 and distance_to_low > 4:
            sell_score += 8
            details['swing_position'] = f'+8 (away from support, below resistance)'
    if fundamental_sentiment == "صعودی":
        fund_score = min(fund_strength * 2, 10)
        buy_score += fund_score
        details['fundamental'] = f'+{fund_score} (bullish sentiment)'
    elif fundamental_sentiment == "نزولی":
        fund_score = min(fund_strength * 2, 10)
        sell_score += fund_score
        details['fundamental'] = f'+{fund_score} (bearish sentiment)'
    else:
        details['fundamental'] = '0 (neutral sentiment)'
    sr_score_buy = 0
    sr_score_sell = 0
    if 'channels' in support_resistance_info:
        for channel in support_resistance_info['channels']:
            if channel['type'] == 'ascending_support':
                sr_score_buy += 4 # کاهش از 5
                details['channel_support'] = '+4 (ascending channel)'
            elif channel['type'] == 'descending_resistance':
                sr_score_sell += 4
                details['channel_resistance'] = '+4 (descending channel)'
    if 'horizontal_levels' in support_resistance_info:
        near_support = False
        near_resistance = False
        for level in support_resistance_info['horizontal_levels']:
            price_diff = abs(current_price - level['price']) / current_price * 100
            if price_diff < 1.2: # افزایش از 1 به 1.2 برای اجازه بیشتر
                if level['type'] == 'horizontal_support':
                    near_support = True
                elif level['type'] == 'horizontal_resistance':
                    near_resistance = True
        if near_support:
            sr_score_buy += 5 # کاهش از 6
            details['horizontal_support'] = '+5 (near horizontal support)'
        if near_resistance:
            sr_score_sell += 5
            details['horizontal_resistance'] = '+5 (near horizontal resistance)'
    if 'trend_levels' in support_resistance_info:
        for trend_level in support_resistance_info['trend_levels']:
            if trend_level['type'] == 'uptrend_line' and trend_level['slope'] > 0:
                sr_score_buy += 4 # کاهش از 5
                details['uptrend_line'] = '+4 (uptrend line support)'
            elif trend_level['type'] == 'downtrend_line' and trend_level['slope'] < 0:
                sr_score_sell += 4
                details['downtrend_line'] = '+4 (downtrend line resistance)'
    if 'prev_day' in support_resistance_info and support_resistance_info['prev_day'] is not None:
        prev_day = support_resistance_info['prev_day']
        if current_price > prev_day['prev_day_high']:
            sr_score_buy += 3 # کاهش از 4
            details['prev_day_breakout'] = '+3 (above previous day high)'
        elif current_price < prev_day['prev_day_low']:
            sr_score_sell += 3
            details['prev_day_breakdown'] = '+3 (below previous day low)'
        elif abs(current_price - prev_day['prev_day_low']) / current_price * 100 < 0.6: # افزایش از 0.5 به 0.6
            sr_score_buy += 2 # کاهش از 3
            details['prev_day_support'] = '+2 (near previous day low)'
        elif abs(current_price - prev_day['prev_day_high']) / current_price * 100 < 0.6:
            sr_score_sell += 2
            details['prev_day_resistance'] = '+2 (near previous day high)'
    if 'ema50' in df.columns:
        ema50 = df['ema50'].iloc[-1]
        if current_price > ema50:
            sr_score_buy += 4 # کاهش از 5
            details['ema50'] = f'+4 (price above EMA50: {ema50:.2f})'
        elif current_price < ema50:
            sr_score_sell += 4
            details['ema50'] = f'+4 (price below EMA50: {ema50:.2f})'
    if 'weekly_map' in support_resistance_info and support_resistance_info['weekly_map'] is not None:
        weekly = support_resistance_info['weekly_map']
        if current_price > weekly['current_week_high']:
            sr_score_buy += 4 # کاهش از 5
            details['weekly_breakout'] = '+4 (above current week high)'
        elif current_price < weekly['current_week_low']:
            sr_score_sell += 4
            details['weekly_breakdown'] = '+4 (below current week low)'
    buy_score += min(sr_score_buy, 25) # کاهش حداکثر از 30 به 25
    sell_score += min(sr_score_sell, 25)
    
    # 🆕🆕🆕 اضافه کردن امتیاز RSI
    rsi_info = detect_rsi_signals(df)
    rsi_buy = 0
    rsi_sell = 0
    if rsi_info['rsi_signal'] == "OVERSOLD":
        rsi_buy += 15  # سیگنال خرید قوی
        details['rsi'] = '+15 (Oversold RSI)'
    elif rsi_info['rsi_signal'] == "OVERBOUGHT":
        rsi_sell += 15
        details['rsi'] = '+15 (Overbought RSI)'
    
    if rsi_info['divergence'] == "BULLISH_DIVERGENCE":
        rsi_buy += 20
        details['rsi_divergence'] = '+20 (Bullish Divergence)'
    elif rsi_info['divergence'] == "BEARISH_DIVERGENCE":
        rsi_sell += 20
        details['rsi_divergence'] = '+20 (Bearish Divergence)'
    
    buy_score += rsi_buy
    sell_score += rsi_sell
    
    return buy_score, sell_score, details
# -----------------------------
def analyze_price_action(df, df_higher_tf=None):
    if df is None or len(df) < MIN_CANDLES_REQUIRED:
        return {
            'signal': 'WAIT',
            'buy_score': 0,
            'sell_score': 0,
            'entry': None,
            'stop_loss': None,
            'targets': {},
            'details': {},
            'structure': 'UNKNOWN',
            'price_structure_text': 'نامشخص',
            'patterns': {},
            'signal_key_bars': None,
            'bullish_breakout': None,
            'bearish_breakout': None,
            'bullish_reversal': None,
            'bearish_reversal': None,
            'volatility': 0,
            'win_rate': 50.0,
            'position_size': 0,
            'trailing_stop': None
        }
    df = df.copy()
    df['volume_ma'] = df['volume'].rolling(VOLUME_PERIOD).mean()
    df = calculate_ema(df)
    # 🆕 تشخیص Signal Bar و Key Bar
    signal_key_bars = detect_signal_and_key_bars(df, lookback=10)
    # 🆕 تشخیص Bullish و Bearish Breakout
    bullish_breakout = detect_bullish_breakout(df, lookback=50)
    bearish_breakout = detect_bearish_breakout(df, lookback=50)
    # 🆕 تشخیص Major Trend Reversal
    bullish_reversal = detect_bullish_trend_reversal(df, lookback=100)
    bearish_reversal = detect_bearish_trend_reversal(df, lookback=100)
    # 🆕 محاسبه نوسان (Volatility)
    volatility = calculate_volatility(df)
    # تشخیص الگوهای تکنیکال
    patterns = {}
    flag_pattern = detect_flag_pattern(df, lookback=30)
    if flag_pattern is not None:
        patterns['flag'] = flag_pattern
    wedge_pattern = detect_wedge_pattern(df, lookback=50)
    if wedge_pattern is not None:
        patterns['wedge'] = wedge_pattern
    rectangle_pattern = detect_rectangle_pattern(df, lookback=50)
    if rectangle_pattern is not None:
        patterns['rectangle'] = rectangle_pattern
    symmetrical_triangle = detect_symmetrical_triangle(df, lookback=50)
    if symmetrical_triangle is not None:
        patterns['symmetrical_triangle'] = symmetrical_triangle
    ascending_triangle = detect_ascending_triangle(df, lookback=50)
    if ascending_triangle is not None:
        patterns['ascending_triangle'] = ascending_triangle
    descending_triangle = detect_descending_triangle(df, lookback=50)
    if descending_triangle is not None:
        patterns['descending_triangle'] = descending_triangle
    channels = detect_channel_levels(df)
    horizontal_levels = detect_horizontal_levels(df)
    trend_levels = detect_trend_levels(df)
    prev_day = detect_previous_day_levels(df)
    weekly_map = get_weekly_map(df)
    support_resistance_info = {
        'channels': channels,
        'horizontal_levels': horizontal_levels,
        'trend_levels': trend_levels,
        'prev_day': prev_day,
        'weekly_map': weekly_map
    }
    structure, seq = determine_market_structure(df)
    trend = compute_trendline_from_structure(df, seq, structure)
    breakout_info = detect_breakout(df, seq, trend, structure)
    fundamental_sentiment = "خنثی"
    fund_strength = 0
    buy_score, sell_score, score_details = calculate_trading_score(
        df, structure, seq, trend, breakout_info,
        fundamental_sentiment, fund_strength, support_resistance_info, patterns, signal_key_bars,
        bullish_breakout, bearish_breakout, bullish_reversal, bearish_reversal
    )
    higher_tf_multiplier = 1.0
    if df_higher_tf is not None:
        higher_structure, _ = determine_market_structure(df_higher_tf)
        if structure == higher_structure and structure != "RANGE":
            higher_tf_multiplier = 1.2 # کاهش از 1.3 برای تعادل
            score_details['higher_tf_alignment'] = f'x1.2 (aligned with higher TF: {higher_structure})'
        elif structure != higher_structure:
            higher_tf_multiplier = 0.8 # افزایش از 0.7 به 0.8 برای کمتر سخت‌گیری
            score_details['higher_tf_alignment'] = f'x0.8 (conflict with higher TF: {higher_structure})'
    buy_score = int(buy_score * higher_tf_multiplier)
    sell_score = int(sell_score * higher_tf_multiplier)
  
    # 🆕 تغییر منطق سیگنال‌دهی: مقایسه مستقیم امتیازها
    if buy_score > sell_score:
        signal = "BUY"
    elif sell_score > buy_score:
        signal = "SELL"
    else:
        signal = "WAIT"
  
    entry = df['close'].iloc[-1]
    stop_loss = None
    targets = {}
    # 🆕 محاسبه وین ریت
    win_rate = calculate_win_rate("", signal) if signal != "WAIT" else 50.0
    # 🆕 محاسبه حجم معامله (فرض می‌کنیم حساب 1000 دلاری است)
    account_balance = 1000.0
    if signal == "BUY":
        position_size = calculate_position_size(entry, entry, account_balance) # placeholder stop_loss
        trailing_stop = calculate_trailing_stop(df, entry, entry, entry, True) # placeholder stop_loss
    elif signal == "SELL":
        position_size = calculate_position_size(entry, entry, account_balance) # placeholder stop_loss
        trailing_stop = calculate_trailing_stop(df, entry, entry, entry, False) # placeholder stop_loss
    else:
        position_size = 0
        trailing_stop = None
    price_structure = f"Trend: {structure}"
    if seq:
        last_swings_str = " | last_swings: " + ", ".join([f"{('H' if s[1]=='H' else 'L')}{s[2]:.5g}" for s in seq[-6:]])
        price_structure += last_swings_str
    if trend and trend.get('type') is not None:
        pts = trend.get('points', [])
        price_structure += f" | trendline: {trend.get('type')}"
    if breakout_info.get('breakout') == True:
        price_structure += f" | BREAKOUT: {breakout_info.get('type')}"
    if patterns is not None and len(patterns) > 0:
        pattern_names = []
        if 'flag' in patterns:
            pattern_names.append(patterns['flag']['type'])
        if 'wedge' in patterns:
            pattern_names.append(patterns['wedge']['type'])
        if 'rectangle' in patterns:
            pattern_names.append(f"rectangle_{patterns['rectangle']['direction']}")
        if 'symmetrical_triangle' in patterns:
            pattern_names.append(f"symmetrical_triangle_{patterns['symmetrical_triangle']['direction']}")
        if 'ascending_triangle' in patterns:
            pattern_names.append('ascending_triangle_bullish')
        if 'descending_triangle' in patterns:
            pattern_names.append('descending_triangle_bearish')
        if pattern_names:
            price_structure += f" | PATTERNS: {', '.join(pattern_names)}"
    # 🆕 اضافه کردن Breakout و Reversal به ساختار قیمت
    if bullish_breakout is not None:
        price_structure += f" | BULLISH_BREAKOUT (confidence: {bullish_breakout['confidence']}%)"
    if bearish_breakout is not None:
        price_structure += f" | BEARISH_BREAKOUT (confidence: {bearish_breakout['confidence']}%)"
    if bullish_reversal is not None:
        price_structure += f" | BULLISH_REVERSAL (confidence: {bullish_reversal['confidence']}%)"
    if bearish_reversal is not None:
        price_structure += f" | BEARISH_REVERSAL (confidence: {bearish_reversal['confidence']}%)"
    # اضافه کردن اطلاعات Signal Bar و Key Bar
    if signal_key_bars is not None:
        if signal_key_bars.get('signal_bar') is not None and signal_key_bars.get('key_bar') is not None:
            price_structure += f" | SIGNAL+KEY: {signal_key_bars['signal_bar']['type']} confirmed"
        elif signal_key_bars.get('signal_bar') is not None:
            price_structure += f" | SIGNAL: {signal_key_bars['signal_bar']['type']} pending"
    result = {
        'signal': signal,
        'buy_score': buy_score,
        'sell_score': sell_score,
        'entry': entry,
        'stop_loss': stop_loss,
        'targets': targets,
        'details': score_details,
        'structure': structure,
        'price_structure_text': price_structure,
        'patterns': patterns,
        'signal_key_bars': signal_key_bars,
        'bullish_breakout': bullish_breakout,
        'bearish_breakout': bearish_breakout,
        'bullish_reversal': bullish_reversal,
        'bearish_reversal': bearish_reversal,
        'volatility': volatility,
        'win_rate': win_rate,
        'position_size': position_size,
        'trailing_stop': trailing_stop
    }
    # 🆕 اعمال Decision Engine برای تصمیم‌گیری نهایی
    decision = decision_engine(result)
    result['final_decision'] = decision['action']
    result['decision_confidence'] = decision['confidence']
    result['decision_reason'] = decision['reason']
    result['risk_level'] = decision['risk_level']
    return result
# -----------------------------
# 🆕🆕🆕 تابع تحلیل کامل برای تمام تایم‌فریم‌ها
def analyze_all_timeframes(symbol):
    """
    تحلیل کامل برای تمام تایم‌فریم‌ها و نمایش نتایج
    """
    # ایجاد دیکشنری برای ذخیره نتایج تحلیل هر تایم‌فریم
    timeframe_results = {}
  
    # لیست تایم‌فریم‌ها برای تحلیل
    timeframes = [
        (TIMEFRAME_TREND_4H, "4H", 100),
        (TIMEFRAME_TREND_1H, "1H", 150),
        (TIMEFRAME_ANALYSIS, "30M", 200),
        (TIMEFRAME_SIGNAL, "15M", 200)
    ]
  
    # تحلیل هر تایم‌فریم
    for tf_code, tf_name, limit in timeframes:
        df = fetch_data(symbol, tf_code, limit)
        if df is None or len(df) < MIN_CANDLES_REQUIRED:
            timeframe_results[tf_name] = {
                'structure': 'UNKNOWN',
                'signal': 'WAIT',
                'buy_score': 0,
                'sell_score': 0,
                'volatility': 0,
                'patterns': {},
                'bullish_breakout': None,
                'bearish_breakout': None,
                'bullish_reversal': None,
                'bearish_reversal': None,
                'price_structure_text': 'داده کافی در دسترس نیست'
            }
            continue
      
        # محاسبه شاخص‌های پایه
        df = calculate_ema(df)
        structure, _ = determine_market_structure(df)
        volatility = calculate_volatility(df)
      
        # تشخیص الگوها و سیگنال‌ها
        patterns = {}
        flag_pattern = detect_flag_pattern(df, lookback=30)
        if flag_pattern is not None:
            patterns['flag'] = flag_pattern
        wedge_pattern = detect_wedge_pattern(df, lookback=50)
        if wedge_pattern is not None:
            patterns['wedge'] = wedge_pattern
        rectangle_pattern = detect_rectangle_pattern(df, lookback=50)
        if rectangle_pattern is not None:
            patterns['rectangle'] = rectangle_pattern
        symmetrical_triangle = detect_symmetrical_triangle(df, lookback=50)
        if symmetrical_triangle is not None:
            patterns['symmetrical_triangle'] = symmetrical_triangle
        ascending_triangle = detect_ascending_triangle(df, lookback=50)
        if ascending_triangle is not None:
            patterns['ascending_triangle'] = ascending_triangle
        descending_triangle = detect_descending_triangle(df, lookback=50)
        if descending_triangle is not None:
            patterns['descending_triangle'] = descending_triangle
      
        # تشخیص Breakout و Reversal
        bullish_breakout = detect_bullish_breakout(df, lookback=50)
        bearish_breakout = detect_bearish_breakout(df, lookback=50)
        bullish_reversal = detect_bullish_trend_reversal(df, lookback=100)
        bearish_reversal = detect_bearish_trend_reversal(df, lookback=100)
      
        # تحلیل سیگنال برای این تایم‌فریم
        result = analyze_price_action(df)
      
        # ذخیره نتایج
        timeframe_results[tf_name] = {
            'structure': structure,
            'signal': result['signal'],
            'buy_score': result['buy_score'],
            'sell_score': result['sell_score'],
            'volatility': volatility,
            'patterns': patterns,
            'bullish_breakout': bullish_breakout,
            'bearish_breakout': bearish_breakout,
            'bullish_reversal': bullish_reversal,
            'bearish_reversal': bearish_reversal,
            'price_structure_text': result['price_structure_text']
        }
  
    return timeframe_results
# -----------------------------
def main():
    print("سیستم تحلیل چند تایم‌فریمی (Multi-Timeframe Analysis)")
    print("="*100)
    print(f"تایم‌فریم‌های تحلیل:")
    print(f" • 4H: تشخیص روند بلندمدت")
    print(f" • 1H: تشخیص روند میان‌مدت")
    print(f" • 30M: تحلیل دقیق پرایس اکشن")
    print(f" • 15M: صدور سیگنال نهایی")
    print(f"\nمنطق سیگنال‌دهی جدید:")
    print(f" • اگر buy_score > sell_score → سیگنال BUY")
    print(f" • اگر sell_score > buy_score → سیگنال SELL")
    print(f" • اگر buy_score == sell_score → سیگنال WAIT")
    print(f"استاپ و تارگت بر اساس پرایس اکشن حرفه‌ای")
    print(f" • Stop Loss: زیر/بالای آخرین سوئینگ + بافر 0.1%")
    print(f" • Targets: بر اساس R:R (1:1, 1:2, 1:3)")
    print(f"الگوهای تکنیکال: Flag, Wedge, Rectangle, Triangles")
    print(f"تحلیل Signal Bar & Key Bar برای نقاط ورود بهتر")
    print(f"Bullish/Bearish Breakout Detection")
    print(f"Major Trend Reversal Analysis (Bullish & Bearish)")
    print(f"محاسبه نوسان (Volatility) برای انتخاب سیگنال‌های با سوددهی بالاتر")
    print(f"محاسبه وین ریت قبل از معامله")
    print(f"مانیجمنت کامل (حجم معامله، تریلینگ استاپ, مدیریت ریسک)")
    print(f"Decision Engine برای تصمیم‌گیری نهایی")
    print(f"استفاده از EMA50 به جای EMA20 برای سیگنال‌های قابل اعتمادتر")
    print(f"فیلتر رژیم بازار برای جلوگیری از سیگنال‌های متناقض")
    print(f"فیلتر ریسک بالا (حداکثر 8%) برای جلوگیری از سیگنال‌های پرریسک")
    print(f"اضافه شدن RSI حرفه‌ای با تشخیص واگرایی")
    print(f"ابزار فیبوناچی برای تنظیم بهتر استاپ و تارگت")
    print(f"محاسبه R:R داینامیک از 1 تا 10 بر اساس بازار و فیبو")
    print(f"\n{'='*100}")

    # تعیین رژیم کلی بازار قبل از تحلیل نمادها
    market_regime, market_strength = get_market_regime("BTC/USDT")
    print(f"\nرژیم کلی بازار (بر اساس BTC/USDT): {market_regime} (قدرت: {market_strength:.2f}%)")
    if market_regime == "STRONG_BULL":
        print("فیلتر فعال: تمام سیگنال‌های SELL روی آلت‌کوین‌ها نادیده گرفته می‌شوند.")
    elif market_regime == "STRONG_BEAR":
        print("فیلتر فعال: تمام سیگنال‌های BUY روی آلت‌کوین‌ها نادیده گرفته می‌شوند.")
    print("="*100)

    for symbol in SYMBOLS:
        all_tf_results = analyze_all_timeframes(symbol)
        result_15m = all_tf_results.get('15M', {})
        df_15m = fetch_data(symbol, TIMEFRAME_SIGNAL, limit=200)
        if df_15m is None or len(df_15m) < MIN_CANDLES_REQUIRED:
            continue

        fundamental, fund_strength = analyze_fundamental(symbol)
        df_30m = fetch_data(symbol, TIMEFRAME_ANALYSIS, limit=200)
        result = analyze_price_action(df_15m, df_30m)

        # فیلتر نوسان
        if result['signal'] in ["BUY", "SELL"] and result['volatility'] < MIN_VOLATILITY_THRESHOLD:
            result['signal'] = "WAIT"
            result['details']['volatility_filter'] = f"0 (نوسان کم: {result['volatility']*100:.2f}% < {MIN_VOLATILITY_THRESHOLD*100:.1f}%)"
        else:
            result['details']['volatility_filter'] = f"+8 (نوسان مناسب: {result['volatility']*100:.2f}%)"
            if result['signal'] == "BUY":
                result['buy_score'] += 8
            elif result['signal'] == "SELL":
                result['sell_score'] += 8

        # فاندامنتال
        if fundamental == "صعودی":
            fund_score = min(fund_strength * 2, 10)
            result['buy_score'] += fund_score
            result['details']['fundamental'] = f'+{fund_score} (bullish sentiment)'
        elif fundamental == "نزولی":
            fund_score = min(fund_strength * 2, 10)
            result['sell_score'] += fund_score
            result['details']['fundamental'] = f'+{fund_score} (bearish sentiment)'

        # همسویی چند تایم‌فریمی
        mtf_alignment_score = 0
        mtf_status = []
        if all_tf_results['4H']['structure'] == all_tf_results['1H']['structure'] == all_tf_results['30M']['structure'] == result['structure'] and result['structure'] != "RANGE":
            mtf_alignment_score = 25
            mtf_status.append("همسویی کامل 4H-1H-30M-15M")
        elif all_tf_results['4H']['structure'] == all_tf_results['1H']['structure'] == all_tf_results['30M']['structure'] and result['structure'] != "RANGE":
            mtf_alignment_score = 20
            mtf_status.append("همسویی 4H-1H-30M")
        elif all_tf_results['4H']['structure'] == all_tf_results['1H']['structure'] and result['structure'] != "RANGE":
            mtf_alignment_score = 15
            mtf_status.append("همسویی 4H-1H")
        elif all_tf_results['4H']['structure'] == result['structure'] and result['structure'] != "RANGE":
            mtf_alignment_score = 12
            mtf_status.append("همسویی 4H-15M")
        elif all_tf_results['1H']['structure'] == result['structure'] and result['structure'] != "RANGE":
            mtf_alignment_score = 8
            mtf_status.append("همسویی 1H-15M")
        else:
            mtf_status.append("عدم همسویی تایم‌فریم‌ها")

        if result['signal'] == "BUY":
            result['buy_score'] += mtf_alignment_score
        elif result['signal'] == "SELL":
            result['sell_score'] += mtf_alignment_score
        result['details']['mtf_alignment'] = f'+{mtf_alignment_score} ({" | ".join(mtf_status)})'

        # تصمیم‌گیری مجدد بر اساس امتیاز نهایی
        if result['buy_score'] > result['sell_score']:
            result['signal'] = "BUY"
        elif result['sell_score'] > result['buy_score']:
            result['signal'] = "SELL"
        else:
            result['signal'] = "WAIT"

        # محاسبه استاپ و تارگت فقط برای سیگنال‌های معتبر
        if result['signal'] in ["BUY", "SELL"]:
            stop_loss, targets = calculate_price_action_targets(result['entry'], result['signal'], df_15m, result['structure'])
            if stop_loss is None or targets is None or 'tp1' not in targets:
                result['signal'] = "WAIT"
                continue

            entry = result['entry']
            risk_raw = abs(entry - stop_loss)
            risk_pct = risk_raw / entry

            # فیلتر ریسک بالا
            if risk_pct > MAX_ACCEPTABLE_RISK_PCT:
                continue

            # فیلتر R:R tp1 < 1
            reward1 = targets['tp1'] - entry if result['signal'] == "BUY" else entry - targets['tp1']
            rr_tp1 = reward1 / risk_raw if risk_raw > 0 else 0
            if rr_tp1 < 1.0:
                continue

            # فیلتر tp3 < 2%
            if 'tp3' in targets:
                profit3 = (targets['tp3'] - entry) / entry * 100 if result['signal'] == "BUY" else (entry - targets['tp3']) / entry * 100
                if profit3 < MIN_PROFIT_MARGIN_PCT:
                    continue

            result['stop_loss'] = stop_loss
            result['targets'] = targets
            result['win_rate'] = calculate_win_rate(symbol, result['signal'])
            result['position_size'] = calculate_position_size(entry, stop_loss, 1000.0, volatility=result['volatility'], win_rate=result['win_rate'])

        decision = decision_engine(result)
        result['final_decision'] = decision['action']
        result['decision_confidence'] = decision['confidence']
        result['decision_reason'] = decision['reason']
        result['risk_level'] = decision['risk_level']

        # فیلتر نهایی: نوسان کم یا وین ریت پایین
        if result['final_decision'] in ["BUY", "SELL"]:
            if result['volatility'] < MIN_VOLATILITY_THRESHOLD or result['win_rate'] < 45:
                result['final_decision'] = "WAIT"

        # فقط سیگنال‌های طلایی چاپ بشن
        if result['final_decision'] in ["BUY", "SELL"]:
            print(f"\n{'LONG' if result['final_decision']=='BUY' else 'SHORT'} جفت‌ارز: {symbol}")
            print(f"{'='*100}")
            print(f"قیمت ورود: {result['entry']:.6f}")
            print(f"استاپ: {result['stop_loss']:.6f} (-{risk_pct*100:.2f}%)")
            for i in range(1, 4):
                k = f'tp{i}'
                if k in targets:
                    rr = abs(targets[k] - entry) / risk_raw
                    print(f"   TP{i}: {targets[k]:.6f} → 1:{rr:.2f}")
            print(f"وین ریت: {result['win_rate']:.1f}% | اعتماد: {result['decision_confidence']:.0f}%")
            print(f"رژیم بازار: {market_regime}")
            print("-" * 120)

if __name__ == "__main__":
    main()