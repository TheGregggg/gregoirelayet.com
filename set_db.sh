docker exec gregoirelayetcom-db-1 psql -U gerg_db_admin -d postgres -f /var/lib/postgresql/sql_script/create_db.sql
docker exec gregoirelayetcom-db-1 psql -U gerg -d gregoirelayet.com -f /var/lib/postgresql/sql_script/setup_db.sql
docker exec gregoirelayetcom-db-1 psql -U gerg -d test_gregoirelayet.com -f /var/lib/postgresql/sql_script/setup_test_db.sql