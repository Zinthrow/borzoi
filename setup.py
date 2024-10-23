from setuptools import setup, find_packages

# Attempt to use setuptools_scm for dynamic versioning if available
try:
    from setuptools_scm import get_version
    version = get_version()
except (ImportError, LookupError):
    version = "0.1.0"  # Fallback version if setuptools_scm is not available or not configured correctly

setup(
    name="borzoi",
    version=version,
    description="borzoi",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="David Kelley, Johannes Linder",
    author_email="drk@calicolabs.com",  # Choose a primary contact email or use a combined one
    url="https://github.com/calico/borzoi",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "h5py~=3.10.0",
        "intervaltree~=3.1.0",
        "joblib~=1.1.1",
        "matplotlib~=3.7.1",
        "google-cloud-storage~=2.0.0",
        "natsort~=7.1.1",
        "networkx~=2.8.4",
        "numpy~=1.24.3",
        "pandas~=1.5.3",
        "pybigwig~=0.3.18",
        "pybedtools~=0.10.0",
        "pysam~=0.22.0",
        "qnorm~=0.8.1",
        "seaborn~=0.12.2",
        "scikit-learn~=1.2.2",
        "scipy~=1.9.1",
        "tensorflow~=2.15.0",
        "tqdm~=4.65.0",
        "pyfaidx~=0.7.1",
        "pyranges~=0.0.129",
    ],
    extras_require={
        "dev": [
            "black~=23.12.1",
            "pytest~=7.4.4",
            "ruff~=0.1.11",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: Apache License",
    ],
    include_package_data=True,
    zip_safe=False,
    use_scm_version={"write_to": "borzoi/_version.py"}  # Optional: if you want to use SCM to write versions
)
