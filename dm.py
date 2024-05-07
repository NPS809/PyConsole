# Вспомогательное (повторяющиеся)
def SaveData(text: list):
    """Сохраняет массив строк данных в файл данных"""
    with open("data.data", "w", encoding='utf-8') as file:
        placetab = False
        for str in text:  # Записываем данные в файл аккуратненько
            if "}" in str:
                placetab = False
            tab = "    " if placetab else ""
            file.write(f"{tab}{str}\n")
            if "{" in str:
                placetab = True
        return True


def OpenDataToRead() -> list:
    """Открывает файл данных и возвращает обработанный(без лишних пробелов и пустых строк) массив строк"""
    with open("data.data", "r", encoding="utf-8") as file:
        text = file.read().split("\n")  # Делим текст на строки
        text = [i.strip() for i in text]  # Убираем пробелы в строках
        while '' in text: text.remove('')  # и убираем пустые строки
        return text


# -----Chapter Tools-------
def CreateChapter(chapter_name: str):
    """Создать раздел"""
    if not isChapterExist(chapter_name):
        with open("data.data", "a", encoding="utf-8") as file:
            file.write(f"${chapter_name}: " + "{\n")
            file.write("}\n")
    else:
        print(f"Раздел {chapter_name} уже существует!")


def DeleteChapter(chapter_name: str):
    """Удалить раздел"""
    if isChapterExist(chapter_name):
        text = OpenDataToRead()
        startPoint, endPoint = GetChapterBorders(text, chapter_name)
        firstPart = text[:startPoint - 1]
        secondPart = text[endPoint + 1:]
        text = firstPart + secondPart
        SaveData(text)
    else:
        print(f"Раздела {chapter_name} не существует!")


def isChapterExist(chapter_name: str) -> bool:
    """Проверяет, существует ли раздел {chapter_name}"""
    with open("data.data", "r", encoding="utf-8") as file:
        isChapterExist = False
        for string in file.read().split("\n"):
            if f'${chapter_name}:' + "{" in string.replace(" ",
                                                           ""):  # Если есть строка с $ и именем нашего раздела, то...
                isChapterExist = True  # раздел существует, и к нему можно обращаться
                break
        return isChapterExist


def ToDict(text: list, startPoint: int, endPoint: int) -> dict:
    """Преобразовывает из раздела(массива строк данных, получаемых PreparingText) в ассоциативный массив"""
    chapter_data = text[startPoint:endPoint]
    new_chapter_data = {}
    for cell in chapter_data:
        c_name, c_data = cell.split(":")
        new_chapter_data[c_name] = c_data
    return new_chapter_data


def GetChapterBorders(text, chapter_name) -> tuple:
    """Получение границ раздела"""
    startPoint = 0
    endPoint = 0
    for i in range(len(text)):
        if f'${chapter_name}:' + "{" in text[i].replace(" ", ""):  # Ищем начало нашего раздела
            startPoint = i + 1
            break
    for i in range(startPoint, len(text)):  # Ищем конец нашего раздела
        if "}" in text[i]:
            endPoint = i
            break
    return (startPoint, endPoint)


def ClearChapter(chapter_name):
    if isChapterExist(chapter_name):
        DeleteChapter(chapter_name)
        CreateChapter(chapter_name)


# -------------------------
class Chapter:
    name = "chapter"

    def __init__(self, chapter_name: str):
        if not isChapterExist(chapter_name):
            input(f"Раздела {chapter_name} не существует! Доступ к данным осуществить невозможно.")
            exit()
        else:
            self.name = chapter_name

    def GetCellsDict(self) -> dict:
        """Возвращает раздел в виде словаря(Минуя базовые функции)"""
        text = OpenDataToRead()
        startPoint, endPoint = GetChapterBorders(text, self.name)
        chapter_data = ToDict(text, startPoint, endPoint)
        return chapter_data

    def Get(self, cell_name: str):
        """Получает значение ячейки по имени"""
        if isChapterExist(self.name):
            chapter_data = self.GetCellsDict()
            if cell_name not in chapter_data.keys():
                print(f"Ячейка {cell_name} не найдена! Получение данных невозможно.")
            else:
                return chapter_data[cell_name].strip()  # Возвращаем данные из ячейки, если таковая есть

    def Set(self, cell_name: str, new_data, create_if_doesnt_exist=True):
        """Устанавливает значение ячейки по имени, если create_if_doesnt_exist и ячейки не существует, создает ее,
        если ячейка существует, перезапишет ее"""
        if isChapterExist(self.name):
            text = OpenDataToRead()

            startPoint, endPoint = GetChapterBorders(text, self.name)
            str_id = -11
            for i in range(startPoint, endPoint):
                if f'{cell_name}' in text[i]:  # Ищем необходимую ячейку
                    str_id = i
                    break

            if str_id == -11 and not create_if_doesnt_exist:
                print("Ячейка не найдена! Изменение данных невозможно")

            elif str_id == -11 and create_if_doesnt_exist:  # Если нет ячейки, но есть параметр create_if_doesnt_exist
                endPoint = GetChapterBorders(text, self.name)[1]
                firstHalf, secondHalf = text[:endPoint], text[endPoint:]
                firstHalf.append(f'{cell_name}: {new_data}')
                text = firstHalf + secondHalf
                SaveData(text)

            else:
                c_name, c_data = text[str_id].split(":")
                text[str_id] = f'{str(c_name)}: {str(new_data)}'
                SaveData(text)

    def Delete(self, cell_name: str):
        """Удаляет ячейку"""
        text = OpenDataToRead()
        startPoint, endPoint = GetChapterBorders(text, self.name)
        for i in range(startPoint, endPoint):
            if f'{cell_name}:' in text[i].replace(" ", ""):
                text.pop(i)
                break
        SaveData(text)

    def GetCells(self):
        """Возвращает все имена ячеек в разделе"""
        return self.GetCellsDict().keys()

    def isCellExist(self, cell_name: str):
        """Проверяет, существует ли данная ячейка"""
        return cell_name in self.GetCellsDict().keys()
