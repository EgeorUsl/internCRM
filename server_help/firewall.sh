#!/bin/bash
WIFACE=ens3 # Internet interface
LOOP=127.0.0.1 # Loopback interface
TCP_PORTS=(22 25 80 443 993) # Открыть TCP порты

function firewall {
ipt=$1
# Очищаем все таблицы iptables
$ipt -F -t nat
$ipt -F

# Правила по умолчанию: запрещаем всё, что явно не разрешено
$ipt -P INPUT DROP
$ipt -P FORWARD DROP
$ipt -P OUTPUT ACCEPT

# Отбрасываем INVALID-пaкeты
$ipt -A INPUT -m state --state INVALID -j DROP
$ipt -A FORWARD -m state --state INVALID -j DROP

# Разрешаем трафик через loopback
$ipt -A INPUT -i $WIFACE -s $LOOP -j DROP
$ipt -A FORWARD -i $WIFACE -s $LOOP -j DROP
$ipt -A INPUT -i $WIFACE -d $LOOP -j DROP
$ipt -A FORWARD -i $WIFACE -d $LOOP -j DROP
$ipt -A INPUT -s $LOOP -j ACCEPT
$ipt -A INPUT -d $LOOP -j ACCEPT

#Разрешаем установленные соединения
$ipt -A INPUT   -m state --state ESTABLISHED,RELATED -j ACCEPT
$ipt -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

#Разрешить все новые проходящие соединения
$ipt -A FORWARD -m state --state NEW -j ACCEPT

# Разрешаем соединения по портам из массива
for port in "${TCP_PORTS[@]}"
do
    $ipt -A INPUT -p tcp --dport $port -j ACCEPT
done
}

firewall /usr/sbin/iptables
LOOP=::1
firewall /usr/sbin/ip6tables
