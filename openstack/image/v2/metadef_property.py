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

    #: An identifier (a name) for the namespace.
    namespace_name = resource.URI('namespace_name')

    #: The name of the property
    name = resource.Body('name', alternate_id=True)
    #: The property type.
    type = resource.Body('type')
    #: The title of the property.
    title = resource.Body('title')
    #: Detailed description of the property.
    description = resource.Body('description')
    #: A list of operator
    operators = resource.Body('operators', type=list)
    #: Default property description.
    default = resource.Body('default')
    #: Indicates whether this is a read-only property.
    readonly = resource.Body('readonly', type=bool)
    #: Minimum allowed numerical value.
    minimum = resource.Body('minimum', type=int)
    #: Maximum allowed numerical value.
    maximum = resource.Body('maximum', type=int)
    #: Enumerated list of property values.
    enum = resource.Body('enum', type=list)
    #: A regular expression ( `ECMA 262 <http://www.ecma-international.org
    # /publications/standards/Ecma-262.htm>`_ )
    #: that a string value must match.
    pattern = resource.Body('pattern')
    #: Minimum allowed string length.
    minLength = resource.Body('minLength', type=int, minimum=0, default=0)
    #: Maximum allowed string length.
    maxLength = resource.Body('maxLength', type=int, minimum=0)
    #: Schema for the items in an array.
    items = resource.Body('items', type=dict)
    #: Indicates whether all values in the array must be distinct.
    uniqueItems = resource.Body('uniqueItems', type=bool, default=False)
    #: Minimum length of an array.
    minItems = resource.Body('minItems', type=int, minimum=0, default=0)
    #: Maximum length of an array.
    maxItems = resource.Body('maxItems', type=int, minimum=0)
    #: Describes extra items, if you use tuple typing.  If the value of
    #: ``items`` is an array (tuple typing) and the instance is longer than
    #: the list of schemas in ``items``, the additional items are described by
    #: the schema in this property.  If this value is ``false``, the instance
    #: cannot be longer than the list of schemas in ``items``.  If this value
    #: is ``true``, that is equivalent to the empty schema (anything goes).
    additionalItems = resource.Body('additionalItems', type=bool)


class MetadefProperties(resource.Resource):
    base_path = '/metadefs/namespaces/%(namespace_name)s/properties'

    # capabilities
    allow_fetch = True

    #: An identifier (a name) for the namespace.
    namespace_name = resource.URI('namespace_name')

    #: A dictionary of key:value pairs, where each value is a property object
    #: as defined by the Metadefs Property Schema.
    properties = resource.Body('properties', type=dict)
