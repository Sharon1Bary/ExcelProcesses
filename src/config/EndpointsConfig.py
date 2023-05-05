from dataclasses import dataclass


@dataclass
class CreateCategoryConfig:
    prefix: str = '/api/v1/create_category'


@dataclass
class UploadFileConfig:
    prefix: str = '/api/v1/upload_file'


@dataclass
class SumTypeConfig:
    prefix: str = '/api/v1/sum_type'


@dataclass
class FindRegionsConfig:
    prefix: str = '/api/v1/find_regions'


class EndpointsConfig:

    create_category_config: CreateCategoryConfig = CreateCategoryConfig()
    upload_file_config: UploadFileConfig = UploadFileConfig()
    sum_type_config: SumTypeConfig = SumTypeConfig()
    find_regions_config: FindRegionsConfig = FindRegionsConfig()
