import sqlite3
sum=0
temp=0
con = sqlite3.connect('A_database.db')
cur = con.cursor()
#cur.execute("CREATE TABLE total_profit (pr_id INTEGER PRIMARY KEY,pr_month REAL,pr_monthly TEXT,pr_profit REAL)");
#cur.execute(f"INSERT INTO total_profit(pr_month,pr_monthly,pr_profit) VALUES('November','{temp}','{temp}')");

cur.execute("UPDATE total_profit SET pr_month = ?, pr_monthly = ?, pr_profit = ?", ('November', temp, temp))
con.commit()
cursor=cur.execute("SELECT * FROM total_profit");
for row in cursor:
    print(row[3])
    #sum=sum+row[1]
print(sum)
con.close()
