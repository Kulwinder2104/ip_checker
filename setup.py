from setuptools import setup, find_packages

setup(
    name="ip_checker",
    version="1.0",
    packages=find_packages(),
    install_requires=[],  # No external dependencies for this project
    entry_points={
        "console_scripts": [
            "ip-checker=ip_checker.ip_checker:fetch_ip",
        ]
    },
    author="Kulwinder Kaur",
    description="A simple IP address checker app",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://your-github-or-website-url",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
