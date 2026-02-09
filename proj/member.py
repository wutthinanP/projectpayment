import sqlite3

conn = sqlite3.connect('member_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        member_id INTEGER,
        total_points INTEGER
    )
''')

def add_member(member_id):
    cursor.execute('SELECT * FROM members WHERE member_id = ?', (member_id,))
    existing_member = cursor.fetchone()

    if existing_member:
        print(f"สมาชิกรหัส {member_id} มีอยู่ในฐานข้อมูลแล้ว")
    else:
        cursor.execute('INSERT INTO members (member_id, total_points) VALUES (?, ?)', (member_id, 0))
        conn.commit()
        print(f"เพิ่มสมาชิกรหัส {member_id} เข้าสู่ระบบ")

def add_points(member_id, points):
    cursor.execute('SELECT total_points FROM members WHERE member_id = ?', (member_id,))
    result = cursor.fetchone()

    if result:
        current_points = result[0]
        new_total = current_points + points
        cursor.execute('UPDATE members SET total_points = ? WHERE member_id = ?', (new_total, member_id))
        conn.commit()
        print(f"เพิ่มเครดิตสะสม {points} ให้กับสมาชิกรหัส {member_id}")
    else:
        print("ไม่พบสมาชิกที่ระบุ")

def show_all_members():
    cursor.execute('SELECT * FROM members')
    all_members = cursor.fetchall()
    print("ข้อมูลสมาชิกทั้งหมด:")
    for member in all_members:
        print(f"รหัสสมาชิก: {member[1]}, คะแนนสะสม: {member[2]}")

# สมัครสมาชิกและเพิ่มคะแนนสะสม
memin=(input("สมัครสมาชิก : "))
code=(input("รหัสสมาชิก : "))
point=float(input("เพิ่มคะเเนน"))
add_member(memin)  # ตัวอย่าง: เพิ่มสมาชิกรหัส 123
add_points(code, point)  # ตัวอย่าง: เพิ่มเครดิตสะสม 10 ให้กับสมาชิกที่มีรหัส 123

show_all_members()

conn.close()