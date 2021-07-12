import streamlit as st
import os.path
from urllib.parse import urlparse
import struct
import sys
from osgeo import gdal

import validate_cloud_optimized_geotiff as validator

CHECK_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/check-box-with-check_2611-fe0f.png"


# Set page title and favicon.
st.set_page_config(
    page_title="COG Validator", 
    page_icon=CHECK_EMOJI_URL,
    layout="wide"
)

# Display header.
st.markdown("<br>", unsafe_allow_html=True)
st.image(CHECK_EMOJI_URL, width=80)

"""
# Cloud Optimized GeoTIFF Validator
"""



col1, col2 = st.beta_columns([1,1])
source = st.radio("Select the source of your Cloud Optimized GeoTIFF",('Local file', 'Link to remote file'))

uploaded_file = None
cog_link = None

def is_file_url(url):
    path = urlparse(cog_link)
    filename = os.path.basename(path.path)
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[-1]
    return ext in {'tiff', 'tif'}


def is_url(url):
  try:
    path = urlparse(cog_link)
    return all([path.scheme, path.netloc])
  except ValueError:
    return False

if source == 'Local file':
    uploaded_file = st.file_uploader("Choose a COG file", type=['tif','tiff'])
    if uploaded_file is not None:
        if st.button('Validate'):
            with st.spinner('Validating your file...'):
                ds = validator.readFile(uploaded_file)
                filename = uploaded_file.name
                validator.main_validate(ds, filename)
elif source == 'Link to remote file':
    cog_link = st.text_input("Insert a URL of your COG file")
    if cog_link is not '':
        if st.button('Validate'):
            if is_url(cog_link) is True: # Checking if the text input is the link
                if is_file_url(cog_link) is True: # Checking if the link pointing on GeoTIFF file
                    with st.spinner('Validating your file...'):
                        ds = validator.readURL(cog_link)
                        a = urlparse(cog_link)
                        filename = os.path.basename(a.path)    
                        validator.main_validate(ds, filename)
                else:
                    st.error('The file extension is not GeoTIFF.')
            else:
                st.error('The link is not valid.')

"""
---
[![Follow](https://img.shields.io/twitter/follow/mykolakozyr?style=social)](https://www.twitter.com/mykolakozyr)
&nbsp[![Follow](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/mykolakozyr/)
&nbsp[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/mykolakozyr)

## Details
The implementation designed to be as simple as possible. The validation code used is the one shared on [COG Developers Guide](https://www.cogeo.org/developers-guide.html) linking to [this source code](https://github.com/OSGeo/gdal/blob/master/gdal/swig/python/gdal-utils/osgeo_utils/samples/validate_cloud_optimized_geotiff.py) by [Even Rouault](https://twitter.com/EvenRouault).
"""

with st.beta_expander("Quality Assurance"):
    st.write("✅ Tested on Google Chrome Version 91.0.4472.114")
    st.write("✅ COG uploaded locally")
    st.write("✅ COG stored on AWS")
with st.beta_expander("Known Limitations"):
    st.write(":warning: Max file size to upload is 200MB")