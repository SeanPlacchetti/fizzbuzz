
echo "Setting up Postgres Database:"
# See if user exists
# from: http://stackoverflow.com/questions/8546759/how-to-check-if-a-postgres-user-exists
if psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='fizzbuzzuser'" | grep -q 1; then
    echo "User exists."
else
    echo "Creating user."
    psql -c "CREATE USER \"fizzbuzzuser\" WITH ENCRYPTED PASSWORD 'fizzbuzzpassword'"
fi

# See if db exists
# from: http://stackoverflow.com/questions/14549270/check-if-database-exists-in-postgresql-using-shell
if psql -lqt | cut -d \| -f 1 | grep -w fizzbuzz; then
    echo "Database exists."
else
    echo "Creating database"
    psql -c "CREATE DATABASE fizzbuzz ENCODING 'UTF8' OWNER fizzbuzzuser TEMPLATE template0"
    psql -c 'GRANT ALL PRIVILEGES ON DATABASE fizzbuzz to fizzbuzzuser'
fi

echo "Finished setting up database"
