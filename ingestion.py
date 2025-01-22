import os

from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from langchain_pinecone import PineconeEmbeddings


api_key = os.environ.get("PINECONE_API_KEY")
index_name = os.environ.get("PINECONE_INDEX_NAME")

# Initialize Pinecone
pc = Pinecone(api_key=api_key, environment="us-east-1")

# Load example document
with open("medium_blog.txt") as f:
    state_of_the_union = f.read()

    loader = TextLoader("medium_blog.txt")
    document = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=1000,
    chunk_overlap=0,
    length_function=len,
    is_separator_regex=False,
)
# Split the document into chunks but without the source text
texts = text_splitter.create_documents([state_of_the_union])

# Split the document into chunks with the source text
doc_texts = text_splitter.split_documents(document)

embeddings = PineconeEmbeddings(model="multilingual-e5-large")


# Create a Pinecone index and store the vectors
index = pc.Index(index_name)

vector_store = PineconeVectorStore.from_documents(
    doc_texts, embedding=embeddings, index_name=index_name
)

print(f"Number of chunks: {len(doc_texts)}")
