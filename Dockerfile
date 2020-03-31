FROM python:3.7-alpine
COPY . /.
WORKDIR /.
RUN pip3 install -r pip-requirements.txt
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["-m", "app.__init__"]
