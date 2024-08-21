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

</7etails>