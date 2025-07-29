# Log processing

## Из корня приложения ../log_processing/

### установите виртуальное окружение и активируйте его
```bazaar
python -m venv venv
source venv/bin/activate # Linux
```

### установите зависимости
```bazaar
python -m pip install -r requirements.txt
```

### запустить тесты
```bazaar
pytest -v
```
![img.png](readme_imgs/img.png)

### проверить процент покрытия тестами
```bazaar
pytest --cov=app tests/
```
![img_1.png](readme_imgs/img_1.png)

### запустить скрипт без даты
```bazaar
python3 app/main.py --file path/to/log1.log path/to/log2.log --report average
```
![img_2.png](readme_imgs/img_2.png)

### запустить скрипт с датой
```bazaar
python3 app/main.py --file path/to/log1.log path/to/log2.log --report average --date 2025-22-06
```
![img_3.png](readme_imgs/img_3.png)

### ### запустить скрипт с записью в файл
```bazaar
python3 app/main.py --file path/to/log1.log path/to/log2.log --report average --date 2025-22-06 --output file --output-file path_to_file
```
![img_4.png](readme_imgs/img_4.png)
