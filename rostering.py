
# [7 ,  8,  9,  10,  11, 12,  13,  14,   15,  16,  17,  18, 19,  20,   21,  22,  23, 00, 1,   2,  3,  4, 5, 6]
# [23, 48, 93, 120, 152, 266, 413, 375, 281, 236, 241, 326, 478, 630, 524, 280, 152, 87, 51, 33, 22, 11, 6, 8]

timing = ['07:00 : 16:00', '08:00 : 17:00', '09:00 : 18:00', '10:00 : 19:00', '11:00 : 20:00', '12:00 : 00:00',
          '13:00 : 22:00', '15:00 : 00:00', '16:00 : 01:00', '17:00 : 02:00', '20:00 : 05:00', '22:00 : 07:00']

required_head_count = [23, 48, 93, 120, 152, 266, 413, 375, 281, 236, 241, 326, 478, 630, 524, 280, 152, 87, 51, 33, 22,
                       11, 6, 8]

till_now_hc = required_head_count[0]
shift_login_hc = []
shift_login_hc.append(required_head_count[0])

print(f'{timing[0]} = {required_head_count[0]}')
for i in range(timing.__len__()-1):
    if timing[i+1] in {'12:00 : 00:00', '13:00 : 22:00', '15:00 : 00:00', '16:00 : 01:00', '17:00 : 02:00',
                       '20:00 : 05:00', '22:00 : 07:00'}:

        # 12pm login
        if timing[i+1] in {'12:00 : 00:00'}:
            # finding login count for 12pm shift
            max_hc_in_peak_hours = max(required_head_count)  # finding max hc, to spread hc among other login shifts
            balancing_peak_hours = max_hc_in_peak_hours
            print(f'Spreading maximum required headcount {balancing_peak_hours} among following shifts 12pm 40%, 1pm 30%, 3pm 20%, 4pm 15%')

            print('12:00 : 00:00 = ' + str(int((balancing_peak_hours/100)*40)))
            twelve_login_count = int((balancing_peak_hours/100)*40)
            shift_login_hc.append(twelve_login_count)
            till_now_hc = till_now_hc + twelve_login_count
            print(f'so far total head count logged in: {till_now_hc}')

        # 1pm login
        if timing[i+1] in {'13:00 : 22:00'}:
            # finding login count for 1pm shift
            print('13:00 : 22:00 = ' + str(int((balancing_peak_hours/100)*30)))
            thirteen_login_count = int((balancing_peak_hours/100)*30)
            shift_login_hc.append(thirteen_login_count)
            till_now_hc = till_now_hc + thirteen_login_count
            print(f'so far total head count logged in: {till_now_hc}')

        # 3pm login
        if timing[i+1] in {'15:00 : 00:00'}:
            # finding login count for 1pm shift
            print('15:00 : 00:00 = ' + str(int((balancing_peak_hours/100)*20)))
            fifteen_login_count = int((balancing_peak_hours/100)*20)
            shift_login_hc.append(fifteen_login_count)
            till_now_hc = till_now_hc + fifteen_login_count
            print(f'so far total head count logged in: {till_now_hc}')

        #4pm shift
        if timing[i+1] in {'16:00 : 01:00'}:
            four_logout = shift_login_hc[0] + shift_login_hc[5]  #7 am and split shift logged in
            till_now_hc = till_now_hc - four_logout
            print(f'7am and split shift will log out at 16 pm, remaining head count will be {till_now_hc}')


            # shift_login_hc.append(four_login_count)
            print('16:00 : 01:00 = ' + str(int((balancing_peak_hours / 100) * 10)))
            sixteen_login_count = int((balancing_peak_hours/100)*10)
            shift_login_hc.append(sixteen_login_count)
            till_now_hc = till_now_hc + sixteen_login_count
            print(f'so far total head count logged in: {till_now_hc}')


        if timing[i+1] in {'17:00 : 02:00'}:
            five_logout = shift_login_hc[1]                          #8 am logged in
            till_now_hc = till_now_hc - five_logout
            # print(f'8am shift will log out at 17 pm')

            print('17:00 : 02:00 = ' + str(int((required_head_count[17] / 100) * 60)))
            seventeen_login_count = int((required_head_count[17] / 100) * 60)
            shift_login_hc.append(seventeen_login_count)
            till_now_hc = till_now_hc + seventeen_login_count
            print(f'8am shift will logout at 17pm and 17pm shift will login, remaining head count will be {till_now_hc}')


            # 6pm logout
            six_logout = shift_login_hc[2]                         #9am logged in
            till_now_hc = till_now_hc - six_logout
            print(f'9am shift will log out at  18 pm, remaining head count will be {till_now_hc}')

            # 7pm logout
            seven_logout = shift_login_hc[3]  # 10am logged in
            till_now_hc = till_now_hc - seven_logout
            print(f'10am shift will log out at  19 pm')

            #7pm split shift login
            split_login = shift_login_hc[5]  # 9am logged in
            till_now_hc = till_now_hc + split_login
            print(f'split shift will log in at 19 pm, remaining head count will be {till_now_hc}')



        if timing[i+1] in {'20:00 : 05:00'}:
            # 8pm logout
            eight_logout = shift_login_hc[4]  # 11am logged in
            till_now_hc = till_now_hc - eight_logout
            # print(f'11am shift will log out at  20 pm, remaining head count will be {till_now_hc}')

            required_head_count[17] #12am required hc
            print('20:00 : 05:00 = ' + str(int((required_head_count[17] / 100) * 30)))
            twenty_login_count = int((required_head_count[17] / 100) * 30)
            shift_login_hc.append(twenty_login_count)
            till_now_hc = till_now_hc + twenty_login_count
            print(f'11am shift will log out at  20 pm and 20 pm shift will login, remaining head count will be {till_now_hc}')

        if timing[i + 1] in {'22:00 : 07:00'}:
            #10pm logout
            ten_logout = shift_login_hc[6]  # 1pm logged in
            till_now_hc = till_now_hc - ten_logout
            # print(f'13 pm shift will log out at  22 pm, remaining head count will be {till_now_hc}')

            print('22:00 : 07:00 = ' + str(int((required_head_count[17] / 100) * 20)))
            twentytwo_login_count = int((required_head_count[17] / 100) * 20)
            shift_login_hc.append(twentytwo_login_count)
            till_now_hc = till_now_hc + twentytwo_login_count
            print(f'13pm shift will log out at  22 pm and 22 pm shift will login, remaining head count will be {till_now_hc}')


            #12am logout
            # split_3pm_logout = shift_login_hc[6] + shift_login_hc[5]
            till_now_hc = till_now_hc - shift_login_hc[5] - shift_login_hc[7]   # 12pm and 3pm logged in
            print(f'split shift and 3 pm shift will log out at  00 pm, remaining head count will be {till_now_hc}')

            #1am logout
            till_now_hc = till_now_hc - shift_login_hc[8]  # 4pm logged in
            print(f'16 pm shift will log out at  01 am, remaining head count will be {till_now_hc}')

            #2am logout
            till_now_hc = till_now_hc - shift_login_hc[9]  # 4pm logged in
            print(f'17 pm shift will log out at  02 am, remaining head count will be {till_now_hc}')

            #5am logout
            till_now_hc = till_now_hc - shift_login_hc[10]  # 4pm logged in
            print(f'20 pm shift will log out at  05 am, remaining head count will be {till_now_hc}')


    else:
        number = required_head_count[i + 1] - required_head_count[i]
        shift_login_hc.append(number)
        print(f'{timing[i + 1]} = ' + str(number))
        till_now_hc = till_now_hc + number


present_hc = []
# 7
present_hc.append(shift_login_hc[0])
# 8
present_hc.append(shift_login_hc[1] + shift_login_hc[0])
# 9
present_hc.append(shift_login_hc[2] + shift_login_hc[1] + shift_login_hc[0])
# 10
present_hc.append(shift_login_hc[3] + shift_login_hc[2] + shift_login_hc[1] + shift_login_hc[0])
# 11
present_hc.append(shift_login_hc[4] + shift_login_hc[3] + shift_login_hc[2] + shift_login_hc[1] + shift_login_hc[0])
# 12
present_hc.append(shift_login_hc[5] + shift_login_hc[4] + shift_login_hc[3] + shift_login_hc[2] + shift_login_hc[1] +
                  shift_login_hc[0])
# 13
present_hc.append(shift_login_hc[6] + shift_login_hc[5] + shift_login_hc[4] + shift_login_hc[3] + shift_login_hc[2] +
                  shift_login_hc[1] + shift_login_hc[0])
# 14
present_hc.append( shift_login_hc[7] + shift_login_hc[6] + shift_login_hc[5] + shift_login_hc[4] + shift_login_hc[3] + shift_login_hc[2] +
                  shift_login_hc[1] + shift_login_hc[0])
# 15
present_hc.append(shift_login_hc[0] + shift_login_hc[1] + shift_login_hc[2] + shift_login_hc[3] + shift_login_hc[4] +
                  shift_login_hc[5] + shift_login_hc[6] + shift_login_hc[7] + shift_login_hc[8])
# 16
present_hc.append(shift_login_hc[1] + shift_login_hc[2] + shift_login_hc[3] + shift_login_hc[4] + shift_login_hc[6] +
                  shift_login_hc[7] + shift_login_hc[8] + shift_login_hc[9])
# 17
present_hc.append(shift_login_hc[2] + shift_login_hc[3] + shift_login_hc[4] +
                  shift_login_hc[6] + shift_login_hc[7] + shift_login_hc[8] + shift_login_hc[9] + shift_login_hc[10])

# 18
present_hc.append(shift_login_hc[3] + shift_login_hc[4] + shift_login_hc[6] + shift_login_hc[7] + shift_login_hc[8] +
                  shift_login_hc[9] + shift_login_hc[10])

# 19
present_hc.append(shift_login_hc[4] + shift_login_hc[5] + shift_login_hc[6] + shift_login_hc[7] + shift_login_hc[8] +
                  shift_login_hc[9] + shift_login_hc[10])

# 20
present_hc.append(shift_login_hc[9] + shift_login_hc[8] + shift_login_hc[7] + shift_login_hc[6] + shift_login_hc[5])

# 21
present_hc.append(shift_login_hc[9] + shift_login_hc[8] + shift_login_hc[7] + shift_login_hc[6] + shift_login_hc[5])

# 22
present_hc.append(shift_login_hc[9] + shift_login_hc[8] + shift_login_hc[7] + shift_login_hc[5] +
                  shift_login_hc[10])

# 23
present_hc.append(shift_login_hc[9] + shift_login_hc[8] + shift_login_hc[7] + shift_login_hc[5] +
                  shift_login_hc[10])

# 00
present_hc.append(shift_login_hc[9] + shift_login_hc[8] + shift_login_hc[7] +
                  shift_login_hc[10])

# 01
present_hc.append(shift_login_hc[9] + shift_login_hc[8] + shift_login_hc[10])

# 02
present_hc.append(shift_login_hc[9] + shift_login_hc[10])

# 03
present_hc.append(shift_login_hc[9] + shift_login_hc[10])

# 04
present_hc.append(shift_login_hc[9] + shift_login_hc[10])

# 05
present_hc.append(shift_login_hc[10])

# 06
present_hc.append(shift_login_hc[10])

print('Required head count')
print(required_head_count)
print('present head count')
print(present_hc)
# changing and push
