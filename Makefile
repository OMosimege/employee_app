up:
	@docker-compose up

upd:
	@docker-compose up -d

build:
	@docker-compose build

stop:
	@docker-compose stop

down:
	@docker-compose down

restart:
	@docker-compose restart

restartw:
	@docker-compose restart web

test:
	@docker-compose run --rm web coverage run --source='.' manage.py test $(app) --parallel

makemigrations:
	@docker-compose run --rm web python manage.py makemigrations

migrate:
	@docker-compose run --rm web python manage.py migrate

shell:
	@docker-compose run --rm web python manage.py shell

collectstatic:
	@docker-compose run --rm web python manage.py collectstatic

logs:
	@docker-compose logs -tf

