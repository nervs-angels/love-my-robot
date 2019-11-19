cd lex
docker build -t love-my-robot/lex:imagetag .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push love-my-robot/lex:imagetag
cd ..