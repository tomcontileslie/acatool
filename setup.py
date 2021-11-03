import setuptools 

setuptools.setup( 
    name='acatool', 
    version='1.0', 
    author='Tom Conti-Leslie', 
    author_email='tom.contileslie@gmail.com', 
    description='Returns academy information about any French town', 
    packages=['acatool'],
    install_requires=[
        'requests'
    ],
    entry_points={ 
        'console_scripts': [ 
            'acatool = acatool.acatool:main' 
        ] 
    },
    package_data = {'acatool' : ['data/academies.csv', 'data/regions.csv']},
    include_package_data=True,
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)
