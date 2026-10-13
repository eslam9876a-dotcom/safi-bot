
import telebot

TOKEN = "8622623540:AAEE6jY4zGwaUdEX1S4u10vzAhfPnsQ57qg"
bot = telebot.TeleBot(TOKEN)

def safi_reply(text):
    text = text.lower()
    if "سلام" in text or "هلا" in text:
        return "هلا والله! انا صافي معاك 😊"
    if "عامل ايه" in text:
        return "زي الفل الحمد لله، انت عامل ايه يا غالي؟"
    if "بحبك" in text:
        return "وانا كمان بحبك اوي ❤️"
    return "سمعتك! قول كمان يا غالي"

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    reply = safi_reply(message.text)
    bot.reply_to(message, reply)

print("بوت صافي شغال على تليجرام...")
bot.infinity_polling()
