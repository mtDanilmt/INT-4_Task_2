# INT-4_Task_2
Этот репозиторий для второго задания DevOps. HTTP + Docker


## Используемые библиотеки

Для создания HTTP-сервера используется встроенная библиотека `http.server`. Можно было бы сделать тоже самое с помощью фреймворков Flask и Django. Но, по моему мнению, использование их в реалиах не больших задач не является целесообразным. (При это же ещё необходимо будет скачивать их, что занимает память).

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
curl -X GET http://127.0.0.1:8080/healthz
```

Windows PowerShell:

```
Invoke-WebRequest -Uri "http://127.0.0.1:8080/healthz" -Method Get
```

Браузер: 

```
http://127.0.0.1:8080/healthz
```
