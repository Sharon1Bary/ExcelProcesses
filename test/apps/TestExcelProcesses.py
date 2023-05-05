from test.mocks import APIMock

from src.lib.domains.Category import Category
from src.lib.utils.sum_type_utils import sum_type_utils
from src.lib.utils.find_regions_utils import find_regions_utils
from src.lib.domains.Core import Core


class TestExcelProcesses:

    def test_create_category(self):

        test_mock = APIMock(name='Security', region='USA', type_='A')
        core_mock = Core()

        # Test create_category() function:
        core_mock.categories[test_mock.name] = \
            (Category(name=test_mock.name,
                      region=test_mock.region,
                      type_=test_mock.type_))
        assert core_mock.categories[test_mock.name].name == 'Security'

        # Test sum_type() function and upload_file():
        s = core_mock.categories.values().mapping['Security']
        s.files.append('test2.xlsx')

        assert sum_type_utils(type_=test_mock.type_, core=core_mock) == 691

        # Test find_regions():

        search_term_mock = 'HELLO'
        assert find_regions_utils(search_term=search_term_mock, core=core_mock) == ['USA']






