from locust import User, TaskSet, task, between
from time import time
#使用@task来声明任务，执行的时候，my_task_3不执行
class MyTaskSet(TaskSet):

    # TaskSet相当于下面所有task的大脑
    @task(1)  # 声明任务
    def task1(self):
        print("执行task1")

    @task(5)
    def task2(self):
        print("执行task2")

    def my_task_3(self):
        print("执行task3")


class WebUser(User):
    task_set = MyTaskSet

    weight = 5
    wait_time = between(5, 15)
    host = ""  # 域名host