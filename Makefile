.PHONY: install install-backend install-frontend dev backend frontend test

install: install-backend install-frontend

install-backend:
	pip install -r requirements.txt

install-frontend:
	cd frontend && npm install

dev:
	make -j2 backend frontend

backend:
	python3 app.py

frontend:
	cd frontend && npm run dev

test:
	pytest tests/ -v
