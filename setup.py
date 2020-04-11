from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='reverse_int',
      version='0.3',
      description='A Simpler lib to Reverse integer',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Arinze1020/reverse_int.git',
      author='Ugwuanyi Arinze',
      author_email='arinzeugwuanyi@gmail.com',
      license='MIT',
      packages=['reverse_int'],
      zip_safe=False,
      
    classifiers=[
        'Development Status :: 4 - Beta',  
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   
        'Programming Language :: Python :: 3',      
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
      
      
    )