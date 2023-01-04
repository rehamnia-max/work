1. Build the docker image

```
sudo docker build --tag work .
```

2. Run the built image

```
sudo docker run --publish 8000:8000 work 
sudo docker run -ti -v /tmp:/tmp work
sudo docker run -ti -v /tmp:/tmp work /bin/bash
```

3. example of 2 types of request :  

-Generally choosing type 2 + applying spelling -> improve better results  in quicker time
-http://127.0.0.1:8000/gettext/2/1/https://old.dztenders.com/sites/default/files/tenders/2022/06/01/Algerieconfluence_01062022__8736_-1.gif/


4. you can use : https://globalvision.co/tools/compare-text/
   to compare the different outputs