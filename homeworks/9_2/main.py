from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import *


app = ApplicationBuilder().token("Токен").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("add", add_information))
app.add_handler(CommandHandler("find", give_information))


print('server start')
app.run_polling()

# from controller import *

# greeting()

# choice_todo()
