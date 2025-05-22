# Telegram Auto-Reply Bot

- Автоответ новым пользователям в ЛС
- .текст [текст] — изменить автоответ
- .блок вкл/выкл — включить/выключить блокировку после автоответа
- Все настройки и блокировки сохраняются
- При первом запуске инструкция в ЛС
- Необходим Python 3.7+

## Запуск:

1. Введите `api_id` и `api_hash` в файле `settings.py` с [https://my.telegram.org](https://my.telegram.org)
2. Запустите `main.py`

## Установка и запуск через Termux (Android):

```sh
pkg update
pkg install python git -y
pip install --upgrade pip
git clone https://github.com/lxdSvetozar/Telegram-Auto-Reply-Bot.git
cd Telegram-Auto-Reply-Bot
pip install -r requirements.txt
# Введите свои api_id и api_hash в settings.py
python main.py
```

## Установка и запуск на Linux:

```sh
sudo apt update
sudo apt install python3 python3-pip git -y
git clone https://github.com/lxdSvetozar/Telegram-Auto-Reply-Bot.git
cd Telegram-Auto-Reply-Bot
pip3 install -r requirements.txt
# Введите свои api_id и api_hash в settings.py
python3 main.py
```

## Установка и запуск на Windows:

1. Установите [Python 3.7+](https://www.python.org/downloads/) и [Git](https://git-scm.com/download/win).
2. Откройте командную строку (Win+R → cmd).
3. Выполните команды:
    ```sh
    git clone https://github.com/lxdSvetozar/Telegram-Auto-Reply-Bot.git
    cd Telegram-Auto-Reply-Bot
    pip install -r requirements.txt
    ```
4. Введите свои api_id и api_hash в settings.py.
5. Запустите:
    ```sh
    python main.py
    ```

## Команды:

- `.текст [текст]`
- `.блок вкл`
- `.блок выкл`
- `.блок`

## Получение api_id и api_hash:

1. Перейдите на [https://my.telegram.org/auth](https://my.telegram.org/auth)
2. Войдите через свой Telegram-аккаунт.
3. Перейдите в раздел **API development tools**.
4. Создайте приложение и скопируйте `api_id` и `api_hash`.

