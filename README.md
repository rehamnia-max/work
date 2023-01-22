# Django API for " CraftsMan Application"
## Description
This is a Django API for " CraftsMan Application", which developed in mobile development science of Dr.Mehdi Nafaa

## 1. DATABASE setup:

```
CREATE DATABASE work CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
```

## 2. Build the docker image

```
sudo docker build --tag work .
```

## 3. Run the built image

```
sudo docker run --publish 8000:8000 work 
sudo docker run -ti -v /tmp:/tmp work
sudo docker run -ti -v /tmp:/tmp work /bin/bash
```

