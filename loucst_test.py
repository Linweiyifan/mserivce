from locust import HttpLocust, TaskSet, task, between


class UserBehavior(TaskSet): # 任务列表类
    @task # task装饰器的内容将被定义为任务
    def my_task(self):
        self.client.get("/api")


class MyWebUser(HttpLocust):
    host = "http://127.0.0.1:5000"  # 设置请求地址以及端口.可选
    task_set = UserBehavior     # 设置行为,必选
    wait_time = between(1, 3) # 设置等待时间,必选

