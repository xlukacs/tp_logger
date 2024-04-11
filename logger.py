import psycopg2
from datetime import datetime


class Logger:
    def generate_log(self, event, value, cron):
        now = datetime.now()
        formatted_now = now.strftime('%Y-%m-%d %H-%M-%S')
        return event + ':' + value + ":" + cron + ":" + formatted_now

    def insert_to_db(self, event, log_value, cron):
        try:
            connection = psycopg2.connect   (
                                                user="postgres",
                                                password="toor",
                                                host="127.0.0.1",
                                                port="5432",
                                                database="catbase_logger"
                                            )

            cursor = connection.cursor()
            querry = "INSERT INTO logs(event, value, cron) VALUES (%s, %s, %s)"    
            data = (str(event), str(log_value), str(cron))

            cursor.execute(querry, data)
            connection.commit()

            if(cursor.rowcount > 0):
                print("Log inserted successfully...")
            else:
                print("Logging failed...")
        except(Exception, psycopg2.Error) as Error:
            print("An error occured: ", Error)

        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def saveLog(self, log):
        with open('logs.txt', 'a') as File:
            File.write(log)


    def logDB(self, event, log_value, cron):
        log = self.generate_log(event, log_value, cron)
        self.saveLog(log)
        self.insert_to_db(event, log_value, cron)