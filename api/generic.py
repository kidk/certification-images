#!/usr/bin/env python

import argparse
import json
import random
import time
import urllib2

#------------------------------------------------------------------------------
# Configuration mode: return the custom metrics data should be defined
def config():
    settings = {
        'maxruntime': 5000,  # How long the script is allowed to run
        'period': 60,  # The period the script will run, in this case it will run every 60 seconds
        'metrics': [
            {
                'id': 1,
                'datatype': 'DOUBLE',
                'name': 'Emails sent',
                'description': 'Number of emails sent to customers',
                'groups': 'API',
                'unit': '#',
                'tags': '',
                'calctype': 'Instant'
            },
            {
                'id': 2,
                'datatype': 'DOUBLE',
                'name': 'Signins',
                'description': 'Number of new customers',
                'groups': 'API',
                'unit': '#',
                'tags': '',
                'calctype': 'Instant'
            },
            {
                'id': 3,
                'datatype': 'DOUBLE',
                'name': 'Total users',
                'description': 'Total number of users subscribed',
                'groups': 'API',
                'unit': '#',
                'tags': '',
                'calctype': 'Instant'
            }
        ]
    }

    print json.dumps(settings, indent=4)

# Data retrieval mode: return the data for the custom metrics
def data():
    content = json.loads(urllib2.urlopen("http://localhost/accounts/stats").read())

    print 'M1 {0}'.format(content['emails_sent'])
    print 'M2 {0}'.format(content['signins'])
    print 'M3 {0}'.format(content['users_total'])

#------------------------------------------------------------------------------
# Switch to check in which mode the script is running
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='output a JSON object detailing the metrics this script collects')
    parser.add_argument('-d', action='store_true', help='output the metrics this script collects')
    args = parser.parse_args()

    if args.c:
        config()
    elif args.d:
        data()
