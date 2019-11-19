cd lex
docker build -t nervsangels/love-my-robot:lex .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push nervsangels/lex:imagetag
cd ..