from setuptools import setup, find_packages

setup(
    name='fasteryoutubesummary',                    # Name of your package
    version='2.1.0',                      # Version number
    packages=find_packages(),             # Automatically find packages
    install_requires=[                    # External dependencies
        'pytubefix', 'groq', 'requests',               # Example of a dependency
    ],
    author='Alexander Jia',
    author_email='hellolightning321@gmail.com',
    description='Faster YouTube Summary is a tool designed to quickly generate detailed summaries of YouTube videos using Groq API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AlexanderJiazx/FasterYouTubeSummary',  # URL to your project
    classifiers=[                         # Additional metadata
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',              # Python version requirement
)