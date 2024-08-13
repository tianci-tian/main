# MySQL
+ 增 Insert
+ 删 Delete
+ 改 Updata
+ 查 Select

## AS
作用：重命名

```sql```
Select 原名 AS 别名 From 表名;

## DISTINCT
作用：去重复



## LIKE函数
作用：在一个字符型字段列中检索包含对应字串的
+ % 包含零个或多个字符的任意字符串
+ _ 任何单个字符
+ [] 指定范围或集合中任何单个字符
+ (*) 等同DOS命令中的通配符,代表多个字符
* ? 等同DOS命令中的通配符,代表单个字符

<font color = 'red'> 做字符串包含一个的查询时，最好使用'%',不用'*',用'*'的时候只用在开头或者只有结尾时,而不能两端全由'*'代替任何字符</font>

举例：删除手机号包含40的手机号信息

```SQL```
Delete 
From `table_name
Where phone_number LIKE '%40%';

