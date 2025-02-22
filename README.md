## Запуск бота 
### инструкция:

```
git clone https://github.com/LuckyMen000/tgbot-itstep
cd tgbot-itstep
```

```
pip install - r requirements.txt
python bot.py
```

### Инлайн клавиатуры - наши кнопки в боте

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на сайт", url="https://mystat.itstep.org/")],
        [InlineKeyboardButton(text="Нажми", callback_data="button_click")]
    ]
)