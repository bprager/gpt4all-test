# gpt4all-test

LangChain experiment with GPT4All and Postgres as vector store

## Installing vector extension on official Docker image

```bash
 exec -it gpt4all-test_postgres_1 /bin/bash
 cd /tmp/
 apt-get update
 apt-get install git
 git clone --branch v0.5.0 https://github.com/pgvector/pgvector.git
 cd pgvector/
 apt-get install make gcc postgresql-server-dev-16
 make
 ls
 make install
 exit
 PGPASSWORD=postgres psql --host localhost --user postgres postgres
 CREATE EXTENSION IF NOT EXISTS vector
    VERSION "0.5.0";
 \q
```
