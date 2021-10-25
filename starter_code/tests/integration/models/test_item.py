from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        # app context makes it so it is like the app is actually running
        with self.app_context():
            item = ItemModel('test', 19.99)
            # created item model
            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                 "Found an item with name {}, but expected not to.".format('test'))
            # checked that it didnt exists in database
            item.save_to_db()
            # saved it to the database
            self.assertIsNotNone(ItemModel.find_by_name('test'))
            # checked that is does exists in the database
            item.delete_from_db()
            # delete it from the database
            self.assertIsNotNone(ItemModel.find_by_name('test'))
            # check that it does not exist in the database
