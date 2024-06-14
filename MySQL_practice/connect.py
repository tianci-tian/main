import mysql.connector

def execute_sql(sql):
    try:
        # 连接数据库
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="mysql"
        )

        # 创建一个游标对象来执行 SQL 查询
        mycursor = mydb.cursor()

        # 执行 SQL 查询
        mycursor.execute(sql)

        # 如果是查询语句，获取查询结果并返回
        if sql.strip().upper().startswith("SELECT"):
            result = mycursor.fetchall()
            return result

        # 提交更改到数据库
        mydb.commit()

    except mysql.connector.Error as err:
        print("执行 SQL 出错:", err)

    finally:
        # 关闭游标和数据库连接
        mycursor.close()
        mydb.close()
'''
# 示例:
# 插入数据
execute_sql("INSERT INTO student VALUES (902,'张老大','男',1985,'计算机系','北京市海淀区')")
'''
# 查询数据
result = execute_sql("SELECT * FROM student")
for row in result:
    print(row)
#删除
#execute_sql("Delete from student where id = 902")