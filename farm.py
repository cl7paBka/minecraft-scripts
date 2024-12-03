import keyboard
import pyautogui
import time

# Флаг, который указывает, активен ли режим автоклика
auto_clicking = False

def click_mouse():
    """Функция для клика мышью каждые 2-3 секунды"""
    while True:
        if auto_clicking:
            pyautogui.click()  # Нажимаем левую кнопку мыши
            print("Клик выполнен.")  # Отладочное сообщение
            time.sleep(0.6)  # Пауза 0.6

def toggle_auto_clicking():
    """Переключает состояние автоклика"""
    global auto_clicking
    auto_clicking = not auto_clicking
    if auto_clicking:
        print("Автокликер включен.")
    else:
        print("Автокликер выключен.")

def setup_hotkey():
    """Функция для назначения глобальной горячей клавиши"""
    keyboard.add_hotkey('v', toggle_auto_clicking)  # Настроить клавишу v для переключения автокликера
    print("Горячая клавиша 'v' активирована.")  # Отладочное сообщение

# Запуск функции горячих клавиш и автоклика в одном потоке
if __name__ == '__main__':
    setup_hotkey()  # Настроим горячую клавишу
    click_mouse()  # Запускаем функцию автоклика
