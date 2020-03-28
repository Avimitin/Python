# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/3/27 18:04
import telebot
import config
from telebot import types
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "爬")

@bot.message_handler(regexp="卡了")
def send_areply(message):
	bot.send_message(message.chat.id,'我不卡啊')

@bot.message_handler(regexp='饿了')
def send_areply(message):
	bot.reply_to(message,'快去吃！')

@bot.message_handler(regexp='渴了')
def send_areply(message):
	bot.reply_to(message,'一起去喝奶茶！')

@bot.message_handler(regexp='炸了')
def send_areply(message):
	bot.reply_to(message,'请报故障节点和本地宽带')

@bot.message_handler(regexp='早上好')
def send_areply(message):
	bot.reply_to(message, 'Ohayo~')

@bot.message_handler(regexp='中午好')
def send_areply(message):
	bot.reply_to(message,'午安(*￣3￣)╭')

@bot.message_handler(regexp='下午好')
def send_areply(message):
	bot.reply_to(message,'一起喝下午茶吧，你喜欢什么奶茶店呀')

@bot.message_handler(regexp='晚上好')
def send_areply(message):
	bot.reply_to(message,'晚上好呀~')

@bot.message_handler(regexp='晚安')
def send_areply(message):
	bot.reply_to(message,'好梦哟~安记梦我')

@bot.message_handler(regexp='#ssr')
def send_areply(message):
	bot.reply_to(message,'请跟随该教程来使用ssr：https://docs.nameless13.com/winssr')

@bot.message_handler(regexp='#小火箭')
def send_areply(message):
	bot.reply_to(message,'请跟随该教程来使用shadowrocket：https://docs.nameless13.com/ios')

@bot.message_handler(regexp='#clashr订阅')
def send_areply(message):
	bot.reply_to(message,'请使用这个链接转换clashr：https://acl4ssr.netlify.com/')

@bot.message_handler(regexp='笨蛋老婆')
def send_areply(message):
	bot.reply_to(message,'我才不是笨蛋！哼╭(╯^╰)╮')

@bot.message_handler(regexp='老婆真棒')
def send_areply(message):
	bot.reply_to(message,'那肯定！我是最棒的老婆(○｀ 3′○)')

@bot.message_handler(regexp='大佬')
def send_areply(message):
	bot.reply_to(message,'大佬也太强了Orz')

@bot.message_handler(regexp='我爱你')
def send_areply(message):
	bot.reply_to(message,'嘻嘻，其实我也是有点喜欢你的，就一点点哦(*/ω＼*)')

@bot.message_handler(regexp='有钱')
def send_areply(message):
	bot.reply_to(message,'快包养老婆！(づ￣ 3￣)づ')

@bot.message_handler(regexp='没钱')
def send_areply(message):
	bot.send_message(message.chat.id,'钱钱木大了QAQ')

@bot.message_handler(regexp='草')
def send_areply(message):
	bot.send_message(message.chat.id,'太草了')

@bot.message_handler(regexp='咕')
def send_areply(message):
	bot.send_message(message.chat.id,'咕咕咕，快做完了，进度0%')

@bot.message_handler(regexp='老板垃圾')
def send_areply(message):
	bot.send_message(message.chat.id,'老板垃圾ψ(｀∇´)ψ')

@bot.message_handler(regexp='牛逼')
def send_areply(message):
	bot.send_message(message.chat.id,'牛逼！')

@bot.message_handler(regexp='你老公是谁')
def send_areply(message):
	bot.reply_to(message,'我老公是Avimitin')

@bot.message_handler(regexp='选A还是选B')
def send_areply(message):
	markup = types.ReplyKeyboardMarkup()
	itembtna = types.KeyboardButton('A')
	itembtnv = types.KeyboardButton('B')
	markup.row(itembtna, itembtnv)
	bot.send_message(message.chat.id,"选择一个选项:", reply_markup=markup)

bot.polling()
