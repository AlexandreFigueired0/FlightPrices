docker build -t database-visualization-container -f ./database-visualization/Dockerfile ./database-visualization
docker build -t visualization-container -f ./visualization/Dockerfile ./visualization
docker build -t test-visualization -f ./tests/Dockerfile.test .
