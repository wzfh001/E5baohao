from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 替换为你的Telegram Bot API令牌
TOKEN = "your_bot_token"

# 定义/start命令处理函数
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("你好！欢迎使用我的Telegram Bot！")

# 设置Updater和CommandHandler
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# 注册/start命令处理函数
start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

# 启动Bot
updater.start_polling()

# 让Bot一直运行，直到手动停止
updater.idle()
