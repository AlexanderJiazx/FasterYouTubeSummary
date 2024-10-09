from setuptools import setup, find_packages
import os

# Read the long description from README.md
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fasteryoutubesummary',  # Name of your package
    version='3.1.0',               # Version number
    packages=find_packages(),      # Automatically find packages
    install_requires=[             # External dependencies
        'pytubefix',
        'groq',
        'requests',
        'click',                    # Added 'click' for CLI functionality
    ],
    entry_points={
        'console_scripts': [
            'fys=fasteryoutubesummary.cli:fys',  # Defines the 'fys' command
        ],
    },
    author='Alexander Jia',
    author_email='hellolightning321@gmail.com',
    description='Faster YouTube Summary is a tool designed to quickly generate detailed summaries of YouTube videos using Groq API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AlexanderJiazx/FasterYouTubeSummary',  # URL to your project
    classifiers=[                  # Additional metadata
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',       # Python version requirement
)
