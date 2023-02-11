FROM python:3.10
WORKDIR /bot
COPY requiremets.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .
CMD [ "python3","D:\PJ\project_vlados\bot\main.py"]