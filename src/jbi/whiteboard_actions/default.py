# Default actions below
from src.jbi import services


def default_action(data):
    print(data)
    svc = services.get_service("service")
    print(svc)


def default_helper():
    pass