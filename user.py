from enum import Enum
from cryptoutils import babble, debabble

DEFAULT_BASE = '的一是了人在有我他这为之来以个们到说和地也子时而要于就下得可你年生自会那后能对着事其里所去行过十用发如然方成者多都三二同么当起与好看学进将还分此心前面又定见只从现因开些长明样已月正想实把相两力等外它并间手应全门点身由何向至物被五及入先己或很最书美山什名曰合加世水果位度马给数次今表原各才几解则气再听提万更比百尔即白许系且光路接结题指感量取场电空边件住放风求形望传笑叫往区达设记字故品象花七服据云像飞远收石类程转千式流每该始术格运怎步让识拉若备造快集布尽称确呢节注存具甚容吃算坐早引似视尚轻况留照写足余星居技属找食'

START_MESSAGE = 'hello, world'

class User(object):
    def __init__(self):
        self.key = ''
        self.base = DEFAULT_BASE

    def encrypt(self, message):
        return babble(message.encode(), self.key.encode(), self.base)

    def decrypt(self, message):
        return debabble(message, self.key.encode(), self.base).decode()

    def handle(self, message):
        if message[0] == '/':
            command = message[1:].split(' ', 1)
            if command[0] == 'start':
                return START_MESSAGE
            elif command[0] == 'setkey':
                if len(command) == 1:
                    self.key = ''
                    return 'Your key has been set to empty.'
                else:
                    self.key = command[1]
                    return 'Your key has been set to "%s".' % command[1]
            elif command[0] == 'setbase':
                if len(command) == 1:
                    self.base = DEFAULT_BASE
                    return ('Your base has been set to the default "%s".'
                          % DEFAULT_BASE)
                else:
                    if len(command[1]) == 256:
                        self.base = command[1]
                        return 'Your base has been set to "%s".' % command[1]
                    else:
                        return 'The base has to be 256-character long.'
        try:
            return self.decrypt(message)
        except:
            return self.encrypt(message)
