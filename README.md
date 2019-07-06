# py-unsplash-source

Python library to get pictures from [source.unsplash.com](https://source.unsplash.com/).
  

## Quickstart

### Installation

* Latest version from sources:

```bash
git clone https://github.com/kromg/py-unsplash-source.git
cd py-unsplash-source
python3 setup.py install
```


* Release from PyPI:

```bash
pip install py_unsplash_source
```

### Usage

**NOTE**: see examples in the `sample` directory for a quick startup. 

To download one or more images from [source.unsplash.com](https://source.unsplash.com/)
create the appropriate getter and call its `get()` method. 
Each time you call the `get()` method, a new picture will be downloaded, unless you're 
requesting a a specific image by id - in which case, you'll keep downloading
the same picture over and over again; the same applies to `daily` and `weekly` pictures, 
that will stay the same until the following day or week, of course. 

Where appropriate, getters support search terms.


#### Get an image by id

```python
from py_unsplash_source.getters import ImageGetter

ig = (ImageGetter('zMyZrfcLXQE')
      .geometry(1920, 1080)         # Optional
      )

image = ig.get()
image.save_as('image.jpg')
```


#### Get a random image

```python
# Using getter directly:
from py_unsplash_source.getters import RandomImageGetter

# Search for an image
ig = (RandomImageGetter()
      .geometry(1920, 1080)             # Optional
      .search('python, programing')     # Optional
      )

image = ig.get()
image.save_as('image.jpg')

# Get the daily image
ig = (RandomImageGetter()
      .geometry(1920, 1080)             # Optional
      .search('programming')
      .daily()
      )

image = ig.get()
image.save_as('daily.jpg')

# Get the weekly image
ig = (RandomImageGetter()
      .geometry(1920, 1080)             # Optional
      .search('programming')
      .weekly()
      )

image = ig.get()
image.save_as('weekly.jpg')
```


#### Get a random image from a featured collection

```python
from py_unsplash_source.getters import ImageFromFeaturedGetter

# Search for an image
ig = (ImageFromFeaturedGetter()
      .geometry(1920, 1080)             # Optional
      .search('python, programing')     # Optional
      )

image = ig.get()
image.save_as('image.jpg')

# Get the daily image
ig = (ImageFromFeaturedGetter()
      .geometry(1920, 1080)             # Optional
      .search('programming')
      .daily()
      )

image = ig.get()
image.save_as('daily.jpg')

# Get the weekly image
ig = (ImageFromFeaturedGetter()
      .geometry(1920, 1080)             # Optional
      .search('programming')
      .weekly()
      )

image = ig.get()
image.save_as('weekly.jpg')
```


#### Get a random image from a specific collection

```python
from py_unsplash_source.getters import ImageFromCollectionGetter

# Search for an image
ig = (ImageFromCollectionGetter(416021)
      .geometry(1920, 1080)             # Optional
      .search('abstract')     # Optional
      )

image = ig.get()
image.save_as('image.jpg')

# Get the daily image
ig = (ImageFromCollectionGetter(416021)
      .geometry(1920, 1080)             # Optional
      .search('abstract')
      .daily()
      )

image = ig.get()
image.save_as('daily.jpg')

# Get the weekly image
ig = (ImageFromCollectionGetter(416021)
      .geometry(1920, 1080)             # Optional
      .search('abstract')
      .weekly()
      )

image = ig.get()
image.save_as('weekly.jpg')
```


#### Get a random image from a user's collection

```python
from py_unsplash_source.getters import ImageFromUserGetter

# Search for an image
ig = (ImageFromUserGetter('@karishea')    # Leading '@' can be omitted, it's removed anyway
      .geometry(1920, 1080)               # Optional
      .search('wallpaper')                # Optional
      )

image = ig.get()
image.save_as('image.jpg')

# Get the daily image
ig = (ImageFromUserGetter('@karishea')
      .geometry(1920, 1080)               # Optional
      .search('wallpaper')                # Optional
      .daily()
      )

image = ig.get()
image.save_as('daily.jpg')

# Get the weekly image
ig = (ImageFromUserGetter('@karishea')      # Leading '@' can be omitted, it's removed anyway
      .geometry(1920, 1080)                 # Optional
      .search('wallpaper')                  # Optional
      .weekly()
      )

image = ig.get()
image.save_as('weekly.jpg')
```


#### Get a random image from a user's likes

```python
from py_unsplash_source.getters import ImageFromUserGetter

# Search for an image
ig = (ImageFromUserGetter('@karishea')    # Leading '@' can be omitted, it's removed anyway
      .geometry(1920, 1080)               # Optional
      .from_likes()
      # .search('no no no')     # Search terms are ignored with "from_likes()"
      # .daily()                # daily() and weekly() are ignored with "from_likes()"
      # .weekly()               # daily() and weekly() are ignored with "from_likes()"
      )

image = ig.get()
image.save_as('image.jpg')
```


#### Use the getter factory

```python
from py_unsplash_source import PyUnsplashSourceClient

# Initialize factory - accepts optional geometry for all generated getters
c = PyUnsplashSourceClient(1920, 1080)

# Get an ImageGetter
ig = c.image('zMyZrfcLXQE')

# Get a RandomImageGetter
rig = c.random_image()

# Get an ImageFromFeaturedGetter
iffg = c.image_from_featured()

# Get an ImageFromCollectionGetter
ifcg = c.image_from_collection(416021)

# Get an ImageFromUserGetter
ifug = c.image_from_user('@karishea')

# then use the getters as in examples above
```
