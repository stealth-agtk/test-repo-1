from setuptools import setup, find_namespace_packages

setup(
    name="feature1",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[],
    python_requires=">=3.6",
)