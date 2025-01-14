list:
	@echo "Available commands:"
	@echo "up - Start the project"
	@echo "upd - Start the project in background"
	@echo "build - Build the project"
	@echo "stop - Stop the project"
	@echo "down - Stop and remove the project"
	@echo "restart - Restart the project"
	@echo "make-migrations - Create new migrations based on the changes you have made to your models"
	@echo "migrate - Apply migrations to your database"
	@echo "shell - Run the Python shell"
	@echo "logs - Show logs"
	@echo "create-super-user - Create a superuser"
	@echo "docker-stop-all - Stop all running containers"
	@echo "load-fixtures - Load fixtures"
	@echo "test - Run tests"
	@echo "dev-quick-install - Run all the necessary commands to start the project"

up:
	@docker compose up

upd:
	@docker compose up -d

build:
	@docker compose build

stop:
	@docker compose stop

down:
	@docker compose down

restart:
	@docker compose restart

make-migrations:
	@docker compose run --rm web python manage.py makemigrations

migrate:
	@docker compose run --rm web python manage.py migrate

shell:
	@docker compose run --rm web python manage.py shell

logs:
	@docker compose logs -tf

create-super-user:
	@docker compose run --rm web python manage.py createsuperuser

docker-stop-all:
	docker stop `docker ps -q`
	docker ps

test:
	@docker compose run --rm web python manage.py test

dev-quick-install:
	@make migrate
	@make load-fixtures
	echo "Creating superuser"
	@make create-super-user
