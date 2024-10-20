import time

from airflow.notifications.basenotifier import BaseNotifier


def send_message(title, message) -> None:
    print(title)
    print(message)
    print("Message sent.")
    with open(f"/tmp/test_notification_message_{time.time_ns()}.txt", "w") as f:
        f.write(f"{title}\n=====\n{message}\n")

class MyNotifier(BaseNotifier):
    template_fields = ("message",)

    def __init__(self, message):
        self.message = message

    def notify(self, context):
        # Send notification here, below is an example
        title = f"Task {context['task_instance'].task_id} failed"
        send_message(title, self.message)
