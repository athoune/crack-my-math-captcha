poetry:
	poetry install --no-root

image:
	docker buildx build --platform linux/amd64,linux/arm64 -t crack-my-math-captcha .
