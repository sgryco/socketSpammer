# socketSpammer
A test project to test Django-channels

Requirements: `docker` and `docker-compose`

To run:
```
docker-compose build
docker-compose up
```

To monitor the connections, run in another terminal:
```
docker-compose exec web bash -c 'watch "netstat -ta | wc -l"' 
```
