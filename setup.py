from setuptools import setup
from pip.req import parse_requirements
install_reqs = parse_requirements("requirements.txt", session='k')

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='zemberek_parser',
    version='1.0.0',
    packages=['zemberek_python'],
    url='https://github.com/kemalcanbora/zemberek_parser',
    license='BSD',
    author='Kemalcan Bora',
    author_email='kemalcanbora@gmail.com',
    description='zemberek kutuphanesinin lite python versiyonu',
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=reqs

)
