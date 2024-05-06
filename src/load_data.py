import os
from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("mongodb.connect_string"))
dbName = "langchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

loader = DirectoryLoader("./sample_files", glob="./*.txt", show_progress=True)
data = loader.load()
embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("openai.api_key"))
vectoreStore = MongoDBAtlasVectorSearch.from_documents(
    data, embeddings, collection=collection
)
