from setuptools import setup, find_packages

setup(
    name='gunCultureAnalysisUSA',
    version='1.0.0',
    author='Group Name',
    url='githuburl',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4',
        'requests',
        'pandas',
        'plotly',
        'seaborn',
        'matplotlib',
        'scikit-learn',
        'numpy',
        'psycopg2-binary',
        'plotly-express',
        'PyYAML',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
