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

from openstack.image.v2 import md_property
from openstack.tests.unit import base

NAMESPACE = 'CIM::ProcessorAllocationSettingData'
IDENTIFIER = 'InstructionSet'
EXAMPLE = {
    'namespace': NAMESPACE,
    'name': IDENTIFIER,
    'type': 'string',
    'title': 'Instruction Set',
    'description': 'Identifies the instruction set of the processor within a '
                   'processor architecture.',
    'operators': ['<or>'],
    'enum': ['x86:i386', 'x86:i486', 'x86:i586', 'x86:i686', 'x86:64',
             'IA-64:IA-64', 'AS/400:TIMI', 'Power:Power_2.03',
             'Power:Power_2.04', 'Power:Power_2.05', 'Power:Power_2.06',
             'S/390:ESA/390', 'S/390:z/Architecture', 'S/390:z/Architecture_2',
             'PA-RISC:PA-RISC_1.0', 'PA-RISC:PA-RISC_2.0', 'ARM:A32',
             'ARM:A64', 'MIPS:MIPS_I', 'MIPS:MIPS_II', 'MIPS:MIPS_III',
             'MIPS:MIPS_IV', 'MIPS:MIPS_V', 'MIPS:MIPS32', 'MIPS64:MIPS64',
             'Alpha:Alpha', 'SPARC:SPARC_V7', 'SPARC:SPARC_V8',
             'SPARC:SPARC_V9', 'SPARC:SPARC_JPS1', 'SPARC:UltraSPARC2005',
             'SPARC:UltraSPARC2007', '68k:68000', '68k:68010', '68k:68020',
             '68k:68030', '68k:68040', '68k:68060']
}


class TestMDProperty(base.TestCase):
    def test_basic(self):
        sot = md_property.MDProperty()
        self.assertIsNone(sot.resource_key)
        self.assertIsNone(sot.resources_key)
        self.assertEqual('/metadefs/namespaces/%(namespace_name)s/properties',
                         sot.base_path)
        self.assertTrue(sot.allow_create)
        self.assertTrue(sot.allow_fetch)
        self.assertTrue(sot.allow_commit)
        self.assertTrue(sot.allow_delete)
        self.assertTrue(sot.allow_list)

    def test_make_it(self):
        sot = md_property.MDProperty(**EXAMPLE)
        self.assertEqual(EXAMPLE['name'], sot.name)
        self.assertEqual(EXAMPLE['namespace'], sot.namespace)
        self.assertEqual(EXAMPLE['type'], sot.type)
        self.assertEqual(EXAMPLE['title'], sot.title)
        self.assertEqual(EXAMPLE['description'], sot.description)
        self.assertEqual(EXAMPLE['operators'], sot.operators)
        self.assertEqual(EXAMPLE['enum'], sot.enum)
