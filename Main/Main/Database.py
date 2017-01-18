import psycopg2

class database:
    def database_command(self, command):
        connection = psycopg2.connect("dbname=**** user=****")
        cursor = connection.cursor()

        cursor.execute(command)
        connection.commit()

        result = None
        try:
            result = cursor.fetchall()
        except psycopg2.ProgrammingError:
            pass
        cursor.close()
        connection.close()

        return result

    def check_existing_names(self, name):   #checks if user exists in scoreboard else returns an empty
        self.query = self.database_command("SELECT Name FROM score WHERE Name = {}".format(name))
        return self.query.rowcount

    def insert_new_score(self, name, score):
        self.database_command("INSERT INTO score VALUES({}, {})".format(name, score))

    ## def save_state(self, state,x1,y1,x2,y2,):#needs more vars since this saves every single variable from the current game

    def get_player(self,name):
        self.database_command("SELECT * FROM score WHERE Name={}}".format(name))

    def update_score(self, name, score):
        self.database_command("UPDATE score SET Score={} WHERE Name={}".format(score, name))

