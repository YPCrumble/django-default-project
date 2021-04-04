broker_url = "amqp://admin:password@localhost/django_default_project"

task_always_eager = broker_url == ""

accept_content = ["json"]

worker_hijack_root_logger = False
