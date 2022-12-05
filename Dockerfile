FROM amsterdam/python3.6

COPY work_blog /app/work_blog

WORKDIR /app/work_blog

RUN pip install --upgrade pip