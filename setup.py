from setuptools import setup

setup(
    name='pytorch_radon',
    version='0.1.4',
    author='Philipp Pelz',
    author_email='philipp.pelz@fau.de',
    packages=['pytorch_radon'],
    url='https://github.com/phernst/pytorch_radon.git',
    license='MIT',
    description='Pytorch implementation of scikit-image\'s radon function and more',
    install_requires=[
        "torch >= 0.4.0",
    ],
)
