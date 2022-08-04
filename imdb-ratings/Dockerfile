FROM python:slim

LABEL maintainer="artembo.dev@gmail.com"


RUN groupadd -g 10000 appuser && \
    useradd -r -u 10000 -g appuser appuser

USER appuser

COPY --chown=appuser:appuser . /home/appuser/app
WORKDIR  /home/appuser/app
RUN pip install --user -r requirements.txt


EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]