FROM python:3.7
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["ifc19_app.py"]
