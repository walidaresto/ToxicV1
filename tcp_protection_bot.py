from telegram.ext import Updater, CommandHandler
from scapy.all import *

# تعريف الأمر /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Toxic V1 Bot! I will start monitoring TCP traffic.")

# تعريف الأمر /help
def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm here to protect your TCP traffic. Just send me a message and I'll start monitoring.")

def main():

    # تعريف الأمر /start وربطه بالوظيفة المناسبة
   updater = Updater("AAH_krphyyODef6ZOmhUR0gaKGBd9EqgAI8", use_context=True)

    # تعريف الأمر /help وربطه بالوظيفة المناسبة
   updater.dispatcher.add_handler(CommandHandler('help', help))

    # بدء الاستماع على التحديثات الواردة من تليجرام
   updater.start_polling()

    # الاستمرار في العمل حتى يتم الضغط على Ctrl-C
   updater.idle()

if __name__ == '__main__':
    main()

# تعريف وظيفة لمراقبة حركة البيانات عبر TCP
def analyze_packet(packet):
    if TCP in packet:
        # يمكنك هنا إضافة تحليل ومعالجة الرسائل الضارة أو الكثيرة
        print("Received TCP packet:", packet.summary())

# بدء مراقبة حركة البيانات عبر TCP
sniff(filter="tcp", prn=analyze_packet, store=0)
