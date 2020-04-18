FROM python
RUN  mkdir -p  /var/test
COPY test.py /var/test/test.py
RUN pip install requests
ENTRYPOINT ["python","/var/test/test.py"]
