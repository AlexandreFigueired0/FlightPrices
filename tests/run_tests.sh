# Create Docker network if not exists
docker network inspect microservices &>/dev/null || {
    echo "Creating Docker network..."
    docker network create microservices
}

# Startup database services
cd ../database-ranking
./run.sh

cd ../database-visualization
./run.sh

cd ../tests
docker build -f Dockerfile.test -t test_visualization ..
docker run -t --network microservices test_visualization 