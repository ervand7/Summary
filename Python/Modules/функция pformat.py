# основная статья: https://pyneng.readthedocs.io/ru/latest/book/12_useful_modules/pprint.html#id2
from pprint import pformat

a = {'interface Tunnel0': [' ip unnumbered Loopback0',
                           ' tunnel mode mpls traffic-eng',
                           ' tunnel destination 10.2.2.2',
                           ' tunnel mpls traffic-eng priority 7 7',
                           ' tunnel mpls traffic-eng bandwidth 5000',
                           ' tunnel mpls traffic-eng path-option 10 dynamic',
                           ' no routing dynamic'],
     'ip access-list standard LDP': [' deny   10.0.0.0 0.0.255.255',
                                     ' permit 10.0.0.0 0.255.255.255'],
     'router bgp 100': {' address-family vpnv4': ['  neighbor 10.2.2.2 activate',
                                                  '  neighbor 10.2.2.2 '
                                                  'send-community both',
                                                  '  exit-address-family'],
                        ' bgp bestpath igp-metric ignore': [],
                        ' bgp log-neighbor-changes': [],
                        ' neighbor 10.2.2.2 next-hop-self': [],
                        ' neighbor 10.2.2.2 remote-as 100': [],
                        ' neighbor 10.2.2.2 update-source Loopback0': [],
                        ' neighbor 10.4.4.4 remote-as 40': []},
     'router ospf 1': [' mpls ldp autoconfig area 0',
                       ' mpls traffic-eng router-id Loopback0',
                       ' mpls traffic-eng area 0',
                       ' network 10.0.0.0 0.255.255.255 area 0']}

print(type(a))  # <class 'dict'>
# приводит все типы данных в строку. + можем кастомизировать эту строку с любым отступом и шириной строки
print(pformat(a, indent=12, width=212))
print(type(pformat(a)))  # <class 'str'>

