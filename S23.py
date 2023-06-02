import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='YU_oppdivide!20', database='menagerie')
cursor = conn.cursor()
select_query ="SELECT owner, COUNT(*) FROM pet GROUP BY owner;"

cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    owner, pet_count = row
    print(f"Owner: {owner}, Number of Pets: {pet_count}")
cursor.close()
conn.close()