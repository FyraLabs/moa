FROM python:3.7

RUN useradd -m -r moa \
  && chown moa /app

RUN apt-get update -qq \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends build-essential git-core \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=source requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --from=source . .
COPY config.py moa/

USER moa
ENV MOA_CONFIG config.ProductionConfig

CMD ["python3", "app.py"]
