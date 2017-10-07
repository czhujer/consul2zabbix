#!/usr/bin/python

import sys
import json
import requests
import socket
import md5

def getDiscovery():
    discovery_list = {}
    discovery_list['data'] = []

    nodeInfo = requests.get(url).text
    #print "DEBUG: nodeServices: " + nodeServices

    sections = json.loads(nodeInfo)

    service_loop_id=0
    zbx_items_final = ""

    for service in sections['Services']:
        zbx_item1 = '"{#SERVICEID}": ' + '"' + service + '"'

        #print "DEBUG: " + str(service)

        for attr in sections['Services'][service]:
           value = sections['Services'][service][attr]
           #print "\t" + str(attr)
           #print "\t\t" + str(value)

           if attr == "Service":
              zbx_item2 = '"{#SERVICENAME}": ' + '"' + value + '"'

           if attr == "Address":
              zbx_item3 = '"{#SERVICEADDRESS}": ' + '"' + value + '"'

           if attr == "Port":
              zbx_item4 = '"{#SERVICEPORT}": ' + '"' + str(value) + '"'

        if service_loop_id == 0:
            zbx_items = ''
        else:
            zbx_items = ',\n'

        zbx_items += '\t{\n\t\t' + zbx_item1 + ',\n\t\t' + zbx_item2 + ',\n\t\t' + zbx_item3 + ',\n\t\t' + zbx_item4 + '\n\t}'

        #print "DEBUG: " + zbx_item

        #discovery_list['data'].append(zbx_items)
        zbx_items_final += zbx_items
        service_loop_id+=1

    #print json.dumps(discovery_list, indent=4, sort_keys=True)
    zbx_items_final  = '{\n\t"data": [\n' + zbx_items_final + '\n\n\t]\n}\n'
    print zbx_items_final

def getStatus(ServiceID):
    nodeService = requests.get(url_service_status).text
    sections = json.loads(nodeService)

    status = 0
    
    for attr in sections[0]['Checks'][0]:
        value = sections[0]['Checks'][0][attr]
        #print attr
        #print '\t' + str(value)

        if attr == "Status":
            if value == 'passing':
                status = 1
            else:
                status = 0

    print status

action = sys.argv[2].lower()
if action == 'discovery':

    nodeName = sys.argv[1]

    #url = 'http://{0}:8500/v1/health/node/{0}'.format(nodeName)
    url = 'http://{0}:8500/v1/catalog/node/{0}'.format(nodeName)
    #print "DEBUG: url: " + url

    getDiscovery()

elif action == 'status':

    nodeName = sys.argv[1]
    serviceName = sys.argv[3]

    url_service_status = 'http://{0}:8500/v1/health/service/{0}'.format(serviceName)
    #print "DEBUG: url_service_status: " + url_service_status

    getStatus(serviceName)

