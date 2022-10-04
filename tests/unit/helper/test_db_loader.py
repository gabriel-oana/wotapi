import os
import unittest
from sqlalchemy import create_engine

from wotapi.orm.data_model import Base, DataModel, PlayerPersonalDataDetailsModel
from wotapi.helper.db_loader import DBLoader


class TestDataModelLoader(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = create_engine('sqlite:///:memory:')
        self.db_loader = DBLoader(path=os.getcwd(), db_engine=self.engine)
        DataModel.create_tables(engine=self.engine)

    def test_create_engine_on_specific_path(self):
        DBLoader(path=f'tests/{os.getcwd()}')

    def test_multiple_insert(self):
        data = [{"id": 3}, {"id": 4}]
        self.db_loader.insert(model=PlayerPersonalDataDetailsModel, data=data)

    def test_insert_raises(self):
        self.assertRaises(RuntimeError, self.db_loader.insert, PlayerPersonalDataDetailsModel, 0)

    def test_supply_data_count_is_0(self):
        result = self.db_loader.check_if_data_exists(PlayerPersonalDataDetailsModel)
        expected = False
        self.assertEqual(result, expected)

    def test_supply_data_count_is_1(self):
        data = [{"id": 6}, {"id": 5}]
        self.db_loader.insert(PlayerPersonalDataDetailsModel, data)
        result = self.db_loader.check_if_data_exists(PlayerPersonalDataDetailsModel)
        expected = True
        self.assertEqual(result, expected)

    def tearDown(self) -> None:
        Base.metadata.drop_all(self.engine)
