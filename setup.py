try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

long_desc = """
	GTD to CSV is a simple free program that converts GTD style event/task text files to a CSV format that Heap CRM and Torch Project Management can import as events and tasks.
"""


setup(name="GTDtoCSV",
      version=1.0,
      description="Convert GTD style events to CSV",
      author="Ben Smith",
      author_email="ben@wbpsystems.com",
      url="https://github.com/tazzben/GTDtoCSV",
      license="MIT",
      packages=[],
      scripts=['GTDtoCSV'],
      package_dir={},
      long_description=long_desc,
      classifiers=[
          'Topic :: Text Processing',
          'Environment :: Console',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: POSIX',
          'Intended Audience :: Developers',
          'Intended Audience :: End Users/Desktop'
      ]
     )