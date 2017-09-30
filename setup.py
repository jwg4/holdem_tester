from setuptools import setup

setup(
    name='holdem_tester',
    version='0.0.1',
    description="Figure out the chance a Hold'em hand has of beating another.",
    url='https://github.com/jwg4/holdem_tester',
    author='Jack Grahl',
    author_email='jack.grahl@gmail.com',
    license='MIT',
    packages=["holdem"],
    install_requires=["deuces"],
    tests_module="test"
)
