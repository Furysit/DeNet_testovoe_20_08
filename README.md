# DeNet_testovoe_20_08

В качестве сервера был выбран FastAPI, так как у него есть Swagger для удобной проверки ручек.
В .env лежит токен и бесплатный API ключ для https://etherscan.io/ 
Пользовался этим сервисом, потому что на PolygonScan висит такая плашка
<img width="1027" height="104" alt="image" src="https://github.com/user-attachments/assets/2ba62f15-63c7-41e6-84dd-6bd74b848cca" />

Уровень F: Поднять сервер для запросов по HTTP (на вышеперечисленные функции).
# Шаги запуска:
1. В своем venv - pip install -r requirements.txt
2. python main.py
3. Будет доступен на 127.0.0.1:8000

Уровень A: Получить баланс выбранного адреса.
Ввод: get_balance 0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d

Уровень B: Получить баланс нескольких адресов сразу.
Ввод: get_several_balances ["0x51f1774249Fc2B0C2603542Ac6184Ae1d048351d", "0x4830AF4aB9cd9E381602aE50f71AE481a7727f7C"]


! Уровень C: Получить топ адресов по балансам токена.
! Уровень D: Получить топ адресов по балансам токена, с информацией по датам последних транзакций.
Реализовал пункт С, но без Pro подписки как оказалось он не позволяет проверить. А без этого, мне кажется, невозможно реализовать.<img width="897" height="392" alt="image" src="https://github.com/user-attachments/assets/d8ef6abe-8876-48b8-9c8c-52f617761a1f" />
<img width="781" height="96" alt="image" src="https://github.com/user-attachments/assets/0de75026-7f63-4e11-8f02-6e5351e57365" />

Уровень E: Произвольная работа по любому из токенов.
get_token_info 0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0


