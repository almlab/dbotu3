from setuptools import find_packages, setup

with open('README.md') as f:
    readme=f.read()

setup(name='dbotu',
    version='1.5.3',
    description='Distribution-based OTU calling',
    long_description=readme,
    author='Scott Olesen',
    author_email='swo@alum.mit.edu',
    platforms=['any'],
    license='License :: OSI Approved :: MIT License',
    url='http://github.com/almlab/dbotu3',
    scripts=['scripts/dbotu3.py', 'scripts/dbotu_restart.py', 'scripts/dbotu_rep_seqs.py'],
    install_requires=['numpy', 'pandas', 'scipy', 'biopython', 'python-Levenshtein'],
    package_data={'dbotu': ['data/input/counts.txt', 'data/input/seq.fa',
        'data/output/log.txt', 'data/output/membership.txt', 'data/output/otu.txt',
        'test/improper_data/counts.csv', 'test/improper_data/counts_biom.txt']},
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console',
        'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Bio-Informatics'],
    packages=find_packages()
    )
