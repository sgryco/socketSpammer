# socketSpammer
A test project to test Django-channels

To run:
```
docker-compose build
docker-compose up
```

To monitor the connections:
```
docker-compose exec web bash -c 'watch "netstat -ta | wc -l"' 
```
