FROM node:15.3.0-alpine3.12 as builder

WORKDIR /usr/src/app
COPY . .
RUN npm install
RUN npm run build
RUN ls /usr/src/app/dist/

FROM nginx:1.19.5-alpine

COPY --from=builder /usr/src/app/dist/angular-skeleton /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
