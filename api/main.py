from flask import Flask
import sys
import optparse
import time
import json
import random
import math

app = Flask(__name__)

start = int(round(time.time()))

@app.route("/accounts/stats")
def get_users():
    users = math.floor(time.time() / 4500)
    emails = random.randint(100, 200)
    signins = random.randint(10, 100)
    return "%s" % json.dumps({
        "emails_sent": emails,
        "signins": signins,
        "users_total": users
    })



if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print "Missing required argument: -p/--port"
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)
