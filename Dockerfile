FROM node as front-builder
RUN npm i -g @quasar/cli
COPY front /app
WORKDIR /app
RUN yarn
RUN quasar build

FROM python:3.7

RUN pip install fastapi uvicorn tortoise-orm[aiomysql] aiofiles

EXPOSE 8081

COPY ./src /src
COPY --from=front-builder /app/dist/spa /src/static

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8081"]