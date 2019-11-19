cd gui
docker build -t nervsangels/gui:0.1 .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push nervsangels/gui:0.1
cd ..