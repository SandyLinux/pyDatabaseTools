'''The numeric values of logging levels are given in the following table. 
These are primarily of interest if you want to define your own levels, and need them to have specific values relative to the predefined levels. If you define a level with the same numeric value, it overwrites the predefined value; the predefined name is lost.
Level	Numeric value
CRITICAL	50
ERROR	40
WARNING	30
INFO	20
DEBUG	10
NOTSET	0
1 -  Logger
2 -  Handler

2.1 stream handler
2.2 file handler
2.3 null handler
2.4 socket handler 
tcp packet

2.5 datagram handler
udp 
3 -  Formatter
They are responsible for converting a LogRecord to (usually) a string which can be interpreted by either a human or an external system. The base Formatter allows a formatting string to be specified. If none is supplied, the default value of '%(message)s' is used, which just includes the message in the logging call. 

A Formatter can be initialized with a format string which makes use of knowledge of the LogRecord attributes - such as the default value mentioned above making use of the fact that the user’s message and arguments are pre-formatted into a LogRecord’s message attribute. This format string contains standard Python %-style mapping keys. 

4 -  Filter
Filters can be used by Handlers and Loggers for more sophisticated filtering than is provided by levels. The base filter class only allows events which are below a certain point in the logger hierarchy. For example, a filter initialized with ‘A.B’ will allow events logged by loggers ‘A.B’, ‘A.B.C’, ‘A.B.C.D’, ‘A.B.D’ etc. but not ‘A.BB’, ‘B.A.B’ etc. If initialized with the empty string, all events are passed.

5 -  LogRecord

LogRecord instances are created automatically by the Logger every time something is logged, and can be created manually via makeLogRecord() (for example, from a pickled event received over the wire).

6 -  LoggerAdapter

7 -  Thread Safe
The logging module is intended to be thread-safe without any special work needing to be done by its clients. It achieves this though using threading locks; there is one lock to serialize access to the module’s shared data, and each handler also creates a lock to serialize access to its underlying I/O.

8 -  Module-level functions
8.1 logging.getLogger([name])
Return a logger with name, if no name is specified, return a logger which is the root logger of the hierarchy. If specified, the name is typically a dot-separated hierarchical name like “a”, “a.b” or “a.b.c.d”. Choice of these names is entirely up to the developer who is using logging.

All calls to this function with a given name return the same logger instance. This means that logger instances never need to be passed between different parts of an application.
8.2 logging.info(msg[, *args[, **kwargs]])
Logs a message with level INFO on the root logger. The arguments are interpreted as for debug().

8.3 logging.warning(msg[, *args[, **kwargs]])
Logs a message with level WARNING on the root logger. The arguments are interpreted as for debug().

8.4 logging.error(msg[, *args[, **kwargs]])
Logs a message with level ERROR on the root logger. The arguments are interpreted as for debug().

8.5 logging.critical(msg[, *args[, **kwargs]])
Logs a message with level CRITICAL on the root logger. The arguments are interpreted as for debug().

8.6 logging.exception(msg[, *args[, **kwargs]])
Logs a message with level ERROR on the root logger. The arguments are interpreted as for debug(), except that any passed exc_info is not inspected. Exception info is always added to the logging message. This function should only be called from an exception handler.

logging.log(level, msg[, *args[, **kwargs]])
Logs a message with level level on the root logger. The other arguments are interpreted as for debug().


'''

import logging
import Task1

'''print(getattr(logging, 'INFO'.upper(),None))
loglevel = 'DEBUG'
if isinstance(getattr(logging, loglevel.upper(), None), int):
    print('yes')
else:
    print('no')
    raise ValueError('Invalid log level: %s' % loglevel)

print(logging.DEBUG)
logging.basicConfig(filename='2.log', filemode='w', level='WARNING')


#logging.warning('this is a  warning ') # message to console, level warning 
#logging.info('this is a infor')
logging.basicConfig(filename='1.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
'''
logging.basicConfig(filename='3.log', 
    format = '%(levelname)s:%(asctime)s:%(message)s', 
    datefmt = '%m-%d-%Y %I:%M:%S %p',
    level=logging.INFO)
#logging.debug('***start****') # debug level is less than info, this line will be be logged

#Task1.task()
#logging.info('***end****')

'''FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')

lh = logging.FileHandler('1.log')
ch = logging.StreamHandler()

logger.warning('Protocol problem: %s', 'connection reset', extra=d)

logger.addHandler(lh)
logger.addHandler(ch)
'''
'''net steps '''
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')



######
##https://docs.python.org/2/howto/logging-cookbook.html

