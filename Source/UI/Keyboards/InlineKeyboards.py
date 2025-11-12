from dublib.TelebotUtils.Users import UserData

from telebot import types

def Delete(label: str) -> types.InlineKeyboardMarkup:
	"""
	Строит Inline-интерфейс: удаление сообщения.
	
	:param label: Подпись кнопки.
	:type label: str
	"""

	Menu = types.InlineKeyboardMarkup()
	Menu.add(types.InlineKeyboardButton(text = label, callback_data = "delete"))

	return Menu

def Share(bot_name: str) -> types.InlineKeyboardMarkup:
	"""
	Строит Inline-интерфейс: поделиться.
	
	:param bot_name: Имя бота.
	:type bot_name: str
	"""

	ShareText = (
		"\n" + "\n".join((bot_name,) * 2) + "\n",
		"**" + "Переводчик с зумерского | Пикми, чечик, найк про" + "**",
		"Как раз то, что ты искал!" + "\n",
		"__" + "Пользуйся и делись с друзьями!" + "__"
	)

	Menu = types.InlineKeyboardMarkup(row_width = 1)
	Menu.add(types.InlineKeyboardButton(text = "Поделиться!", switch_inline_query = "\n".join(ShareText)))
	Menu.add(types.InlineKeyboardButton(text = "Назад", callback_data = "delete"))

	return Menu

def Subscribe(subscriptions: dict[str, dict]) -> types.InlineKeyboardMarkup:
	"""
	Строит Inline-интерфейс: кнопки подписки.
	
	:param subscriptions: Словарь с данными необходимых подписок, где ключ – название кнопки, а в словаре-значении имеется два поля: _id_ и _link_.
	:type subscriptions: dict[str, dict]
	"""

	Menu = types.InlineKeyboardMarkup(row_width = 1)
	for Name in subscriptions.keys(): Menu.add(types.InlineKeyboardButton(text = Name, url = subscriptions[Name]["link"]))
	Menu.add(types.InlineKeyboardButton(text = "Я подписался!", callback_data = "after_subscribe"))

	return Menu

def Switcher(user: UserData) -> types.InlineKeyboardMarkup:
	"""
	Строит Inline-интерфейс: кнопки подписки.
	
	:param user: Данные пользователя.
	:type user: UserData
	"""

	Statuses = ("✅ ", "") if user.get_property("mode") == "from" else ("", "✅ ")

	Menu = types.InlineKeyboardMarkup(row_width = 1)
	Menu.add(types.InlineKeyboardButton(text = Statuses[0] + "С зумерского на нормальный", callback_data = "switch_mode_from"))
	Menu.add(types.InlineKeyboardButton(text = Statuses[1] + "С нормального на зумерский", callback_data = "switch_mode_to"))

	return Menu