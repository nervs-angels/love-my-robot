cd gui
docker build -t nervsangels/love-my-robot:gui .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push nervsangels/gui:imagetag
cd ..