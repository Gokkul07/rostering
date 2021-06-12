
# [7 ,  8,  9,  10,  11, 12,  13,  14,   15,  16,  17,  18, 19,  20,   21,  22,  23, 00, 1,   2,  3,  4, 5, 6]
# [23, 48, 93, 120, 152, 266, 413, 375, 281, 236, 241, 326, 478, 630, 524, 280, 152, 87, 51, 33, 22, 11, 6, 8]

timing = ['07:00 : 16:00', '08:00 : 17:00', '09:00 : 18:00', '10:00 : 19:00', '11:00 : 20:00', '12:00 : 23:00',
          '13:00 : 22:00', '16:00 : 01:00', '17:00 : 02:00', '20:00 : 05:00', '22:00 : 07:00']

required_head_count = [23, 48, 93, 120, 152, 266, 413, 375, 281, 236, 241, 326, 478, 630, 524, 280, 152, 87, 51, 33, 22,
                       11, 6, 8]

till_now_hc = required_head_count[0]
shift_login_hc = []
shift_login_hc.append(required_head_count[0])

print(f'{timing[0]} = {required_head_count[0]}')
for i in range(9):
    if timing[i+1] in {'16:00 : 01:00', '17:00 : 02:00', '20:00 : 05:00', '22:00 : 07:00'}:
        if timing[i+1] in {'16:00 : 01:00'}:
            four_logout = shift_login_hc[0] + shift_login_hc[5]  #7 am and split shift logged in
            till_now_hc = till_now_hc - four_logout
            print(f'After 4pm shift logged out, remaining head count is {till_now_hc}')
        if timing[i+1] in {'17:00 : 02:00'}:
            five_logout = shift_login_hc[1]                          #8 am logged in
            till_now_hc = till_now_hc - five_logout
            print(f'After 5pm shift logged out, remaining head count is {till_now_hc}')
        if timing[i+1] in {'20:00 : 05:00'}:
            eight_logout = shift_login_hc[2] + shift_login_hc[3] + shift_login_hc[4]    #9, 10, 11 am logged in
            till_now_hc = till_now_hc - eight_logout
            till_now_hc = till_now_hc + shift_login_hc[5]  # adding split shift head count
            print(f'After 8pm shift logged out, remaining head count is {till_now_hc}')

            max_hc_in_peak_hours = max(required_head_count) #finding max hc, to spread hc among other login shifts
            balancing_peak_hours = max_hc_in_peak_hours - till_now_hc
            print(f'Need to spread {balancing_peak_hours} among three shifts 4pm 50%, 5pm 35%, 8pm 25%')

            #finding login count for 4pm shift
            print('16:00 : 01:00 = ' + str(int((balancing_peak_hours/100)*50)))
            four_login_count = int((balancing_peak_hours/100)*50)
            shift_login_hc.append(four_login_count)
            extra_hc_at_4 = shift_login_hc[1] + shift_login_hc[2] + shift_login_hc[3] + shift_login_hc[4] + \
                            shift_login_hc[6] + shift_login_hc[7]
            extra_hc_at_4 = extra_hc_at_4 - required_head_count[9]
            # print(f'Required head count at 4 is {required_head_count[9]}. Extra head count is {extra_hc_at_4}')

            # finding login count for 5pm shift
            print('17:00 : 02:00 = ' + str(int((balancing_peak_hours/100)*25)))
            five_login_count = int((balancing_peak_hours/100)*25)
            shift_login_hc.append(five_login_count)
            extra_hc_at_5 = shift_login_hc[2] + shift_login_hc[3] + shift_login_hc[4] + shift_login_hc[6] + \
                            shift_login_hc[7]
            extra_hc_at_5 = extra_hc_at_5 - required_head_count[10]
            # print(f'Required head count at 5 is {required_head_count[10]}. Extra head count is {extra_hc_at_5}')


            # finding login count for 8pm shift
            print('20:00 : 05:00 = ' + str(int((balancing_peak_hours/100)*25)))
            eight_login_count = int((balancing_peak_hours/100)*25) + 1
            shift_login_hc.append(eight_login_count)
            extra_hc_at_8 = shift_login_hc[5] + shift_login_hc[6] + shift_login_hc[7] + shift_login_hc[8] + \
                            shift_login_hc[9]
            extra_hc_at_8 = (extra_hc_at_8 - required_head_count[13]) + 1
            # print(f'Required head count at 8 is {required_head_count[13]}. Extra head count is {extra_hc_at_8}')



            # finding login count for 10pm shift
            print('22:00 : 07:00 = ' + str(int((balancing_peak_hours / 100) * 10)))
            nine_login_count = int((balancing_peak_hours / 100) * 10)
            shift_login_hc.append(nine_login_count)
            extra_hc_at_10 = shift_login_hc[5] + shift_login_hc[7] + shift_login_hc[8] + shift_login_hc[9] + \
                            shift_login_hc[10]
            extra_hc_at_10 = extra_hc_at_10 - required_head_count[15]
            # print(f'Required head count at 10 is {required_head_count[15]}. Extra head count is {extra_hc_at_10}')

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
present_hc.append(shift_login_hc[6] + shift_login_hc[5] + shift_login_hc[4] + shift_login_hc[3] + shift_login_hc[2] +
                  shift_login_hc[1] + shift_login_hc[0])
# 15
present_hc.append(shift_login_hc[6] + shift_login_hc[5] + shift_login_hc[4] + shift_login_hc[3] + shift_login_hc[2] +
                  shift_login_hc[1] + shift_login_hc[0])
# 16
present_hc.append(shift_login_hc[7] + shift_login_hc[6] + shift_login_hc[4] + shift_login_hc[3] + shift_login_hc[2] +
                  shift_login_hc[1])
# 17
present_hc.append(shift_login_hc[8] + shift_login_hc[7] + shift_login_hc[6] + shift_login_hc[4] + shift_login_hc[3] +
                  shift_login_hc[2])

# 18
present_hc.append(shift_login_hc[8] + shift_login_hc[7] + shift_login_hc[6] + shift_login_hc[4] + shift_login_hc[3])

# 19
present_hc.append(shift_login_hc[8] + shift_login_hc[7] + shift_login_hc[6] + shift_login_hc[5] + shift_login_hc[4])

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

print(present_hc)
# changing and push
