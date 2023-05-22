# Группа 4 Итоговый проект Програмная инжинерия II

Состав группы:
 - Dmitrii-Krasnov Dmitrii Krasnov
 - svwk Savoskina Svetlana
 - GLOBB1000 Artem Solodukhin
 - Oshutkova Rudenko Darya
 ## Описание проекта
 Модуль формолизация текста подключаемый через FastAPI
 ## Технологии
 - fastapi>=0.95.1
- uvicorn>=0.21.1
- pydantic>=1.10.7
- transformers>=4.28.0
- torch>=1.13.0
- httpx>=0.24.0
- styleformer @ git+https://github.com/PrithivirajDamodaran/Styleformer.git@main

## Использование
###Установка зависимостей
- Для установки зависимостей, выполните команду:
  pip install -r requirements.txt
###Web client for Text style convert API
- Configure client
  Run npm install from /WebClient folder.
- Start client
  Run npx ng serve from /WebClient folder to start. Navigate to http://localhost:4200/.

