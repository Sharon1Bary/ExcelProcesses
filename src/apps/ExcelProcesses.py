from src.config import EndpointsConfig

from src.lib.domains.Category import Category
from src.lib.domains.Core import Core
from src.lib.utils.sum_type_utils import sum_type_utils
from src.lib.utils.find_regions_utils import find_regions_utils
from src.lib.utils.create_category_utils import is_duplicate

from fastapi import APIRouter, FastAPI, Query


app = FastAPI(title="Excel Processes")

router_create_category = APIRouter()
router_upload_file = APIRouter()
router_sum_type = APIRouter()
router_find_regions = APIRouter()

endpoint_config = EndpointsConfig()


@app.get('/', status_code=200, tags=['Health Check'])
def health_check():
    return "The service is up and running."


@router_create_category.get(endpoint_config.create_category_config.prefix, status_code=200)
async def create_category(category_name: str = Query(None, alias='category_name'),
                          region: str = Query(None, alias='region'),
                          type_: str = Query(None, alias='type_')):
    """
    Create a new category based on region and type_ provided.
        :param category_name: str
        :param region: str
        :param type_: str
        :return: category_name
    """
    try:
        if not is_duplicate(category_name=category_name,
                            region=region,
                            type_=type_,
                            categories=core.categories.values()):
            core.categories[category_name] = (Category(name=category_name, region=region, type_=type_))
            return core.categories[category_name].name
        else:
            raise 'Duplicate category'
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


@router_upload_file.get(endpoint_config.upload_file_config.prefix, status_code=200)
async def upload_file(category_name: str = Query(None, alias='category_name'),
                      file: str = Query(None, alias='file')):
    """
    Uploading a file into a category provided.
        :param file:
        :param category_name: str
        :return: bool
    """
    try:
        if file not in core.categories[category_name].files:
            core.categories[category_name].files.append(file)
            return core.categories[category_name].uuid
        else:
            raise 'Duplicate file'
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


@router_sum_type.get(endpoint_config.sum_type_config.prefix, status_code=200)
async def sum_type(type_: str = Query(None, alias='type_')) -> int:
    """
    Returns the sum of all numbers in all the Excel files in categories of this type.
        :param type_: str
        :return: sum: int
    """
    try:
        return sum_type_utils(type_=type_, core=core)
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


@router_find_regions.get(endpoint_config.find_regions_config.prefix, status_code=200)
async def find_regions(search_term: str = Query(None, alias='search_term')) -> list:
    """
    Returns all regions of categories that have at least one Excel file that contains the search_term.
        :param search_term:
        :return: regions: list
    """
    try:
        return find_regions_utils(search_term=search_term, core=core)
    except Exception as el:
        logger.exception(f'Error occurred: {el}')


# add the routs to the app.
app.include_router(router_create_category, tags=["Create Category"])
app.include_router(router_upload_file, tags=["Upload File"])
app.include_router(router_sum_type, tags=["Sum Type"])
app.include_router(router_find_regions, tags=["Find Regions"])

if __name__ == "__main__":
    """
    The main is creating logger, core and activation the fast-api using uvicorn.
    To login the swagger please go to - http://127.0.0.1:8000/docs#/
    """

    import uvicorn
    import logging
    import sys

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

    try:
        core = Core()
        uvicorn.run(app, port=8000, log_level="debug")
    except Exception as e:
        logger.exception(e)
