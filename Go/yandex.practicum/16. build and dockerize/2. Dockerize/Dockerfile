FROM golang:1.19 as builder

ARG VERSION=uncnown

WORKDIR /app
COPY . .

# тут создастся файл cmd в /app/build и в него скопмилируется все из исходника main.go
RUN GO111MODULE=on GOOS=linux CGO_ENABLED=0 \
    go build -ldflags "-X main.version=${VERSION}" \
    -o /app/build/cmd main.go

FROM alpine:latest

RUN apk --no-cache add ca-certificates
WORKDIR /app
COPY --from=builder /app/build/cmd /bin/cmd

# запускается скомпилированный файл cmd
ENTRYPOINT ["cmd"]