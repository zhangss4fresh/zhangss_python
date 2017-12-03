# coding:utf-8
# !/usr/bin/env python

import numpy as np


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

    print machine_array
    print time_array

    return machine_array, time_array


def main():
    # 从文件中读取参数(order_list:安排顺序, machine_array:机器分配, time_array:工序耗时)
    m, n, order_list, machine_array, time_array = get_parameters_from_txt()

    order_tuple = list()  # 从原始的order list 解析出 j-k 操作,即工件号-工序号
    order_machine = list()  # 从原始的order list 解析出 j-k 操作对应的机器编号
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
        order_machine.append(machine_array[gongjian_num, gongxu_num])
        print (gongjian_num, gongxu_num), machine_array[gongjian_num, gongxu_num]
    print order_machine

    # 将 j-k 操作 按所安排的机器编号归组,保存在assign_machine
    assign_machine = dict()
    for index, machine_num in enumerate(order_machine):
        the_tuple = order_tuple[index]
        if machine_num not in assign_machine:
            assign_machine[machine_num] = [the_tuple]
        else:
            assign_machine[machine_num].append(the_tuple)
    print assign_machine

    # 消耗时间计时
    time_cost = 0
    while True:
        for machine_id in assign_machine.keys():  # 遍历所有机器
            task_list = assign_machine[machine_id]
            if len(task_list) == 0:
                pass
            else:
                gongjian_num, gongxu_num = task_list[0]
                if gongxu_num == 0:
                    time_array[gongjian_num, gongxu_num] -= 1
                else:
                    if sum(time_array[gongjian_num, :gongxu_num]) == 0:
                        time_array[gongjian_num, gongxu_num] -= 1
                    else:
                        pass

                if time_array[gongjian_num, gongxu_num] == 0:
                    task_list = task_list[1:]
                    assign_machine[machine_id] = task_list

        # 所有任务时间都归0时结束
        if np.sum(time_array) == 0:
            break

        # 每迭代一次,耗时加一
        time_cost += 1
    print "cost min time is %d" % time_cost

    # 结果保存在jso.out
    out_path = 'jsp.out'
    with open(out_path, 'w') as out_file:
        out_file.write('%d' % time_cost)
        out_file.flush()


if __name__ == '__main__':
    main()
