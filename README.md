## 🚀 QA Automation Project: Chitai-Gorod
**Проект по автоматизации тестирования UI** интернет-магазина [chitai-gorod.ru](https://www.chitai-gorod.ru/) с использованием Python, Selenium, Pytest, Allure и Selenoid.  
![Python](https://img.shields.io/badge/Python-3.14-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![Allure](https://img.shields.io/badge/Allure-2.x-orange)
![Pytest](https://img.shields.io/badge/Pytest-9.x-red)
### 🛠️ Setup
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
### 🧪 Running Tests
#### Local
```bash
pytest
```
#### Selenoid
```bash
pytest --selenoid  
```
### 📊 Allure Report
```bash
# Run tests with Allure results
pytest --alluredir=allure-results

# Generate and open Allure report
allure generate allure-results -o allure-report --clean
allure open allure-report
```
### 🔴 Watch tests in Selenoid
During test execution, open:
```bash
UI: https://selenoid.qa.guru/ui/
```

### 🧪 Покрытие тестами

| Тест | Описание                                                                     |
| :--- |:-----------------------------------------------------------------------------|
| `test_search_book` | Поиск книги по запросу и проверка результатов                                |
| `test_view_all_books` | Открытие каталога и переход к просмотру всех товаров                         |
| `test_add_book_to_cart` | Добавление первой книги из каталога в корзину и проверка заголовка "Корзина" |