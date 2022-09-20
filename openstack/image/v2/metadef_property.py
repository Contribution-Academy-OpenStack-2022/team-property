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


class MetadefProperty(resource.Resource):
    base_path = '/metadefs/namespaces/%(namespace_name)s/properties'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    _store_unknown_attrs_as_properties = True
    _allow_unknown_attrs_in_body = True

    # TODO(eunyoung): Add more attrs & docstring
    namespace_name = resource.URI('namespace_name')

    name = resource.Body('name', alternate_id=True)
    title = resource.Body('title')
    description = resource.Body('description')
    operators = resource.Body('operators', type=list)
    type = resource.Body('type')
    required = resource.Body('required')
    minimum = resource.Body('minimum', type=int)
    maximum = resource.Body('maximum', type=int)
    maxLength = resource.Body('maxLength', type=int, minimum=0)
    minLength = resource.Body('minLength', type=int, minimum=0, default=0)
    pattern = resource.Body('pattern')
    enum = resource.Body('enum', type=list)
    readonly = resource.Body('readonly', type=bool)
    maxItems = resource.Body('maxItems', type=int, minimum=0)
    minItems = resource.Body('minItems', type=int, minimum=0, default=0)
    uniqueItems = resource.Body('uniqueItems', type=bool, default=False)
    additionalItems = resource.Body('additionalItems', type=bool)
    properties = resource.Body('properties', type=dict)
