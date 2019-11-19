cd gui
docker build -t nervsangels/gui:imagetag .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push nervsangels/gui:imagetag
cd ..