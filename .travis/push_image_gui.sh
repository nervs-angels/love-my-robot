cd gui
docker build -t love-my-robot/gui:imagetag .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push love-my-robot/gui:imagetag
cd ..