from setuptools import setup, find_packages

VERSION = '0.3.2'
LONG_DESC = """\
Fullhistory for Django
"""

setup(name='fullhistory',
      version=VERSION,
      description="Fullhistory for Django",
      long_description=LONG_DESC,
      classifiers=[
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      keywords='django history',
      author='Jason Kraus, Rob Combs, Mark Ransom',
      author_email='zbyte64@gmail.com',
      url="https://github.com/cuker/django-fullhistory.git",
      install_requires=[
	  'Django>=1.2',
      ],
      packages=find_packages(exclude=['ez_setup', 'examples', 'testproject', 'tests']),
      include_package_data=True,
      zip_safe=False,
      test_suite="testproject.runtests.runtests",
      )
