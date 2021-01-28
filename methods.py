import config
import sqlite3
from config import db_name


def commands(commands1, bot_username=config.bot_username):
    commands1 = [
        rf'^\/({i})+(\@{bot_username}\w*(_\w+)*)?([ \f\n\r\t\v\u00A0\u2028\u2029].*)?$' for i in commands1
    ]
    return '|'.join([i for i in commands1])


def commandList(commands, bot_username=config.bot_username):
    commandsCopy = commands.copy()
    for i in commands:
        commandsCopy.append(i + "@" + bot_username)
    return commandsCopy


def registered(tid):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT 1
            FROM citizens
            where tid = :tid;""", {"tid": tid}
                       )
        result = cursor.fetchall()
        if not result:
            return False
        else:
            return True


def create_user(tid, status=0, alias=""):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO citizens (tid, status, alias)
        VALUES (:tid, :status, :alias)
        """, {"tid": tid, "status": status, "alias": alias})


def update_status(tid, status):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE citizens
        set status = :status
        WHERE tid = :tid
        """, {"tid": tid, "status": status})
        conn.commit()


def update_alias(tid, alias):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE citizens
        set alias = :alias
        WHERE tid = :tid
        """, {"tid": tid, "alias": alias})
        conn.commit()


async def update_alias_group(tid, group_id, client):
    await client.edit_admin(group_id,
                            tid,
                            change_info=True,
                            delete_messages=None,
                            ban_users=None,
                            invite_users=None,
                            pin_messages=None,
                            add_admins=None,
                            manage_call=True,
                            title=get_alias(tid)
                            )


def update_rp(tid, rp):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE citizens
        set rp = :rp
        WHERE tid = :tid
        """, {"tid": tid, "rp": rp})
        conn.commit()


def update_balance(tid, balance):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE citizens
        set balance = :balance
        WHERE tid = :tid
        """, {"tid": tid, "balance": balance})
        conn.commit()


def update_married(tid, married):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""UPDATE citizens
        set married = :married
        WHERE tid = :tid
        """, {"tid": tid, "married": married})
        conn.commit()


def get_status(tid):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT status
        FROM citizens
        where tid = :tid;
        """, {"tid": tid})
        return cursor.fetchall()[0][0]


def get_alias(tid):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT alias
        FROM citizens
        where tid = :tid;
        """, {"tid": tid})
        return cursor.fetchall()[0][0]


def get_married(tid):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT married
        FROM citizens
        where tid = :tid;
        """, {"tid": tid})
        return cursor.fetchall()[0][0]


def get_marry_list(tid):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT married
        FROM marry
        where tid = :tid;
        """, {"tid": tid})
        return cursor.fetchall()[0]


def get_rp(tid):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT rp
        FROM citizens
        where tid = :tid;
        """, {"tid": tid})
        return cursor.fetchall()[0][0]


def get_balance(tid):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT balance
        FROM citizens
        where tid = :tid;
        """, {"tid": tid})
        return cursor.fetchall()[0][0]


def get_all_citizens():
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT *
        FROM citizens
        WHERE status >= 1
        """)
        return cursor.fetchall()


def change_rp(tid, value):
    update_rp(tid, get_rp(tid) + value)


def change_balance(tid, value):
    if value < 0 and get_balance(tid) < abs(value):
        return False
    else:
        update_balance(tid, get_balance(tid) + value)
        return True


def can_change_balance(tid, value):
    return False if get_balance(tid) < abs(value) else True


def create():
    with sqlite3.connect("kyy.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS citizens(
                id INTEGER AUTO_INCREMENT,
                tid INTEGER NOT NULL,
                alias VARCHAR(16),
                rp INTEGER NOT NULL default(100),
                balance INTEGER NOT NULL default(1000),
                status INTEGER NOT NULL default(0),
                married TINYINT NOT NULL default(0),
                PRIMARY KEY (tid)
                )'''
        )


update_status(549729560, 3)
# (1, 549729560, 'ADMIN', 9601, 711300, 2, 0)
# tid 1, alias 2
