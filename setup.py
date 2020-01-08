from setuptools import setup

import versioneer

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    name="CANape",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python Module for Vector CANape",
    url="https://github.com/jed-frey/python_CANape",
    author="Jed Frey",
    author_email="",
    license="MIT",
    packages=["CANape"],
    setup_requires=["numpy"],
    tests_require=["pytest"],
    python_requires="<3.9,==3.*,>=3.5.0",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
)
