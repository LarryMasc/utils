#!/usr/bin/python
#
# Utils is always imported first
#
import csv
import string

def main():
    #import lank.utils
    # print (logfile)'
    #lank.utils.logit("hello",1,"crit")
    
    #from lank import utils

    # We set the PYTHONPATH so that we don't have to specify the modules dir.
    # Alternatively, we can set it in the main program as follows
    # sys.path.append('/u/gitwork/utils/python/admin/lank')
    from lank import utils
    # import signal

    #from vars import dbname, dbuser, dbpass, dbport
    from lank.vars import db_creds
    utils.init()
    # utils.create_key()
    # crd = utils.encrypt_cred('587')
    # print(crd)
    # exit(0)
    # from lank.vars import smtp_user, smtp_passwd, smtp_server, smtp_port
    # (gmus, gmpa, gmse, gmpo) = utils.get_creds(smtp_user, smtp_passwd, smtp_server, smtp_port)
    # print(gmus, gmpa, gmse, gmpo)
    # exit(0)

    recipient = ['larry.masc@gmail.com', 'larry_mario@yahoo.com']
    # recipient = 'larry_mario@yahoo.com'
    # recipient = 'larry.masc@gmail.com'
    subject = 'Test from Python'
    body = 'Test 5 to GMail and Yahoo with Mimetext and Multipart with file'
    # body = """
    # <html>
    # <head></head>
    # <body>
    # <p>Hi!
      # <br><b>How are you?<br></b>
       # Here is the <a href="https://www.python.org">link</a> you wanted.
    # </p>
    # </body>
    # </html>
    # """
    attachment = "/u/tmp/test.html"
    # attachment = "NOFILE"
    # attachment = "/home/lmascare/misc/earthmoon_nasa.jpg"
    # attachment = "/home/lmascare/misc/KEYS.gz"
    attachment = "NOFILE"

    # Process a CSV file and send the data as a table.
    csv_file = "/u/tmp/cities.csv"
    with open(csv_file, "r") as csv_data:
        csv_reader = csv.reader(csv_data, dialect="excel", delimiter=",", quotechar='"')
        # Begin table definition
        table = "<!DOCTYPE html>"
        table += "<html>"
        table += "<head>"
        table += "<style>"
        table += """
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        """
        table += "</head>"
        table += "</style>"
        table += "<table>\n"
        for row in csv_reader:
            table += "<tr>" + \
                          "<td>" + \
                              string.join( row, "</td><td>" ) + \
                          "</td>" + \
                     "</tr>\n"
        # End table definition
        table += "</table>"

        table += "</html>"
    # print table
    utils.send_mail(recipient, subject, table, attachment)





    exit(0)
    dbnames = db_creds.keys()
    print(dbnames)

    for dbcred in dbnames:
        print dbcred

        dbname = db_creds[dbcred]['db_name']
        print(dbname)

        dbuser = db_creds[dbcred]['db_user']
        print(dbuser)

        dbpass = db_creds[dbcred]['db_pass']
        print(dbpass)

        dbport = db_creds[dbcred]['db_port']
        print(dbport)

        (db_name, db_user, db_pass, db_port) = utils.get_creds(dbname, dbuser, dbpass, dbport)
        print("DBNAME = {} DBUSER = {} DBPASS = {} DBPORT = {}".format(db_name, db_user, db_pass, db_port))

    #utils.hello()
    #utils.logit("hello","critical")
    #utils.logit("hello","error")
    #utils.logit("hello","warning")
    #utils.logit("hello","info")

    ##utils.logit("info", "hello", 1)
    ##utils.timeout(1)
    ##signal.pause()
    
    utils.runcmd('ps -eaf')
    #utils.runcmd('ifconfig -a')

    # OO Programming

    # we set PYTHONPATH env variable
    #import sys
    #sys.path.append('/u/gitwork/utils/python/admin/lank')

    #import obj_utils

    #mylog = obj_utils.logme()
    #mylog.critical('Critical Message')
    #mylog.error('Error Message')
    #mylog.warning('Warning Message')
    #mylog.debug('DEBUG Message')
    #mylog.info('INFO Message')

if __name__ == "__main__":
    main()
