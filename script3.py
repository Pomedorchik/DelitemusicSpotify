
import pyautogui
import keyboard
import time

pyautogui.FAILSAFE = True

def calibrate(name):
    input(f"\nНаведи мышку на {name} и нажми Enter.")
    print("Запоминаю положение через 5 секунд...")
    time.sleep(5)
    pos = pyautogui.position()
    print(f"Координаты: {pos}")
    return pos

print("=== SPOTIFY CLEANER ===")
print("Открой Любимые треки и разверни Spotify.")

input("Нажми Enter для калибровки.")

# Первая зелёная галочка песни
song = calibrate("зелёную галочку первой песни")

# Открываем меню
pyautogui.click(song)
time.sleep(2)

# Галочка напротив Любимые треки
liked = calibrate("кружок напротив Любимые треки")

# Нажимаем на него
pyautogui.click(liked)
time.sleep(2)

# Кнопка Готово
done = calibrate("кнопку Готово")

# Проверяем одну песню
pyautogui.click(done)
time.sleep(2)

print("\nПроверь Spotify: первая песня должна исчезнуть из любимых.")

if input("Удаление прошло успешно? (да/нет): ").lower() not in ("да", "д"):
    print("Остановлено.")
    exit()

print("\nНачинаю удаление оставшихся 144 песен.")

for i in range(144):
    if keyboard.is_pressed("esc"):
        print("Остановка по ESC!")
        break

    pyautogui.click(song)
    time.sleep(1)

    pyautogui.click(liked)
    time.sleep(1)

    pyautogui.click(done)
    time.sleep(1)

    print(f"Удалено: {i + 2}/145")

print("Работа завершена!")
