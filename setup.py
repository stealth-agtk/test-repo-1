from setuptools import setup, find_packages

setup(
    name="url_extras_package",
    version="0.1.0",
    packages=find_packages(),
    description="A package demonstrating URL-based extras dependencies",
    author="Your Name",
    author_email="your.email@example.com",
    # Regular dependencies
    install_requires=[
        "requests>=2.25.0",
    ],
    # Extras with different types of URL dependencies
    extras_require={
        "json_data": [
            "json_data @ https://example.com/path/to/json_data-0.1.0.zip",
        ],
        "monorepo_component": [
            "json_data @ git+https://github.com/stealth-agtk/test-repo-1.git@main#subdirectory=feature1",
        ],
    },
    # Make package include data files
    include_package_data=True,
    # Python requires
    python_requires=">=3.6",
    # Add classifiers for PyPI
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
