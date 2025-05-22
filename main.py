import sqlite3
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from settings import api_id, api_hash

session_name = "userbot"

conn = sqlite3.connect("blocked_users.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS blacklist (
        user_id INTEGER PRIMARY KEY
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY CHECK (id = 1),
        auto_reply TEXT DEFAULT 'Здравствуйте! Владелец аккаунта сейчас не может ответить.',
        block_enabled INTEGER DEFAULT 0
    )
''')
cursor.execute("INSERT OR IGNORE INTO settings (id) VALUES (1)")
conn.commit()

def get_settings():
    cursor.execute("SELECT auto_reply, block_enabled FROM settings WHERE id = 1")
    row = cursor.fetchone()
    return row[0], bool(row[1])

def set_auto_reply(text):
    cursor.execute("UPDATE settings SET auto_reply = ? WHERE id = 1", (text,))
    conn.commit()

def set_block_enabled(enabled: bool):
    cursor.execute("UPDATE settings SET block_enabled = ? WHERE id = 1", (1 if enabled else 0,))
    conn.commit()

app = Client(session_name, api_id=api_id, api_hash=api_hash)

@app.on_message(filters.private & ~filters.me)
async def handler(client: Client, message: Message):
    user_id = message.from_user.id
    auto_reply, block_enabled = get_settings()
    cursor.execute("SELECT 1 FROM blacklist WHERE user_id = ?", (user_id,))
    if not cursor.fetchone():
        await message.reply_text(auto_reply)
        cursor.execute("INSERT INTO blacklist (user_id) VALUES (?)", (user_id,))
        conn.commit()
        if block_enabled:
            await client.block_user(user_id)

@app.on_message(filters.me & filters.command("текст", prefixes="."))
async def set_text_handler(client: Client, message: Message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        await message.reply("Укажите текст: .текст [текст]")
        return
    set_auto_reply(text[1])
    await message.reply("Текст автоответа обновлён.")

@app.on_message(filters.me & filters.command("блок", prefixes="."))
async def block_handler(client: Client, message: Message):
    args = message.text.split()
    if len(args) == 1:
        _, block_enabled = get_settings()
        await message.reply(f"Блокировка: {'ВКЛ' if block_enabled else 'ВЫКЛ'}")
    elif args[1].lower() == "вкл":
        set_block_enabled(True)
        await message.reply("Блокировка: ВКЛ")
    elif args[1].lower() == "выкл":
        set_block_enabled(False)
        await message.reply("Блокировка: ВЫКЛ")
    else:
        await message.reply("Используйте: .блок вкл / .блок выкл / .блок")

if __name__ == "__main__":
    print("Бот запущен.")
    try:
        app.run()
    finally:
        conn.close()