FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install uv
RUN uv sync

CMD ["uv", "run", "uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]