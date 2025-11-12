from telebot import types

def Menu() -> types.ReplyKeyboardMarkup:
	"""Строит Reply-интерфейс: меню бота."""

	Menu = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
	Menu.add(types.KeyboardButton("💩 " + "Переключить режим"))
	Menu.add(types.KeyboardButton("🤪 " + "Поделиться с друзьям"))

	return Menu