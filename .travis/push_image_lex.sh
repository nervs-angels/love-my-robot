cd lex
docker build -t nervsangels/lex:0.1 .
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push nervsangels/lex:0.1
cd ..