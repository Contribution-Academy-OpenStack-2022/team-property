from openstack.common import tag
from openstack import exceptions
from openstack.image import _download
from openstack import resource
from openstack import utils
import json

class Property(resource.Resource):
    resources_key = 'metadefs'
    base_path = '/metadefs/namespaces/'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    # Store all unknown attributes under 'properties' in the image.
    # Remotely they would be still in the resource root
    _store_unknown_attrs_as_properties = True

    _query_mapping = resource.QueryParameters(
        "description", "namespace", "name", "title", "schema"
    )

    namespace = resource.Body('namespace')
    name = resource.Body('name')
    description = resource.Body('description')
    title = resource.Body('title')
    schema = resource.Body('schema')

    data = dict()

    def create(self, session, prepend_key=True, base_path=None, **params):
        url = utils.urljoin(self.base_path, self.namespace, 'properties')
        print(url)
        self.data['name'] = self.name
        self.data['namespace'] = self.namespace
        self.data['title'] = self.title
        self.data['schema'] = self.schema

        print(self.data)
        res = session.post(url, json=self.data)
        print(res.text)
        return res
