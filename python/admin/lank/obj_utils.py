"""
Will be used by logme
"""
import sys
import os
import logging

# from vars import dbname,dbuser,dbpass,dbport
# import subprocess
# import shlex

"""
This module contains Classes
 - logme (logging in OO)      -- Status completed
 - runcmd (run an OS command) -- Status not started
"""

# ToDo
"""
 - Define a module which has only variables. Those should be imported here.
    -- Completed

 - The logdir check should be outside the class as every invocation of the
   class will run the logdir check. It is called once when class object is
   initialzed. Change logging so that log.debug will display to STDOUT as well.
   Default will be log.info
    -- Completed.
 - Port runcmd.
 - Create a class to import CSV files.
 """


class logme:

    """
    Class logme

    In this section we
     - define the directory for global logging,
     - create the directory
     - create the file
     - ensure both are world writable

     Example of usage
       import obj_utils
          mylog = obj_utils.logme()
          mylog.critical('Critical Error')

       This will write "Critical Error" to the logfile as follows
       <-- time stamp  -->:<Level> :<PID>:  <script>  :<message>
       12-03-2016 22:54:12:CRITICAL:19790:lm.py:Critical Error

     """

    logdir = '/u/logs'
    global logfile
    logfile = logdir + '/lank.log'
    # print logfile
    if not (os.path.exists(logdir)):
        os.mkdir(logdir)
        os.chmod(logdir, 0o777)
        os.open(logfile, 'w', 0o777)
        os.close(logfile)

    def __init__(self):
        # print(logfile)
        pass

    def critical(self, message):
        """Critical messages will
         -- Display to STDOUT
         -- Write to the logfile
         -- Exit with error code 1
         """
        plevel = 50
        self.message = message
        self.writelog(plevel, message)

    def error(self, message):
        plevel = 40
        self.message = message
        self.writelog(plevel, message)

    def warning(self, message):
        plevel = 30
        self.message = message
        self.writelog(plevel, message)

    def info(self, message):
        plevel = 20
        self.message = message
        self.writelog(plevel, message)

    def debug(self, message):
        """This level will write to the logfile as well as STDOUT"""
        plevel = 10
        self.message = message
        self.writelog(plevel, message)

    def notset(self, message):
        plevel = 0
        self.message = message
        self.writelog(plevel, message)

    def writelog(self, plevel, message):
        # filename = os.path.basename(sys.argv[0])
        # We need to log the source filename. Easiest way is to prepend
        # it to the message
        # 06/06/2017. We can prepend source filename as we cannot have a
        # string and dict/list object added
        # message = src_filename + ':' + message
        # print(filename)
        logging.basicConfig(
            filename=logfile,
            level=logging.DEBUG,
            format='%(asctime)s:%(levelname)-8s:%(process)d:%(message)s',
            datefmt='%m-%d-%Y %H:%M:%S'
        )
        logging.log(plevel, message)

        if (plevel == 10):
            print("{}".format(message))

        if (plevel == 50):
            print("{}".format(message))
            print("CRITICAL Level : Mandatory Exit...")
            sys.exit(1)

# End class logme
#################
