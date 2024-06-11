CREATE ROLE gerg WITH LOGIN PASSWORD 'gerg_pass';
GRANT CONNECT ON DATABASE "postgres" TO gerg;

--- Django user recommendation
ALTER ROLE gerg SET client_encoding TO 'utf8';
ALTER ROLE gerg SET default_transaction_isolation TO 'read committed';
ALTER ROLE gerg SET timezone TO 'UTC';

CREATE DATABASE "gregoirelayet.com";   
GRANT ALL PRIVILEGES ON DATABASE "gregoirelayet.com" TO gerg;

CREATE DATABASE "test_gregoirelayet.com";
GRANT ALL PRIVILEGES ON DATABASE "test_gregoirelayet.com" TO gerg;