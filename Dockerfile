FROM organbase:1.0

# Get latest pip
RUN pip install --upgrade pip

COPY ./requirements.txt /home/organdonation/

RUN pip install --upgrade -r /home/organdonation/requirements.txt

# Copying required files
COPY ./setup.py /home/organdonation/
COPY ./app.py /home/organdonation/
COPY ./config.cfg /home/organdonation/
COPY ./organdonationwebapp /home/organdonation/organdonationwebapp
COPY ./tests /home/organdonation/tests

# Running initial setup
WORKDIR /home/organdonation