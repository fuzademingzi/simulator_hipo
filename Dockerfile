FROM python:3.8
COPY . /var/www/python
WORKDIR /var/www/python
COPY REQUIREMENTS.txt REQUIREMENTS.txt
RUN pip install -r ./REQUIREMENTS.txt
ENTRYPOINT ["streamlit", "run"]
CMD ["./hipoteca.py"]
