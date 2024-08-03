docker build -f tests/Dockerfile.test -t test_visualization .
docker run --rm -t test_visualization 