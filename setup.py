from setuptools import setup, find_packages

setup(
    name = 'dbts',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(),
    install_requires = [
        # Github Private Repository - needs entry in `dependency_links`
        'https://github.com/schizommph/dtbs.py'
    ],

    dependency_links=[
        # Make sure to include the `#egg` portion so the `install_requires` recognizes the package
        'git+ssh://git@https://github.com/schizommph/dtbs.py#egg=dtbs-0.1'
		
    ]
)