def IccidListContent(iccid, maxnumber):
    list = []
    for i in range(maxnumber):
        list.append(str(iccid))  # 将数字转换为字符串并添加
        iccid += 1
    print(list)

IccidListContent(24052400000000003299, 2000)