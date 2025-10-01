poetry:
	poetry install --no-root

image:
	docker build -t crack-my-math-captcha .
