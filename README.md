
## Зачем ветка?

Эта ветка создания http сервера с помощью фреймворка Django.

### Команды для установки Docker и всего необходимого(Ubuntu):

``` 
sudo apt-get update
sudo apt-get install ca-certificates curl 
```

Добавить оф. ключ GPG Docker:

```
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Установка пакетов Docker:

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Команды для установки Docker и всего необходимого(Debian):

```
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Установка Docker:

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```


## Команда запуска в корневой директории проекта:
```
sudo docker compose up -d
```

## Тестирование работоспособности: 

Linux:

```
curl -X GET http://localhost:8000/healthz
```

Windows PowerShell:

```
Invoke-WebRequest -Uri "http://localhost:8000/healthz" -Method Get
```

Браузер: 

```
http://localhost:8000/healthz
```

## Изменения:

1. views.py: Этот файл будет содержать функцию для обработки запроса на /healthz, возвращая 200 OK.
2. urls.py: Этот файл содержит маршрутизацию для URL-адреса /healthz, чтобы направлять его в views.health_check.
3. main.py: Этот файл инициализирует Django-приложение, настраивает его конфигурацию и запускает сервер.







