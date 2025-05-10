from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-simple-email-sender",
    version="1.0.0",
    author='Avi Zaguri',
    author_email="",
    description="Enhanced Gmail sender",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aviz92/python-simple-email-sender",
    project_urls={
        'Repository': 'https://github.com/aviz92/python-simple-email-sender',
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.9",
    install_requires=[
        'setuptools',
        'wheel',
        'dotenv',
        "custom-python-logger>=0.1.4",
    ],
    keywords="email, gmail, smtplib",
)
