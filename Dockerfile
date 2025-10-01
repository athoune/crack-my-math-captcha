FROM python:3.13-alpine3.22

RUN adduser -D captcha
RUN pip install poetry
COPY . /home/captcha
WORKDIR /home/captcha
USER captcha
RUN poetry install --no-root
CMD ["/usr/local/bin/poetry", "run", "/home/captcha/server.py"]
