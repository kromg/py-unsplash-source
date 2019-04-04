# py-unsplash-source

Python library to get pictures from [source.unsplash.com](https://source.unsplash.com/).

**NOTE**: some APIs are still subject to change:
* getter names are being revised;
* the `width`/`height` methods could be joined into a single `geometry` method.  

## Quickstart

To download one or more images from [source.unsplash.com](https://source.unsplash.com/)
create the appropriate getter and call its `get()` method. 
Each time you call the `get()` method, a new picture will be downloaded, unless you're 
requesting a a specific image by id - in which case, you'll keep downloading
the same picture over and over again; the same applies to `daily` and `weekly` pictures, 
that will stay the same until the following day or week, of course. 

Where appropriate, getters support search terms.


### Get an image by id

```python

# Using getter directly
from py_unsplash_source.getters import ItemGetter

ig = (ItemGetter('zMyZrfcLXQE')
      .width(1920)          # Optional
      .height(1080)         # Optional
      )

image = ig.get()
image.save_as('image.jpg')


# Using getter factory
from py_unsplash_source import PyUnsplashSourceClient

su = PyUnsplashSourceClient()
ig = (su.item_getter('zMyZrfcLXQE')
      .width(1920)  # Optional
      .height(1080)  # Optional
      )
image = ig.get()
image.save_as('image.jpg')

```



### Get a random image

TBDocumented. Use `RandomGetter`


### Get a random image from a featured collection

TBDocumented. Use `FeaturedGetter`


### Get a random image from a specific collection

TBDocumented. Use `CollectionItemGetter`


### Get a random image from a user's collection

TBDocumented. Use `UserItemGetter`


### Get a random image from a user's likes

TBDocumented. Use `UserItemGetter` + `with_likes()` 