#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable

if [ "$DJANGO_SUPERUSER_USERNAME" ]
then
    python manage.py createsuperuser \
        --noinput \
        --username $DJANGO_SUPERUSER_USERNAME  \
        --email $DJANGO_SUPERUSER_EMAIL
fi

python manage.py add_sample

exec "$@"




# if ! [[ "18.04 20.04 22.04" == *"$(lsb_release -rs)"* ]];
# then
#     echo "Ubuntu $(lsb_release -rs) is not currently supported.";
#     exit;
# fi

# sudo su
# curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list

# exit
# sudo apt-get update
# sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18
# # optional: for bcp and sqlcmd
# sudo ACCEPT_EULA=Y apt-get install -y mssql-tools18
# echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc
# source ~/.bashrc
# # optional: for unixODBC development headers
# sudo apt-get install -y unixodbc-dev