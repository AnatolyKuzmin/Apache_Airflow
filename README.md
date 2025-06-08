# Apache_Airflow

## Начало

Проверка:
```
docker --version  # Должно быть не ниже 20.10.0
wsl -l -v         # Убедитесь, что WSL 2 активен
```

Создаем [docker-compose.yml](https://github.com/AnatolyKuzmin/Apache_Airflow/tree/main) в папке `C:/airflow`

Запускаем контейнер `docker-compose up -d`  
Проверяем логи `docker-compose logs -f airflow-webserver`
