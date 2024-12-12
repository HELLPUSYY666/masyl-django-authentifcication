FROM python:3.12-slim as builder
ENV PYTHONUNBUFFERED=1

RUN pip install -U pip setuptools wheel

WORKDIR /wheels
COPY requirements.txt /requirements.txt

RUN pip wheel -r /requirements.txt

FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1

COPY --from=builder /wheels /wheels
RUN pip install -U pip setuptools wheel \
      && pip install /wheels/* \
      && rm -rf /wheels \
      && rm -rf /root/.cache/pip/*

WORKDIR /app
COPY . .

EXPOSE 8000
ENV PYTHONPATH /app

ENV DJANGO_SETTINGS_MODULE=animal_blog.settings
RUN python manage.py collectstatic --noinput || echo "Collectstatic failed, continuing..."

CMD ["gunicorn", "-c", "docker/gunicorn.py", "animal_blog.wsgi:application"]
