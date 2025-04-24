from setuptools import setup, find_packages

setup(
    name='qutip_heom',
    version='0.1.0',
    description='Custom HEOM solver for non-Markovian quantum systems using QuTiP.',
    author='Intrafere',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20',
        'scipy>=1.5',
        'qutip>=4.6'
    ],
    python_requires='>=3.7',
)
