# gpt4all-test

LangChain experiment with GPT4All and Postgres as vector store

## Installing vector extension on official Docker image

```bash
docker exec -it gpt4all-test_postgres_1 /bin/bash
apt-get update
apt-get install git make gcc postgresql-server-dev-16
cd /tmp/
git clone --branch v0.5.0 https://github.com/pgvector/pgvector.git
cd pgvector/
make
make install
exit
PGPASSWORD=postgres psql --host localhost --user postgres postgres
CREATE EXTENSION IF NOT EXISTS vector
  VERSION "0.5.0";
\q
exit
```

## Various tests

- Ask OpenAI to tell a joke (openAI.py)
- Ask Llama about "Hello world" (llama_test.py)
- Ask Falcon about "Hello world" (falcon_test.py)
- Read PDF file into a vector store (readPDF.py)
- Chain a similarity search in the vector back to the LLM (llama_embeddings_test.py)
