
# LLRA

Утилита LLRA (live lib reviews analysis) позволит получить список всех ваших рецензий с вашего аккаунта LiveLib в отсортированном порядке.

## Проблема
Рецензии на LiveLib сортируются по кол-ву лайков. Я считаю, что это неправильно. В LLRA реценизии сортируются по многим фактрам, например, влияет фактор прошедшего времени со дня публикации. Или отношение кол-ва лайков к просмотрам.

## Локальный запуск
После клонирования репозитория нужно установить зависимости:
```bash
pip install -r requirements.txt
```

При запуске скрипта можно передать следующие параметры:

- `--username` - обязательный параметр. Название аккаунта на LiveLib. По нему будет строится URl к рецензиям;
- `--reverse` - необязательный параметр. Если указан `true`, то сортировка будет в порядке убывания рейтинга, иначе по возрастанию. По умолчанию `true`;
- `--in_file` - необязательный параметр. Если указан `true`, то вывод будет перенаправлен в файл, иначе в stdout. По умолчанию `false`.

Чтобы запустить скрипт, в корне проекта нужно прописать:
```bash
python3 main.py --username=USERNAME --reverse=true
```