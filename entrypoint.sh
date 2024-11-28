#!/usr/bin/env bash

airflow db upgrade
airflow users create -r Admin -u admin -p admin -f Air -l Flow -e admin@example.com
airflow webserver