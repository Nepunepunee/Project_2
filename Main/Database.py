import psycopg2
from Db_pass import *
password = get_pass()


def database_command(command):
    connection = psycopg2.connect("dbname='game' user='postgres' host='localhost' password='"+password+"'")
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
def database_fetch(command):
    connection = psycopg2.connect("dbname='game' user='postgres' host='localhost' password='"+password+"'")
    cursor = connection.cursor()

    cursor.execute(command)
    connection.commit()

    result = None
    try:
        result = cursor.rowcount
    except psycopg2.ProgrammingError:
        pass
    cursor.close()
    connection.close()

    return result

def check_existing_names(name):   #checks if user exists in scoreboard else returns an empty
        query = database_command("SELECT Name FROM score WHERE Name = {}".format(name))
        return query.rowcount

def insert_new_score(name, score):
    query = database_fetch("Select * FROM score Where name = {}".format("'"+name+"'"))
    if(query == 0):
        database_command("INSERT INTO score (name, score) VALUES({},{})".format("'"+name+"'", score))

def save_state(state,player,x1,y1,x2=None,y2=None,x3=None,y3=None,damage_x1=None,damage__y1=None,damage_x2=None,damage__y2=None,damage_x3=None,damage__y3=None):
    database_command("INSERT INTO state VALUES({}, {},{},{},{},{},{},{},{},{},{},{},{},{})".format(state, player, x1, y1, x2, y2, x3, y3, damage_x1, damage__y1, damage_x2, damage__y2, damage_x3, damage__y3))

def get_state(state):
    database_command("SELECT * FROM state WHERE State={}".format(state))

def get_player(name):
    database_command("SELECT * FROM score WHERE Name={}".format(name))

def update_score(name, score):
    database_command("UPDATE score SET Score={} WHERE Name={}".format(score, name))

def Get_top():
    result = database_command("SELECT * FROM score ORDER BY Score DESC LIMIT 10 ")
    return result