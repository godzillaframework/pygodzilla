import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygodzilla",
    version="1.0.0",
    author="Krisna Pranav",
    license="MIT",
    url="https://github.com/GodzillaFramework/pygodzilla",
    description="MicroService Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    package_dir={"": "."},
    install_requires=["pyzmq", "msgspec"],
)