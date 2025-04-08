# 🌟 PostFlow_v2: Улучшенная блог-платформа на Django

## Описание проекта

📚 **PostFlow_v2** — это блог-платформа на Django с поддержкой базы данных, позволяющая создавать, редактировать и управлять публикациями, категориями и географическими метками. Проект включает админ-панель с русской локализацией и фильтрацию контента.

## Возможности

- **Главная страница**: Выводит последние 5 публикаций, отфильтрованных по дате, статусу публикации и активности категории.  
- **Страница категории**: Отображает публикации, принадлежащие выбранной категории.  
- **Страница публикации**: Детальный просмотр отдельного поста.  
- **Админ-панель**: Управление публикациями, категориями и локациями с русской локализацией.  
- **Фильтрация**: Публикации отображаются только при выполнении следующих условий:  
  - Дата публикации не позже текущего времени.  
  - Публикация опубликована (`is_published=True`).  
  - Категория активна (`is_published=True`).  

## Технологии

- **Django**: Фреймворк для создания веб-приложений.  
- **ORM**: Работа с базой данных через модели.  
- **HTML & CSS**: Верстка страниц и подключение статики.  
- **Шаблоны Django**: Использование контекста, циклов и условий.

## Как использовать

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/ваш_профиль/PostFlow_v2.git
   cd django_sprint3
2. **Создайте и активируйте виртуальное окружение :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/MacOS
   venv\Scripts\activate     # Для Windows
   ```
3. **Установите зависимости :
   ```bash
   pip install -r requirements.txt
   ```
4. **Примените миграции :
   ```bash
   python manage.py migrate
   ```
5. **Загрузите фикстуры :
   ```bash
   python manage.py loaddata db.json
   ```
6. **Запустите сервер :
   ```bash
   python manage.py runserver
   ```
7. **Откройте в браузере :
   ```bash
   http://127.0.0.1:8000/
   ```
