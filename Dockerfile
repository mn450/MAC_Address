FROM python
RUN  mkdir -p  /var/test
COPY main.py /var/test/main.py
RUN pip install requests
ENTRYPOINT ["python","/var/test/main.py"]
