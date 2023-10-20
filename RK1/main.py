import sys
import random

# Деталь
class detail:
    def __init__(self, id, name, price, provider_id):
        self.id = id
        self.name = name
        self.price = price
        self.provider_id = provider_id

# Поставщик
class provider:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Детали поставщика
class ProvDet:
    def __init__(self, provider_id, detail_id):
        self.provider_id = provider_id
        self.detail_id = detail_id

details = [
    detail(1, "Винт", 100, 1),
    detail(2, "Гайка", 300, 2),
    detail(3, "Шайба", 250, 3),
    detail(4, "Болт", 50, 4),
    detail(5, "Пружина", 65, 5),
    detail(6, "Плитка", 154, 6),
    detail(7, "Кабель", 39, 7),
    detail(8, "Датчик", 439, 8),
    detail(9, "Кнопка", 120, 9),
    detail(10, "Реле", 30, 10),
    detail(11, "Панель", 13, 11),
    detail(12, "Ручка", 34, 12),
    detail(13, "Штекер", 99, 13),
    detail(14, "Датчик движения", 129, 14),
    detail(15, "Мотор", 500, 15),
    detail(16, "Зубчатое колесо", 210, 16),
    detail(17, "Трубка", 59, 17),
    detail(18, "Пластик", 60, 18),
    detail(19, "Стекло", 70, 19),
    detail(20, "Металл", 80, 20),
    detail(21, "Пластмасса", 90, 10),
    detail(22, "Платина", 100, 9),
    detail(23, "Батарейка", 90, 9),
    detail(24, "Светодиод", 80, 8),
    detail(25, "Жгут проводов", 70, 7),
    detail(26, "Рамка", 60, 7),
    detail(27, "Разъём", 50, 6),
    detail(28, "Микроконтроллер", 304, 5),
    detail(29, "Дисплей", 230, 5),
    detail(30, "Слуховой аппарат", 27, 4),
    detail(31, "Колесо", 85, 3),
    detail(32, "Зеркало", 69, 3),
    detail(33, "Клавиша", 30, 2),
    detail(34, "Звезда", 31, 1),
    detail(35, "Спичка", 5, 1),
    detail(36, "Подшипник", 19, 20),
    detail(37, "Транзистор", 20, ),
    detail(38, "Динамик", 30),
    detail(39, "Магнит", 34),
    detail(40, "Проводник", 39),
    detail(41, "Сирена", 96),
    detail(42, "Скрепка", 78),
    detail(43, "Шестерня", 127),
    detail(44, "Колпачок", 149),
    detail(45, "Трансформатор", 203),
    detail(46, "Зарядное устройство", 459),
    detail(47, "Пульт управления", 67),
    detail(48, "Антенна", 206),
    detail(49, "Светильник", 105),
    detail(50, "Вентилятор", 200)
]

providers = [
    provider(1, "ООО 'ТехноКомпания'"),
    provider(2, "АО 'Индустрия'"),
    provider(3, "ЗАО 'Производство'"),
    provider(4, "ИП 'МастерТех'"),
    provider(5, "ОАО 'Прогресс'"),
    provider(6, "Техногрупп"),
    provider(7, "МастерМеханика"),
    provider(8, "Инновационные Технологии"),
    provider(9, "СпецПромТехника"),
    provider(10, "Автоэлектрика"),
    provider(11, "Производство и Сервис"),
    provider(12, "ТехноСревисГарант"),
    provider(13, "ПромХолдинг"),
    provider(14, "Инженерные Решения"),
    provider(15, "АгроТехника"),
    provider(16, "МедТехИнжиниринг"),
    provider(17, "ЭнергоСервис"),
    provider(18, "ТехноВидение"),
    provider(19, "СпецТехноГрупп"),
    provider(20, "ГоризонтПроизводство")
]


details_on_p = [(d.name, d.price) for d in details if d.name.startswith("П")]
print("Деталис с названием на 'П':")
for i in details_on_p:
    print(i)
print()
