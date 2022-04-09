# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

import os

# .env fayl ichidan quydagilarni o'qiymiz
ADMINS = list(os.environ.get("ADMINS"))  # ADMINLAR RO'YXATI
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # bOT TOKEN

# IP = str(os.environ.get("ip"))  # hosting ip manzili
# PROVIDER_TOKEN = str(os.environ.get("PROVIDER-TOKEN"))
