FROM fedora:30

ENV APP_HOME=/opt/camelot
ENV APP_NAME-=docs-gen

ENV LOG_DIR=/var/$APP_NAME

RUN mkdir -p $LOG_DIR

EXPOSE 5000

RUN dnf install -y java-11-openjdk java-11-openjdk-devel which

RUN pip3 install --upgrade pip

RUN pip3 install pipenv

WORKDIR $APP_HOME

COPY Pipfile Pipfile.lock gunicorn_config.py $APP_HOME/

RUN pipenv install --deploy --system

COPY dist/*.whl $APP_HOME/

RUN pip3 install *.whl

RUN rm -rf $APP_HOME/*.whl

CMD gunicorn --config gunicorn_config.py "code_generators:create_app()"
