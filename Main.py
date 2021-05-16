from google.cloud import pubsub_v1
import random as random
import time


# TODO(developer)
project_id = "double-archive-310010"
topic_id = "pub_sub_messages"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

for n in range(1, 40):
    #data = "Message number {}".format(n)
    country = ["US", "GB", "RQ", "VI", "GU"]
    crand = random.randint(0,4)
    data = ""
    data = data + country[crand]
    data = data + ","
    type_aircraft = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    trand = random.randint(0,8)
    data = data + type_aircraft[trand]
    data = data + ","
    year_mfr = ["1936", "1942", "1953", "1964", "1975", "1986", "1997", "2008", "2019"]
    yrand = random.randint(0,8)
    data = data + year_mfr[yrand]

    # Data must be a bytestring
    data = data.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())
    time.sleep(2)

print(f"Published messages to {topic_path}.")