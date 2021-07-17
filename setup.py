from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_descriptio = "\n" + fh.read()

VERSION = '0.0.11'
DESCRIPTION = ''

# Setting up
setup(
    name="TimeSeriesInterpretorRNN",
    version=VERSION,
    author="Dara Sravan Kumar",
    author_email="<sravandara007@gmail.com>",
    description=DESCRIPTION,
    long_description=long_descriptio,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["tensorflow==2.2","numpy","shap==0.39.0","pandas","plotly"],
    keywords=["RNNInterpretor","TimeSeriesInterpretor","TimeSeriesRNNInterpretor"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)