# RetrievalService
A webservice prototype retrieval system for multiple sequence alignment built using FastAPI.

## Installation
Please install the conda environment via conda env create -f environment.yml

This app is dependent on OLLAMA and qwen2.5:7b-instruct which need to be installed seperately.

The Webservice can then be started from the project root directory using the command uvicorn app:app --host 0.0.0.0 --port 9002

##Configuration
Configuration, such as the url and port for the embedding service, the name of the chroma vector store dir, the name of the collection to use for retrieval, the model to use for the rewriting, and the ollama url can be set in the .env file.

