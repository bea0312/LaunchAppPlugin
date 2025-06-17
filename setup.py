from setuptools import setup, find_packages

setup(
    name="LaunchAppPlugin",
    version="0.1.0",
    author="Isabelle",
    author_email="icisamanda@gmail.com",
    description="A plugin to launch the GNOME calculator.",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'launch-calculator=launch_calculator:LaunchCalculator',
        ],
    },
)