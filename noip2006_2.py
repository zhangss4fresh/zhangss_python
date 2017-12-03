# coding:utf-8
# !/usr/bin/env python

import numpy as np

max_time = 100

# key 为机器号
time_dict = {1: [0] * max_time,
             2: [0] * max_time}


# 从文件中读取参数
def get_parameters_from_txt(txt_path='jsp.in'):
    parameter_list = list()
    for line in open(txt_path):
        split_list = line.split(' ')
        for i in range(len(split_list)):
            split_list[i] = int(split_list[i])
        parameter_list.extend(split_list)

    m, n = parameter_list[0], parameter_list[1]  # 机器数,工件数
    order_list = parameter_list[2:2 + m * n]  # m * n 为安排顺序的长度
    machine_list = parameter_list[-2 * m * n:-m * n]
    time_list = parameter_list[-m * n:]

    if len(parameter_list) != 2 + m * n + m * n + m * n:
        print "error: please check parameter number!"

    machine_array, time_array = deal_parameters(machine_list, time_list)
    return m, n, order_list, machine_array, time_array


# 将list转为二维数组,方便按二维索引取值
def deal_parameters(machine_list, time_list):
    machine_array = np.array(machine_list, dtype='int32').reshape(-1, 2)
    time_array = np.array(time_list, dtype='int32').reshape(-1, 2)

    # print machine_array
    # print time_array

    return machine_array, time_array


# 添加工序 注意: 工件和工序下标均从0开始
def add_gongxu(order_list, machine_array, m, n):
    order_tuple = list()  # 从原始的order list 解析出 j-k 操作,即工件号-工序号
    flag_array = np.zeros([n, m], dtype='int32')  # 解析出 j-k 操作 依赖的临时标识
    for gongjian_num in order_list:
        gongjian_num -= 1

        gongxu_num = 0
        for index, flag in enumerate(flag_array[gongjian_num, :]):
            if int(flag) == 0:
                flag_array[gongjian_num, index] = 1
                gongxu_num = index
                break
            else:
                pass
        order_tuple.append((gongjian_num, gongxu_num))
        print '工件:%d,工序:%d,机器号:%d' % (gongjian_num, gongxu_num, machine_array[gongjian_num, gongxu_num])

    return order_tuple


# 结果保存
def write_result(time_cost):
    # 结果保存在jso.out
    out_path = 'jsp.out'
    with open(out_path, 'w') as out_file:
        out_file.write('%d' % time_cost)
        out_file.flush()


def find_perfect(machine, time, start_time):
    time_list = time_dict[machine]
    for i in range(start_time, len(time_list) - time):
        if time_list[i:i+time] == [0] * time:
            return i


def set_one(machine, time_perfect, time, x, y):
    time_list = time_dict[machine]
    time_list[time_perfect: time_perfect + time] = [(x, y)] * time

    time_dict[machine] = time_list


def find_end(gongjian, gongxu, machine):
    time_list = time_dict[machine]
    end_time = 0
    for index, tuple_ in enumerate(time_list):
        if tuple_ == (gongjian, gongxu):
            end_time = index
    return end_time


def final_time(list_):
    time = 0
    for index, tuple_ in enumerate(list_):
        if tuple_ != 0:
            time = index

    return time


def main():
    # 从文件中读取参数(order_list:安排顺序, machine_array:机器分配, time_array:工序耗时)
    m, n, order_list, machine_array, time_array = get_parameters_from_txt()

    order_tuple = add_gongxu(order_list, machine_array, m, n)

    for (x, y) in order_tuple:  # x:工件, y:工序
        if y == 0:
            machine = machine_array[x, y]
            time = time_array[x, y]
            print 'machine:%d, time:%d' % (machine, time)
            time_perfect = find_perfect(machine, time, 0)
            set_one(machine, time_perfect, time, x, y)
        else:
            machine = machine_array[x, y]
            time = time_array[x, y]
            print 'machine:%d, time:%d' % (machine, time)
            time_end = find_end(x, y-1, machine)
            time_perfect = find_perfect(machine, time, time_end + 1)
            set_one(machine, time_perfect, time, x, y)

    t_max = 0
    for i in range(1, m+1):
        tmp = final_time(time_dict[i])
        if tmp > t_max:
            t_max = tmp

    time_cost = t_max + 1
    print "cost min time is %d" % time_cost

    write_result(time_cost)

if __name__ == '__main__':
    main()
