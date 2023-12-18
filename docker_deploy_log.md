```bash
(base) majeedk@tosh:~/Documents/ml.zoom.camp/capstone01$ sudo docker build -t car-price-prediction-service .
[sudo] password for majeedk: 
[+] Building 61.5s (11/11) FINISHED                                                                                                                      docker:default
 => [internal] load build definition from Dockerfile                                                                                                               0.0s
 => => transferring dockerfile: 641B                                                                                                                               0.0s
 => [internal] load .dockerignore                                                                                                                                  0.0s
 => => transferring context: 2B                                                                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.11                                                                                                     1.4s
 => [1/6] FROM docker.io/library/python:3.11@sha256:c0c5e12cd9fe77a556dea3bc71a71e16bb2fcb35974ce82215095d4cd279fb93                                              19.9s
 => => resolve docker.io/library/python:3.11@sha256:c0c5e12cd9fe77a556dea3bc71a71e16bb2fcb35974ce82215095d4cd279fb93                                               0.0s
 => => sha256:c0c5e12cd9fe77a556dea3bc71a71e16bb2fcb35974ce82215095d4cd279fb93 2.14kB / 2.14kB                                                                     0.0s
 => => sha256:fea225597f8cb462e92f46e144c73e73f6f05f939afdc5dabeed2801c5348ef5 2.01kB / 2.01kB                                                                     0.0s
 => => sha256:90e5e7d8b87a34877f61c2b86d053db1c4f440b9054cf49573e3be5d6a674a47 49.58MB / 49.58MB                                                                   1.6s
 => => sha256:27e1a8ca91d35598fbae8dee7f1c211f0f93cec529f6804a60e9301c53a604d0 24.05MB / 24.05MB                                                                   1.3s
 => => sha256:3810972689cfd1ed1b323d3bcc1942ed87000ce3671927d47acf49e4a4538713 7.53kB / 7.53kB                                                                     0.0s
 => => sha256:d3a767d1d12e57724b9f254794e359f3b04d4d5ad966006e5b5cda78cc382762 64.13MB / 64.13MB                                                                   3.5s
 => => sha256:711be5dc50448ab08ccab0b44d65962f36574d341749ab30651b78ec0d4bfd1c 211.07MB / 211.07MB                                                                 6.4s
 => => sha256:45df5ffe8c3b669e51c3e8b33cc0993647ba499ca32ea3ee38603e78fe6eef89 6.39MB / 6.39MB                                                                     1.9s
 => => extracting sha256:90e5e7d8b87a34877f61c2b86d053db1c4f440b9054cf49573e3be5d6a674a47                                                                          2.8s
 => => sha256:ab7061826bef0e1c4fdbff2c63354bbe0e81aba83a0d1a18fc833df35f77b88d 19.80MB / 19.80MB                                                                   2.8s
 => => sha256:5ac9dfcd906b5555cb11957987f203ece5ae63b7ab4def779793feb429c519c6 245B / 245B                                                                         2.9s
 => => sha256:6d6c69a512900ef116269d86a3719a4dc8839b75c2f26e786305e3c16a09b64c 3.11MB / 3.11MB                                                                     3.2s
 => => extracting sha256:27e1a8ca91d35598fbae8dee7f1c211f0f93cec529f6804a60e9301c53a604d0                                                                          0.8s
 => => extracting sha256:d3a767d1d12e57724b9f254794e359f3b04d4d5ad966006e5b5cda78cc382762                                                                          3.0s
 => => extracting sha256:711be5dc50448ab08ccab0b44d65962f36574d341749ab30651b78ec0d4bfd1c                                                                          9.3s
 => => extracting sha256:45df5ffe8c3b669e51c3e8b33cc0993647ba499ca32ea3ee38603e78fe6eef89                                                                          0.3s
 => => extracting sha256:ab7061826bef0e1c4fdbff2c63354bbe0e81aba83a0d1a18fc833df35f77b88d                                                                          0.8s
 => => extracting sha256:5ac9dfcd906b5555cb11957987f203ece5ae63b7ab4def779793feb429c519c6                                                                          0.0s
 => => extracting sha256:6d6c69a512900ef116269d86a3719a4dc8839b75c2f26e786305e3c16a09b64c                                                                          0.4s
 => [internal] load build context                                                                                                                                  0.4s
 => => transferring context: 37.67MB                                                                                                                               0.4s
 => [2/6] WORKDIR /app                                                                                                                                             1.5s
 => [3/6] RUN pip install pipenv                                                                                                                                   8.9s
 => [4/6] COPY Pipfile Pipfile.lock ./                                                                                                                             0.1s
 => [5/6] RUN pipenv install --system --deploy                                                                                                                    25.6s
 => [6/6] COPY [predict.py, model.joblib, preprocessor.joblib,  ./]                                                                                                0.3s
 => exporting to image                                                                                                                                             3.8s
 => => exporting layers                                                                                                                                            3.8s
 => => writing image sha256:08cbae2e797039c0e05d5ac8f291c222d098a798876cb347856f2d50963efdff                                                                       0.0s
 => => naming to docker.io/library/car-price-prediction-service                                                                                                    0.0s
(base) majeedk@tosh:~/Documents/ml.zoom.camp/capstone01$ sudo docker images -a
REPOSITORY                     TAG       IMAGE ID       CREATED              SIZE
car-price-prediction-service   latest    08cbae2e7970   About a minute ago   1.52GB
zoomcamp-model                 hw10      0b4c09a56d39   2 weeks ago          504MB
kindest/node                   <none>    89e7dc9f9131   6 months ago         932MB
(base) majeedk@tosh:~/Documents/ml.zoom.camp/capstone01$ sudo docker run -it -p 9696:9696 car-price-prediction-service
[2023-12-18 14:39:58 +0000] [1] [INFO] Starting gunicorn 21.2.0
[2023-12-18 14:39:58 +0000] [1] [INFO] Listening at: http://0.0.0.0:9696 (1)
[2023-12-18 14:39:58 +0000] [1] [INFO] Using worker: sync
[2023-12-18 14:39:58 +0000] [7] [INFO] Booting worker with pid: 7
```