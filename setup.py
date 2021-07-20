from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='cc1_levelset_proto',
    url='https://github.com/ChipMcCallahan/CC1LevelsetProto',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=find_packages(),
    # Needed for dependencies
    install_requires=[],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='LICENSE',
    description='Protos and generated python files for working with CC1 levelsets.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
