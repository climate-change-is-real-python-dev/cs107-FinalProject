import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()


setuptools.setup(
	name="socialAD",
	version="0.1.2",
	scripts=["socialAD"],
	author="Ju Chulakadabba, Tao Tsui, Jenny Wang, Dash Young-Saver",
	author_email="ywang1@hsph.harvard.edu",
	dscription="Autodifferentiation",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/climate-change-is-real-python-dev",
	packages=setuptools.find_packages(),
	classifiers=[
	"Programming Language :: Python :: 3",
	"License :: OSI Approved :: MIT License",
	"Operating System :: OS Independent",
	],
)