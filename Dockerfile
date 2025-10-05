FROM --platform=$BUILDPLATFORM alpine:3.22 AS dev
ARG BUILDPLATFORM

RUN adduser -D captcha
RUN apk update && apk add --no-cache python3 py3-pip
COPY . /home/captcha
WORKDIR /home/captcha
USER captcha
RUN python3 -m venv venv && ./venv/bin/python -m pip install poetry
RUN ./venv/bin/python -m poetry install --no-root --no-cache
RUN ./venv/bin/python -m poetry run pytest --cov -p no:cacheprovider .


FROM --platform=$BUILDPLATFORM alpine:3.22
ARG BUILDPLATFORM

RUN adduser -D captcha
RUN apk update && apk add --no-cache python3
WORKDIR /home/captcha
USER captcha
COPY --from=dev /home/captcha /home/captcha
RUN ./venv/bin/python -m poetry install --no-root --without=dev --no-cache

ENV PLAUSIBLE_DOMAIN=""
ENV CAPTCHA_DOMAIN=""
EXPOSE 8080

CMD ["/usr/local/bin/poetry", "run", "/home/captcha/server.py"]
