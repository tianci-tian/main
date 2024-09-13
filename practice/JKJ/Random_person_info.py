import random
import datetime
import openpyxl

# 常见姓氏列表
last_names = ['王', '李', '张', '刘', '陈', '杨', '黄', '赵', '吴', '周']

# 男性名字列表
male_first_names = ['伟', '俊', '勇', '毅', '峰', '磊', '洋', '辉', '强', '军']

# 女性名字列表
female_first_names = ['丽', '娜', '静', '慧', '颖', '雅', '婷', '雪', '悦', '怡']


def generate_random_name(gender):
    last_name = random.choice(last_names)
    if gender == '男':
        first_name = random.choice(male_first_names)
    else:
        first_name = random.choice(female_first_names)
    return last_name + first_name


def generate_random_birthday():
    # 获取当前年份
    current_year = datetime.datetime.now().year
    birth_year = random.randint(1920, current_year)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    return f'{birth_year}-{birth_month:02d}-{birth_day:02d}'


def generate_random_gender():
    return random.choice(['男', '女'])


# 省份列表
provinces = ['北京市', '上海市', '广东省', '江苏省', '浙江省']

# 城市和区的对应字典
cities_and_districts = {
    '北京市': ['东城区', '西城区', '朝阳区', '丰台区', '石景山区', '海淀区', '门头沟区', '房山区', '通州区',
               '顺义区', '昌平区', '大兴区', '怀柔区', '平谷区', '密云区', '延庆区'],
    '上海市': ['黄浦区', '徐汇区', '长宁区', '静安区', '普陀区', '虹口区', '杨浦区', '闵行区', '宝山区',
               '嘉定区', '浦东新区', '金山区', '松江区', '青浦区', '奉贤区', '崇明区'],
    '广东省': {
        '广州市': ['越秀区', '荔湾区', '海珠区', '天河区', '白云区', '黄埔区', '番禺区', '花都区', '南沙区',
                   '从化区', '增城区'],
        '深圳市': ['罗湖区', '福田区', '南山区', '宝安区', '龙岗区', '盐田区', '龙华区', '坪山区', '光明区'],
        '珠海市': ['香洲区', '斗门区', '金湾区']
    },
    '江苏省': {
        '南京市': ['玄武区', '秦淮区', '建邺区', '鼓楼区', '浦口区', '栖霞区', '雨花台区', '江宁区', '六合区',
                   '溧水区', '高淳区'],
        '苏州市': ['姑苏区', '虎丘区', '吴中区', '相城区', '吴江区', '常熟市', '张家港市', '昆山市', '太仓市'],
        '无锡市': ['锡山区', '惠山区', '滨湖区', '梁溪区', '新吴区']
    },
    '浙江省': {
        '杭州市': ['上城区', '下城区', '江干区', '拱墅区', '西湖区', '滨江区', '萧山区', '余杭区', '富阳区',
                   '临安区', '桐庐县', '淳安县', '建德市'],
        '宁波市': ['海曙区', '江北区', '北仑区', '镇海区', '鄞州区', '奉化区', '余姚市', '慈溪市', '象山县',
                   '宁海县'],
        '温州市': ['鹿城区', '龙湾区', '瓯海区', '洞头区', '瑞安市', '乐清市', '永嘉县', '平阳县', '苍南县',
                   '文成县', '泰顺县']
    }
}


def generate_random_address():
    province = random.choice(provinces)
    if province == '北京市':
        city = '北京市'
        district = random.choice(cities_and_districts['北京市'])
    elif province == '上海市':
        city = '上海市'
        district = random.choice(cities_and_districts['上海市'])
    else:
        city = random.choice(list(cities_and_districts[province].keys()))
        district = random.choice(cities_and_districts[province][city])
    street_number = random.randint(1, 1000)
    return f'{province}{city}{district}{street_number}号'


# 随机生成手机号码
def generate_random_phone_number():
    prefix = random.choice(['13', '15', '18'])
    number = ''.join(str(random.randint(0, 9)) for _ in range(8))
    return f'{prefix}{number}'


def generate_random_id_number(random_birthday):
    # 随机生成省份代码（前两位）
    province_code = str(random.randint(11, 99))

    # 随机生成城市代码（第3-4位）
    city_code = str(random.randint(10, 99))

    # 随机生成区县代码（第5-6位）
    district_code = str(random.randint(10, 99))

    # 获取当前年份
    current_year = datetime.datetime.now().year

    # 确保出生年份在合理范围内（1920年到当前年份）
    birth_year = str(random.randint(1920, current_year))

    # 随机生成出生月份（01-12）
    birth_month = str(random.randint(1, 12)).zfill(2)
    birth = generate_random_birthday()
    # 随机生成出生日期（01-28、30、31，排除特殊情况）
    birth_day = str(random.randint(1, 28)).zfill(2)

    # 随机生成顺序号（000-999）
    sequence_number = str(random.randint(0, 999)).zfill(3)
    ge_number = int(sequence_number)
    ge_number = ge_number % 10
    if ge_number % 2 == 1:
        sex = '男'
    else:
        sex = '女'

    # 计算校验码
    id_number_without_check_digit = province_code + city_code + district_code + random_birthday + sequence_number
    check_digit = calculate_check_digit(id_number_without_check_digit)

    return id_number_without_check_digit + check_digit , sex


def calculate_check_digit(id_number):
    # 加权因子
    weight_factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_values = "10X98765432"

    sum_result = 0
    for i in range(17):
        sum_result += int(id_number[i]) * weight_factors[i]

    remainder = sum_result % 11
    return check_code_values[remainder]


if __name__ == '__main__':
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(['姓名', '生日', '性别', '家庭住址', '手机号', '身份证号码'])
    for _ in range(1000):
        random_name = generate_random_name(generate_random_gender())
        random_birthday = generate_random_birthday()
        random_birthday_number = random_birthday.split('-')
        new_random_birthday = "".join(random_birthday_number)
        random_gender = generate_random_gender()
        random_address = generate_random_address()
        random_phone_number = generate_random_phone_number()
        random_id_number,sex = generate_random_id_number(new_random_birthday)
        sheet.append([random_name, random_birthday, sex , random_address, random_phone_number, random_id_number])
    workbook.save('random_data.xlsx')