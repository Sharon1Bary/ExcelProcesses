# ExcelProcesses Service Introduction:

ExcelProcesses is an exported REST API service that handle Excel files actions.


## Endpoints:

It gives us the ability to make the following requests:

1. create_category() - Create a new Category

2. upload_file() - Upload file to a Category.

3. sum_type() - Returns the sum of all numbers in all the Excel files in categories of a type provided.

4. find_regions() - Returns all the regions based on search team in at least on Excel file.

 
#### create_category(category_name: str, region: str , type_: str) 
* category_name - The category name
* region - The category region
* type_ - The category type



#### upload_file(category_name: str, file: str)
* category_name - The category name
* category_name - The Excel file path


#### sum_type(type: str)
* type_ - The category type


#### find_regions(search_term: str)
* search_term - The string to search


## Examples: 
### create_category(category_name: str, region: str , type_: str)

* category_name - Security
* region - USA
* type_ - A
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/create_category?category_name=Security&region=USA&type_=A' \
  -H 'accept: application/json'
```

### upload_file(category_name: str, file: str)
* category_name - Security
* file - \<PATH-TO-PROJECT>\src\lib\adapters\test1.xlsx

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/upload_file?category_name=Security&file=C%3A%5CUsers%5C%D7%9E%D7%A9%D7%AA%D7%9E%D7%A9%5CPycharmProjects%5CExcelProcesses%5Csrc%5Clib%5Cadapters%5Ctest2.xlsx' \
  -H 'accept: application/json'
```


### sum_type(type: str)
* type_ - A
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/sum_type?type_=A' \
  -H 'accept: application/json'
```


### find_regions(search_term: str)
* search_term - The string to search

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/find_regions?search_term=HELLO' \
  -H 'accept: application/json'
```


## Installation

* Use python 3.8 version. https://www.python.org/downloads/release/python-380/

* Use Docker. https://docs.docker.com/language/python/build-images/

* src.apps.ExcelProcesses.py can be run without the Docker as well, execute the src.apps.ExcelProcesses.py and use the Swagger. (see below - 'Fast-API Swagger')



```bash
# Build the Image
docker build -t tasker-fast-api

# Run the Docker
docker run tasker-fast-api
```



## Fast-API Swagger
To open the Swagger go to  http://127.0.0.1:8000/docs#/

