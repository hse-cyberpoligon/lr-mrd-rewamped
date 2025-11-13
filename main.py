from variants import variants
from transliterate import translit # type: ignore
from utils    import *
import requests, time, os          # type: ignore
import json

LAB_NAME = "Мандатное разграничение доступа Astra Linux"
LAB_SLUG = "mandatnoe-razgranichenie-dostupa-astra-linux"

def request_tasks(surname, name):
    print("Запрос заданий для выполнения...")
    url = "http://172.18.4.200:8080/api/start"
    payload = {
        "username":   surname + "_" + name,
        "lab_slug":   LAB_SLUG
    }
    payload = json.dumps(payload).encode('utf-8')

    response = requests.request("GET", url, data=payload)
    response.encoding = 'utf-8'
    response = json.loads(response.text)
    return response


def finish_exact_task(surname, name, task_id):
    url = "http://172.18.4.200:8080/api/answers"
    payload = {
        "user":   surname + "_" + name,
        "lab_slug":   LAB_SLUG,
        "task": task_id
    }
    payload = json.dumps(payload).encode('utf-8')

    response = requests.request("POST", url, data=payload)
    response.encoding = 'utf-8'
    response = json.loads(response.text)
    return response


def fill_templates(variant, surname):
    for task in variant:
        for condition in task['conditions']:
            for key in ['path', 'owner', 'group']:
                if key in condition:
                    condition[key] = condition[key].replace('SURNAME', translit(surname.lower(),'ru', reversed=True))


def main():
    os.system('clear')

    surname = input("Введите Фамилию: ")
    name = input("Введите Имя:     ")

    response = request_tasks(surname, name)
    if 'type' not in response.keys() or 'tasks' not in response.keys():
        print("Ошибка получения заданий для выполнения! Неизвестный ответ:")
        print(response)
        exit()

    tasks = sorted(response['tasks'])
    lab_type = response['type'].lower()

    show_tips = True
    if lab_type == 'exam':
        show_tips = False

    try:
        target_variant = variants[lab_type]
    except KeyError:
        print("Ошибка получения заданий для выполнения! Неизвестный тип работы:")
        print(lab_type)
        exit()
    fill_templates(target_variant, surname)

    time_passed = 0
    while True:
        os.system('clear')

        print(f"{surname} {name},")
        print(f"Тебе осталось выполнить задания:\n{tasks}")
        print(f"Прошло времени: {time_passed//60:02}:{time_passed%60:02}")
        print(f"======================================")

        for task_id in list(tasks):
            # tasks present
            task = next((task for task in target_variant if task['id'] == task_id), None)
            task_completed = True

            if task is not None:
                task_completed = False

                for f in task['conditions']:
                    file_path = f['path']
                    file_type = f['type'] if ('type' in f) else ''

                    if not check_1_exist(file_path, file_type):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Объект не существует")
                        break

                    if ('permissions' in f) and not check_2_perms(file_path, f['permissions']):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Неверные права доступа")
                            print(f"Должно быть: {f['permissions']}")
                        break

                    if ('owner' in f) and not check_3_owner(file_path, f['owner']):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Неверный владелец объекта")
                            print(f"Должно быть: {f['owner']}")
                        break

                    if ('group' in f) and not check_4_group(file_path, f['group']):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Неверная группа объекта")
                            print(f"Должно быть: {f['group']}")
                        break

                    if ('privacy_label' in f) and not check_5_privacy(file_path, f['privacy_label']):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Неверный уровень конфиденциальности")
                            print(f"Должно быть: {f['privacy_label']}")
                        break

                    if ('integrity' in f) and not check_6_integrity(file_path, f['integrity']):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Неверный уровень целостности")
                            print(f"Должно быть: {f['integrity']}")
                        break

                    if ('categories' in f) and not check_7_categories(file_path, f['categories']):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Неверно присвоены категории")
                            print(f"Должно быть: {f['categories']}")
                        break

                    if ('flags' in f) and not check_8_flags(file_path, f['flags']):
                        if show_tips:
                            print(f"Объект: {file_path}\nОшибка: Неверно присвоены специальные флаги")
                            print(f"Должно быть: {f['flags']}")
                        break
                else:
                    task_completed = True

            if task_completed:
                try:
                    finish_exact_task(surname, name, task_id)
                except Exception as ex:
                    print("Не удалось оповестить сервер о выполненном задании.\n", ex)
                    input()
                    print(f"Нажмите любую кнопку для продолжения...")

                tasks.remove(task_id)
            else:
                # task is not completed
                break
        else:
            # no tasks left
            break

        time.sleep(1)
        time_passed += 1
        

    print(f"Лабораторная работа завершена!")
    print(f"Ответ сервера: {response['message']}")
    input()
    input()
    exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\nВыполнение работы прервано!")
