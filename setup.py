from setuptools import setup

setup(
    name='chaos-guineapig',
    version='0.1',
    py_modules=['chaos_guineapig'],
    install_requires=[
        'click',
        'pyyaml'
    ],
    entry_points='''
        [console_scripts]
        chaos-guineapig=chaos_guineapig.guineapig:main
    ''',
)
