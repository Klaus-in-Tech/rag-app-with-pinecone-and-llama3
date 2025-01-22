# Intro to Vector Databases with LangChain and Pinecone

This project demonstrates how to use vector databases with LangChain and Pinecone for document retrieval and question answering. It includes scripts for ingesting documents into a Pinecone vector store and retrieving information using LangChain.

## Prerequisites

- Python 3.8+
- [Pinecone](https://www.pinecone.io/)
- [LangChain](https://www.langchain.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Klaus-in-Tech/rag-app-with-pinecone-and-llama3
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Pinecone and LangChain API keys:
    ```env
    PINECONE_API_KEY=<your-pinecone-api-key>
    PINECONE_INDEX_NAME=<your-pinecone-index-name>
    LANGCHAIN_API_KEY=<your-langchain-api-key>
    ```

## Ingesting Documents

To ingest documents into the Pinecone vector store, run the `ingestion.py` script. This script reads a text file, splits it into chunks, and stores the chunks as vectors in Pinecone.

```sh
python ingestion.py
```

## Retrieving Information

To retrieve information from the Pinecone vector store, run the `retrieval.py` script. This script uses LangChain to query the vector store and return relevant information.

```sh
python retrieval.py
```

## Example Document

The `medium_blog.txt` file contains an example document about vector databases. This file is used in the ingestion process.

## Project Structure

- `ingestion.py`: Script for ingesting documents into Pinecone.
- `retrieval.py`: Script for retrieving information from Pinecone.
- `medium_blog.txt`: Example document used for ingestion.
- `README.md`: Project documentation.

## License

This project is licensed under the MIT License.