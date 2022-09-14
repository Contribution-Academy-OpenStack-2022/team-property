
from openstack import resource


class Metadef(resource.Resource):
    base_path = '/metadefs/namespace'

    # capabilities
    allow_create = True
    allow_fetch = True
    allow_commit = True
    allow_delete = True
    allow_list = True

    namespace = resource.Body('namespace')
    name = resource.Body('name')
    description = resource.Body('description')


