# simple build 

# FROM python:3.13-slim

# WORKDIR /app

# COPY backend/requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY backend/ .

# CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]


# Multistage Build 



# Stage 1
FROM python:3.13-slim AS builder

WORKDIR /app

COPY backend/requirements.txt .

RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY backend/ .

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]