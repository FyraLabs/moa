# syntax=docker/dockerfile:1

FROM python:3.7

RUN apt-get update -qq \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends build-essential git-core \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN useradd -m -r moa \
  && chown moa /app

COPY --chown=moa --from=source requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --chown=moa --from=source . .
COPY --chown=moa config.py .
COPY --chown=moa worker.sh .

RUN chmod +x worker.sh

USER moa
EXPOSE 5000
CMD ["python3", "app.py"]
