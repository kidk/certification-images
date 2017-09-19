import time
import random
import uuid

while True:
    number = random.randint(10, 30)
    print "Received %s work items" % number
    
    for i in range(0, number):
        failed = random.randint(0, 100)
        latency = random.randint(50, 300) / 1000.0
        time.sleep(latency)
        if failed > 15 and failed > 5:
            print "Processing %s took %2.4f ms" % (i, latency)
        elif failed <= 5:
            print "%s" % uuid.uuid4()
        else:
            print "Processing failed for %s" % i

