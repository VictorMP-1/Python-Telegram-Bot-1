
from telegram.ext import *
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices
from datetime import datetime
import Constants as keys
import Responses as R
from telegram.ext import Updater
from telegram.ext import CommandHandler

print("Bot Iniciando...")


def start_command(update, context):
    update.message.reply_text('Digite algo para começar.')


def help_command(update, context):
    update.message.reply_text('Se você precisar de ajuda contate o administrador do grupo.')  

def tempo_command(update, context):
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")
    update.message.reply_text(date_time)      


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def crypto_command(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Moeda: {coin}\nPreço: R${price:,.2f}\nVariação na última hora: {change_hour:.3f}%\nVariação no último dia: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("tempo", tempo_command))
    dp.add_handler(CommandHandler("crypto", crypto_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

    

main()







