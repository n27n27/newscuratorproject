import bcrypt
import sqlite3

def connect_db():
    conn = sqlite3.connect('log_in.db', isolation_level=None)

    c = conn.cursor()

    table_exist = c.execute(f'SELECT * from sqlite_master WHERE type="table" and name="user_data"').fetchall()
    if table_exist:
        pass
    else:   
        c.execute("CREATE TABLE user_data \
            (id text PRIMARY KEY, name text, passwd text)")
    return conn, c

def load_data_from_db():
    conn, c = connect_db()
    c.execute("SELECT * FROM user_data")
    result = c.fetchall()
    conn.close()
    return result

def pw_to_hs(pw):
    bt_pw = pw.encode()
    hashed_pw = bcrypt.hashpw(password=bt_pw, salt=bcrypt.gensalt())
    return hashed_pw.decode('utf-8')

def sign_in(id, name, hs_pw):
    conn, c = connect_db()
    login_db = load_data_from_db()
    for each in login_db:
        if each[0] == id:
            print("이미 존재하는 id 입니다.")
            return
    
    c.execute(f"INSERT INTO user_data \
        VALUES('{id}', '{name}', '{hs_pw}')")

    conn.close()

def check_pw(id, pw, hs_pw):
    bt_pw = pw.encode()
    bt_hs_pw = hs_pw.encode()
    is_correct = bcrypt.checkpw(bt_pw, bt_hs_pw)
    return is_correct

def log_in(id, pw):
    conn, c = connect_db()
    login_db = load_data_from_db()
    for each in login_db:
        if each[0] == id:
            cur_user = each
            conn.close()
            break

    try:
        correct_pw = check_pw(id, pw, cur_user[2])
        if correct_pw:
            conn.close()
            return correct_pw
        else:
            print("패스워드가 일치하지 않습니다.")
            conn.close()
            return
    except:
        conn.close()
        print("id 정보가 없습니다.")

def delete_user(id, pw):
    conn, c = connect_db()
    # correct_pw = check_pw(id, pw, )
    # c.execute('DELETE FROM user_data WHERE id=:id', {'id': id})