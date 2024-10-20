"""
prefect deployment build \
	src/flow/f_04_forloop_submit.py:f_04_forloop_submit \
	-n docker \
	-p test \
	-q docker-deplymet \
  -sb "github/github-prefect-demo" \
  -ib "docker-container/demo-docker-container" \
  -a
"""
import pandas as pd
from prefect import flow, task

@task
def generate_some_str() -> str:
    return "HELLO"

@task
def do_something(some_str: str) -> list[str]:
    return list(some_str)

@task
def print_something_separately(something: str | list) -> None:
    print("======")
    print(something)
    print("======")

@flow(name="f_04_forloop_submit")
def f_04_forloop_submit() -> None:
    some_str = generate_some_str()
    result = do_something(some_str)
    for each_str in result:
        print_something_separately.submit(each_str)

if __name__ == "__main__":
    from prefect_github import GitHubRepository
    f_04_forloop_submit()

    # f_04_forloop_submit.from_source(
    #     source=GitHubRepository.load("github-prefect-demo"),
    #     entrypoint="src/flow/f_04_forloop_submit.py:f_04_forloop_submit",
    # ).deploy(
    #     name="test-deploy",
    #     tags=["test", "project_4"],
    #     work_pool_name="test-docker",
    #     job_variables=dict(pull_policy="Never"),
    #     # parameters=dict(name="Marvin"),
    #     cron="*/30 0-8,9-15,16-23 * * *"
    # )
