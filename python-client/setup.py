import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gabriel-client",
    version="2.0.2",
    author="Roger Iyengar",
    author_email="ri@rogeriyengar.com",
    description="Networking components for Gabriel Python clients",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gabriel.cs.cmu.edu",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    license="Apache",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    install_requires=[
        "gabriel-protocol==2.0.1",
        "websockets==8.0; python_version>=\"3.6\"",
        "websockets==7.0; python_version<\"3.6\"",
        "opencv-python>=3, <5"
    ],
)
