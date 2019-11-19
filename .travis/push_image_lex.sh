cd lex
docker build -t nervsangels/lex:imagetag .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push nervsangels/lex:imagetag
cd ..