# Cloud Optimized GeoTIFF Validator
Simple [Cloud Optimized GeoTIFF](https://www.cogeo.org/) Validator. Just upload a file or paste a COG link to the text input and validate.

![COG Validator Demo](https://cogviewerapp.s3.eu-central-1.amazonaws.com/cogvalidator.gif)

## Details
The implementation designed to be as simple as possible. The validation code used is the one shared on [COG Developers Guide](https://www.cogeo.org/developers-guide.html) linking to [this source code](https://github.com/OSGeo/gdal/blob/master/gdal/swig/python/gdal-utils/osgeo_utils/samples/validate_cloud_optimized_geotiff.py) by [Even Rouault](https://twitter.com/EvenRouault).

### Known Limitations
- :warning: Max file size to upload is 200MB
