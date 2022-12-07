# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:58:36 2022

@author: Poorya_Fekri
"""

#Importing liberaries======================>

import logging
from telegram import Update
from telegram.ext import  ApplicationBuilder,ContextTypes, CommandHandler

# Creating logging=========================>


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    )

# Creating Functions=======================>

async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Salam man Poorya hastam'
                     )
# Creating Aplication ====================>

if __name__ == '__main__':
    application=ApplicationBuilder().token('5379957830:AAHGOV-O9hfwISkZs2gDTxLMx9E-fZMTtWc').build()

 # Creatin Handler=======================>

    bot_handler=CommandHandler('start', start)
    application.add_handler(bot_handler)             
    application.run_polling()