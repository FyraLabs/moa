# syntax=docker/dockerfile:1

FROM python:3.7

RUN apt-get update -qq \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends build-essential git-core \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN useradd -m -r moa \
  && chown moa /app

COPY --from=source requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --from=source . .
COPY config.py .
COPY worker.sh .

RUN chmod +x worker.sh

USER moa

CMD ["python3", "app.py"]
