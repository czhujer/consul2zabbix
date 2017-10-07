# consul2zabbix
get docker apps and ports from consul services catelog

originaly developed and tested on:

 consul 0.8.0 / 0.9.3

 gliderlabs/registrator

 CentOS 7.x x86_64

 docker 1.12

# Installation

1. create containers with consul and registrator

2. copy consul2zabbix.py

3. run it :)

# Usage

```
# ./consul2zabbix.py sf-consul-s1 discovery
```

```
{
    "data": [
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-influxdb-s1:8083",
	"{#SERVICENAME}": "influxdb-8083",
	"{#SERVICEADDRESS}": "172.23.0.4",
	"{#SERVICEPORT}": "8083"
    },
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-influxdb-s1:8086",
	"{#SERVICENAME}": "influxdb-8086",
	"{#SERVICEADDRESS}": "172.23.0.4",
	"{#SERVICEPORT}": "8086"
    },
    {
	"{#SERVICEID}": "consul",
	"{#SERVICENAME}": "consul",
	"{#SERVICEADDRESS}": "",
	"{#SERVICEPORT}": "8300"
    },
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-grafana-s1:3000",
	"{#SERVICENAME}": "grafana-xxl",
	"{#SERVICEADDRESS}": "172.23.0.2",
	"{#SERVICEPORT}": "3000"
    },
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-telegraf-s11:8094",
	"{#SERVICENAME}": "telegraf-8094",
	"{#SERVICEADDRESS}": "172.17.0.3",
	"{#SERVICEPORT}": "8094"
    },
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-consul-s1:8500",
	"{#SERVICENAME}": "consul-admin",
	"{#SERVICEADDRESS}": "172.20.0.3",
	"{#SERVICEPORT}": "8500"
    },
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-telegraf-s11:8125:udp",
	"{#SERVICENAME}": "telegraf-8125",
	"{#SERVICEADDRESS}": "172.17.0.3",
	"{#SERVICEPORT}": "8125"
    },
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-cadvisor-s1:8080",
	"{#SERVICENAME}": "cadvisor",
	"{#SERVICEADDRESS}": "172.23.0.3",
	"{#SERVICEPORT}": "8080"
    },
    {
	"{#SERVICEID}": "sf-registrator-s1:sf-telegraf-s11:8092:udp",
	"{#SERVICENAME}": "telegraf-8092",
	"{#SERVICEADDRESS}": "172.17.0.3",
	"{#SERVICEPORT}": "8092"
    }

    ]
}
```

