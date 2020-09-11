
FROM python:3.6

RUN git clone https://github.com/WencesVillegasMarset/CharlaDockerML.git

WORKDIR /CharlaDockerML

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "server.py"]

EXPOSE 5000
