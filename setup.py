from setuptools import setup

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    requirement_field_name = 'requirement'
except ImportError:  # for pip <= 9.0.3
    requirement_field_name = 'req'

with open("requirements.txt") as f:
    dependencies = [line for line in f if "==" in line]

setup(
    name='zemberek_parser',
    version='1.1.1',
    packages=['core', 'core.kefir_', 'core.spellChecker', 'core.tika_', 'core.zemberek', 'core.zemberek.parser', 'core.zemberek.parser.tools', 'core.zemberek.parser.tools.ner', 'core.zemberek.parser.tools.pos', 'core.zemberek.parser.tools.stem', 'core.zemberek.parser.tools.tokenization', 'core.zemberek.parser.tools.translation', 'core.zemberek.parser.tools.word', 'core.zemberek.parser.tools.word2vec', 'core.zemberek_python', 'core.zemberek_python.main_libs', 'core.zemberek_python.settings'],
    url='https://github.com/kemalcanbora/zemberek_parser',
    license='BSD',
    package_data = { '' : ['zemberek-tum-2.0.jar']},
    author='Kemalcan Bora',
    author_email='kemalcanbora@gmail.com',
    description='zemberek kutuphanesinin lite python versiyonu',
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=dependencies


)
