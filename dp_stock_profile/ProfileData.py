def PlanProfileDpStock(file_path, number):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip()
    first_data_line = lines[1].strip()

    data_fields = first_data_line.split(',')

    profile_id_field = data_fields[0].split(':')[0]
    iccid_field = data_fields[0].split(':')[1]

    new_lines = [header]

    for num in range(1, number + 1):
        profile_id = str(int(profile_id_field) + num).zfill(len(profile_id_field))
        iccid = str(int(iccid_field) + num).zfill(len(iccid_field))
        imsi = str(int(data_fields[1]) + num).zfill(len(data_fields[1]))
        ki = increment_hex(data_fields[2], num)
        opc = increment_hex(data_fields[3], num)
        msisdn = data_fields[4]
        busi_data = str(int(data_fields[5]) + num).zfill(len(data_fields[5]))
        qrcode = increment_qrcode(data_fields[6], num)

        new_line = f"{profile_id}:{iccid},{imsi},{ki},{opc},{msisdn},{busi_data},{qrcode}"
        new_lines.append(new_line)

    with open('D://桌面//QR-ESIMGO入库-20240628-Modified.txt', 'w') as file:
        for line in new_lines:
            file.write(line + '\n')

    # print(new_lines)


def increment_hex(hex_str, increment):
    hex_int = int(hex_str, 16)
    incremented_hex = hex_int + increment
    return f"{incremented_hex:X}".zfill(len(hex_str))


def increment_qrcode(qrcode_str, increment):
    parts = qrcode_str.split('$')
    last_part = parts[-1].split('-')

    if last_part[-1].isdigit():
        last_part[-1] = str(int(last_part[-1]) + increment).zfill(len(last_part[-1]))

    parts[-1] = '-'.join(last_part)
    return '$'.join(parts)


if __name__ == '__main__':
    PlanProfileDpStock(file_path='D://桌面//QR-ESIMGO入库-20240628.txt', number=3)
