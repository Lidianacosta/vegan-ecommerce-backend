from abc import ABC, abstractmethod


class BaseRepository(ABC):
    """ Base classe for performing actions on the database. """

    @staticmethod
    @abstractmethod
    def get_all_instances():
        """ Return all instances of a model. """

    @staticmethod
    @abstractmethod
    def create_instance(data):
        """ Create and return an instance of a model. """

    @staticmethod
    @abstractmethod
    def get_instance_by_id(instance_id):
        """ Filter a model instance by its ID. """

    @staticmethod
    @abstractmethod
    def update_instance(instance_id, data):
        """
            Update the model instance fields, filtering it by its ID, with
        provided data.
        """

    @staticmethod
    @abstractmethod
    def delete_instance(instance_id):
        """ Delete the model instance, filtering it by its ID. """
