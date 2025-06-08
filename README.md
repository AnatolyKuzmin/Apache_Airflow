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

Доступ к Airflow `http://localhost:8080`. airflow

### Первый DAG
Создаём файл dags/01_first_dag.py. Обновляем веб-интерфейс — DAG должен появиться в списке.  
Запуск вручную через UI или CLI `docker-compose exec airflow-webserver airflow dags trigger hello_world`
Если есть ошибки, нужно проверит логи `docker-compose logs -f airflow-scheduler`

