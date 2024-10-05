DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'customer-db'
   ) THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE "customer-db"');
   END IF;
END
$do$;
