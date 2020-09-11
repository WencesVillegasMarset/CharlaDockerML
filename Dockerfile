
FROM python:3.6

RUN git clone https://github.com/WencesVillegasMarset/CharlaDockerML.git

WORKDIR /CharlaDockerML

EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python", "server.py"]