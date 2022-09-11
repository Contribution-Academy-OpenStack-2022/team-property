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


class MDProperty(resource.Resource):
    base_path = '/metadefs/namespaces/%(namespace_name)s/properties'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    requires_id = False

    _store_unknown_attrs_as_properties = True
    _allow_unknown_attrs_in_body = True
    _unknown_attrs_in_body = True

    namespace_name = resource.URI('namespace_name')

    name = resource.Body('name', alternate_id=True)
    title = resource.Body('title')
    type = resource.Body('type')
    description = resource.Body('description')
    enum = resource.Body('enum', type=list)
    operators = resource.Body('operators', type=list)
    pattern = resource.Body('pattern')
    readonly = resource.Body('readonly', type=bool)
    default = resource.Body('default')
    minimum = resource.Body('minimum', type=int)
