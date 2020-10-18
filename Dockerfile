FROM clearlinux

RUN swupd update
RUN swupd bundle-add python3-basic

WORKDIR /usr/src/app

ENV PORT=5000

EXPOSE 5000

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./index.py"]