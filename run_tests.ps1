docker build -t saucedemo-tests .

Write-Host "Running tests inside Docker container..."
docker run --rm -v ${PWD}/allure-results:/app/allure-results saucedemo-tests
