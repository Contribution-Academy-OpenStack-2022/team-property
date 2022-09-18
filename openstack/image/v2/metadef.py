# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from openstack import resource
from openstack.common import metadata
from openstack.utils import urljoin
import json
import warlock
from openstack import exceptions

class Property(resource.Resource):
    resources_key = 'metadefs'
    base_path = '/metadefs/namespaces'

    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    _store_unknown_attrs_as_properties = True

    _query_mapping = resource.QueryParameters(
        "namespace", "name", "title", "type", "additionalItems", "description", "default", "items", "operators", "enum", "maximum", "minItems", "readonly", "minimum", "maxItems", "maxLength", "uniqueItems", "pattern", "minLength"
    )

    namespace = resource.Body('namespace')
    name = resource.Body('name')
    title = resource.Body('title')
    schema = resource.Body('schema')

    data = dict()

    def create(self, session, prepend_key=True, base_path=None, **params):
        """Create a new metadata definitions property inside a namespace."""

        try:
            schema = json.loads(self.schema)
        except ValueError:
            print('Schema is not a valid JSON object.')
        else:
            fields = {'name': self.name, 'title': self.title}
            fields.update(schema)

            # https://docs.openstack.org/api-ref/image/v2/metadefs-index.html?expanded=create-property-detail
            url = urljoin(self.base_path, self.namespace, 'properties')

            response = session.post(url, json=fields)
            exceptions.raise_from_response(response)
            return response

