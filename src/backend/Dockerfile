FROM python:3.10.4 AS builder

COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.10.4-slim
WORKDIR /code

ENV PYTHONPATH "${PYTHONPATH}:/root/.local"

COPY --from=builder /root/.local /root/.local
COPY . .
COPY ./docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]
CMD [""]
