## 🚀 QA Automation Project: Chitai-Gorod
**Проект по автоматизации тестирования UI** интернет-магазина [chitai-gorod.ru](https://www.chitai-gorod.ru/) с использованием Python, Selenium, Pytest, Allure и Selenoid.  
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![Allure](https://img.shields.io/badge/Allure-2.x-orange)
![Pytest](https://img.shields.io/badge/Pytest-9.x-red)
![Selenoid](https://img.shields.io/badge/Selenoid-Docker-blueviolet)
### 🛠️ Установка
Клонируйте репозиторий, создайте и активируйте виртуальное окружение, установите зависимости.
```bash
git clone https://github.com/alagunskaya/qa_guru_hw_chitai-project.git
cd qa_guru_hw_chitai-project
```
```bash
python -m venv .venv
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```
### 🧪 Запуск тестов
#### Local
```bash
pytest
```
#### Selenoid
```bash
pytest --selenoid  
```
### 📊 Отчёты Allure
```bash
# Run tests with Allure results
pytest --alluredir=allure-results

# Generate and open Allure report
allure generate allure-results -o allure-report --clean
allure open allure-report
```
### 💡 **Что вы увидите в отчёте:**
- Скриншоты
- HTML-исходный код страницы
- Логи браузера
- Видео (если тесты запускались в `Selenoid`)
- Наглядную структуру шагов через `allure.step()`

### 🔴 Просмотр тестов в Selenoid
```bash
UI: https://selenoid.qa.guru/ui/
```

### 🧪 Покрытие тестами
| Файл | Тест | Описание                                                                               |
| :--- | :--- |:---------------------------------------------------------------------------------------|
| `test_search.py` | `test_search_book` | Поиск книги по запросу и проверка результатов                                          |
| `test_search.py` | `test_empty_search` | Проверка поиска с пустым запросом                                                      |
| `test_search.py` | `test_search_no_results` | Поиск несуществующего товара и проверка сообщения                                      |
| `test_catalog.py` | `test_view_all_books` | Открытие каталога и переход к просмотру всех товаров                                   |
| `test_catalog.py` | `test_catalog_url` | Проверка URL после открытия каталога                                                   |
| `test_cart.py` | `test_add_book_to_cart` | Добавление книги из каталога в корзину и проверка заголовка                            |
| `test_cart.py` | `test_cart_opens` | Проверка открытия корзины                                                              |
| `test_ui_elements.py` | `test_header_elements_are_visible` | Проверка наличия элементов в хедере (логотип, каталог, поиск)                          |
| `test_ui_elements.py` | `test_header_right_elements_are_visible` | Проверка наличия элементов в правой части хедера (профиль, заказы, мои книги, корзина) |  

###  🤖 CI/CD (Jenkins)
Проект настроен и запускается через Jenkins.    
**Сборка автоматически выполняет следующие шаги:**
- Клонирование репозитория
- Установка зависимостей
- Запуск тестов в Selenoid
- Генерация Allure-отчета
- Отправка оповещения о результатах тестирования Telegram-ботом
  
![This is an image](/src/Allure.png)
![This is an image](/src/Allure2.png)
<img src="/src/Jenkins.png" alt="Сборка Jenkins" height ="290"><img src="/src/Results.png" alt="Оповещение" height="290">

**Пример видеозаписи прохождения теста:**  
![This is an image](/src/CG_test.gif)