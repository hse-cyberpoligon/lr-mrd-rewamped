# Чекер для ЛР по МРД в Astra Linux

## Changelog
- Восстановлены и исправлены варианты ДЗ и Экзамена
- Добавлен вариант ПЗ
- Переведено на новое API 
- Доработана отправка статуса выполнения заданий

## Туториал (старый)
Программа связывается с сервером, получает набор заданий, проверяет их выполнение и отсылает на сервер результат выполнения работы

```
main.py     – Входная точка и основной программный цикл
utils.py    – Функции проверки выполнения заданий
variants.py – Наборы вариантов заданий
```

Установка на Астру
```
apt install ca-certificates
apt update
apt install python3-venv
python3 -m venv .venv
source .venc/bin/activate
pip install -r requirments.txt
```

Компиляция
```
pyinstaller --collect-all="transliterate" -F main.py
```

Развертывание бинарника на ВМ
```
sudo su
chown root Checker
chgrp root Checker
chmod a=rx Checker
# Add to Autostart
```

## С чем пришлось столкнуться (Новый туториал)

На чистом образе астры нет `ca-certificates`, поэтому на их устоновить.
Чтобы их установить придется в `/etc/apt/sources.list` добавить репозиторий Астры без TLS:
`deb http://dl.astralinux.ru/astra/stable/1.7_x86-64/repository-base/ 1.7_x86-64 main`

Затем нужно обновить `sudo apt-get update`. После этого наконец можно будет установить все нужные модули python3.

Затем скопировать содержимое этого репозитория на астру.

После установки и проверки что код работает надо скомпилировать чекер.
Для этого устанавливаем модули python3: python3-dev python3-pip build-essential zlib1g-dev pyinstaller
(Первые 4 потребовались для Астры).

Активируем venv.
Скачиваем `pip3 install nuitka`.
Скачиваем `apt install patchelf`.
Выполняем команду: `nuitka --standalone --onefile --follow-imports --include-package=transliterate main.py`
