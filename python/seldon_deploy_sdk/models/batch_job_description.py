# coding: utf-8

"""
    Seldon Deploy API

    API to interact and manage the lifecycle of your machine learning models deployed through Seldon Deploy.  # noqa: E501

    OpenAPI spec version: v1alpha1
    Contact: hello@seldon.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BatchJobDescription(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'finished_at': 'str',
        'started_at': 'str',
        'workflow_name': 'str',
        'workflow_status': 'NodePhase',
        'workflow_uid': 'UID'
    }

    attribute_map = {
        'finished_at': 'FinishedAt',
        'started_at': 'StartedAt',
        'workflow_name': 'workflowName',
        'workflow_status': 'workflowStatus',
        'workflow_uid': 'workflowUID'
    }

    def __init__(self, finished_at=None, started_at=None, workflow_name=None, workflow_status=None, workflow_uid=None):  # noqa: E501
        """BatchJobDescription - a model defined in Swagger"""  # noqa: E501

        self._finished_at = None
        self._started_at = None
        self._workflow_name = None
        self._workflow_status = None
        self._workflow_uid = None
        self.discriminator = None

        if finished_at is not None:
            self.finished_at = finished_at
        if started_at is not None:
            self.started_at = started_at
        if workflow_name is not None:
            self.workflow_name = workflow_name
        if workflow_status is not None:
            self.workflow_status = workflow_status
        if workflow_uid is not None:
            self.workflow_uid = workflow_uid

    @property
    def finished_at(self):
        """Gets the finished_at of this BatchJobDescription.  # noqa: E501

        Time when job finished  # noqa: E501

        :return: The finished_at of this BatchJobDescription.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this BatchJobDescription.

        Time when job finished  # noqa: E501

        :param finished_at: The finished_at of this BatchJobDescription.  # noqa: E501
        :type: str
        """

        self._finished_at = finished_at

    @property
    def started_at(self):
        """Gets the started_at of this BatchJobDescription.  # noqa: E501

        Time when job started  # noqa: E501

        :return: The started_at of this BatchJobDescription.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this BatchJobDescription.

        Time when job started  # noqa: E501

        :param started_at: The started_at of this BatchJobDescription.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def workflow_name(self):
        """Gets the workflow_name of this BatchJobDescription.  # noqa: E501

        Name of related Argo Workflow  # noqa: E501

        :return: The workflow_name of this BatchJobDescription.  # noqa: E501
        :rtype: str
        """
        return self._workflow_name

    @workflow_name.setter
    def workflow_name(self, workflow_name):
        """Sets the workflow_name of this BatchJobDescription.

        Name of related Argo Workflow  # noqa: E501

        :param workflow_name: The workflow_name of this BatchJobDescription.  # noqa: E501
        :type: str
        """

        self._workflow_name = workflow_name

    @property
    def workflow_status(self):
        """Gets the workflow_status of this BatchJobDescription.  # noqa: E501


        :return: The workflow_status of this BatchJobDescription.  # noqa: E501
        :rtype: NodePhase
        """
        return self._workflow_status

    @workflow_status.setter
    def workflow_status(self, workflow_status):
        """Sets the workflow_status of this BatchJobDescription.


        :param workflow_status: The workflow_status of this BatchJobDescription.  # noqa: E501
        :type: NodePhase
        """

        self._workflow_status = workflow_status

    @property
    def workflow_uid(self):
        """Gets the workflow_uid of this BatchJobDescription.  # noqa: E501


        :return: The workflow_uid of this BatchJobDescription.  # noqa: E501
        :rtype: UID
        """
        return self._workflow_uid

    @workflow_uid.setter
    def workflow_uid(self, workflow_uid):
        """Sets the workflow_uid of this BatchJobDescription.


        :param workflow_uid: The workflow_uid of this BatchJobDescription.  # noqa: E501
        :type: UID
        """

        self._workflow_uid = workflow_uid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BatchJobDescription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BatchJobDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
