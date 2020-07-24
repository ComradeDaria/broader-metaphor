from setuptools import setup, find_packages
import sys


if sys.version_info[0] == 3:
    requires = [
        "xgboost==0.80",
        "tqdm==4.28.1",
        "sklearn2==0.0.11",
        "scipy==1.1.0",
        "numpy==1.14.3",
        "pandas==0.23.4",
        "spacy==2.0.18",
        "allennlp==0.7.1",
    ]
else:
    requires = [
        "xgboost==0.80",
        "tqdm==4.28.1",
        "sklearn2==0.0.11",
        "scipy==1.1.0",
        "numpy==1.14.3",
        "pandas==0.23.4",
        "spacy==2.0.18",
    ]

tests_require = [
]

setup(
    name="broader_metaphor",
    version="0.0.1",
    include_package_data=True,
    zip_safe=False,
    extras_require={"testing": tests_require},
    install_requires=requires,
    entry_points={
    },
)
