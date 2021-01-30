FROM golang:1.15.3 as build
ENV GOPROXY=https://goproxy.cn,direct
WORKDIR /code
ADD go.mod /code/go.mod
ADD go.sum /code/go.sum
RUN go mod download

ADD . /code
RUN go build -tags netgo -o /build/client hello_go/client/client.go
RUN go build -tags netgo -o /build/server hello_go/server/server.go


FROM alpine
WORKDIR /build
COPY --from=build /build/ /build/
CMD /build/server
