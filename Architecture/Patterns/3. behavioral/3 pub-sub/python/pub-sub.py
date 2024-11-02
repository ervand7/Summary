# https://github.com/ervand7/python-design-patterns/blob/master/PubSub.py
"""
The publish-subscribe pattern, also known as the "observer pattern"
is generally used to decouple the sending and receiving of messages.
The publisher does not need to care about the receiving object, but only
needs to send the message to an intermediate broker (Broker); the subscriber
can subscribe to the interested message according to the topic, and
the Broker will route the message.
"""


class Broker(object):

    def __init__(self, name=''):
        self._name = name
        self._subscribers = []  # maintain a list of subscribers

    def attach(self, subscriber: Subscriber):
        """bind a subscriber"""
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def detach(self, subscriber: Subscriber):
        """unbind"""
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def route(self, msg, topic=''):
        """Methods of routing messages"""
        for subscriber in self._subscribers:  # type: Subscriber
            if topic in subscriber.topic:
                subscriber.sub(msg)


class Publisher(object):

    def __init__(self, name, broker: Broker):
        self._name = name
        self._broker = broker

    def pub(self, msg, topic=''):
        print('[Publisher: {}] topic: {}, message: {}'.format(self._name, topic, msg))
        self._broker.route(msg, topic)


class Subscriber(object):

    def __init__(self, name, broker: Broker, topic=None):
        self._name = name
        broker.attach(self)
        self._topic = [] if topic is None else topic

    def sub(self, msg):
        print('[Subscriber: {}] got message: {}'.format(self._name, msg))

    @property
    def topic(self):
        return self._topic


def main():
    # declare an intermediate proxy
    broker = Broker()

    # Declare two publishers, connected to the specified broker
    p1 = Publisher('p1', broker)
    p2 = Publisher('p2', broker)

    # Declare two subscribers, connect to the specified broker, and subscribe to the specified topic
    s1 = Subscriber('s1', broker, topic=['A'])
    s2 = Subscriber('s2', broker, topic=['A', 'B'])

    # p1, p2 publish a message
    p1.pub('hello world', topic='A')
    p2.pub('good bye', topic='B')


if __name__ == '__main__':
    main()

    # [Publisher: p1] topic: A, message: hello world
    # [Subscriber: s1] got message: hello world
    # [Subscriber: s2] got message: hello world
    # [Publisher: p2] topic: B, message: good bye
    # [Subscriber: s2] got message: good bye
