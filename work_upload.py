# -*- coding: utf-8 -*-
# __author__ = '刘彬旭'
# 用于将工作记录转化为工作日志并提交到OM
import os
import sys
import requests
import subprocess


def get_today_work():
    git_diff_cmd = "git log -n 1 -p |grep '*'"
    # print(git_diff_cmd)
    output = subprocess.check_output(git_diff_cmd, shell=True)
    # print(output)
    diff_list = output.decode("utf-8")
    change_diff = []
    # print(diff_list)
    for diff in diff_list.split("\n"):
        if diff.startswith("+"):
            change_diff.append(diff.lstrip("+* "))
    return change_diff

def get_diff_work_tree(task="task.org"):
    # print("**** ")
    work_tree = parse_work_tree(task)
    change_diff = get_today_work()
    print(change_diff)

    for k1, v1 in work_tree.items():
        if len(v1.keys()) == 0:
            pass
        else:
            k1_str = k1.lstrip("*").lstrip(" ")
            
            for k2, v2 in v1.items():
                k2_str = k2.lstrip("*").lstrip(" ")
                if k2 in change_diff:
                    print("{}\t{}".format(k1_str, k2_str))
                if len(v2.keys()) == 0:
                    pass
                else:
                    for k3, v3 in v2.items():
                        k3_str = k3.lstrip("*").lstrip(" ")
                        if k3 in change_diff:
                            print("{}\t{}".format(k2_str, k3_str))
                        
                        if len(v3.keys()) == 0:
                            pass
                        else:
                            for k4, v4 in v3.items():
                                k4_str = k4.lstrip("*").lstrip(" ")
                                if k4 in change_diff:
                                    print("{}\t{}".format(k2_str, k4_str))
                                



def parse_work_tree(task_org):
    work_tree = dict()
    with open(task_org, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("* "):
                k1 = line.split("* ")[1]
                k2 = ""
                k3 = ""
                if k1 in work_tree:
                    pass
                else:
                    work_tree[k1] = {}
            if line.startswith("** "):
                k2 = line.split("** ")[1]
                if k2 in work_tree[k1]:
                    pass
                else:
                    work_tree[k1][k2] = {}
            if line.startswith("*** "):
                k3 = line.split("*** ")[1]
                # print(k1)
                # print(work_tree[k1])
                if k2 == "":
                    work_tree[k1][k2] = dict()
                if k3 in work_tree[k1][k2]:
                    pass
                else:
                    work_tree[k1][k2][k3] = {}
            if line.startswith("**** "):
                k4 = line.split("**** ")[1]
                if k2 == "":
                    work_tree[k1][k2] = dict()
                if k3 == "":
                    work_tree[k1][k2][k3] = dict()
                if k4 in work_tree[k1][k2][k3]:
                    pass
                else:
                    work_tree[k1][k2][k3][k4] = {}
    return work_tree

    
def request():
    # 登录请求
    response = requests.post('http://example.com/login', json={
    'username': 'yourusername',
    'password': 'yourpassword'
    })
    # if response.status_code == 200:
    # 获取返回的 token
    # token = response.json()['token']

    # # 在之后的请求中使用该 token 进行授权
    # response = requests.get('http://example.com/api/data', headers={
    #     'Authorization': f'Bearer {token}'
    # })
    # if response.status_code == 200:
    #     print(response.json())

if __name__ == "__main__":
    # print("aad ***")
    get_diff_work_tree()
