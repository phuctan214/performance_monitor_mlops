#!/usr/bin/env python3

import argparse
import os
import logging
import subprocess

import pandas as pd


# suppress SettingWithCopyWarning: warning
pd.options.mode.chained_assignment = None


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )


def check_docker_installation():
    logging.info("Check docker version")
    docker_version_result = os.system("docker -v")

    if docker_version_result:
        exit("Docker was not found. Try to install it with https://www.docker.com")


def run_docker_compose():
    logging.info("Run docker compose")
    run_script(cmd=["docker", "compose", "up", "-d"], wait=True)


def run_script(cmd: list, wait: bool) -> None:
    logging.info("Run %s", ' '.join(cmd))
    script_process = subprocess.Popen(' '.join(cmd), stdout=subprocess.PIPE, shell=True)

    if wait:
        script_process.wait()

        if script_process.returncode != 0:
            exit(script_process.returncode)


def send_data_requests():
    os.system("scripts/example_run_request.py")


def stop_docker_compose():
    os.system("docker compose down")


def main():
    setup_logger()
    check_docker_installation()
    run_docker_compose()
    send_data_requests()


if __name__ == "__main__":
    main()
