.PHONY: install install-backend install-frontend dev backend frontend test benchmark plot setup-cron

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
	pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html:coverage_report

benchmark:
	@START=$$(date +%s); bash build.sh; END=$$(date +%s); \
	echo "$$(date +%Y-%m-%d) $$((END - START))" >> build_time_log.txt; \
	echo "Build time: $$((END - START))s logged to build_time_log.txt"

plot:
	gnuplot plot_build_times.gp
	@echo "Graph saved to build_time_graph.png"

setup-cron:
	@PROJ=$$(pwd); \
	(crontab -l 2>/dev/null; echo "0 9 * * 0 cd $$PROJ && gnuplot plot_build_times.gp") | crontab -
	@echo "Cron job added: gnuplot runs every Sunday at 9am"
