#Paypal test integration

0. You will need Docker installed on your laptop

1. Build the image with docker

docker build . -t simple-server

2. Run the a new container and choose a port

docker run  --rm -p 5000:5000 simple-server

3. Open a browser and put the URL

http:// localhost:5000/client.html





