dup:
		docker-compose up -d --build --remove-orphans
duu:
		docker-compose up -d
ddo:
		docker-compose down
dps:
		docker-compose ps -a
dlo: #make arg=silvertracker dlo
		docker-compose logs $(arg) -f
dba:
		docker exec -it silvertracker /bin/bash
dip:
		docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db
dmk:
		docker-compose run silvertracker sh -c "python manage.py makemigrations"
dmm:
		docker-compose run silvertracker sh -c "python manage.py migrate"
dmf: #make arg="financeiros 0027 --fake" dmf
		docker-compose run silvertracker sh -c "python manage.py migrate $(arg)"
gmg:
		git merge --no-ff master
dru:
		docker run
drb:
		docker run -it --rm silvertracker:1.0 bash
dtg:
		docker image tag  silvertracker:1.0 pinheiroras/silvertracker:1.0
dbu:
		docker build -t silvertracker:1.0  .
dpgr:
		pg_restore --host "172.25.0.2" --port "5432" --username "postgres" --dbname "silvertracker" --no-owner --no-privileges --no-tablespaces --no-comments --verbose /home/raimundo.sousa/Downloads/silvertracker_16022024.backup
dcp: #make dcp arg=raimundo.sousa
		docker-compose run silvertracker python manage.py changepassword $(arg)
