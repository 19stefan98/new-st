FROM ubuntu:xenial

ARG VENV_DIR=/venv
ARG PIP_EXEC=$VENV_DIR/bin/pip

RUN apt-get update && apt-get install -y \
    python3 python3-pip \
    libgconf2-4 libnss3-1d libxss1 \
    fonts-liberation libappindicator1 xdg-utils \
    software-properties-common \
    curl unzip wget \
    xvfb

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

COPY requirements.txt .

RUN pip3 install virtualenv && \
    virtualenv $VENV_DIR && \
    $PIP_EXEC install -r requirements.txt

ENV APP_HOME /usr/src/app
WORKDIR $APP_HOME
COPY . $APP_HOME

ENV ALLURE_FOLDER_CHROME /result
ENV TEST_HOST https://dev.tenderplan3.lmx.su/
ENV BROWSER chrome

VOLUME $ALLURE_FOLDER_CHROME

CMD /venv/bin/pytest -v -n2 run.py --alluredir=/$ALLURE_FOLDER_CHROME