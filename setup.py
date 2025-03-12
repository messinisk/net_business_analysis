from setuptools import setup, find_packages

setup(
    name="net_analysis",
    version="0.3.5a0",  # PEP 440 συμβατή έκδοση
    description="A package for financial analysis using numerical indicators.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="kostas messinis",
    author_email="messinisk35@gmail.com",
    url="https://github.com/messinisk/net_business_analysis",  # Αν έχεις GitHub repo
    packages=find_packages(include=["net_analysis", "net_analysis.*"]),
    python_requires=">=3.12.9",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Βεβαιώσου ότι ταιριάζει με την άδειά σου
    ],
)
