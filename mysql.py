import pymysql
import logging

class DB():

    def __init__(self, host='localhost', user='', password='', database='', port=3306):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
    
    def __call__(self, command):
        return self.execute(command)
    
    def connect(self):
        try:
            self.conn = pymysql.connect(self.host, self.user, self.password, self.database, self.port)
            self.cursor = self.conn.cursor()
        except Exception as e:
            logging.error('Failed to connect to {}:{}'.format(self.host, self.port))
            logging.error(e)
            return False
        logging.info('Succeed to connect DB({}:{})'.format(self.host, self.port))
        return True

        
    def select(self, sql):
        logging.info(sql)
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            logging.error(sql)
            logging.error(e)

    def execute(self, *sql):
        try:
            for ss in sql:
                logging.info(ss)
                self.cursor.execute(ss)
            self.conn.commit()
        except Exception as e:
            logging.error(sql)
            logging.error(e)
            self.conn.rollback()
            return False
        return True
    
    def close(self):
        logging.info('Close DB({})'.format(self.host))
        self.cursor.close()
        self.conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, err_type, err_value, err_traceback):
        if err_type:
            return False
        else:
            self.close()
            return True

def main():
    sql = ''
  

if __name__ == '__main__':
    main()
        