from abc import ABC, abstractmethod


class BaseService(ABC):
    """ Base classe for business rules management. """

    @staticmethod
    @abstractmethod
    def list_all_instances():
        """ return a list of instances of model. """

    @staticmethod
    @abstractmethod
    def create_instance(**validated_data):
        """ Create and return an instance of a model. """

    @staticmethod
    @abstractmethod
    def retrieve_instance(instance_id):
        """ Retrieve a model instance by its ID. """

    @staticmethod
    @abstractmethod
    def update_instance(instance_id, **validated_data):
        """
            Update the model instance fields, filtering it by its ID, with
        provided data.
        """

    @staticmethod
    @abstractmethod
    def partial_update_instance(instance_id, **validated_data):
        """
            Partial update the model instance fields, filtering it by its ID,
        with provided data.
        """

    @staticmethod
    @abstractmethod
    def destroy_instance(instance_id):
        """ Destroy the model instance, filtering it by its ID. """
