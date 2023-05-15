from pythonforandroid.recipe import Recipe


class TablesRecipe(Recipe):
    name = 'tables'
    version = '3.8.0'
    md5sum = '65f87a6feb06cced3f4760ef80263b1f'
    depends = ['setuptools','wheel','numpy','packaging','py-cpuinfo','Cython','blosc2 >=2.0.0']
    url = 'https://files.pythonhosted.org/packages/bc/42/07b37c0c64a13f005bfe95c8eec5f454fc8dd2caf85fa28add5b2a35b7ab/tables-3.8.0.tar.gz'
recipe = TablesRecipe()
