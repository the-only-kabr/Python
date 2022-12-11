from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
from controller import *
import import_data as control_import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name} !')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y} ')

async def add_information(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    await update.message.reply_text(f'Данные введены ')
    items = msg.split()
    li = []
    for i in range(1,len(items)):
        li.append(items[i])
    import_data(li)
    await update.message.reply_text(f'Информация добавлена в справочник')

async def give_information(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    await update.message.reply_text(f'Подождите проводится поиск ')
    items = msg.split()
    x = items[1]
    data = export_data()
    i = search_data(x, data)
    if i != None:
        await update.message.reply_text(f'{i[1]} {i[2]} {i[3]} {i[4]}')
    else:
        await update.message.reply_text("Данные не обнаружены")


# greeting()

# choice_todo()