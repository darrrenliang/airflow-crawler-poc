# airflow-crawler-poc


## Python Crawler

#### build image
`docker build -t webcrawler .`

#### execute crawler
`docker run webcrawler python ./app/crawler.py https://google.com`


## Airflow

#### download yaml template
`curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.1/docker-compose.yaml'`


#### setup related folder
`mkdir -p ./dags ./logs ./plugins ./config`


#### initialize services
`docker-compose up airflow-init`

#### start services
`docker-compose up`



# Reference
- https://github.com/ChickenBenny/Airflow-scraping-ETL-tutorial
- https://github.com/ChickenBenny/Airflow-tutorial