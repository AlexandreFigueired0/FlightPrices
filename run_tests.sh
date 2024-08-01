# Create Docker network if not exists
docker network inspect microservices &>/dev/null || {
    echo "Creating Docker network..."
    docker network create microservices
}

# Startup database services
cd database-visualization
./run.sh

cd ..
docker build -f tests/Dockerfile.test -t test_visualization .
docker run --rm -t --network microservices test_visualization 