run:
	API_KEY="fb855f761ec376f0412eb81bb4a0b4bb" \
	DB_HOST="localhost" \
	DB_PORT="27017" \
	DB_USERNAME="erikrios" \
	DB_PASSWORD="supersecretpassword" \
	uvicorn main:app --port 8000 --reload

gen-venv:
	python3 -m venv venv

rm-venv:
	rm -rf venv

install-dep:
	pip install -r requirements.txt