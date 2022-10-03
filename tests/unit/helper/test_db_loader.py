import unittest
from sqlalchemy import create_engine

from wotapi.orm.data_model import Base, DataModel, PlayerPersonalDataDetailsModel
from wotapi.helper.db_loader import DBLoader

data = [{"id": 1}, {"id": 2}]


class TestDataModelLoader(unittest.TestCase):
    engine = create_engine('sqlite:///:memory:')

    def setUp(self) -> None:
        DataModel.create_tables(self.engine)

    def test_multiple_insert(self):
        DBLoader.insert(PlayerPersonalDataDetailsModel, data, db_engine=self.engine)

    def test_insert_raises(self):
        engine = create_engine('sqlite:///:memory:')
        self.assertRaises(RuntimeError, DBLoader.insert, PlayerPersonalDataDetailsModel, data, engine)

    def test_supply_data_count_is_0(self):
        result = DBLoader.check_if_data_exists(PlayerPersonalDataDetailsModel, db_engine=self.engine)
        expected = False
        self.assertEqual(result, expected)

    def test_supply_data_count_is_1(self):
        DBLoader.insert(PlayerPersonalDataDetailsModel, data, db_engine=self.engine)
        result = DBLoader.check_if_data_exists(PlayerPersonalDataDetailsModel, db_engine=self.engine)
        expected = True
        self.assertEqual(result, expected)

    def tearDown(self) -> None:
        Base.metadata.drop_all(self.engine)
