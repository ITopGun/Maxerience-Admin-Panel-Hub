# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
FROM public.ecr.aws/amazonlinux/amazonlinux:latest
RUN yum install python3.8.13 -y && curl -O https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && yum update -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN python manage.py collectstatic
RUN python manage.py migrate
RUN	python manage.py createsuperuser
CMD	python manage.py runserver
EXPOSE 8080
