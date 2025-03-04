import random
import telebot

API_TOKEN = "your token"
bot = telebot.TeleBot(API_TOKEN)

participants = {}
santa_pairs = {}

def register_participant(user_id, text):
    if not text:
        return None, "Будь ласка, введіть ім'я та побажання через кому після /register."
    name, *wishlist = text.split(",")
    participants[user_id] = {"name": name.strip(), "wishlist": [item.strip() for item in wishlist]}
    return name, None

def generate_santa_pairs():
    global santa_pairs
    if len(participants) < 2:
        return "Має бути хоча б 2 учасники!"
    user_ids = list(participants.keys())
    random.shuffle(user_ids)
    santa_pairs = {user_ids[i]: user_ids[(i + 1) % len(user_ids)] for i in range(len(user_ids))}
    return None

def notify_participants():
    for giver_id, receiver_id in santa_pairs.items():
        receiver = participants[receiver_id]
        text = f"Ви Таємний Санта для {receiver['name']}! 🎁 Побажання: {', '.join(receiver['wishlist'])}"
        bot.send_message(giver_id, text)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привіт! Я бот для Таємного Санти 🎅. Напиши /register ім'я, побажання через кому, щоб зареєструватися. Коли всі готові, напишіть /play.")

@bot.message_handler(commands=['register'])
def register(message):
    user_id = message.from_user.id
    text = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else ""
    name, error = register_participant(user_id, text)
    if error:
        bot.reply_to(message, error)
    else:
        bot.reply_to(message, f"{name} зареєстрований! 🎁")

@bot.message_handler(commands=['play'])
def play(message):
    error = generate_santa_pairs()
    if error:
        bot.reply_to(message, error)
    else:
        notify_participants()
        bot.reply_to(message, "Розподіл завершено! Учасники отримали свої повідомлення.")

bot.polling()
