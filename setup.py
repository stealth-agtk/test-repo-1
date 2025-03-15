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
        # Standard package extra
        'standard': ["numpy"],
        
        # File URL extras (zip, tar.gz)
        'json_data': [
            'https://example.com/path/to/json_data-0.1.0.zip',  # Zip file with JSON data
        ],
        
        # Git repository extra
        'git_component': [
            'git+https://github.com/user/repo.git@main#egg=git_component',  # Basic Git repo
        ],
        
        # Git repository with subdirectory (monorepo example)
        'monorepo_component': [
            'git+https://github.com/stealth-agtk/test-repo-1.git@main#egg=json_data&subdirectory=examples/json_data_package',
        ],
        
        # Combinations
        'complete': [
            'numpy',
            'https://example.com/path/to/json_data-0.1.0.zip',
            'git+https://github.com/user/repo.git@main#egg=git_component',
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
