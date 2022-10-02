from osc_lib.command import command
from openstackclient.i18n import _
import json


class CreatePropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(CreatePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            '--name',
            metavar='<NAME>',
            help=_('NAME'),
        )
        parser.add_argument(
            '--title',
            metavar='<TITLE>',
            help=_('TITLE'),
        )
        parser.add_argument(
            '--schema',
            metavar='<SCHEMA>',
            help=_('SCHEMA'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image

        try:
            schema = json.loads(parsed_args.schema)
        except ValueError:
            print('Schema is not a valid JSON object.')
        else:
            fields = {'name': parsed_args.name, 'title': parsed_args.title}
            fields.update(schema)

            kwargs = {"name": parsed_args.name, "title": parsed_args.title, "type": fields["type"], "enum": fields["enum"], "description": fields["description"]}
            metadata_object = image_client.create_metadata_property(parsed_args.namespace, **kwargs)
            # 출력
            schema = eval(metadata_object.text)

            column_headers = (
                'Property',
                'Value',
            )

            columns = (
                ("description", schema["description"]),
                ("enum", schema["enum"]),
                ("name", schema["name"]),
                ("title", schema["title"]),
                ("type", schema["type"]),
            )

            table = (
                column_headers,
                (
                    columns
                ),
            )
            return table


class DeletePropertyMd(command.Lister):
    _description = _("md-property-delete")

    def get_parser(self, prog_name):
        parser = super(DeletePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            'property_name',
            metavar='<property_name>',
            help=_('property_name'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image
        image_client.delete_metadata_property(parsed_args.namespace, parsed_args.property_name)


class ShowPropertyMd(command.Lister):
    _description = _("md-property-show")

    def get_parser(self, prog_name):
        parser = super(ShowPropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            'property_name',
            metavar='<property_name>',
            help=_('property_name'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image
        metadata_object = image_client.show_metadata_property(parsed_args.namespace, parsed_args.property_name)

        # 출력
        schema = eval(metadata_object.text)

        column_headers = (
            'Property',
            'Value',
        )

        columns = (
            ("description", schema["description"]),
            ("enum", schema["enum"]),
            ("name", schema["name"]),
            ("title", schema["title"]),
            ("type", schema["type"]),
        )

        table = (
            column_headers,
            (
                columns
            ),
        )
        return table


class UpdatePropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(UpdatePropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        parser.add_argument(
            'property_name',
            metavar='<property_name>',
            help=_('property_name'),
        )
        parser.add_argument(
            '--name',
            metavar='<NAME>',
            help=_('NAME'),
        )
        parser.add_argument(
            '--title',
            metavar='<TITLE>',
            help=_('TITLE'),
        )
        parser.add_argument(
            '--schema',
            metavar='<SCHEMA>',
            help=_('SCHEMA'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image

        try:
            schema = json.loads(parsed_args.schema)
        except ValueError:
            print('Schema is not a valid JSON object.')
        else:
            fields = {'name': parsed_args.name, 'title': parsed_args.title}
            fields.update(schema)

            kwargs = {"name": parsed_args.name, "title": parsed_args.title, "type": fields["type"], "enum": fields["enum"], "description": fields["description"]}
            metadata_object = image_client.update_metadata_property(parsed_args.namespace, parsed_args.property_name, **kwargs)
            # 출력
            schema = eval(metadata_object.text)

            column_headers = (
                'Property',
                'Value',
            )

            columns = (
                ("description", schema["description"]),
                ("enum", schema["enum"]),
                ("name", schema["name"]),
                ("title", schema["title"]),
                ("type", schema["type"]),
            )

            table = (
                column_headers,
                (
                    columns
                ),
            )
            return table


class ListPropertyMd(command.Lister):
    _description = _("md-property-create")

    def get_parser(self, prog_name):
        parser = super(ListPropertyMd, self).get_parser(prog_name)
        parser.add_argument(
            'namespace',
            metavar='<namespace>',
            help=_('namespace'),
        )
        return parser

    def take_action(self, parsed_args):
        image_client = self.app.client_manager.image
        metadata_object = image_client.list_metadata_property(parsed_args.namespace)

        column_headers = (
            'name',
            'title',
            'type',
        )

        columns = (

        )

        schema = eval(metadata_object.text)["properties"]

        for metadef in schema:
            column = (
                (
                    schema[metadef]["name"],
                    schema[metadef]["title"],
                    schema[metadef]["type"],
                ),
            )
            columns += column


        table = (
            column_headers,
            (
                columns
            ),
        )

        return table