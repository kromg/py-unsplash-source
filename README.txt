==================
Py Unsplash Source
==================

py_unsplash_source is a really really simple library to easily interface with
the source.unsplash.com service.
Typical usage often looks like this::

    #!/usr/bin/env python

    from py_unsplash_source import PyUnsplashSourceClient

    su = PyUnsplashSourceClient(width=1920, height=1080)

    # Random √
    image = (su.random_image()
             .daily()       # Or .weekly()
             .search('nature,landscape')).get()

    image.save_as('/tmp/random.jpg')

    # Random from a specific user √
    image = (su.image_from_user('gangdise')
             .from_likes()).get()

    image.save_as('/tmp/user.jpg')

    # Random from a collection √
    image = su.image_from_collection(145698).get()

    image.save_as('/tmp/collection.jpg')

    # Random from featured collection √
    image = (su.image_from_featured()
             .search('nature,landscape', 'sunset')).get()

    image.save_as('/tmp/featured.jpg')

    # Speficic image √
    image = su.image("ieic5Tq8YMk").get()

    image.save_as('/tmp/item.jpg')


