poetry:
	poetry install --no-root

docker-image:
	docker buildx build \
		--platform linux/amd64,linux/arm64 \
		--load \
		--tag crack-my-math-captcha .

docker-image-native:
	docker buildx build \
		--tag crack-my-math-captcha .
docker-test:
	docker run -t --rm crack-my-math-captcha ./venv/bin/python -m pytest -p no:cacheprovider .

test:
	poetry run pytest .
