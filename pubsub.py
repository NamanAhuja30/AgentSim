# pubsub.py
import redis

r = redis.Redis(host='localhost', port=6379)

def publish_message(channel, message):
    r.publish(channel, message)

def subscribe_to_channel(channel):
    pubsub = r.pubsub()
    pubsub.subscribe(channel)
    return pubsub