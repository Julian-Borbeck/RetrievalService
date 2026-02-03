FROM continuumio/miniconda3:latest

WORKDIR /app

COPY environment.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml && conda clean -afy

ENV CONDA_DEFAULT_ENV=retrieval
ENV PATH=/opt/conda/envs/retrieval/bin:$PATH

COPY app.py settings.py .env /app/
COPY query/ /app/query/
COPY models/ /app/models/
COPY llm/ /app/llm/
COPY data/ /app/data

EXPOSE 9002
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9002", "--workers", "2"]
