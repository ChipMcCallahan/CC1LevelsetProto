from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='CC1LevelsetProto',
    url='https://github.com/ChipMcCallahan/CC1LevelsetProto',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=['cc1_levelset_proto'],
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='GNU General Public License v3.0',
    description='Protos and generated python files for working with CC1 levelsets.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
