from app import  db, psycopg2
import json


def get_columns(table):
    column = None
    try:
        # db.execute("SHOW columns FROM "+table)
        db.execute("SELECT column_name FROM information_schema.columns WHERE table_schema = 'public' AND table_name='"+table+"'")
        column = [row[0] for row in db.fetchall()]
    except (Exception, psycopg2.DatabaseError) as e:
        raise e
    else:
        return column


def get_all(table):
    column = get_columns(table)
    results = list()
    try:
        db.execute("SELECT * FROM "+table)
        rows = db.fetchall()
        for row in rows:
            results.append(dict(zip(column, row)))
    except (Exception, psycopg2.DatabaseError) as e:
        raise e
    else:
        return results


def get_by_id(table, field= None, value= None):
    column = get_columns(table)
    results = list()
    try:
        db.execute("SELECT * FROM "+table+" WHERE "+field+"=%s",(value,))
        rows = db.fetchall()
        for row in rows:
            results.append(dict(zip(column, row)))
    except (Exception, psycopg2.DatabaseError) as e:
        raise e
    else:
        return results