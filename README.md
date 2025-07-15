# 1. Setup project

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

---
## Project Structure

* `notebook/`: analysis and prototyping
* `scripts/`: reusable Python modules
* `data/`: local shapefiles and input data
* `output/`: generated maps and results

SAR/
├─ data/
│  ├─ aoi/
│  │  ├─ aoi_1km7x14_3035.cpg
│  │  ├─ aoi_1km7x14_3035.dbf
│  │  ├─ aoi_1km7x14_3035.prj
│  │  ├─ aoi_1km7x14_3035.qmd
│  │  ├─ aoi_1km7x14_3035.shp
│  │  └─ aoi_1km7x14_3035.shx
│  ├─ csv/
│  └─ raster/
├─ doc/
│  ├─ sar_moisture/
│  │  ├─ 2505.00265v1.pdf
│  │  └─ remotesensing-17-00542.pdf
│  └─ var/
├─ notebook/
│  └─ 1_s1_moisture.ipynb
├─ output/
│  ├─ s1/
│  │  └─ sar_vv_2024_04_09.tif
│  └─ var/
├─ scripts/
│  ├─ __pycache__/
│  │  ├─ aoi_loader.cpython-312.pyc
│  │  └─ download_s1.cpython-312.pyc
│  ├─ __init__.py
│  ├─ aoi_loader.py
│  ├─ conv_db_sm.py
│  └─ download_s1.py
├─ utils/
│  └─ config.py
├─ venv/
│  ├─ etc/
│  │  └─ jupyter/
│  │     └─ nbconfig/
│  │        └─ notebook.d/
│  │           ├─ bqplot.json
│  │           ├─ ipyevents.json
│  │           ├─ ipytree.json
│  │           ├─ jupyter-leaflet.json
│  │           └─ widgetsnbextension.json
│  ├─ Include/
│  ├─ Lib/
│  │  └─ site-packages/
│  │     ├─ __pycache__/
│  │     │  ├─ click_plugins.cpython-312.pyc
│  │     │  ├─ colour.cpython-312.pyc
│  │     │  ├─ decorator.cpython-312.pyc
│  │     │  ├─ google_auth_httplib2.cpython-312.pyc
│  │     │  ├─ ipykernel_launcher.cpython-312.pyc
│  │     │  ├─ ipython_pygments_lexers.cpython-312.pyc
│  │     │  ├─ jupyter.cpython-312.pyc
│  │     │  ├─ nest_asyncio.cpython-312.pyc
│  │     │  ├─ pylab.cpython-312.pyc
│  │     │  ├─ pythoncom.cpython-312.pyc
│  │     │  ├─ shapefile.cpython-312.pyc
│  │     │  └─ six.cpython-312.pyc
│  │     ├─ _distutils_hack/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ override.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ override.py
│  │     ├─ _plotly_utils/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ basevalidators.cpython-312.pyc
│  │     │  │  ├─ data_utils.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ files.cpython-312.pyc
│  │     │  │  ├─ importers.cpython-312.pyc
│  │     │  │  ├─ optional_imports.cpython-312.pyc
│  │     │  │  ├─ png.cpython-312.pyc
│  │     │  │  └─ utils.cpython-312.pyc
│  │     │  ├─ colors/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _swatches.cpython-312.pyc
│  │     │  │  │  ├─ carto.cpython-312.pyc
│  │     │  │  │  ├─ cmocean.cpython-312.pyc
│  │     │  │  │  ├─ colorbrewer.cpython-312.pyc
│  │     │  │  │  ├─ cyclical.cpython-312.pyc
│  │     │  │  │  ├─ diverging.cpython-312.pyc
│  │     │  │  │  ├─ plotlyjs.cpython-312.pyc
│  │     │  │  │  ├─ qualitative.cpython-312.pyc
│  │     │  │  │  └─ sequential.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _swatches.py
│  │     │  │  ├─ carto.py
│  │     │  │  ├─ cmocean.py
│  │     │  │  ├─ colorbrewer.py
│  │     │  │  ├─ cyclical.py
│  │     │  │  ├─ diverging.py
│  │     │  │  ├─ plotlyjs.py
│  │     │  │  ├─ qualitative.py
│  │     │  │  └─ sequential.py
│  │     │  ├─ __init__.py
│  │     │  ├─ basevalidators.py
│  │     │  ├─ data_utils.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ files.py
│  │     │  ├─ importers.py
│  │     │  ├─ optional_imports.py
│  │     │  ├─ png.py
│  │     │  └─ utils.py
│  │     ├─ adodbapi/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ ado_consts.cpython-312.pyc
│  │     │  │  ├─ adodbapi.cpython-312.pyc
│  │     │  │  ├─ apibase.cpython-312.pyc
│  │     │  │  ├─ is64bit.cpython-312.pyc
│  │     │  │  ├─ process_connect_string.cpython-312.pyc
│  │     │  │  ├─ schema_table.cpython-312.pyc
│  │     │  │  └─ setup.cpython-312.pyc
│  │     │  ├─ examples/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ db_print.cpython-312.pyc
│  │     │  │  │  ├─ db_table_names.cpython-312.pyc
│  │     │  │  │  ├─ xls_read.cpython-312.pyc
│  │     │  │  │  └─ xls_write.cpython-312.pyc
│  │     │  │  ├─ db_print.py
│  │     │  │  ├─ db_table_names.py
│  │     │  │  ├─ xls_read.py
│  │     │  │  └─ xls_write.py
│  │     │  ├─ test/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ adodbapitest.cpython-312.pyc
│  │     │  │  │  ├─ adodbapitestconfig.cpython-312.pyc
│  │     │  │  │  ├─ dbapi20.cpython-312.pyc
│  │     │  │  │  ├─ is64bit.cpython-312.pyc
│  │     │  │  │  ├─ setuptestframework.cpython-312.pyc
│  │     │  │  │  ├─ test_adodbapi_dbapi20.cpython-312.pyc
│  │     │  │  │  └─ tryconnection.cpython-312.pyc
│  │     │  │  ├─ adodbapitest.py
│  │     │  │  ├─ adodbapitestconfig.py
│  │     │  │  ├─ dbapi20.py
│  │     │  │  ├─ is64bit.py
│  │     │  │  ├─ setuptestframework.py
│  │     │  │  ├─ test_adodbapi_dbapi20.py
│  │     │  │  └─ tryconnection.py
│  │     │  ├─ __init__.py
│  │     │  ├─ ado_consts.py
│  │     │  ├─ adodbapi.py
│  │     │  ├─ apibase.py
│  │     │  ├─ is64bit.py
│  │     │  ├─ license.txt
│  │     │  ├─ process_connect_string.py
│  │     │  ├─ readme.txt
│  │     │  ├─ schema_table.py
│  │     │  └─ setup.py
│  │     ├─ affine/
│  │     │  ├─ __pycache__/
│  │     │  │  └─ __init__.cpython-312.pyc
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  ├─ test_rotation.cpython-312.pyc
│  │     │  │  │  ├─ test_serialize.cpython-312.pyc
│  │     │  │  │  └─ test_transform.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ test_pickle.py
│  │     │  │  ├─ test_rotation.py
│  │     │  │  ├─ test_serialize.py
│  │     │  │  └─ test_transform.py
│  │     │  └─ __init__.py
│  │     ├─ affine-2.4.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ apiclient/
│  │     │  ├─ __pycache__/
│  │     │  │  └─ __init__.cpython-312.pyc
│  │     │  └─ __init__.py
│  │     ├─ asttokens/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ astroid_compat.cpython-312.pyc
│  │     │  │  ├─ asttokens.cpython-312.pyc
│  │     │  │  ├─ line_numbers.cpython-312.pyc
│  │     │  │  ├─ mark_tokens.cpython-312.pyc
│  │     │  │  ├─ util.cpython-312.pyc
│  │     │  │  └─ version.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ astroid_compat.py
│  │     │  ├─ asttokens.py
│  │     │  ├─ line_numbers.py
│  │     │  ├─ mark_tokens.py
│  │     │  ├─ py.typed
│  │     │  ├─ util.py
│  │     │  └─ version.py
│  │     ├─ asttokens-3.0.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ attr/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _cmp.cpython-312.pyc
│  │     │  │  ├─ _compat.cpython-312.pyc
│  │     │  │  ├─ _config.cpython-312.pyc
│  │     │  │  ├─ _funcs.cpython-312.pyc
│  │     │  │  ├─ _make.cpython-312.pyc
│  │     │  │  ├─ _next_gen.cpython-312.pyc
│  │     │  │  ├─ _version_info.cpython-312.pyc
│  │     │  │  ├─ converters.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ filters.cpython-312.pyc
│  │     │  │  ├─ setters.cpython-312.pyc
│  │     │  │  └─ validators.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  ├─ _cmp.py
│  │     │  ├─ _cmp.pyi
│  │     │  ├─ _compat.py
│  │     │  ├─ _config.py
│  │     │  ├─ _funcs.py
│  │     │  ├─ _make.py
│  │     │  ├─ _next_gen.py
│  │     │  ├─ _typing_compat.pyi
│  │     │  ├─ _version_info.py
│  │     │  ├─ _version_info.pyi
│  │     │  ├─ converters.py
│  │     │  ├─ converters.pyi
│  │     │  ├─ exceptions.py
│  │     │  ├─ exceptions.pyi
│  │     │  ├─ filters.py
│  │     │  ├─ filters.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ setters.py
│  │     │  ├─ setters.pyi
│  │     │  ├─ validators.py
│  │     │  └─ validators.pyi
│  │     ├─ attrs/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ converters.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ filters.cpython-312.pyc
│  │     │  │  ├─ setters.cpython-312.pyc
│  │     │  │  └─ validators.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  ├─ converters.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ filters.py
│  │     │  ├─ py.typed
│  │     │  ├─ setters.py
│  │     │  └─ validators.py
│  │     ├─ attrs-25.3.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ box/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ box_list.cpython-312.pyc
│  │     │  │  ├─ box.cpython-312.pyc
│  │     │  │  ├─ config_box.cpython-312.pyc
│  │     │  │  ├─ converters.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ from_file.cpython-312.pyc
│  │     │  │  └─ shorthand_box.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ box_list.c
│  │     │  ├─ box_list.cp312-win_amd64.pyd
│  │     │  ├─ box_list.py
│  │     │  ├─ box_list.pyi
│  │     │  ├─ box.c
│  │     │  ├─ box.cp312-win_amd64.pyd
│  │     │  ├─ box.py
│  │     │  ├─ box.pyi
│  │     │  ├─ config_box.c
│  │     │  ├─ config_box.cp312-win_amd64.pyd
│  │     │  ├─ config_box.py
│  │     │  ├─ config_box.pyi
│  │     │  ├─ converters.c
│  │     │  ├─ converters.cp312-win_amd64.pyd
│  │     │  ├─ converters.py
│  │     │  ├─ converters.pyi
│  │     │  ├─ exceptions.c
│  │     │  ├─ exceptions.cp312-win_amd64.pyd
│  │     │  ├─ exceptions.py
│  │     │  ├─ exceptions.pyi
│  │     │  ├─ from_file.c
│  │     │  ├─ from_file.cp312-win_amd64.pyd
│  │     │  ├─ from_file.py
│  │     │  ├─ from_file.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ shorthand_box.c
│  │     │  ├─ shorthand_box.cp312-win_amd64.pyd
│  │     │  ├─ shorthand_box.py
│  │     │  └─ shorthand_box.pyi
│  │     ├─ bqplot/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ axes.cpython-312.pyc
│  │     │  │  ├─ colorschemes.cpython-312.pyc
│  │     │  │  ├─ default_tooltip.cpython-312.pyc
│  │     │  │  ├─ figure.cpython-312.pyc
│  │     │  │  ├─ install.cpython-312.pyc
│  │     │  │  ├─ interacts.cpython-312.pyc
│  │     │  │  ├─ market_map.cpython-312.pyc
│  │     │  │  ├─ marks.cpython-312.pyc
│  │     │  │  ├─ plotting_widgets.cpython-312.pyc
│  │     │  │  ├─ pyplot.cpython-312.pyc
│  │     │  │  ├─ scales.cpython-312.pyc
│  │     │  │  ├─ toolbar.cpython-312.pyc
│  │     │  │  └─ traits.cpython-312.pyc
│  │     │  ├─ map_data/
│  │     │  │  ├─ EuropeMap.json
│  │     │  │  ├─ USCountiesMap.json
│  │     │  │  ├─ USStatesMap.json
│  │     │  │  └─ WorldMap.json
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  ├─ axes.py
│  │     │  ├─ colorschemes.py
│  │     │  ├─ default_tooltip.py
│  │     │  ├─ figure.py
│  │     │  ├─ install.py
│  │     │  ├─ interacts.py
│  │     │  ├─ market_map.py
│  │     │  ├─ marks.py
│  │     │  ├─ plotting_widgets.py
│  │     │  ├─ pyplot.py
│  │     │  ├─ scales.py
│  │     │  ├─ toolbar.py
│  │     │  └─ traits.py
│  │     ├─ bqplot-0.12.45.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ branca/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ colormap.cpython-312.pyc
│  │     │  │  ├─ element.cpython-312.pyc
│  │     │  │  └─ utilities.cpython-312.pyc
│  │     │  ├─ templates/
│  │     │  │  └─ color_scale.js
│  │     │  ├─ __init__.py
│  │     │  ├─ _cnames.json
│  │     │  ├─ _schemes.json
│  │     │  ├─ _version.py
│  │     │  ├─ colormap.py
│  │     │  ├─ element.py
│  │     │  ├─ py.typed
│  │     │  ├─ scheme_base_codes.json
│  │     │  ├─ scheme_info.json
│  │     │  └─ utilities.py
│  │     ├─ branca-0.8.1.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ cachetools/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _decorators.cpython-312.pyc
│  │     │  │  ├─ func.cpython-312.pyc
│  │     │  │  └─ keys.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ _decorators.py
│  │     │  ├─ func.py
│  │     │  └─ keys.py
│  │     ├─ cachetools-5.5.2.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ certifi/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  └─ core.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ cacert.pem
│  │     │  ├─ core.py
│  │     │  └─ py.typed
│  │     ├─ certifi-2025.7.14.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ charset_normalizer/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ api.cpython-312.pyc
│  │     │  │  ├─ cd.cpython-312.pyc
│  │     │  │  ├─ constant.cpython-312.pyc
│  │     │  │  ├─ legacy.cpython-312.pyc
│  │     │  │  ├─ md.cpython-312.pyc
│  │     │  │  ├─ models.cpython-312.pyc
│  │     │  │  ├─ utils.cpython-312.pyc
│  │     │  │  └─ version.cpython-312.pyc
│  │     │  ├─ cli/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __main__.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __main__.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ api.py
│  │     │  ├─ cd.py
│  │     │  ├─ constant.py
│  │     │  ├─ legacy.py
│  │     │  ├─ md__mypyc.cp312-win_amd64.pyd
│  │     │  ├─ md.cp312-win_amd64.pyd
│  │     │  ├─ md.py
│  │     │  ├─ models.py
│  │     │  ├─ py.typed
│  │     │  ├─ utils.py
│  │     │  └─ version.py
│  │     ├─ charset_normalizer-3.4.2.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ click/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _compat.cpython-312.pyc
│  │     │  │  ├─ _termui_impl.cpython-312.pyc
│  │     │  │  ├─ _textwrap.cpython-312.pyc
│  │     │  │  ├─ _winconsole.cpython-312.pyc
│  │     │  │  ├─ core.cpython-312.pyc
│  │     │  │  ├─ decorators.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ formatting.cpython-312.pyc
│  │     │  │  ├─ globals.cpython-312.pyc
│  │     │  │  ├─ parser.cpython-312.pyc
│  │     │  │  ├─ shell_completion.cpython-312.pyc
│  │     │  │  ├─ termui.cpython-312.pyc
│  │     │  │  ├─ testing.cpython-312.pyc
│  │     │  │  ├─ types.cpython-312.pyc
│  │     │  │  └─ utils.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _termui_impl.py
│  │     │  ├─ _textwrap.py
│  │     │  ├─ _winconsole.py
│  │     │  ├─ core.py
│  │     │  ├─ decorators.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ formatting.py
│  │     │  ├─ globals.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ shell_completion.py
│  │     │  ├─ termui.py
│  │     │  ├─ testing.py
│  │     │  ├─ types.py
│  │     │  └─ utils.py
│  │     ├─ click_plugins/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ core.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ core.py
│  │     ├─ click_plugins-1.1.1.2.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  ├─ AUTHORS.txt
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ click-8.2.1.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ cligj/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ features.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ features.py
│  │     ├─ cligj-0.7.2.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ colorama/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ ansi.cpython-312.pyc
│  │     │  │  ├─ ansitowin32.cpython-312.pyc
│  │     │  │  ├─ initialise.cpython-312.pyc
│  │     │  │  ├─ win32.cpython-312.pyc
│  │     │  │  └─ winterm.cpython-312.pyc
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ ansi_test.cpython-312.pyc
│  │     │  │  │  ├─ ansitowin32_test.cpython-312.pyc
│  │     │  │  │  ├─ initialise_test.cpython-312.pyc
│  │     │  │  │  ├─ isatty_test.cpython-312.pyc
│  │     │  │  │  ├─ utils.cpython-312.pyc
│  │     │  │  │  └─ winterm_test.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ ansi_test.py
│  │     │  │  ├─ ansitowin32_test.py
│  │     │  │  ├─ initialise_test.py
│  │     │  │  ├─ isatty_test.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ winterm_test.py
│  │     │  ├─ __init__.py
│  │     │  ├─ ansi.py
│  │     │  ├─ ansitowin32.py
│  │     │  ├─ initialise.py
│  │     │  ├─ win32.py
│  │     │  └─ winterm.py
│  │     ├─ colorama-0.4.6.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ colour-0.1.5.dist-info/
│  │     │  ├─ DESCRIPTION.rst
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ metadata.json
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ comm/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ base_comm.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ base_comm.py
│  │     │  └─ py.typed
│  │     ├─ comm-0.2.2.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ contourpy/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ array.cpython-312.pyc
│  │     │  │  ├─ chunk.cpython-312.pyc
│  │     │  │  ├─ convert.cpython-312.pyc
│  │     │  │  ├─ dechunk.cpython-312.pyc
│  │     │  │  ├─ enum_util.cpython-312.pyc
│  │     │  │  ├─ typecheck.cpython-312.pyc
│  │     │  │  └─ types.cpython-312.pyc
│  │     │  ├─ util/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _build_config.cpython-312.pyc
│  │     │  │  │  ├─ bokeh_renderer.cpython-312.pyc
│  │     │  │  │  ├─ bokeh_util.cpython-312.pyc
│  │     │  │  │  ├─ data.cpython-312.pyc
│  │     │  │  │  ├─ mpl_renderer.cpython-312.pyc
│  │     │  │  │  ├─ mpl_util.cpython-312.pyc
│  │     │  │  │  └─ renderer.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _build_config.py
│  │     │  │  ├─ bokeh_renderer.py
│  │     │  │  ├─ bokeh_util.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ mpl_renderer.py
│  │     │  │  ├─ mpl_util.py
│  │     │  │  └─ renderer.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _contourpy.cp312-win_amd64.lib
│  │     │  ├─ _contourpy.cp312-win_amd64.pyd
│  │     │  ├─ _contourpy.pyi
│  │     │  ├─ _version.py
│  │     │  ├─ array.py
│  │     │  ├─ chunk.py
│  │     │  ├─ convert.py
│  │     │  ├─ dechunk.py
│  │     │  ├─ enum_util.py
│  │     │  ├─ py.typed
│  │     │  ├─ typecheck.py
│  │     │  └─ types.py
│  │     ├─ contourpy-1.3.2.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ cycler/
│  │     │  ├─ __pycache__/
│  │     │  │  └─ __init__.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  └─ py.typed
│  │     ├─ cycler-0.12.1.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ dateutil/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _common.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ easter.cpython-312.pyc
│  │     │  │  ├─ relativedelta.cpython-312.pyc
│  │     │  │  ├─ rrule.cpython-312.pyc
│  │     │  │  ├─ tzwin.cpython-312.pyc
│  │     │  │  └─ utils.cpython-312.pyc
│  │     │  ├─ parser/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _parser.cpython-312.pyc
│  │     │  │  │  └─ isoparser.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _parser.py
│  │     │  │  └─ isoparser.py
│  │     │  ├─ tz/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _common.cpython-312.pyc
│  │     │  │  │  ├─ _factories.cpython-312.pyc
│  │     │  │  │  ├─ tz.cpython-312.pyc
│  │     │  │  │  └─ win.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _common.py
│  │     │  │  ├─ _factories.py
│  │     │  │  ├─ tz.py
│  │     │  │  └─ win.py
│  │     │  ├─ zoneinfo/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ rebuild.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dateutil-zoneinfo.tar.gz
│  │     │  │  └─ rebuild.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _common.py
│  │     │  ├─ _version.py
│  │     │  ├─ easter.py
│  │     │  ├─ relativedelta.py
│  │     │  ├─ rrule.py
│  │     │  ├─ tzwin.py
│  │     │  └─ utils.py
│  │     ├─ debugpy/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  └─ public_api.cpython-312.pyc
│  │     │  ├─ _vendored/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _pydevd_packaging.cpython-312.pyc
│  │     │  │  │  ├─ _util.cpython-312.pyc
│  │     │  │  │  └─ force_pydevd.cpython-312.pyc
│  │     │  │  ├─ pydevd/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ pydev_app_engine_debug_startup.cpython-312.pyc
│  │     │  │  │  │  ├─ pydev_coverage.cpython-312.pyc
│  │     │  │  │  │  ├─ pydev_pysrc.cpython-312.pyc
│  │     │  │  │  │  ├─ pydev_run_in_console.cpython-312.pyc
│  │     │  │  │  │  ├─ pydevconsole.cpython-312.pyc
│  │     │  │  │  │  ├─ pydevd_file_utils.cpython-312.pyc
│  │     │  │  │  │  ├─ pydevd_tracing.cpython-312.pyc
│  │     │  │  │  │  ├─ pydevd.cpython-312.pyc
│  │     │  │  │  │  └─ setup_pydevd_cython.cpython-312.pyc
│  │     │  │  │  ├─ _pydev_bundle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_calltip_util.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_completer.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_execfile.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_filesystem_encoding.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_getopt.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_imports_tipper.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_jy_imports_tipper.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_log.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_saved_modules.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_sys_patch.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _pydev_tipper_common.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_console_utils.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_import_hook.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_imports.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_ipython_console_011.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_ipython_console.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_is_thread_alive.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_localhost.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_log.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_monkey_qt.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_monkey.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_override.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_umd.cpython-312.pyc
│  │     │  │  │  │  │  └─ pydev_versioncheck.cpython-312.pyc
│  │     │  │  │  │  ├─ fsnotify/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ __init__.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _pydev_calltip_util.py
│  │     │  │  │  │  ├─ _pydev_completer.py
│  │     │  │  │  │  ├─ _pydev_execfile.py
│  │     │  │  │  │  ├─ _pydev_filesystem_encoding.py
│  │     │  │  │  │  ├─ _pydev_getopt.py
│  │     │  │  │  │  ├─ _pydev_imports_tipper.py
│  │     │  │  │  │  ├─ _pydev_jy_imports_tipper.py
│  │     │  │  │  │  ├─ _pydev_log.py
│  │     │  │  │  │  ├─ _pydev_saved_modules.py
│  │     │  │  │  │  ├─ _pydev_sys_patch.py
│  │     │  │  │  │  ├─ _pydev_tipper_common.py
│  │     │  │  │  │  ├─ pydev_console_utils.py
│  │     │  │  │  │  ├─ pydev_import_hook.py
│  │     │  │  │  │  ├─ pydev_imports.py
│  │     │  │  │  │  ├─ pydev_ipython_console_011.py
│  │     │  │  │  │  ├─ pydev_ipython_console.py
│  │     │  │  │  │  ├─ pydev_is_thread_alive.py
│  │     │  │  │  │  ├─ pydev_localhost.py
│  │     │  │  │  │  ├─ pydev_log.py
│  │     │  │  │  │  ├─ pydev_monkey_qt.py
│  │     │  │  │  │  ├─ pydev_monkey.py
│  │     │  │  │  │  ├─ pydev_override.py
│  │     │  │  │  │  ├─ pydev_umd.py
│  │     │  │  │  │  └─ pydev_versioncheck.py
│  │     │  │  │  ├─ _pydev_runfiles/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_runfiles_coverage.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_runfiles_nose.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_runfiles_parallel_client.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_runfiles_parallel.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_runfiles_pytest2.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_runfiles_unittest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydev_runfiles_xml_rpc.cpython-312.pyc
│  │     │  │  │  │  │  └─ pydev_runfiles.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ pydev_runfiles_coverage.py
│  │     │  │  │  │  ├─ pydev_runfiles_nose.py
│  │     │  │  │  │  ├─ pydev_runfiles_parallel_client.py
│  │     │  │  │  │  ├─ pydev_runfiles_parallel.py
│  │     │  │  │  │  ├─ pydev_runfiles_pytest2.py
│  │     │  │  │  │  ├─ pydev_runfiles_unittest.py
│  │     │  │  │  │  ├─ pydev_runfiles_xml_rpc.py
│  │     │  │  │  │  └─ pydev_runfiles.py
│  │     │  │  │  ├─ _pydevd_bundle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevconsole_code.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_additional_thread_info_regular.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_additional_thread_info.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_api.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_breakpoints.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_bytecode_utils_py311.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_bytecode_utils.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_code_to_source.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_collect_bytecode_info.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_comm_constants.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_comm.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_command_line_handling.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_console.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_constants.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_custom_frames.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_cython_wrapper.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_daemon_thread.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_defaults.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_dont_trace_files.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_dont_trace.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_exec2.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_extension_api.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_extension_utils.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_filtering.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_frame_utils.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_frame.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_gevent_integration.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_import_class.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_io.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_json_debug_options.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_net_command_factory_json.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_net_command_factory_xml.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_net_command.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_plugin_utils.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_process_net_command_json.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_process_net_command.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_referrers.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_reload.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_resolver.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_runpy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_safe_repr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_save_locals.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_signature.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_source_mapping.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_stackless.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_suspended_frames.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_thread_lifecycle.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_timeout.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_trace_dispatch_regular.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_trace_dispatch.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_traceproperty.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_utils.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_vars.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_vm_type.cpython-312.pyc
│  │     │  │  │  │  │  └─ pydevd_xml.cpython-312.pyc
│  │     │  │  │  │  ├─ _debug_adapter/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ __main__pydevd_gen_debug_adapter_protocol.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ pydevd_base_schema.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ pydevd_schema_log.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ pydevd_schema.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ __main__pydevd_gen_debug_adapter_protocol.py
│  │     │  │  │  │  │  ├─ debugProtocol.json
│  │     │  │  │  │  │  ├─ debugProtocolCustom.json
│  │     │  │  │  │  │  ├─ pydevd_base_schema.py
│  │     │  │  │  │  │  ├─ pydevd_schema_log.py
│  │     │  │  │  │  │  └─ pydevd_schema.py
│  │     │  │  │  │  ├─ pydevd_concurrency_analyser/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ pydevd_concurrency_logger.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ pydevd_thread_wrappers.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ pydevd_concurrency_logger.py
│  │     │  │  │  │  │  └─ pydevd_thread_wrappers.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ pydevconsole_code.py
│  │     │  │  │  │  ├─ pydevd_additional_thread_info_regular.py
│  │     │  │  │  │  ├─ pydevd_additional_thread_info.py
│  │     │  │  │  │  ├─ pydevd_api.py
│  │     │  │  │  │  ├─ pydevd_breakpoints.py
│  │     │  │  │  │  ├─ pydevd_bytecode_utils_py311.py
│  │     │  │  │  │  ├─ pydevd_bytecode_utils.py
│  │     │  │  │  │  ├─ pydevd_code_to_source.py
│  │     │  │  │  │  ├─ pydevd_collect_bytecode_info.py
│  │     │  │  │  │  ├─ pydevd_comm_constants.py
│  │     │  │  │  │  ├─ pydevd_comm.py
│  │     │  │  │  │  ├─ pydevd_command_line_handling.py
│  │     │  │  │  │  ├─ pydevd_console.py
│  │     │  │  │  │  ├─ pydevd_constants.py
│  │     │  │  │  │  ├─ pydevd_custom_frames.py
│  │     │  │  │  │  ├─ pydevd_cython_wrapper.py
│  │     │  │  │  │  ├─ pydevd_cython.c
│  │     │  │  │  │  ├─ pydevd_cython.cp312-win_amd64.pyd
│  │     │  │  │  │  ├─ pydevd_cython.pxd
│  │     │  │  │  │  ├─ pydevd_cython.pyx
│  │     │  │  │  │  ├─ pydevd_daemon_thread.py
│  │     │  │  │  │  ├─ pydevd_defaults.py
│  │     │  │  │  │  ├─ pydevd_dont_trace_files.py
│  │     │  │  │  │  ├─ pydevd_dont_trace.py
│  │     │  │  │  │  ├─ pydevd_exec2.py
│  │     │  │  │  │  ├─ pydevd_extension_api.py
│  │     │  │  │  │  ├─ pydevd_extension_utils.py
│  │     │  │  │  │  ├─ pydevd_filtering.py
│  │     │  │  │  │  ├─ pydevd_frame_utils.py
│  │     │  │  │  │  ├─ pydevd_frame.py
│  │     │  │  │  │  ├─ pydevd_gevent_integration.py
│  │     │  │  │  │  ├─ pydevd_import_class.py
│  │     │  │  │  │  ├─ pydevd_io.py
│  │     │  │  │  │  ├─ pydevd_json_debug_options.py
│  │     │  │  │  │  ├─ pydevd_net_command_factory_json.py
│  │     │  │  │  │  ├─ pydevd_net_command_factory_xml.py
│  │     │  │  │  │  ├─ pydevd_net_command.py
│  │     │  │  │  │  ├─ pydevd_plugin_utils.py
│  │     │  │  │  │  ├─ pydevd_process_net_command_json.py
│  │     │  │  │  │  ├─ pydevd_process_net_command.py
│  │     │  │  │  │  ├─ pydevd_referrers.py
│  │     │  │  │  │  ├─ pydevd_reload.py
│  │     │  │  │  │  ├─ pydevd_resolver.py
│  │     │  │  │  │  ├─ pydevd_runpy.py
│  │     │  │  │  │  ├─ pydevd_safe_repr.py
│  │     │  │  │  │  ├─ pydevd_save_locals.py
│  │     │  │  │  │  ├─ pydevd_signature.py
│  │     │  │  │  │  ├─ pydevd_source_mapping.py
│  │     │  │  │  │  ├─ pydevd_stackless.py
│  │     │  │  │  │  ├─ pydevd_suspended_frames.py
│  │     │  │  │  │  ├─ pydevd_thread_lifecycle.py
│  │     │  │  │  │  ├─ pydevd_timeout.py
│  │     │  │  │  │  ├─ pydevd_trace_dispatch_regular.py
│  │     │  │  │  │  ├─ pydevd_trace_dispatch.py
│  │     │  │  │  │  ├─ pydevd_traceproperty.py
│  │     │  │  │  │  ├─ pydevd_utils.py
│  │     │  │  │  │  ├─ pydevd_vars.py
│  │     │  │  │  │  ├─ pydevd_vm_type.py
│  │     │  │  │  │  └─ pydevd_xml.py
│  │     │  │  │  ├─ _pydevd_frame_eval/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_frame_eval_cython_wrapper.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_frame_eval_main.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pydevd_frame_tracing.cpython-312.pyc
│  │     │  │  │  │  │  └─ pydevd_modify_bytecode.cpython-312.pyc
│  │     │  │  │  │  ├─ vendored/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ pydevd_fix_code.cpython-312.pyc
│  │     │  │  │  │  │  ├─ bytecode/
│  │     │  │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ bytecode.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ cfg.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ concrete.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ flags.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ instr.cpython-312.pyc
│  │     │  │  │  │  │  │  │  └─ peephole_opt.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ tests/
│  │     │  │  │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_bytecode.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_cfg.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_code.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_concrete.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_flags.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_instr.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_misc.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  ├─ test_peephole_opt.cpython-312.pyc
│  │     │  │  │  │  │  │  │  │  └─ util_annotation.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  │  ├─ test_bytecode.py
│  │     │  │  │  │  │  │  │  ├─ test_cfg.py
│  │     │  │  │  │  │  │  │  ├─ test_code.py
│  │     │  │  │  │  │  │  │  ├─ test_concrete.py
│  │     │  │  │  │  │  │  │  ├─ test_flags.py
│  │     │  │  │  │  │  │  │  ├─ test_instr.py
│  │     │  │  │  │  │  │  │  ├─ test_misc.py
│  │     │  │  │  │  │  │  │  ├─ test_peephole_opt.py
│  │     │  │  │  │  │  │  │  └─ util_annotation.py
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  ├─ bytecode.py
│  │     │  │  │  │  │  │  ├─ cfg.py
│  │     │  │  │  │  │  │  ├─ concrete.py
│  │     │  │  │  │  │  │  ├─ flags.py
│  │     │  │  │  │  │  │  ├─ instr.py
│  │     │  │  │  │  │  │  └─ peephole_opt.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ pydevd_fix_code.py
│  │     │  │  │  │  │  └─ README.txt
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ .gitignore
│  │     │  │  │  │  ├─ pydevd_frame_eval_cython_wrapper.py
│  │     │  │  │  │  ├─ pydevd_frame_eval_main.py
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.c
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.pxd
│  │     │  │  │  │  ├─ pydevd_frame_evaluator.template.pyx
│  │     │  │  │  │  ├─ pydevd_frame_tracing.py
│  │     │  │  │  │  ├─ pydevd_modify_bytecode.py
│  │     │  │  │  │  └─ release_mem.h
│  │     │  │  │  ├─ _pydevd_sys_monitoring/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ _pydevd_sys_monitoring.cpython-312.pyc
│  │     │  │  │  │  │  └─ pydevd_sys_monitoring.cpython-312.pyc
│  │     │  │  │  │  ├─ _pydevd_sys_monitoring_cython.c
│  │     │  │  │  │  ├─ _pydevd_sys_monitoring_cython.cp312-win_amd64.pyd
│  │     │  │  │  │  ├─ _pydevd_sys_monitoring_cython.pxd
│  │     │  │  │  │  ├─ _pydevd_sys_monitoring_cython.pyx
│  │     │  │  │  │  ├─ _pydevd_sys_monitoring.py
│  │     │  │  │  │  └─ pydevd_sys_monitoring.py
│  │     │  │  │  ├─ pydev_ipython/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhook.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookglut.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookgtk.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookgtk3.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookpyglet.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookqt4.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookqt5.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookqt6.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhooktk.cpython-312.pyc
│  │     │  │  │  │  │  ├─ inputhookwx.cpython-312.pyc
│  │     │  │  │  │  │  ├─ matplotlibtools.cpython-312.pyc
│  │     │  │  │  │  │  ├─ qt_for_kernel.cpython-312.pyc
│  │     │  │  │  │  │  ├─ qt_loaders.cpython-312.pyc
│  │     │  │  │  │  │  ├─ qt.cpython-312.pyc
│  │     │  │  │  │  │  └─ version.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ inputhook.py
│  │     │  │  │  │  ├─ inputhookglut.py
│  │     │  │  │  │  ├─ inputhookgtk.py
│  │     │  │  │  │  ├─ inputhookgtk3.py
│  │     │  │  │  │  ├─ inputhookpyglet.py
│  │     │  │  │  │  ├─ inputhookqt4.py
│  │     │  │  │  │  ├─ inputhookqt5.py
│  │     │  │  │  │  ├─ inputhookqt6.py
│  │     │  │  │  │  ├─ inputhooktk.py
│  │     │  │  │  │  ├─ inputhookwx.py
│  │     │  │  │  │  ├─ matplotlibtools.py
│  │     │  │  │  │  ├─ qt_for_kernel.py
│  │     │  │  │  │  ├─ qt_loaders.py
│  │     │  │  │  │  ├─ qt.py
│  │     │  │  │  │  ├─ README
│  │     │  │  │  │  └─ version.py
│  │     │  │  │  ├─ pydev_sitecustomize/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  └─ sitecustomize.cpython-312.pyc
│  │     │  │  │  │  ├─ __not_in_default_pythonpath.txt
│  │     │  │  │  │  └─ sitecustomize.py
│  │     │  │  │  ├─ pydevd_attach_to_process/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ _always_live_program.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _check.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _test_attach_to_process_linux.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _test_attach_to_process.cpython-312.pyc
│  │     │  │  │  │  │  ├─ add_code_to_python_process.cpython-312.pyc
│  │     │  │  │  │  │  ├─ attach_pydevd.cpython-312.pyc
│  │     │  │  │  │  │  └─ attach_script.cpython-312.pyc
│  │     │  │  │  │  ├─ common/
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace_310.hpp
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace_311.hpp
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace_common.hpp
│  │     │  │  │  │  │  ├─ py_custom_pyeval_settrace.hpp
│  │     │  │  │  │  │  ├─ py_settrace.hpp
│  │     │  │  │  │  │  ├─ py_utils.hpp
│  │     │  │  │  │  │  ├─ py_version.hpp
│  │     │  │  │  │  │  ├─ python.h
│  │     │  │  │  │  │  └─ ref_utils.hpp
│  │     │  │  │  │  ├─ linux_and_mac/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  └─ lldb_prepare.cpython-312.pyc
│  │     │  │  │  │  │  ├─ .gitignore
│  │     │  │  │  │  │  ├─ attach.cpp
│  │     │  │  │  │  │  ├─ compile_linux.sh
│  │     │  │  │  │  │  ├─ compile_mac.sh
│  │     │  │  │  │  │  ├─ compile_manylinux.cmd
│  │     │  │  │  │  │  └─ lldb_prepare.py
│  │     │  │  │  │  ├─ winappdbg/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ breakpoint.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ compat.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ crash.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ debug.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ disasm.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ event.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ interactive.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ module.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ process.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ registry.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ search.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ sql.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ system.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ textio.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ thread.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ util.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ window.cpython-312.pyc
│  │     │  │  │  │  │  ├─ win32/
│  │     │  │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ advapi32.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ context_amd64.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ context_i386.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ dbghelp.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ defines.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ gdi32.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ kernel32.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ ntdll.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ peb_teb.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ psapi.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ shell32.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ shlwapi.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ user32.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ version.cpython-312.pyc
│  │     │  │  │  │  │  │  │  └─ wtsapi32.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  ├─ advapi32.py
│  │     │  │  │  │  │  │  ├─ context_amd64.py
│  │     │  │  │  │  │  │  ├─ context_i386.py
│  │     │  │  │  │  │  │  ├─ dbghelp.py
│  │     │  │  │  │  │  │  ├─ defines.py
│  │     │  │  │  │  │  │  ├─ gdi32.py
│  │     │  │  │  │  │  │  ├─ kernel32.py
│  │     │  │  │  │  │  │  ├─ ntdll.py
│  │     │  │  │  │  │  │  ├─ peb_teb.py
│  │     │  │  │  │  │  │  ├─ psapi.py
│  │     │  │  │  │  │  │  ├─ shell32.py
│  │     │  │  │  │  │  │  ├─ shlwapi.py
│  │     │  │  │  │  │  │  ├─ user32.py
│  │     │  │  │  │  │  │  ├─ version.py
│  │     │  │  │  │  │  │  └─ wtsapi32.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ breakpoint.py
│  │     │  │  │  │  │  ├─ compat.py
│  │     │  │  │  │  │  ├─ crash.py
│  │     │  │  │  │  │  ├─ debug.py
│  │     │  │  │  │  │  ├─ disasm.py
│  │     │  │  │  │  │  ├─ event.py
│  │     │  │  │  │  │  ├─ interactive.py
│  │     │  │  │  │  │  ├─ module.py
│  │     │  │  │  │  │  ├─ process.py
│  │     │  │  │  │  │  ├─ registry.py
│  │     │  │  │  │  │  ├─ search.py
│  │     │  │  │  │  │  ├─ sql.py
│  │     │  │  │  │  │  ├─ system.py
│  │     │  │  │  │  │  ├─ textio.py
│  │     │  │  │  │  │  ├─ thread.py
│  │     │  │  │  │  │  ├─ util.py
│  │     │  │  │  │  │  └─ window.py
│  │     │  │  │  │  ├─ windows/
│  │     │  │  │  │  │  ├─ attach.cpp
│  │     │  │  │  │  │  ├─ attach.h
│  │     │  │  │  │  │  ├─ compile_windows.bat
│  │     │  │  │  │  │  ├─ inject_dll.cpp
│  │     │  │  │  │  │  ├─ py_win_helpers.hpp
│  │     │  │  │  │  │  ├─ run_code_in_memory.hpp
│  │     │  │  │  │  │  ├─ run_code_on_dllmain.cpp
│  │     │  │  │  │  │  ├─ stdafx.cpp
│  │     │  │  │  │  │  ├─ stdafx.h
│  │     │  │  │  │  │  └─ targetver.h
│  │     │  │  │  │  ├─ _always_live_program.py
│  │     │  │  │  │  ├─ _check.py
│  │     │  │  │  │  ├─ _test_attach_to_process_linux.py
│  │     │  │  │  │  ├─ _test_attach_to_process.py
│  │     │  │  │  │  ├─ add_code_to_python_process.py
│  │     │  │  │  │  ├─ attach_amd64.dll
│  │     │  │  │  │  ├─ attach_amd64.pdb
│  │     │  │  │  │  ├─ attach_pydevd.py
│  │     │  │  │  │  ├─ attach_script.py
│  │     │  │  │  │  ├─ attach_x86.dll
│  │     │  │  │  │  ├─ attach_x86.pdb
│  │     │  │  │  │  ├─ inject_dll_amd64.exe
│  │     │  │  │  │  ├─ inject_dll_amd64.pdb
│  │     │  │  │  │  ├─ inject_dll_x86.exe
│  │     │  │  │  │  ├─ inject_dll_x86.pdb
│  │     │  │  │  │  ├─ README.txt
│  │     │  │  │  │  ├─ run_code_on_dllmain_amd64.dll
│  │     │  │  │  │  ├─ run_code_on_dllmain_amd64.pdb
│  │     │  │  │  │  ├─ run_code_on_dllmain_x86.dll
│  │     │  │  │  │  └─ run_code_on_dllmain_x86.pdb
│  │     │  │  │  ├─ pydevd_plugins/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ django_debug.cpython-312.pyc
│  │     │  │  │  │  │  ├─ jinja2_debug.cpython-312.pyc
│  │     │  │  │  │  │  └─ pydevd_line_validation.cpython-312.pyc
│  │     │  │  │  │  ├─ extensions/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ types/
│  │     │  │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ pydevd_helpers.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ pydevd_plugin_numpy_types.cpython-312.pyc
│  │     │  │  │  │  │  │  │  ├─ pydevd_plugin_pandas_types.cpython-312.pyc
│  │     │  │  │  │  │  │  │  └─ pydevd_plugins_django_form_str.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  ├─ pydevd_helpers.py
│  │     │  │  │  │  │  │  ├─ pydevd_plugin_numpy_types.py
│  │     │  │  │  │  │  │  ├─ pydevd_plugin_pandas_types.py
│  │     │  │  │  │  │  │  └─ pydevd_plugins_django_form_str.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ README.md
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ django_debug.py
│  │     │  │  │  │  ├─ jinja2_debug.py
│  │     │  │  │  │  └─ pydevd_line_validation.py
│  │     │  │  │  ├─ pydev_app_engine_debug_startup.py
│  │     │  │  │  ├─ pydev_coverage.py
│  │     │  │  │  ├─ pydev_pysrc.py
│  │     │  │  │  ├─ pydev_run_in_console.py
│  │     │  │  │  ├─ pydevconsole.py
│  │     │  │  │  ├─ pydevd_file_utils.py
│  │     │  │  │  ├─ pydevd_tracing.py
│  │     │  │  │  ├─ pydevd.py
│  │     │  │  │  └─ setup_pydevd_cython.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _pydevd_packaging.py
│  │     │  │  ├─ _util.py
│  │     │  │  └─ force_pydevd.py
│  │     │  ├─ adapter/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ clients.cpython-312.pyc
│  │     │  │  │  ├─ components.cpython-312.pyc
│  │     │  │  │  ├─ launchers.cpython-312.pyc
│  │     │  │  │  ├─ servers.cpython-312.pyc
│  │     │  │  │  └─ sessions.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ clients.py
│  │     │  │  ├─ components.py
│  │     │  │  ├─ launchers.py
│  │     │  │  ├─ servers.py
│  │     │  │  └─ sessions.py
│  │     │  ├─ common/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ json.cpython-312.pyc
│  │     │  │  │  ├─ log.cpython-312.pyc
│  │     │  │  │  ├─ messaging.cpython-312.pyc
│  │     │  │  │  ├─ singleton.cpython-312.pyc
│  │     │  │  │  ├─ sockets.cpython-312.pyc
│  │     │  │  │  ├─ stacks.cpython-312.pyc
│  │     │  │  │  ├─ timestamp.cpython-312.pyc
│  │     │  │  │  └─ util.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ json.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ messaging.py
│  │     │  │  ├─ singleton.py
│  │     │  │  ├─ sockets.py
│  │     │  │  ├─ stacks.py
│  │     │  │  ├─ timestamp.py
│  │     │  │  └─ util.py
│  │     │  ├─ launcher/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ debuggee.cpython-312.pyc
│  │     │  │  │  ├─ handlers.cpython-312.pyc
│  │     │  │  │  ├─ output.cpython-312.pyc
│  │     │  │  │  └─ winapi.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ debuggee.py
│  │     │  │  ├─ handlers.py
│  │     │  │  ├─ output.py
│  │     │  │  └─ winapi.py
│  │     │  ├─ server/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  ├─ attach_pid_injected.cpython-312.pyc
│  │     │  │  │  └─ cli.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ api.py
│  │     │  │  ├─ attach_pid_injected.py
│  │     │  │  └─ cli.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ _version.py
│  │     │  ├─ public_api.py
│  │     │  └─ ThirdPartyNotices.txt
│  │     ├─ debugpy-1.8.14.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ decorator-5.2.1.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ pbr.json
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ earthengine_api-1.5.23.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ee/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _arg_types.cpython-312.pyc
│  │     │  │  ├─ _cloud_api_utils.cpython-312.pyc
│  │     │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  ├─ _utils.cpython-312.pyc
│  │     │  │  ├─ apifunction.cpython-312.pyc
│  │     │  │  ├─ apitestcase.cpython-312.pyc
│  │     │  │  ├─ batch.cpython-312.pyc
│  │     │  │  ├─ blob.cpython-312.pyc
│  │     │  │  ├─ classifier.cpython-312.pyc
│  │     │  │  ├─ clusterer.cpython-312.pyc
│  │     │  │  ├─ collection.cpython-312.pyc
│  │     │  │  ├─ computedobject.cpython-312.pyc
│  │     │  │  ├─ confusionmatrix.cpython-312.pyc
│  │     │  │  ├─ customfunction.cpython-312.pyc
│  │     │  │  ├─ data.cpython-312.pyc
│  │     │  │  ├─ daterange.cpython-312.pyc
│  │     │  │  ├─ deprecation.cpython-312.pyc
│  │     │  │  ├─ deserializer.cpython-312.pyc
│  │     │  │  ├─ dictionary.cpython-312.pyc
│  │     │  │  ├─ ee_array.cpython-312.pyc
│  │     │  │  ├─ ee_date.cpython-312.pyc
│  │     │  │  ├─ ee_exception.cpython-312.pyc
│  │     │  │  ├─ ee_list.cpython-312.pyc
│  │     │  │  ├─ ee_number.cpython-312.pyc
│  │     │  │  ├─ ee_string.cpython-312.pyc
│  │     │  │  ├─ ee_types.cpython-312.pyc
│  │     │  │  ├─ element.cpython-312.pyc
│  │     │  │  ├─ encodable.cpython-312.pyc
│  │     │  │  ├─ errormargin.cpython-312.pyc
│  │     │  │  ├─ feature.cpython-312.pyc
│  │     │  │  ├─ featurecollection.cpython-312.pyc
│  │     │  │  ├─ filter.cpython-312.pyc
│  │     │  │  ├─ function.cpython-312.pyc
│  │     │  │  ├─ geometry.cpython-312.pyc
│  │     │  │  ├─ image_converter.cpython-312.pyc
│  │     │  │  ├─ image.cpython-312.pyc
│  │     │  │  ├─ imagecollection.cpython-312.pyc
│  │     │  │  ├─ join.cpython-312.pyc
│  │     │  │  ├─ kernel.cpython-312.pyc
│  │     │  │  ├─ mapclient.cpython-312.pyc
│  │     │  │  ├─ model.cpython-312.pyc
│  │     │  │  ├─ oauth.cpython-312.pyc
│  │     │  │  ├─ pixeltype.cpython-312.pyc
│  │     │  │  ├─ projection.cpython-312.pyc
│  │     │  │  ├─ reducer.cpython-312.pyc
│  │     │  │  ├─ serializer.cpython-312.pyc
│  │     │  │  ├─ table_converter.cpython-312.pyc
│  │     │  │  └─ terrain.cpython-312.pyc
│  │     │  ├─ cli/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ commands.cpython-312.pyc
│  │     │  │  │  ├─ eecli_wrapper.cpython-312.pyc
│  │     │  │  │  ├─ eecli.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ commands.py
│  │     │  │  ├─ eecli_wrapper.py
│  │     │  │  ├─ eecli.py
│  │     │  │  └─ utils.py
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ _cloud_api_utils_test.cpython-312.pyc
│  │     │  │  │  ├─ _helpers_test.cpython-312.pyc
│  │     │  │  │  ├─ _utils_test.cpython-312.pyc
│  │     │  │  │  ├─ apifunction_test.cpython-312.pyc
│  │     │  │  │  ├─ batch_test.cpython-312.pyc
│  │     │  │  │  ├─ blob_test.cpython-312.pyc
│  │     │  │  │  ├─ classifier_test.cpython-312.pyc
│  │     │  │  │  ├─ clusterer_test.cpython-312.pyc
│  │     │  │  │  ├─ collection_test.cpython-312.pyc
│  │     │  │  │  ├─ computedobject_test.cpython-312.pyc
│  │     │  │  │  ├─ confusionmatrix_test.cpython-312.pyc
│  │     │  │  │  ├─ data_test.cpython-312.pyc
│  │     │  │  │  ├─ daterange_test.cpython-312.pyc
│  │     │  │  │  ├─ deprecation_test.cpython-312.pyc
│  │     │  │  │  ├─ deserializer_test.cpython-312.pyc
│  │     │  │  │  ├─ dictionary_test.cpython-312.pyc
│  │     │  │  │  ├─ ee_array_test.cpython-312.pyc
│  │     │  │  │  ├─ ee_date_test.cpython-312.pyc
│  │     │  │  │  ├─ ee_list_test.cpython-312.pyc
│  │     │  │  │  ├─ ee_number_test.cpython-312.pyc
│  │     │  │  │  ├─ ee_string_test.cpython-312.pyc
│  │     │  │  │  ├─ ee_test.cpython-312.pyc
│  │     │  │  │  ├─ ee_types_test.cpython-312.pyc
│  │     │  │  │  ├─ element_test.cpython-312.pyc
│  │     │  │  │  ├─ errormargin_test.cpython-312.pyc
│  │     │  │  │  ├─ feature_test.cpython-312.pyc
│  │     │  │  │  ├─ featurecollection_test.cpython-312.pyc
│  │     │  │  │  ├─ filter_test.cpython-312.pyc
│  │     │  │  │  ├─ function_test.cpython-312.pyc
│  │     │  │  │  ├─ geometry_point_test.cpython-312.pyc
│  │     │  │  │  ├─ geometry_test.cpython-312.pyc
│  │     │  │  │  ├─ image_converter_test.cpython-312.pyc
│  │     │  │  │  ├─ image_test.cpython-312.pyc
│  │     │  │  │  ├─ imagecollection_test.cpython-312.pyc
│  │     │  │  │  ├─ join_test.cpython-312.pyc
│  │     │  │  │  ├─ kernel_test.cpython-312.pyc
│  │     │  │  │  ├─ model_test.cpython-312.pyc
│  │     │  │  │  ├─ oauth_test.cpython-312.pyc
│  │     │  │  │  ├─ pixeltype_test.cpython-312.pyc
│  │     │  │  │  ├─ projection_test.cpython-312.pyc
│  │     │  │  │  ├─ reducer_test.cpython-312.pyc
│  │     │  │  │  ├─ serializer_test.cpython-312.pyc
│  │     │  │  │  ├─ table_converter_test.cpython-312.pyc
│  │     │  │  │  └─ terrain_test.cpython-312.pyc
│  │     │  │  ├─ _cloud_api_utils_test.py
│  │     │  │  ├─ _helpers_test.py
│  │     │  │  ├─ _utils_test.py
│  │     │  │  ├─ algorithms.json
│  │     │  │  ├─ apifunction_test.py
│  │     │  │  ├─ batch_test.py
│  │     │  │  ├─ blob_test.py
│  │     │  │  ├─ classifier_test.py
│  │     │  │  ├─ cloud_api_discovery_document.json
│  │     │  │  ├─ clusterer_test.py
│  │     │  │  ├─ collection_test.py
│  │     │  │  ├─ computedobject_test.py
│  │     │  │  ├─ confusionmatrix_test.py
│  │     │  │  ├─ data_test.py
│  │     │  │  ├─ daterange_test.py
│  │     │  │  ├─ deprecation_test.py
│  │     │  │  ├─ deserializer_test.py
│  │     │  │  ├─ dictionary_test.py
│  │     │  │  ├─ ee_array_test.py
│  │     │  │  ├─ ee_date_test.py
│  │     │  │  ├─ ee_list_test.py
│  │     │  │  ├─ ee_number_test.py
│  │     │  │  ├─ ee_string_test.py
│  │     │  │  ├─ ee_test.py
│  │     │  │  ├─ ee_types_test.py
│  │     │  │  ├─ element_test.py
│  │     │  │  ├─ errormargin_test.py
│  │     │  │  ├─ feature_test.py
│  │     │  │  ├─ featurecollection_test.py
│  │     │  │  ├─ filter_test.py
│  │     │  │  ├─ function_test.py
│  │     │  │  ├─ geometry_point_test.py
│  │     │  │  ├─ geometry_test.py
│  │     │  │  ├─ image_converter_test.py
│  │     │  │  ├─ image_test.py
│  │     │  │  ├─ imagecollection_test.py
│  │     │  │  ├─ join_test.py
│  │     │  │  ├─ kernel_test.py
│  │     │  │  ├─ model_test.py
│  │     │  │  ├─ oauth_test.py
│  │     │  │  ├─ pixeltype_test.py
│  │     │  │  ├─ projection_test.py
│  │     │  │  ├─ reducer_test.py
│  │     │  │  ├─ serializer_test.py
│  │     │  │  ├─ table_converter_test.py
│  │     │  │  └─ terrain_test.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _arg_types.py
│  │     │  ├─ _cloud_api_utils.py
│  │     │  ├─ _helpers.py
│  │     │  ├─ _utils.py
│  │     │  ├─ apifunction.py
│  │     │  ├─ apitestcase.py
│  │     │  ├─ batch.py
│  │     │  ├─ blob.py
│  │     │  ├─ classifier.py
│  │     │  ├─ clusterer.py
│  │     │  ├─ collection.py
│  │     │  ├─ computedobject.py
│  │     │  ├─ confusionmatrix.py
│  │     │  ├─ customfunction.py
│  │     │  ├─ data.py
│  │     │  ├─ daterange.py
│  │     │  ├─ deprecation.py
│  │     │  ├─ deserializer.py
│  │     │  ├─ dictionary.py
│  │     │  ├─ ee_array.py
│  │     │  ├─ ee_date.py
│  │     │  ├─ ee_exception.py
│  │     │  ├─ ee_list.py
│  │     │  ├─ ee_number.py
│  │     │  ├─ ee_string.py
│  │     │  ├─ ee_types.py
│  │     │  ├─ element.py
│  │     │  ├─ encodable.py
│  │     │  ├─ errormargin.py
│  │     │  ├─ feature.py
│  │     │  ├─ featurecollection.py
│  │     │  ├─ filter.py
│  │     │  ├─ function.py
│  │     │  ├─ geometry.py
│  │     │  ├─ image_converter.py
│  │     │  ├─ image.py
│  │     │  ├─ imagecollection.py
│  │     │  ├─ join.py
│  │     │  ├─ kernel.py
│  │     │  ├─ mapclient.py
│  │     │  ├─ model.py
│  │     │  ├─ oauth.py
│  │     │  ├─ pixeltype.py
│  │     │  ├─ projection.py
│  │     │  ├─ py.typed
│  │     │  ├─ reducer.py
│  │     │  ├─ serializer.py
│  │     │  ├─ table_converter.py
│  │     │  └─ terrain.py
│  │     ├─ eerepr/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ config.cpython-312.pyc
│  │     │  │  ├─ html.cpython-312.pyc
│  │     │  │  ├─ repr.cpython-312.pyc
│  │     │  │  └─ style.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ config.py
│  │     │  ├─ html.py
│  │     │  ├─ repr.py
│  │     │  └─ style.py
│  │     ├─ eerepr-0.1.2.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ executing/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _exceptions.cpython-312.pyc
│  │     │  │  ├─ _position_node_finder.cpython-312.pyc
│  │     │  │  ├─ _pytest_utils.cpython-312.pyc
│  │     │  │  ├─ executing.cpython-312.pyc
│  │     │  │  └─ version.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ _exceptions.py
│  │     │  ├─ _position_node_finder.py
│  │     │  ├─ _pytest_utils.py
│  │     │  ├─ executing.py
│  │     │  ├─ py.typed
│  │     │  └─ version.py
│  │     ├─ executing-2.2.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ folium/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ elements.cpython-312.pyc
│  │     │  │  ├─ features.cpython-312.pyc
│  │     │  │  ├─ folium.cpython-312.pyc
│  │     │  │  ├─ map.cpython-312.pyc
│  │     │  │  ├─ raster_layers.cpython-312.pyc
│  │     │  │  ├─ template.cpython-312.pyc
│  │     │  │  ├─ utilities.cpython-312.pyc
│  │     │  │  └─ vector_layers.cpython-312.pyc
│  │     │  ├─ plugins/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ antpath.cpython-312.pyc
│  │     │  │  │  ├─ beautify_icon.cpython-312.pyc
│  │     │  │  │  ├─ boat_marker.cpython-312.pyc
│  │     │  │  │  ├─ draw.cpython-312.pyc
│  │     │  │  │  ├─ dual_map.cpython-312.pyc
│  │     │  │  │  ├─ encoded.cpython-312.pyc
│  │     │  │  │  ├─ fast_marker_cluster.cpython-312.pyc
│  │     │  │  │  ├─ feature_group_sub_group.cpython-312.pyc
│  │     │  │  │  ├─ float_image.cpython-312.pyc
│  │     │  │  │  ├─ fullscreen.cpython-312.pyc
│  │     │  │  │  ├─ geocoder.cpython-312.pyc
│  │     │  │  │  ├─ geoman.cpython-312.pyc
│  │     │  │  │  ├─ groupedlayercontrol.cpython-312.pyc
│  │     │  │  │  ├─ heat_map_withtime.cpython-312.pyc
│  │     │  │  │  ├─ heat_map.cpython-312.pyc
│  │     │  │  │  ├─ locate_control.cpython-312.pyc
│  │     │  │  │  ├─ marker_cluster.cpython-312.pyc
│  │     │  │  │  ├─ measure_control.cpython-312.pyc
│  │     │  │  │  ├─ minimap.cpython-312.pyc
│  │     │  │  │  ├─ mouse_position.cpython-312.pyc
│  │     │  │  │  ├─ overlapping_marker_spiderfier.cpython-312.pyc
│  │     │  │  │  ├─ pattern.cpython-312.pyc
│  │     │  │  │  ├─ polyline_offset.cpython-312.pyc
│  │     │  │  │  ├─ polyline_text_path.cpython-312.pyc
│  │     │  │  │  ├─ realtime.cpython-312.pyc
│  │     │  │  │  ├─ scroll_zoom_toggler.cpython-312.pyc
│  │     │  │  │  ├─ search.cpython-312.pyc
│  │     │  │  │  ├─ semicircle.cpython-312.pyc
│  │     │  │  │  ├─ side_by_side.cpython-312.pyc
│  │     │  │  │  ├─ tag_filter_button.cpython-312.pyc
│  │     │  │  │  ├─ terminator.cpython-312.pyc
│  │     │  │  │  ├─ time_slider_choropleth.cpython-312.pyc
│  │     │  │  │  ├─ timeline.cpython-312.pyc
│  │     │  │  │  ├─ timestamped_geo_json.cpython-312.pyc
│  │     │  │  │  ├─ timestamped_wmstilelayer.cpython-312.pyc
│  │     │  │  │  ├─ treelayercontrol.cpython-312.pyc
│  │     │  │  │  └─ vectorgrid_protobuf.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ antpath.py
│  │     │  │  ├─ beautify_icon.py
│  │     │  │  ├─ boat_marker.py
│  │     │  │  ├─ draw.py
│  │     │  │  ├─ dual_map.py
│  │     │  │  ├─ encoded.py
│  │     │  │  ├─ fast_marker_cluster.py
│  │     │  │  ├─ feature_group_sub_group.py
│  │     │  │  ├─ float_image.py
│  │     │  │  ├─ fullscreen.py
│  │     │  │  ├─ geocoder.py
│  │     │  │  ├─ geoman.py
│  │     │  │  ├─ groupedlayercontrol.py
│  │     │  │  ├─ heat_map_withtime.py
│  │     │  │  ├─ heat_map.py
│  │     │  │  ├─ locate_control.py
│  │     │  │  ├─ marker_cluster.py
│  │     │  │  ├─ measure_control.py
│  │     │  │  ├─ minimap.py
│  │     │  │  ├─ mouse_position.py
│  │     │  │  ├─ overlapping_marker_spiderfier.py
│  │     │  │  ├─ pattern.py
│  │     │  │  ├─ polyline_offset.py
│  │     │  │  ├─ polyline_text_path.py
│  │     │  │  ├─ realtime.py
│  │     │  │  ├─ scroll_zoom_toggler.py
│  │     │  │  ├─ search.py
│  │     │  │  ├─ semicircle.py
│  │     │  │  ├─ side_by_side.py
│  │     │  │  ├─ tag_filter_button.py
│  │     │  │  ├─ terminator.py
│  │     │  │  ├─ time_slider_choropleth.py
│  │     │  │  ├─ timeline.py
│  │     │  │  ├─ timestamped_geo_json.py
│  │     │  │  ├─ timestamped_wmstilelayer.py
│  │     │  │  ├─ treelayercontrol.py
│  │     │  │  └─ vectorgrid_protobuf.py
│  │     │  ├─ templates/
│  │     │  │  ├─ leaflet_heat.min.js
│  │     │  │  ├─ pa7_hm.min.js
│  │     │  │  └─ pa7_leaflet_hm.min.js
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  ├─ elements.py
│  │     │  ├─ features.py
│  │     │  ├─ folium.py
│  │     │  ├─ map.py
│  │     │  ├─ py.typed
│  │     │  ├─ raster_layers.py
│  │     │  ├─ template.py
│  │     │  ├─ utilities.py
│  │     │  └─ vector_layers.py
│  │     ├─ folium-0.20.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ fontTools/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ afmLib.cpython-312.pyc
│  │     │  │  ├─ agl.cpython-312.pyc
│  │     │  │  ├─ fontBuilder.cpython-312.pyc
│  │     │  │  ├─ help.cpython-312.pyc
│  │     │  │  ├─ tfmLib.cpython-312.pyc
│  │     │  │  ├─ ttx.cpython-312.pyc
│  │     │  │  └─ unicode.cpython-312.pyc
│  │     │  ├─ cffLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ CFF2ToCFF.cpython-312.pyc
│  │     │  │  │  ├─ CFFToCFF2.cpython-312.pyc
│  │     │  │  │  ├─ specializer.cpython-312.pyc
│  │     │  │  │  ├─ transforms.cpython-312.pyc
│  │     │  │  │  └─ width.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ CFF2ToCFF.py
│  │     │  │  ├─ CFFToCFF2.py
│  │     │  │  ├─ specializer.py
│  │     │  │  ├─ transforms.py
│  │     │  │  └─ width.py
│  │     │  ├─ colorLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ builder.cpython-312.pyc
│  │     │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  ├─ geometry.cpython-312.pyc
│  │     │  │  │  ├─ table_builder.cpython-312.pyc
│  │     │  │  │  └─ unbuilder.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ geometry.py
│  │     │  │  ├─ table_builder.py
│  │     │  │  └─ unbuilder.py
│  │     │  ├─ config/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ cu2qu/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ benchmark.cpython-312.pyc
│  │     │  │  │  ├─ cli.cpython-312.pyc
│  │     │  │  │  ├─ cu2qu.cpython-312.pyc
│  │     │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  └─ ufo.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ benchmark.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ cu2qu.c
│  │     │  │  ├─ cu2qu.cp312-win_amd64.pyd
│  │     │  │  ├─ cu2qu.py
│  │     │  │  ├─ errors.py
│  │     │  │  └─ ufo.py
│  │     │  ├─ designspaceLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ split.cpython-312.pyc
│  │     │  │  │  ├─ statNames.cpython-312.pyc
│  │     │  │  │  └─ types.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ split.py
│  │     │  │  ├─ statNames.py
│  │     │  │  └─ types.py
│  │     │  ├─ encodings/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ codecs.cpython-312.pyc
│  │     │  │  │  ├─ MacRoman.cpython-312.pyc
│  │     │  │  │  └─ StandardEncoding.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ codecs.py
│  │     │  │  ├─ MacRoman.py
│  │     │  │  └─ StandardEncoding.py
│  │     │  ├─ feaLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ ast.cpython-312.pyc
│  │     │  │  │  ├─ builder.cpython-312.pyc
│  │     │  │  │  ├─ error.cpython-312.pyc
│  │     │  │  │  ├─ lexer.cpython-312.pyc
│  │     │  │  │  ├─ location.cpython-312.pyc
│  │     │  │  │  ├─ lookupDebugInfo.cpython-312.pyc
│  │     │  │  │  ├─ parser.cpython-312.pyc
│  │     │  │  │  └─ variableScalar.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ ast.py
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ lexer.c
│  │     │  │  ├─ lexer.cp312-win_amd64.pyd
│  │     │  │  ├─ lexer.py
│  │     │  │  ├─ location.py
│  │     │  │  ├─ lookupDebugInfo.py
│  │     │  │  ├─ parser.py
│  │     │  │  └─ variableScalar.py
│  │     │  ├─ merge/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  ├─ cmap.cpython-312.pyc
│  │     │  │  │  ├─ layout.cpython-312.pyc
│  │     │  │  │  ├─ options.cpython-312.pyc
│  │     │  │  │  ├─ tables.cpython-312.pyc
│  │     │  │  │  ├─ unicode.cpython-312.pyc
│  │     │  │  │  └─ util.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ cmap.py
│  │     │  │  ├─ layout.py
│  │     │  │  ├─ options.py
│  │     │  │  ├─ tables.py
│  │     │  │  ├─ unicode.py
│  │     │  │  └─ util.py
│  │     │  ├─ misc/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ arrayTools.cpython-312.pyc
│  │     │  │  │  ├─ bezierTools.cpython-312.pyc
│  │     │  │  │  ├─ classifyTools.cpython-312.pyc
│  │     │  │  │  ├─ cliTools.cpython-312.pyc
│  │     │  │  │  ├─ configTools.cpython-312.pyc
│  │     │  │  │  ├─ cython.cpython-312.pyc
│  │     │  │  │  ├─ dictTools.cpython-312.pyc
│  │     │  │  │  ├─ eexec.cpython-312.pyc
│  │     │  │  │  ├─ encodingTools.cpython-312.pyc
│  │     │  │  │  ├─ etree.cpython-312.pyc
│  │     │  │  │  ├─ filenames.cpython-312.pyc
│  │     │  │  │  ├─ fixedTools.cpython-312.pyc
│  │     │  │  │  ├─ intTools.cpython-312.pyc
│  │     │  │  │  ├─ iterTools.cpython-312.pyc
│  │     │  │  │  ├─ lazyTools.cpython-312.pyc
│  │     │  │  │  ├─ loggingTools.cpython-312.pyc
│  │     │  │  │  ├─ macCreatorType.cpython-312.pyc
│  │     │  │  │  ├─ macRes.cpython-312.pyc
│  │     │  │  │  ├─ psCharStrings.cpython-312.pyc
│  │     │  │  │  ├─ psLib.cpython-312.pyc
│  │     │  │  │  ├─ psOperators.cpython-312.pyc
│  │     │  │  │  ├─ py23.cpython-312.pyc
│  │     │  │  │  ├─ roundTools.cpython-312.pyc
│  │     │  │  │  ├─ sstruct.cpython-312.pyc
│  │     │  │  │  ├─ symfont.cpython-312.pyc
│  │     │  │  │  ├─ testTools.cpython-312.pyc
│  │     │  │  │  ├─ textTools.cpython-312.pyc
│  │     │  │  │  ├─ timeTools.cpython-312.pyc
│  │     │  │  │  ├─ transform.cpython-312.pyc
│  │     │  │  │  ├─ treeTools.cpython-312.pyc
│  │     │  │  │  ├─ vector.cpython-312.pyc
│  │     │  │  │  ├─ visitor.cpython-312.pyc
│  │     │  │  │  ├─ xmlReader.cpython-312.pyc
│  │     │  │  │  └─ xmlWriter.cpython-312.pyc
│  │     │  │  ├─ plistlib/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ arrayTools.py
│  │     │  │  ├─ bezierTools.c
│  │     │  │  ├─ bezierTools.cp312-win_amd64.pyd
│  │     │  │  ├─ bezierTools.py
│  │     │  │  ├─ classifyTools.py
│  │     │  │  ├─ cliTools.py
│  │     │  │  ├─ configTools.py
│  │     │  │  ├─ cython.py
│  │     │  │  ├─ dictTools.py
│  │     │  │  ├─ eexec.py
│  │     │  │  ├─ encodingTools.py
│  │     │  │  ├─ etree.py
│  │     │  │  ├─ filenames.py
│  │     │  │  ├─ fixedTools.py
│  │     │  │  ├─ intTools.py
│  │     │  │  ├─ iterTools.py
│  │     │  │  ├─ lazyTools.py
│  │     │  │  ├─ loggingTools.py
│  │     │  │  ├─ macCreatorType.py
│  │     │  │  ├─ macRes.py
│  │     │  │  ├─ psCharStrings.py
│  │     │  │  ├─ psLib.py
│  │     │  │  ├─ psOperators.py
│  │     │  │  ├─ py23.py
│  │     │  │  ├─ roundTools.py
│  │     │  │  ├─ sstruct.py
│  │     │  │  ├─ symfont.py
│  │     │  │  ├─ testTools.py
│  │     │  │  ├─ textTools.py
│  │     │  │  ├─ timeTools.py
│  │     │  │  ├─ transform.py
│  │     │  │  ├─ treeTools.py
│  │     │  │  ├─ vector.py
│  │     │  │  ├─ visitor.py
│  │     │  │  ├─ xmlReader.py
│  │     │  │  └─ xmlWriter.py
│  │     │  ├─ mtiLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __main__.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __main__.py
│  │     │  ├─ otlLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ builder.cpython-312.pyc
│  │     │  │  │  ├─ error.cpython-312.pyc
│  │     │  │  │  └─ maxContextCalc.cpython-312.pyc
│  │     │  │  ├─ optimize/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  └─ gpos.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  └─ gpos.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ error.py
│  │     │  │  └─ maxContextCalc.py
│  │     │  ├─ pens/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ areaPen.cpython-312.pyc
│  │     │  │  │  ├─ basePen.cpython-312.pyc
│  │     │  │  │  ├─ boundsPen.cpython-312.pyc
│  │     │  │  │  ├─ cairoPen.cpython-312.pyc
│  │     │  │  │  ├─ cocoaPen.cpython-312.pyc
│  │     │  │  │  ├─ cu2quPen.cpython-312.pyc
│  │     │  │  │  ├─ explicitClosingLinePen.cpython-312.pyc
│  │     │  │  │  ├─ filterPen.cpython-312.pyc
│  │     │  │  │  ├─ freetypePen.cpython-312.pyc
│  │     │  │  │  ├─ hashPointPen.cpython-312.pyc
│  │     │  │  │  ├─ momentsPen.cpython-312.pyc
│  │     │  │  │  ├─ perimeterPen.cpython-312.pyc
│  │     │  │  │  ├─ pointInsidePen.cpython-312.pyc
│  │     │  │  │  ├─ pointPen.cpython-312.pyc
│  │     │  │  │  ├─ qtPen.cpython-312.pyc
│  │     │  │  │  ├─ qu2cuPen.cpython-312.pyc
│  │     │  │  │  ├─ quartzPen.cpython-312.pyc
│  │     │  │  │  ├─ recordingPen.cpython-312.pyc
│  │     │  │  │  ├─ reportLabPen.cpython-312.pyc
│  │     │  │  │  ├─ reverseContourPen.cpython-312.pyc
│  │     │  │  │  ├─ roundingPen.cpython-312.pyc
│  │     │  │  │  ├─ statisticsPen.cpython-312.pyc
│  │     │  │  │  ├─ svgPathPen.cpython-312.pyc
│  │     │  │  │  ├─ t2CharStringPen.cpython-312.pyc
│  │     │  │  │  ├─ teePen.cpython-312.pyc
│  │     │  │  │  ├─ transformPen.cpython-312.pyc
│  │     │  │  │  ├─ ttGlyphPen.cpython-312.pyc
│  │     │  │  │  └─ wxPen.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ areaPen.py
│  │     │  │  ├─ basePen.py
│  │     │  │  ├─ boundsPen.py
│  │     │  │  ├─ cairoPen.py
│  │     │  │  ├─ cocoaPen.py
│  │     │  │  ├─ cu2quPen.py
│  │     │  │  ├─ explicitClosingLinePen.py
│  │     │  │  ├─ filterPen.py
│  │     │  │  ├─ freetypePen.py
│  │     │  │  ├─ hashPointPen.py
│  │     │  │  ├─ momentsPen.c
│  │     │  │  ├─ momentsPen.cp312-win_amd64.pyd
│  │     │  │  ├─ momentsPen.py
│  │     │  │  ├─ perimeterPen.py
│  │     │  │  ├─ pointInsidePen.py
│  │     │  │  ├─ pointPen.py
│  │     │  │  ├─ qtPen.py
│  │     │  │  ├─ qu2cuPen.py
│  │     │  │  ├─ quartzPen.py
│  │     │  │  ├─ recordingPen.py
│  │     │  │  ├─ reportLabPen.py
│  │     │  │  ├─ reverseContourPen.py
│  │     │  │  ├─ roundingPen.py
│  │     │  │  ├─ statisticsPen.py
│  │     │  │  ├─ svgPathPen.py
│  │     │  │  ├─ t2CharStringPen.py
│  │     │  │  ├─ teePen.py
│  │     │  │  ├─ transformPen.py
│  │     │  │  ├─ ttGlyphPen.py
│  │     │  │  └─ wxPen.py
│  │     │  ├─ qu2cu/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ benchmark.cpython-312.pyc
│  │     │  │  │  ├─ cli.cpython-312.pyc
│  │     │  │  │  └─ qu2cu.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ benchmark.py
│  │     │  │  ├─ cli.py
│  │     │  │  ├─ qu2cu.c
│  │     │  │  ├─ qu2cu.cp312-win_amd64.pyd
│  │     │  │  └─ qu2cu.py
│  │     │  ├─ subset/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ cff.cpython-312.pyc
│  │     │  │  │  ├─ svg.cpython-312.pyc
│  │     │  │  │  └─ util.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ cff.py
│  │     │  │  ├─ svg.py
│  │     │  │  └─ util.py
│  │     │  ├─ svgLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ path/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ arc.cpython-312.pyc
│  │     │  │  │  │  ├─ parser.cpython-312.pyc
│  │     │  │  │  │  └─ shapes.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ arc.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  └─ shapes.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ t1Lib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ ttLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ macUtils.cpython-312.pyc
│  │     │  │  │  ├─ removeOverlaps.cpython-312.pyc
│  │     │  │  │  ├─ reorderGlyphs.cpython-312.pyc
│  │     │  │  │  ├─ scaleUpem.cpython-312.pyc
│  │     │  │  │  ├─ sfnt.cpython-312.pyc
│  │     │  │  │  ├─ standardGlyphOrder.cpython-312.pyc
│  │     │  │  │  ├─ ttCollection.cpython-312.pyc
│  │     │  │  │  ├─ ttFont.cpython-312.pyc
│  │     │  │  │  ├─ ttGlyphSet.cpython-312.pyc
│  │     │  │  │  ├─ ttVisitor.cpython-312.pyc
│  │     │  │  │  └─ woff2.cpython-312.pyc
│  │     │  │  ├─ tables/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _a_n_k_r.cpython-312.pyc
│  │     │  │  │  │  ├─ _a_v_a_r.cpython-312.pyc
│  │     │  │  │  │  ├─ _b_s_l_n.cpython-312.pyc
│  │     │  │  │  │  ├─ _c_i_d_g.cpython-312.pyc
│  │     │  │  │  │  ├─ _c_m_a_p.cpython-312.pyc
│  │     │  │  │  │  ├─ _c_v_a_r.cpython-312.pyc
│  │     │  │  │  │  ├─ _c_v_t.cpython-312.pyc
│  │     │  │  │  │  ├─ _f_e_a_t.cpython-312.pyc
│  │     │  │  │  │  ├─ _f_p_g_m.cpython-312.pyc
│  │     │  │  │  │  ├─ _f_v_a_r.cpython-312.pyc
│  │     │  │  │  │  ├─ _g_a_s_p.cpython-312.pyc
│  │     │  │  │  │  ├─ _g_c_i_d.cpython-312.pyc
│  │     │  │  │  │  ├─ _g_l_y_f.cpython-312.pyc
│  │     │  │  │  │  ├─ _g_v_a_r.cpython-312.pyc
│  │     │  │  │  │  ├─ _h_d_m_x.cpython-312.pyc
│  │     │  │  │  │  ├─ _h_e_a_d.cpython-312.pyc
│  │     │  │  │  │  ├─ _h_h_e_a.cpython-312.pyc
│  │     │  │  │  │  ├─ _h_m_t_x.cpython-312.pyc
│  │     │  │  │  │  ├─ _k_e_r_n.cpython-312.pyc
│  │     │  │  │  │  ├─ _l_c_a_r.cpython-312.pyc
│  │     │  │  │  │  ├─ _l_o_c_a.cpython-312.pyc
│  │     │  │  │  │  ├─ _l_t_a_g.cpython-312.pyc
│  │     │  │  │  │  ├─ _m_a_x_p.cpython-312.pyc
│  │     │  │  │  │  ├─ _m_e_t_a.cpython-312.pyc
│  │     │  │  │  │  ├─ _m_o_r_t.cpython-312.pyc
│  │     │  │  │  │  ├─ _m_o_r_x.cpython-312.pyc
│  │     │  │  │  │  ├─ _n_a_m_e.cpython-312.pyc
│  │     │  │  │  │  ├─ _o_p_b_d.cpython-312.pyc
│  │     │  │  │  │  ├─ _p_o_s_t.cpython-312.pyc
│  │     │  │  │  │  ├─ _p_r_e_p.cpython-312.pyc
│  │     │  │  │  │  ├─ _p_r_o_p.cpython-312.pyc
│  │     │  │  │  │  ├─ _s_b_i_x.cpython-312.pyc
│  │     │  │  │  │  ├─ _t_r_a_k.cpython-312.pyc
│  │     │  │  │  │  ├─ _v_h_e_a.cpython-312.pyc
│  │     │  │  │  │  ├─ _v_m_t_x.cpython-312.pyc
│  │     │  │  │  │  ├─ asciiTable.cpython-312.pyc
│  │     │  │  │  │  ├─ B_A_S_E_.cpython-312.pyc
│  │     │  │  │  │  ├─ BitmapGlyphMetrics.cpython-312.pyc
│  │     │  │  │  │  ├─ C_B_D_T_.cpython-312.pyc
│  │     │  │  │  │  ├─ C_B_L_C_.cpython-312.pyc
│  │     │  │  │  │  ├─ C_F_F__2.cpython-312.pyc
│  │     │  │  │  │  ├─ C_F_F_.cpython-312.pyc
│  │     │  │  │  │  ├─ C_O_L_R_.cpython-312.pyc
│  │     │  │  │  │  ├─ C_P_A_L_.cpython-312.pyc
│  │     │  │  │  │  ├─ D__e_b_g.cpython-312.pyc
│  │     │  │  │  │  ├─ D_S_I_G_.cpython-312.pyc
│  │     │  │  │  │  ├─ DefaultTable.cpython-312.pyc
│  │     │  │  │  │  ├─ E_B_D_T_.cpython-312.pyc
│  │     │  │  │  │  ├─ E_B_L_C_.cpython-312.pyc
│  │     │  │  │  │  ├─ F__e_a_t.cpython-312.pyc
│  │     │  │  │  │  ├─ F_F_T_M_.cpython-312.pyc
│  │     │  │  │  │  ├─ G__l_a_t.cpython-312.pyc
│  │     │  │  │  │  ├─ G__l_o_c.cpython-312.pyc
│  │     │  │  │  │  ├─ G_D_E_F_.cpython-312.pyc
│  │     │  │  │  │  ├─ G_M_A_P_.cpython-312.pyc
│  │     │  │  │  │  ├─ G_P_K_G_.cpython-312.pyc
│  │     │  │  │  │  ├─ G_P_O_S_.cpython-312.pyc
│  │     │  │  │  │  ├─ G_S_U_B_.cpython-312.pyc
│  │     │  │  │  │  ├─ G_V_A_R_.cpython-312.pyc
│  │     │  │  │  │  ├─ grUtils.cpython-312.pyc
│  │     │  │  │  │  ├─ H_V_A_R_.cpython-312.pyc
│  │     │  │  │  │  ├─ J_S_T_F_.cpython-312.pyc
│  │     │  │  │  │  ├─ L_T_S_H_.cpython-312.pyc
│  │     │  │  │  │  ├─ M_A_T_H_.cpython-312.pyc
│  │     │  │  │  │  ├─ M_E_T_A_.cpython-312.pyc
│  │     │  │  │  │  ├─ M_V_A_R_.cpython-312.pyc
│  │     │  │  │  │  ├─ O_S_2f_2.cpython-312.pyc
│  │     │  │  │  │  ├─ otBase.cpython-312.pyc
│  │     │  │  │  │  ├─ otConverters.cpython-312.pyc
│  │     │  │  │  │  ├─ otData.cpython-312.pyc
│  │     │  │  │  │  ├─ otTables.cpython-312.pyc
│  │     │  │  │  │  ├─ otTraverse.cpython-312.pyc
│  │     │  │  │  │  ├─ S__i_l_f.cpython-312.pyc
│  │     │  │  │  │  ├─ S__i_l_l.cpython-312.pyc
│  │     │  │  │  │  ├─ S_I_N_G_.cpython-312.pyc
│  │     │  │  │  │  ├─ S_T_A_T_.cpython-312.pyc
│  │     │  │  │  │  ├─ S_V_G_.cpython-312.pyc
│  │     │  │  │  │  ├─ sbixGlyph.cpython-312.pyc
│  │     │  │  │  │  ├─ sbixStrike.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I__0.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I__1.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I__2.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I__3.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I__5.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I_B_.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I_C_.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I_D_.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I_J_.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I_P_.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I_S_.cpython-312.pyc
│  │     │  │  │  │  ├─ T_S_I_V_.cpython-312.pyc
│  │     │  │  │  │  ├─ T_T_F_A_.cpython-312.pyc
│  │     │  │  │  │  ├─ ttProgram.cpython-312.pyc
│  │     │  │  │  │  ├─ TupleVariation.cpython-312.pyc
│  │     │  │  │  │  ├─ V_A_R_C_.cpython-312.pyc
│  │     │  │  │  │  ├─ V_D_M_X_.cpython-312.pyc
│  │     │  │  │  │  ├─ V_O_R_G_.cpython-312.pyc
│  │     │  │  │  │  └─ V_V_A_R_.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _a_n_k_r.py
│  │     │  │  │  ├─ _a_v_a_r.py
│  │     │  │  │  ├─ _b_s_l_n.py
│  │     │  │  │  ├─ _c_i_d_g.py
│  │     │  │  │  ├─ _c_m_a_p.py
│  │     │  │  │  ├─ _c_v_a_r.py
│  │     │  │  │  ├─ _c_v_t.py
│  │     │  │  │  ├─ _f_e_a_t.py
│  │     │  │  │  ├─ _f_p_g_m.py
│  │     │  │  │  ├─ _f_v_a_r.py
│  │     │  │  │  ├─ _g_a_s_p.py
│  │     │  │  │  ├─ _g_c_i_d.py
│  │     │  │  │  ├─ _g_l_y_f.py
│  │     │  │  │  ├─ _g_v_a_r.py
│  │     │  │  │  ├─ _h_d_m_x.py
│  │     │  │  │  ├─ _h_e_a_d.py
│  │     │  │  │  ├─ _h_h_e_a.py
│  │     │  │  │  ├─ _h_m_t_x.py
│  │     │  │  │  ├─ _k_e_r_n.py
│  │     │  │  │  ├─ _l_c_a_r.py
│  │     │  │  │  ├─ _l_o_c_a.py
│  │     │  │  │  ├─ _l_t_a_g.py
│  │     │  │  │  ├─ _m_a_x_p.py
│  │     │  │  │  ├─ _m_e_t_a.py
│  │     │  │  │  ├─ _m_o_r_t.py
│  │     │  │  │  ├─ _m_o_r_x.py
│  │     │  │  │  ├─ _n_a_m_e.py
│  │     │  │  │  ├─ _o_p_b_d.py
│  │     │  │  │  ├─ _p_o_s_t.py
│  │     │  │  │  ├─ _p_r_e_p.py
│  │     │  │  │  ├─ _p_r_o_p.py
│  │     │  │  │  ├─ _s_b_i_x.py
│  │     │  │  │  ├─ _t_r_a_k.py
│  │     │  │  │  ├─ _v_h_e_a.py
│  │     │  │  │  ├─ _v_m_t_x.py
│  │     │  │  │  ├─ asciiTable.py
│  │     │  │  │  ├─ B_A_S_E_.py
│  │     │  │  │  ├─ BitmapGlyphMetrics.py
│  │     │  │  │  ├─ C_B_D_T_.py
│  │     │  │  │  ├─ C_B_L_C_.py
│  │     │  │  │  ├─ C_F_F__2.py
│  │     │  │  │  ├─ C_F_F_.py
│  │     │  │  │  ├─ C_O_L_R_.py
│  │     │  │  │  ├─ C_P_A_L_.py
│  │     │  │  │  ├─ D__e_b_g.py
│  │     │  │  │  ├─ D_S_I_G_.py
│  │     │  │  │  ├─ DefaultTable.py
│  │     │  │  │  ├─ E_B_D_T_.py
│  │     │  │  │  ├─ E_B_L_C_.py
│  │     │  │  │  ├─ F__e_a_t.py
│  │     │  │  │  ├─ F_F_T_M_.py
│  │     │  │  │  ├─ G__l_a_t.py
│  │     │  │  │  ├─ G__l_o_c.py
│  │     │  │  │  ├─ G_D_E_F_.py
│  │     │  │  │  ├─ G_M_A_P_.py
│  │     │  │  │  ├─ G_P_K_G_.py
│  │     │  │  │  ├─ G_P_O_S_.py
│  │     │  │  │  ├─ G_S_U_B_.py
│  │     │  │  │  ├─ G_V_A_R_.py
│  │     │  │  │  ├─ grUtils.py
│  │     │  │  │  ├─ H_V_A_R_.py
│  │     │  │  │  ├─ J_S_T_F_.py
│  │     │  │  │  ├─ L_T_S_H_.py
│  │     │  │  │  ├─ M_A_T_H_.py
│  │     │  │  │  ├─ M_E_T_A_.py
│  │     │  │  │  ├─ M_V_A_R_.py
│  │     │  │  │  ├─ O_S_2f_2.py
│  │     │  │  │  ├─ otBase.py
│  │     │  │  │  ├─ otConverters.py
│  │     │  │  │  ├─ otData.py
│  │     │  │  │  ├─ otTables.py
│  │     │  │  │  ├─ otTraverse.py
│  │     │  │  │  ├─ S__i_l_f.py
│  │     │  │  │  ├─ S__i_l_l.py
│  │     │  │  │  ├─ S_I_N_G_.py
│  │     │  │  │  ├─ S_T_A_T_.py
│  │     │  │  │  ├─ S_V_G_.py
│  │     │  │  │  ├─ sbixGlyph.py
│  │     │  │  │  ├─ sbixStrike.py
│  │     │  │  │  ├─ T_S_I__0.py
│  │     │  │  │  ├─ T_S_I__1.py
│  │     │  │  │  ├─ T_S_I__2.py
│  │     │  │  │  ├─ T_S_I__3.py
│  │     │  │  │  ├─ T_S_I__5.py
│  │     │  │  │  ├─ T_S_I_B_.py
│  │     │  │  │  ├─ T_S_I_C_.py
│  │     │  │  │  ├─ T_S_I_D_.py
│  │     │  │  │  ├─ T_S_I_J_.py
│  │     │  │  │  ├─ T_S_I_P_.py
│  │     │  │  │  ├─ T_S_I_S_.py
│  │     │  │  │  ├─ T_S_I_V_.py
│  │     │  │  │  ├─ T_T_F_A_.py
│  │     │  │  │  ├─ table_API_readme.txt
│  │     │  │  │  ├─ ttProgram.py
│  │     │  │  │  ├─ TupleVariation.py
│  │     │  │  │  ├─ V_A_R_C_.py
│  │     │  │  │  ├─ V_D_M_X_.py
│  │     │  │  │  ├─ V_O_R_G_.py
│  │     │  │  │  └─ V_V_A_R_.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ macUtils.py
│  │     │  │  ├─ removeOverlaps.py
│  │     │  │  ├─ reorderGlyphs.py
│  │     │  │  ├─ scaleUpem.py
│  │     │  │  ├─ sfnt.py
│  │     │  │  ├─ standardGlyphOrder.py
│  │     │  │  ├─ ttCollection.py
│  │     │  │  ├─ ttFont.py
│  │     │  │  ├─ ttGlyphSet.py
│  │     │  │  ├─ ttVisitor.py
│  │     │  │  └─ woff2.py
│  │     │  ├─ ufoLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ converters.cpython-312.pyc
│  │     │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  ├─ etree.cpython-312.pyc
│  │     │  │  │  ├─ filenames.cpython-312.pyc
│  │     │  │  │  ├─ glifLib.cpython-312.pyc
│  │     │  │  │  ├─ kerning.cpython-312.pyc
│  │     │  │  │  ├─ plistlib.cpython-312.pyc
│  │     │  │  │  ├─ pointPen.cpython-312.pyc
│  │     │  │  │  ├─ utils.cpython-312.pyc
│  │     │  │  │  └─ validators.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ converters.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ etree.py
│  │     │  │  ├─ filenames.py
│  │     │  │  ├─ glifLib.py
│  │     │  │  ├─ kerning.py
│  │     │  │  ├─ plistlib.py
│  │     │  │  ├─ pointPen.py
│  │     │  │  ├─ utils.py
│  │     │  │  └─ validators.py
│  │     │  ├─ unicodedata/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ Blocks.cpython-312.pyc
│  │     │  │  │  ├─ Mirrored.cpython-312.pyc
│  │     │  │  │  ├─ OTTags.cpython-312.pyc
│  │     │  │  │  ├─ ScriptExtensions.cpython-312.pyc
│  │     │  │  │  └─ Scripts.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ Blocks.py
│  │     │  │  ├─ Mirrored.py
│  │     │  │  ├─ OTTags.py
│  │     │  │  ├─ ScriptExtensions.py
│  │     │  │  └─ Scripts.py
│  │     │  ├─ varLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ avar.cpython-312.pyc
│  │     │  │  │  ├─ avarPlanner.cpython-312.pyc
│  │     │  │  │  ├─ builder.cpython-312.pyc
│  │     │  │  │  ├─ cff.cpython-312.pyc
│  │     │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  ├─ featureVars.cpython-312.pyc
│  │     │  │  │  ├─ hvar.cpython-312.pyc
│  │     │  │  │  ├─ interpolatable.cpython-312.pyc
│  │     │  │  │  ├─ interpolatableHelpers.cpython-312.pyc
│  │     │  │  │  ├─ interpolatablePlot.cpython-312.pyc
│  │     │  │  │  ├─ interpolatableTestContourOrder.cpython-312.pyc
│  │     │  │  │  ├─ interpolatableTestStartingPoint.cpython-312.pyc
│  │     │  │  │  ├─ interpolate_layout.cpython-312.pyc
│  │     │  │  │  ├─ iup.cpython-312.pyc
│  │     │  │  │  ├─ merger.cpython-312.pyc
│  │     │  │  │  ├─ models.cpython-312.pyc
│  │     │  │  │  ├─ multiVarStore.cpython-312.pyc
│  │     │  │  │  ├─ mutator.cpython-312.pyc
│  │     │  │  │  ├─ mvar.cpython-312.pyc
│  │     │  │  │  ├─ plot.cpython-312.pyc
│  │     │  │  │  ├─ stat.cpython-312.pyc
│  │     │  │  │  └─ varStore.cpython-312.pyc
│  │     │  │  ├─ instancer/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  ├─ featureVars.cpython-312.pyc
│  │     │  │  │  │  ├─ names.cpython-312.pyc
│  │     │  │  │  │  └─ solver.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  ├─ featureVars.py
│  │     │  │  │  ├─ names.py
│  │     │  │  │  └─ solver.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ avar.py
│  │     │  │  ├─ avarPlanner.py
│  │     │  │  ├─ builder.py
│  │     │  │  ├─ cff.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ featureVars.py
│  │     │  │  ├─ hvar.py
│  │     │  │  ├─ interpolatable.py
│  │     │  │  ├─ interpolatableHelpers.py
│  │     │  │  ├─ interpolatablePlot.py
│  │     │  │  ├─ interpolatableTestContourOrder.py
│  │     │  │  ├─ interpolatableTestStartingPoint.py
│  │     │  │  ├─ interpolate_layout.py
│  │     │  │  ├─ iup.c
│  │     │  │  ├─ iup.cp312-win_amd64.pyd
│  │     │  │  ├─ iup.py
│  │     │  │  ├─ merger.py
│  │     │  │  ├─ models.py
│  │     │  │  ├─ multiVarStore.py
│  │     │  │  ├─ mutator.py
│  │     │  │  ├─ mvar.py
│  │     │  │  ├─ plot.py
│  │     │  │  ├─ stat.py
│  │     │  │  └─ varStore.py
│  │     │  ├─ voltLib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ ast.cpython-312.pyc
│  │     │  │  │  ├─ error.cpython-312.pyc
│  │     │  │  │  ├─ lexer.cpython-312.pyc
│  │     │  │  │  ├─ parser.cpython-312.pyc
│  │     │  │  │  └─ voltToFea.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ ast.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ lexer.py
│  │     │  │  ├─ parser.py
│  │     │  │  └─ voltToFea.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ afmLib.py
│  │     │  ├─ agl.py
│  │     │  ├─ fontBuilder.py
│  │     │  ├─ help.py
│  │     │  ├─ tfmLib.py
│  │     │  ├─ ttx.py
│  │     │  └─ unicode.py
│  │     ├─ fonttools-4.58.5.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  ├─ LICENSE
│  │     │  │  └─ LICENSE.external
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ future/
│  │     │  ├─ __pycache__/
│  │     │  │  └─ __init__.cpython-312.pyc
│  │     │  ├─ backports/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _markupbase.cpython-312.pyc
│  │     │  │  │  ├─ datetime.cpython-312.pyc
│  │     │  │  │  ├─ misc.cpython-312.pyc
│  │     │  │  │  ├─ socket.cpython-312.pyc
│  │     │  │  │  ├─ socketserver.cpython-312.pyc
│  │     │  │  │  └─ total_ordering.cpython-312.pyc
│  │     │  │  ├─ email/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _encoded_words.cpython-312.pyc
│  │     │  │  │  │  ├─ _header_value_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ _parseaddr.cpython-312.pyc
│  │     │  │  │  │  ├─ _policybase.cpython-312.pyc
│  │     │  │  │  │  ├─ base64mime.cpython-312.pyc
│  │     │  │  │  │  ├─ charset.cpython-312.pyc
│  │     │  │  │  │  ├─ encoders.cpython-312.pyc
│  │     │  │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  │  ├─ feedparser.cpython-312.pyc
│  │     │  │  │  │  ├─ generator.cpython-312.pyc
│  │     │  │  │  │  ├─ header.cpython-312.pyc
│  │     │  │  │  │  ├─ headerregistry.cpython-312.pyc
│  │     │  │  │  │  ├─ iterators.cpython-312.pyc
│  │     │  │  │  │  ├─ message.cpython-312.pyc
│  │     │  │  │  │  ├─ parser.cpython-312.pyc
│  │     │  │  │  │  ├─ policy.cpython-312.pyc
│  │     │  │  │  │  ├─ quoprimime.cpython-312.pyc
│  │     │  │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  │  ├─ mime/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ application.cpython-312.pyc
│  │     │  │  │  │  │  ├─ audio.cpython-312.pyc
│  │     │  │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  │  ├─ image.cpython-312.pyc
│  │     │  │  │  │  │  ├─ message.cpython-312.pyc
│  │     │  │  │  │  │  ├─ multipart.cpython-312.pyc
│  │     │  │  │  │  │  ├─ nonmultipart.cpython-312.pyc
│  │     │  │  │  │  │  └─ text.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ application.py
│  │     │  │  │  │  ├─ audio.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ image.py
│  │     │  │  │  │  ├─ message.py
│  │     │  │  │  │  ├─ multipart.py
│  │     │  │  │  │  ├─ nonmultipart.py
│  │     │  │  │  │  └─ text.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _encoded_words.py
│  │     │  │  │  ├─ _header_value_parser.py
│  │     │  │  │  ├─ _parseaddr.py
│  │     │  │  │  ├─ _policybase.py
│  │     │  │  │  ├─ base64mime.py
│  │     │  │  │  ├─ charset.py
│  │     │  │  │  ├─ encoders.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ feedparser.py
│  │     │  │  │  ├─ generator.py
│  │     │  │  │  ├─ header.py
│  │     │  │  │  ├─ headerregistry.py
│  │     │  │  │  ├─ iterators.py
│  │     │  │  │  ├─ message.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ policy.py
│  │     │  │  │  ├─ quoprimime.py
│  │     │  │  │  └─ utils.py
│  │     │  │  ├─ html/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ entities.cpython-312.pyc
│  │     │  │  │  │  └─ parser.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ entities.py
│  │     │  │  │  └─ parser.py
│  │     │  │  ├─ http/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ client.cpython-312.pyc
│  │     │  │  │  │  ├─ cookiejar.cpython-312.pyc
│  │     │  │  │  │  ├─ cookies.cpython-312.pyc
│  │     │  │  │  │  └─ server.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ client.py
│  │     │  │  │  ├─ cookiejar.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  └─ server.py
│  │     │  │  ├─ test/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ pystone.cpython-312.pyc
│  │     │  │  │  │  ├─ ssl_servers.cpython-312.pyc
│  │     │  │  │  │  └─ support.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ badcert.pem
│  │     │  │  │  ├─ badkey.pem
│  │     │  │  │  ├─ dh512.pem
│  │     │  │  │  ├─ https_svn_python_org_root.pem
│  │     │  │  │  ├─ keycert.passwd.pem
│  │     │  │  │  ├─ keycert.pem
│  │     │  │  │  ├─ keycert2.pem
│  │     │  │  │  ├─ nokia.pem
│  │     │  │  │  ├─ nullbytecert.pem
│  │     │  │  │  ├─ nullcert.pem
│  │     │  │  │  ├─ pystone.py
│  │     │  │  │  ├─ sha256.pem
│  │     │  │  │  ├─ ssl_cert.pem
│  │     │  │  │  ├─ ssl_key.passwd.pem
│  │     │  │  │  ├─ ssl_key.pem
│  │     │  │  │  ├─ ssl_servers.py
│  │     │  │  │  └─ support.py
│  │     │  │  ├─ urllib/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ error.cpython-312.pyc
│  │     │  │  │  │  ├─ parse.cpython-312.pyc
│  │     │  │  │  │  ├─ request.cpython-312.pyc
│  │     │  │  │  │  ├─ response.cpython-312.pyc
│  │     │  │  │  │  └─ robotparser.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ error.py
│  │     │  │  │  ├─ parse.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  └─ robotparser.py
│  │     │  │  ├─ xmlrpc/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ client.cpython-312.pyc
│  │     │  │  │  │  └─ server.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ client.py
│  │     │  │  │  └─ server.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _markupbase.py
│  │     │  │  ├─ datetime.py
│  │     │  │  ├─ misc.py
│  │     │  │  ├─ socket.py
│  │     │  │  ├─ socketserver.py
│  │     │  │  └─ total_ordering.py
│  │     │  ├─ builtins/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ disabled.cpython-312.pyc
│  │     │  │  │  ├─ iterators.cpython-312.pyc
│  │     │  │  │  ├─ misc.cpython-312.pyc
│  │     │  │  │  ├─ new_min_max.cpython-312.pyc
│  │     │  │  │  ├─ newnext.cpython-312.pyc
│  │     │  │  │  ├─ newround.cpython-312.pyc
│  │     │  │  │  └─ newsuper.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ disabled.py
│  │     │  │  ├─ iterators.py
│  │     │  │  ├─ misc.py
│  │     │  │  ├─ new_min_max.py
│  │     │  │  ├─ newnext.py
│  │     │  │  ├─ newround.py
│  │     │  │  └─ newsuper.py
│  │     │  ├─ moves/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _dummy_thread.cpython-312.pyc
│  │     │  │  │  ├─ _markupbase.cpython-312.pyc
│  │     │  │  │  ├─ _thread.cpython-312.pyc
│  │     │  │  │  ├─ builtins.cpython-312.pyc
│  │     │  │  │  ├─ collections.cpython-312.pyc
│  │     │  │  │  ├─ configparser.cpython-312.pyc
│  │     │  │  │  ├─ copyreg.cpython-312.pyc
│  │     │  │  │  ├─ itertools.cpython-312.pyc
│  │     │  │  │  ├─ multiprocessing.cpython-312.pyc
│  │     │  │  │  ├─ pickle.cpython-312.pyc
│  │     │  │  │  ├─ queue.cpython-312.pyc
│  │     │  │  │  ├─ reprlib.cpython-312.pyc
│  │     │  │  │  ├─ socketserver.cpython-312.pyc
│  │     │  │  │  ├─ subprocess.cpython-312.pyc
│  │     │  │  │  ├─ sys.cpython-312.pyc
│  │     │  │  │  └─ winreg.cpython-312.pyc
│  │     │  │  ├─ dbm/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ dumb.cpython-312.pyc
│  │     │  │  │  │  ├─ gnu.cpython-312.pyc
│  │     │  │  │  │  └─ ndbm.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ dumb.py
│  │     │  │  │  ├─ gnu.py
│  │     │  │  │  └─ ndbm.py
│  │     │  │  ├─ html/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ entities.cpython-312.pyc
│  │     │  │  │  │  └─ parser.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ entities.py
│  │     │  │  │  └─ parser.py
│  │     │  │  ├─ http/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ client.cpython-312.pyc
│  │     │  │  │  │  ├─ cookiejar.cpython-312.pyc
│  │     │  │  │  │  ├─ cookies.cpython-312.pyc
│  │     │  │  │  │  └─ server.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ client.py
│  │     │  │  │  ├─ cookiejar.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  └─ server.py
│  │     │  │  ├─ test/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ support.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ support.py
│  │     │  │  ├─ tkinter/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ colorchooser.cpython-312.pyc
│  │     │  │  │  │  ├─ commondialog.cpython-312.pyc
│  │     │  │  │  │  ├─ constants.cpython-312.pyc
│  │     │  │  │  │  ├─ dialog.cpython-312.pyc
│  │     │  │  │  │  ├─ dnd.cpython-312.pyc
│  │     │  │  │  │  ├─ filedialog.cpython-312.pyc
│  │     │  │  │  │  ├─ font.cpython-312.pyc
│  │     │  │  │  │  ├─ messagebox.cpython-312.pyc
│  │     │  │  │  │  ├─ scrolledtext.cpython-312.pyc
│  │     │  │  │  │  ├─ simpledialog.cpython-312.pyc
│  │     │  │  │  │  ├─ tix.cpython-312.pyc
│  │     │  │  │  │  └─ ttk.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ colorchooser.py
│  │     │  │  │  ├─ commondialog.py
│  │     │  │  │  ├─ constants.py
│  │     │  │  │  ├─ dialog.py
│  │     │  │  │  ├─ dnd.py
│  │     │  │  │  ├─ filedialog.py
│  │     │  │  │  ├─ font.py
│  │     │  │  │  ├─ messagebox.py
│  │     │  │  │  ├─ scrolledtext.py
│  │     │  │  │  ├─ simpledialog.py
│  │     │  │  │  ├─ tix.py
│  │     │  │  │  └─ ttk.py
│  │     │  │  ├─ urllib/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ error.cpython-312.pyc
│  │     │  │  │  │  ├─ parse.cpython-312.pyc
│  │     │  │  │  │  ├─ request.cpython-312.pyc
│  │     │  │  │  │  ├─ response.cpython-312.pyc
│  │     │  │  │  │  └─ robotparser.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ error.py
│  │     │  │  │  ├─ parse.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  ├─ response.py
│  │     │  │  │  └─ robotparser.py
│  │     │  │  ├─ xmlrpc/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ client.cpython-312.pyc
│  │     │  │  │  │  └─ server.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ client.py
│  │     │  │  │  └─ server.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _dummy_thread.py
│  │     │  │  ├─ _markupbase.py
│  │     │  │  ├─ _thread.py
│  │     │  │  ├─ builtins.py
│  │     │  │  ├─ collections.py
│  │     │  │  ├─ configparser.py
│  │     │  │  ├─ copyreg.py
│  │     │  │  ├─ itertools.py
│  │     │  │  ├─ multiprocessing.py
│  │     │  │  ├─ pickle.py
│  │     │  │  ├─ queue.py
│  │     │  │  ├─ reprlib.py
│  │     │  │  ├─ socketserver.py
│  │     │  │  ├─ subprocess.py
│  │     │  │  ├─ sys.py
│  │     │  │  └─ winreg.py
│  │     │  ├─ standard_library/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ base.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ base.py
│  │     │  ├─ types/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ newbytes.cpython-312.pyc
│  │     │  │  │  ├─ newdict.cpython-312.pyc
│  │     │  │  │  ├─ newint.cpython-312.pyc
│  │     │  │  │  ├─ newlist.cpython-312.pyc
│  │     │  │  │  ├─ newmemoryview.cpython-312.pyc
│  │     │  │  │  ├─ newobject.cpython-312.pyc
│  │     │  │  │  ├─ newopen.cpython-312.pyc
│  │     │  │  │  ├─ newrange.cpython-312.pyc
│  │     │  │  │  └─ newstr.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ newbytes.py
│  │     │  │  ├─ newdict.py
│  │     │  │  ├─ newint.py
│  │     │  │  ├─ newlist.py
│  │     │  │  ├─ newmemoryview.py
│  │     │  │  ├─ newobject.py
│  │     │  │  ├─ newopen.py
│  │     │  │  ├─ newrange.py
│  │     │  │  └─ newstr.py
│  │     │  ├─ utils/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ surrogateescape.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ surrogateescape.py
│  │     │  └─ __init__.py
│  │     ├─ future-1.0.0.dist-info/
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ geemap/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ ai.cpython-312.pyc
│  │     │  │  ├─ basemaps.cpython-312.pyc
│  │     │  │  ├─ cartoee.cpython-312.pyc
│  │     │  │  ├─ chart.cpython-312.pyc
│  │     │  │  ├─ cli.cpython-312.pyc
│  │     │  │  ├─ colormaps.cpython-312.pyc
│  │     │  │  ├─ common.cpython-312.pyc
│  │     │  │  ├─ conversion.cpython-312.pyc
│  │     │  │  ├─ core.cpython-312.pyc
│  │     │  │  ├─ coreutils.cpython-312.pyc
│  │     │  │  ├─ datasets.cpython-312.pyc
│  │     │  │  ├─ deck.cpython-312.pyc
│  │     │  │  ├─ ee_tile_layers.cpython-312.pyc
│  │     │  │  ├─ foliumap.cpython-312.pyc
│  │     │  │  ├─ geemap.cpython-312.pyc
│  │     │  │  ├─ kepler.cpython-312.pyc
│  │     │  │  ├─ legends.cpython-312.pyc
│  │     │  │  ├─ map_widgets.cpython-312.pyc
│  │     │  │  ├─ maplibregl.cpython-312.pyc
│  │     │  │  ├─ ml.cpython-312.pyc
│  │     │  │  ├─ osm.cpython-312.pyc
│  │     │  │  ├─ plot.cpython-312.pyc
│  │     │  │  ├─ plotlymap.cpython-312.pyc
│  │     │  │  ├─ report.cpython-312.pyc
│  │     │  │  ├─ timelapse.cpython-312.pyc
│  │     │  │  └─ toolbar.cpython-312.pyc
│  │     │  ├─ data/
│  │     │  │  ├─ fonts/
│  │     │  │  │  ├─ alibaba.otf
│  │     │  │  │  └─ arial.ttf
│  │     │  │  ├─ javascripts/
│  │     │  │  │  ├─ ClippedComposite.js
│  │     │  │  │  ├─ FromName.js
│  │     │  │  │  ├─ ModisQaBands.js
│  │     │  │  │  ├─ NormalizedDifference.js
│  │     │  │  │  └─ QualityMosaic.js
│  │     │  │  ├─ python/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ javascript_to_python.cpython-312.pyc
│  │     │  │  │  └─ javascript_to_python.py
│  │     │  │  ├─ template/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ template.cpython-312.pyc
│  │     │  │  │  ├─ ee_api_docs.csv
│  │     │  │  │  ├─ ee_api_docs.html
│  │     │  │  │  ├─ ee_data_catalog.csv
│  │     │  │  │  ├─ ee_legend_table.txt
│  │     │  │  │  ├─ legend_style.html
│  │     │  │  │  ├─ legend.html
│  │     │  │  │  ├─ legend.txt
│  │     │  │  │  ├─ NLCD.qml
│  │     │  │  │  ├─ template.py
│  │     │  │  │  └─ toolbox.csv
│  │     │  │  ├─ census_data.json
│  │     │  │  └─ gee_f.json
│  │     │  ├─ examples/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ datasets.txt
│  │     │  ├─ __init__.py
│  │     │  ├─ ai.py
│  │     │  ├─ basemaps.py
│  │     │  ├─ cartoee.py
│  │     │  ├─ chart.py
│  │     │  ├─ cli.py
│  │     │  ├─ colormaps.py
│  │     │  ├─ common.py
│  │     │  ├─ conversion.py
│  │     │  ├─ core.py
│  │     │  ├─ coreutils.py
│  │     │  ├─ datasets.py
│  │     │  ├─ deck.py
│  │     │  ├─ ee_tile_layers.py
│  │     │  ├─ foliumap.py
│  │     │  ├─ geemap.py
│  │     │  ├─ kepler.py
│  │     │  ├─ legends.py
│  │     │  ├─ map_widgets.py
│  │     │  ├─ maplibregl.py
│  │     │  ├─ ml.py
│  │     │  ├─ osm.py
│  │     │  ├─ plot.py
│  │     │  ├─ plotlymap.py
│  │     │  ├─ report.py
│  │     │  ├─ timelapse.py
│  │     │  └─ toolbar.py
│  │     ├─ geemap-0.35.3.dist-info/
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ geocoder/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ api.cpython-312.pyc
│  │     │  │  ├─ arcgis_reverse.cpython-312.pyc
│  │     │  │  ├─ arcgis.cpython-312.pyc
│  │     │  │  ├─ baidu_reverse.cpython-312.pyc
│  │     │  │  ├─ baidu.cpython-312.pyc
│  │     │  │  ├─ base.cpython-312.pyc
│  │     │  │  ├─ bing_batch_forward.cpython-312.pyc
│  │     │  │  ├─ bing_batch_reverse.cpython-312.pyc
│  │     │  │  ├─ bing_batch.cpython-312.pyc
│  │     │  │  ├─ bing_reverse.cpython-312.pyc
│  │     │  │  ├─ bing.cpython-312.pyc
│  │     │  │  ├─ canadapost.cpython-312.pyc
│  │     │  │  ├─ cli.cpython-312.pyc
│  │     │  │  ├─ distance.cpython-312.pyc
│  │     │  │  ├─ freegeoip.cpython-312.pyc
│  │     │  │  ├─ gaode_reverse.cpython-312.pyc
│  │     │  │  ├─ gaode.cpython-312.pyc
│  │     │  │  ├─ geocodefarm_reverse.cpython-312.pyc
│  │     │  │  ├─ geocodefarm.cpython-312.pyc
│  │     │  │  ├─ geolytica.cpython-312.pyc
│  │     │  │  ├─ geonames_children.cpython-312.pyc
│  │     │  │  ├─ geonames_details.cpython-312.pyc
│  │     │  │  ├─ geonames_hierarchy.cpython-312.pyc
│  │     │  │  ├─ geonames.cpython-312.pyc
│  │     │  │  ├─ gisgraphy_reverse.cpython-312.pyc
│  │     │  │  ├─ gisgraphy.cpython-312.pyc
│  │     │  │  ├─ google_elevation.cpython-312.pyc
│  │     │  │  ├─ google_places.cpython-312.pyc
│  │     │  │  ├─ google_reverse.cpython-312.pyc
│  │     │  │  ├─ google_timezone.cpython-312.pyc
│  │     │  │  ├─ google.cpython-312.pyc
│  │     │  │  ├─ here_reverse.cpython-312.pyc
│  │     │  │  ├─ here.cpython-312.pyc
│  │     │  │  ├─ ipinfo.cpython-312.pyc
│  │     │  │  ├─ keys.cpython-312.pyc
│  │     │  │  ├─ komoot_reverse.cpython-312.pyc
│  │     │  │  ├─ komoot.cpython-312.pyc
│  │     │  │  ├─ location.cpython-312.pyc
│  │     │  │  ├─ locationiq_reverse.cpython-312.pyc
│  │     │  │  ├─ locationiq.cpython-312.pyc
│  │     │  │  ├─ mapbox_reverse.cpython-312.pyc
│  │     │  │  ├─ mapbox.cpython-312.pyc
│  │     │  │  ├─ mapquest_batch.cpython-312.pyc
│  │     │  │  ├─ mapquest_reverse.cpython-312.pyc
│  │     │  │  ├─ mapquest.cpython-312.pyc
│  │     │  │  ├─ mapzen_reverse.cpython-312.pyc
│  │     │  │  ├─ mapzen.cpython-312.pyc
│  │     │  │  ├─ maxmind.cpython-312.pyc
│  │     │  │  ├─ opencage_reverse.cpython-312.pyc
│  │     │  │  ├─ opencage.cpython-312.pyc
│  │     │  │  ├─ osm_reverse.cpython-312.pyc
│  │     │  │  ├─ osm.cpython-312.pyc
│  │     │  │  ├─ ottawa_parcel.cpython-312.pyc
│  │     │  │  ├─ ottawa.cpython-312.pyc
│  │     │  │  ├─ tamu.cpython-312.pyc
│  │     │  │  ├─ tgos.cpython-312.pyc
│  │     │  │  ├─ tomtom.cpython-312.pyc
│  │     │  │  ├─ uscensus_batch.cpython-312.pyc
│  │     │  │  ├─ uscensus_reverse.cpython-312.pyc
│  │     │  │  ├─ uscensus.cpython-312.pyc
│  │     │  │  ├─ w3w_reverse.cpython-312.pyc
│  │     │  │  ├─ w3w.cpython-312.pyc
│  │     │  │  ├─ yahoo.cpython-312.pyc
│  │     │  │  ├─ yandex_reverse.cpython-312.pyc
│  │     │  │  └─ yandex.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ api.py
│  │     │  ├─ arcgis_reverse.py
│  │     │  ├─ arcgis.py
│  │     │  ├─ baidu_reverse.py
│  │     │  ├─ baidu.py
│  │     │  ├─ base.py
│  │     │  ├─ bing_batch_forward.py
│  │     │  ├─ bing_batch_reverse.py
│  │     │  ├─ bing_batch.py
│  │     │  ├─ bing_reverse.py
│  │     │  ├─ bing.py
│  │     │  ├─ canadapost.py
│  │     │  ├─ cli.py
│  │     │  ├─ distance.py
│  │     │  ├─ freegeoip.py
│  │     │  ├─ gaode_reverse.py
│  │     │  ├─ gaode.py
│  │     │  ├─ geocodefarm_reverse.py
│  │     │  ├─ geocodefarm.py
│  │     │  ├─ geolytica.py
│  │     │  ├─ geonames_children.py
│  │     │  ├─ geonames_details.py
│  │     │  ├─ geonames_hierarchy.py
│  │     │  ├─ geonames.py
│  │     │  ├─ gisgraphy_reverse.py
│  │     │  ├─ gisgraphy.py
│  │     │  ├─ google_elevation.py
│  │     │  ├─ google_places.py
│  │     │  ├─ google_reverse.py
│  │     │  ├─ google_timezone.py
│  │     │  ├─ google.py
│  │     │  ├─ here_reverse.py
│  │     │  ├─ here.py
│  │     │  ├─ ipinfo.py
│  │     │  ├─ keys.py
│  │     │  ├─ komoot_reverse.py
│  │     │  ├─ komoot.py
│  │     │  ├─ location.py
│  │     │  ├─ locationiq_reverse.py
│  │     │  ├─ locationiq.py
│  │     │  ├─ mapbox_reverse.py
│  │     │  ├─ mapbox.py
│  │     │  ├─ mapquest_batch.py
│  │     │  ├─ mapquest_reverse.py
│  │     │  ├─ mapquest.py
│  │     │  ├─ mapzen_reverse.py
│  │     │  ├─ mapzen.py
│  │     │  ├─ maxmind.py
│  │     │  ├─ opencage_reverse.py
│  │     │  ├─ opencage.py
│  │     │  ├─ osm_reverse.py
│  │     │  ├─ osm.py
│  │     │  ├─ ottawa_parcel.py
│  │     │  ├─ ottawa.py
│  │     │  ├─ tamu.py
│  │     │  ├─ tgos.py
│  │     │  ├─ tomtom.py
│  │     │  ├─ uscensus_batch.py
│  │     │  ├─ uscensus_reverse.py
│  │     │  ├─ uscensus.py
│  │     │  ├─ w3w_reverse.py
│  │     │  ├─ w3w.py
│  │     │  ├─ yahoo.py
│  │     │  ├─ yandex_reverse.py
│  │     │  └─ yandex.py
│  │     ├─ geocoder-1.38.1.dist-info/
│  │     │  ├─ DESCRIPTION.rst
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ metadata.json
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ geopandas/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _compat.cpython-312.pyc
│  │     │  │  ├─ _config.cpython-312.pyc
│  │     │  │  ├─ _decorator.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ accessors.cpython-312.pyc
│  │     │  │  ├─ array.cpython-312.pyc
│  │     │  │  ├─ base.cpython-312.pyc
│  │     │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  ├─ explore.cpython-312.pyc
│  │     │  │  ├─ geodataframe.cpython-312.pyc
│  │     │  │  ├─ geoseries.cpython-312.pyc
│  │     │  │  ├─ plotting.cpython-312.pyc
│  │     │  │  ├─ sindex.cpython-312.pyc
│  │     │  │  └─ testing.cpython-312.pyc
│  │     │  ├─ datasets/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ io/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _geoarrow.cpython-312.pyc
│  │     │  │  │  ├─ _pyarrow_hotfix.cpython-312.pyc
│  │     │  │  │  ├─ arrow.cpython-312.pyc
│  │     │  │  │  ├─ file.cpython-312.pyc
│  │     │  │  │  ├─ sql.cpython-312.pyc
│  │     │  │  │  └─ util.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ generate_legacy_storage_files.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arrow.cpython-312.pyc
│  │     │  │  │  │  ├─ test_file_geom_types_drivers.cpython-312.pyc
│  │     │  │  │  │  ├─ test_file.cpython-312.pyc
│  │     │  │  │  │  ├─ test_geoarrow.cpython-312.pyc
│  │     │  │  │  │  ├─ test_infer_schema.cpython-312.pyc
│  │     │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  └─ test_sql.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ generate_legacy_storage_files.py
│  │     │  │  │  ├─ test_arrow.py
│  │     │  │  │  ├─ test_file_geom_types_drivers.py
│  │     │  │  │  ├─ test_file.py
│  │     │  │  │  ├─ test_geoarrow.py
│  │     │  │  │  ├─ test_infer_schema.py
│  │     │  │  │  ├─ test_pickle.py
│  │     │  │  │  └─ test_sql.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _geoarrow.py
│  │     │  │  ├─ _pyarrow_hotfix.py
│  │     │  │  ├─ arrow.py
│  │     │  │  ├─ file.py
│  │     │  │  ├─ sql.py
│  │     │  │  └─ util.py
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  ├─ test_array.cpython-312.pyc
│  │     │  │  │  ├─ test_compat.cpython-312.pyc
│  │     │  │  │  ├─ test_config.cpython-312.pyc
│  │     │  │  │  ├─ test_crs.cpython-312.pyc
│  │     │  │  │  ├─ test_datasets.cpython-312.pyc
│  │     │  │  │  ├─ test_decorator.cpython-312.pyc
│  │     │  │  │  ├─ test_dissolve.cpython-312.pyc
│  │     │  │  │  ├─ test_explore.cpython-312.pyc
│  │     │  │  │  ├─ test_extension_array.cpython-312.pyc
│  │     │  │  │  ├─ test_geocode.cpython-312.pyc
│  │     │  │  │  ├─ test_geodataframe.cpython-312.pyc
│  │     │  │  │  ├─ test_geom_methods.cpython-312.pyc
│  │     │  │  │  ├─ test_geoseries.cpython-312.pyc
│  │     │  │  │  ├─ test_merge.cpython-312.pyc
│  │     │  │  │  ├─ test_op_output_types.cpython-312.pyc
│  │     │  │  │  ├─ test_overlay.cpython-312.pyc
│  │     │  │  │  ├─ test_pandas_accessor.cpython-312.pyc
│  │     │  │  │  ├─ test_pandas_methods.cpython-312.pyc
│  │     │  │  │  ├─ test_plotting.cpython-312.pyc
│  │     │  │  │  ├─ test_show_versions.cpython-312.pyc
│  │     │  │  │  ├─ test_sindex.cpython-312.pyc
│  │     │  │  │  ├─ test_testing.cpython-312.pyc
│  │     │  │  │  ├─ test_types.cpython-312.pyc
│  │     │  │  │  └─ util.cpython-312.pyc
│  │     │  │  ├─ data/
│  │     │  │  │  └─ null_geom.geojson
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ test_api.py
│  │     │  │  ├─ test_array.py
│  │     │  │  ├─ test_compat.py
│  │     │  │  ├─ test_config.py
│  │     │  │  ├─ test_crs.py
│  │     │  │  ├─ test_datasets.py
│  │     │  │  ├─ test_decorator.py
│  │     │  │  ├─ test_dissolve.py
│  │     │  │  ├─ test_explore.py
│  │     │  │  ├─ test_extension_array.py
│  │     │  │  ├─ test_geocode.py
│  │     │  │  ├─ test_geodataframe.py
│  │     │  │  ├─ test_geom_methods.py
│  │     │  │  ├─ test_geoseries.py
│  │     │  │  ├─ test_merge.py
│  │     │  │  ├─ test_op_output_types.py
│  │     │  │  ├─ test_overlay.py
│  │     │  │  ├─ test_pandas_accessor.py
│  │     │  │  ├─ test_pandas_methods.py
│  │     │  │  ├─ test_plotting.py
│  │     │  │  ├─ test_show_versions.py
│  │     │  │  ├─ test_sindex.py
│  │     │  │  ├─ test_testing.py
│  │     │  │  ├─ test_types.py
│  │     │  │  └─ util.py
│  │     │  ├─ tools/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _random.cpython-312.pyc
│  │     │  │  │  ├─ _show_versions.cpython-312.pyc
│  │     │  │  │  ├─ clip.cpython-312.pyc
│  │     │  │  │  ├─ geocoding.cpython-312.pyc
│  │     │  │  │  ├─ hilbert_curve.cpython-312.pyc
│  │     │  │  │  ├─ overlay.cpython-312.pyc
│  │     │  │  │  ├─ sjoin.cpython-312.pyc
│  │     │  │  │  └─ util.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_clip.cpython-312.pyc
│  │     │  │  │  │  ├─ test_hilbert_curve.cpython-312.pyc
│  │     │  │  │  │  ├─ test_random.cpython-312.pyc
│  │     │  │  │  │  ├─ test_sjoin.cpython-312.pyc
│  │     │  │  │  │  └─ test_tools.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_clip.py
│  │     │  │  │  ├─ test_hilbert_curve.py
│  │     │  │  │  ├─ test_random.py
│  │     │  │  │  ├─ test_sjoin.py
│  │     │  │  │  └─ test_tools.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _random.py
│  │     │  │  ├─ _show_versions.py
│  │     │  │  ├─ clip.py
│  │     │  │  ├─ geocoding.py
│  │     │  │  ├─ hilbert_curve.py
│  │     │  │  ├─ overlay.py
│  │     │  │  ├─ sjoin.py
│  │     │  │  └─ util.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _compat.py
│  │     │  ├─ _config.py
│  │     │  ├─ _decorator.py
│  │     │  ├─ _version.py
│  │     │  ├─ accessors.py
│  │     │  ├─ array.py
│  │     │  ├─ base.py
│  │     │  ├─ conftest.py
│  │     │  ├─ explore.py
│  │     │  ├─ geodataframe.py
│  │     │  ├─ geoseries.py
│  │     │  ├─ plotting.py
│  │     │  ├─ sindex.py
│  │     │  └─ testing.py
│  │     ├─ geopandas-1.1.1.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google/
│  │     │  ├─ _async_resumable_media/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _download.cpython-312.pyc
│  │     │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  └─ _upload.cpython-312.pyc
│  │     │  │  ├─ requests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _request_helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ download.cpython-312.pyc
│  │     │  │  │  │  └─ upload.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _request_helpers.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  └─ upload.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _download.py
│  │     │  │  ├─ _helpers.py
│  │     │  │  └─ _upload.py
│  │     │  ├─ _upb/
│  │     │  │  └─ _message.pyd
│  │     │  ├─ api/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ annotations_pb2.cpython-312.pyc
│  │     │  │  │  ├─ auth_pb2.cpython-312.pyc
│  │     │  │  │  ├─ backend_pb2.cpython-312.pyc
│  │     │  │  │  ├─ billing_pb2.cpython-312.pyc
│  │     │  │  │  ├─ client_pb2.cpython-312.pyc
│  │     │  │  │  ├─ config_change_pb2.cpython-312.pyc
│  │     │  │  │  ├─ consumer_pb2.cpython-312.pyc
│  │     │  │  │  ├─ context_pb2.cpython-312.pyc
│  │     │  │  │  ├─ control_pb2.cpython-312.pyc
│  │     │  │  │  ├─ distribution_pb2.cpython-312.pyc
│  │     │  │  │  ├─ documentation_pb2.cpython-312.pyc
│  │     │  │  │  ├─ endpoint_pb2.cpython-312.pyc
│  │     │  │  │  ├─ error_reason_pb2.cpython-312.pyc
│  │     │  │  │  ├─ field_behavior_pb2.cpython-312.pyc
│  │     │  │  │  ├─ field_info_pb2.cpython-312.pyc
│  │     │  │  │  ├─ http_pb2.cpython-312.pyc
│  │     │  │  │  ├─ httpbody_pb2.cpython-312.pyc
│  │     │  │  │  ├─ label_pb2.cpython-312.pyc
│  │     │  │  │  ├─ launch_stage_pb2.cpython-312.pyc
│  │     │  │  │  ├─ log_pb2.cpython-312.pyc
│  │     │  │  │  ├─ logging_pb2.cpython-312.pyc
│  │     │  │  │  ├─ metric_pb2.cpython-312.pyc
│  │     │  │  │  ├─ monitored_resource_pb2.cpython-312.pyc
│  │     │  │  │  ├─ monitoring_pb2.cpython-312.pyc
│  │     │  │  │  ├─ policy_pb2.cpython-312.pyc
│  │     │  │  │  ├─ quota_pb2.cpython-312.pyc
│  │     │  │  │  ├─ resource_pb2.cpython-312.pyc
│  │     │  │  │  ├─ routing_pb2.cpython-312.pyc
│  │     │  │  │  ├─ service_pb2.cpython-312.pyc
│  │     │  │  │  ├─ source_info_pb2.cpython-312.pyc
│  │     │  │  │  ├─ system_parameter_pb2.cpython-312.pyc
│  │     │  │  │  ├─ usage_pb2.cpython-312.pyc
│  │     │  │  │  └─ visibility_pb2.cpython-312.pyc
│  │     │  │  ├─ annotations_pb2.py
│  │     │  │  ├─ annotations_pb2.pyi
│  │     │  │  ├─ annotations.proto
│  │     │  │  ├─ auth_pb2.py
│  │     │  │  ├─ auth_pb2.pyi
│  │     │  │  ├─ auth.proto
│  │     │  │  ├─ backend_pb2.py
│  │     │  │  ├─ backend_pb2.pyi
│  │     │  │  ├─ backend.proto
│  │     │  │  ├─ billing_pb2.py
│  │     │  │  ├─ billing_pb2.pyi
│  │     │  │  ├─ billing.proto
│  │     │  │  ├─ client_pb2.py
│  │     │  │  ├─ client_pb2.pyi
│  │     │  │  ├─ client.proto
│  │     │  │  ├─ config_change_pb2.py
│  │     │  │  ├─ config_change_pb2.pyi
│  │     │  │  ├─ config_change.proto
│  │     │  │  ├─ consumer_pb2.py
│  │     │  │  ├─ consumer_pb2.pyi
│  │     │  │  ├─ consumer.proto
│  │     │  │  ├─ context_pb2.py
│  │     │  │  ├─ context_pb2.pyi
│  │     │  │  ├─ context.proto
│  │     │  │  ├─ control_pb2.py
│  │     │  │  ├─ control_pb2.pyi
│  │     │  │  ├─ control.proto
│  │     │  │  ├─ distribution_pb2.py
│  │     │  │  ├─ distribution_pb2.pyi
│  │     │  │  ├─ distribution.proto
│  │     │  │  ├─ documentation_pb2.py
│  │     │  │  ├─ documentation_pb2.pyi
│  │     │  │  ├─ documentation.proto
│  │     │  │  ├─ endpoint_pb2.py
│  │     │  │  ├─ endpoint_pb2.pyi
│  │     │  │  ├─ endpoint.proto
│  │     │  │  ├─ error_reason_pb2.py
│  │     │  │  ├─ error_reason_pb2.pyi
│  │     │  │  ├─ error_reason.proto
│  │     │  │  ├─ field_behavior_pb2.py
│  │     │  │  ├─ field_behavior_pb2.pyi
│  │     │  │  ├─ field_behavior.proto
│  │     │  │  ├─ field_info_pb2.py
│  │     │  │  ├─ field_info_pb2.pyi
│  │     │  │  ├─ field_info.proto
│  │     │  │  ├─ http_pb2.py
│  │     │  │  ├─ http_pb2.pyi
│  │     │  │  ├─ http.proto
│  │     │  │  ├─ httpbody_pb2.py
│  │     │  │  ├─ httpbody_pb2.pyi
│  │     │  │  ├─ httpbody.proto
│  │     │  │  ├─ label_pb2.py
│  │     │  │  ├─ label_pb2.pyi
│  │     │  │  ├─ label.proto
│  │     │  │  ├─ launch_stage_pb2.py
│  │     │  │  ├─ launch_stage_pb2.pyi
│  │     │  │  ├─ launch_stage.proto
│  │     │  │  ├─ log_pb2.py
│  │     │  │  ├─ log_pb2.pyi
│  │     │  │  ├─ log.proto
│  │     │  │  ├─ logging_pb2.py
│  │     │  │  ├─ logging_pb2.pyi
│  │     │  │  ├─ logging.proto
│  │     │  │  ├─ metric_pb2.py
│  │     │  │  ├─ metric_pb2.pyi
│  │     │  │  ├─ metric.proto
│  │     │  │  ├─ monitored_resource_pb2.py
│  │     │  │  ├─ monitored_resource_pb2.pyi
│  │     │  │  ├─ monitored_resource.proto
│  │     │  │  ├─ monitoring_pb2.py
│  │     │  │  ├─ monitoring_pb2.pyi
│  │     │  │  ├─ monitoring.proto
│  │     │  │  ├─ policy_pb2.py
│  │     │  │  ├─ policy_pb2.pyi
│  │     │  │  ├─ policy.proto
│  │     │  │  ├─ quota_pb2.py
│  │     │  │  ├─ quota_pb2.pyi
│  │     │  │  ├─ quota.proto
│  │     │  │  ├─ resource_pb2.py
│  │     │  │  ├─ resource_pb2.pyi
│  │     │  │  ├─ resource.proto
│  │     │  │  ├─ routing_pb2.py
│  │     │  │  ├─ routing_pb2.pyi
│  │     │  │  ├─ routing.proto
│  │     │  │  ├─ service_pb2.py
│  │     │  │  ├─ service_pb2.pyi
│  │     │  │  ├─ service.proto
│  │     │  │  ├─ source_info_pb2.py
│  │     │  │  ├─ source_info_pb2.pyi
│  │     │  │  ├─ source_info.proto
│  │     │  │  ├─ system_parameter_pb2.py
│  │     │  │  ├─ system_parameter_pb2.pyi
│  │     │  │  ├─ system_parameter.proto
│  │     │  │  ├─ usage_pb2.py
│  │     │  │  ├─ usage_pb2.pyi
│  │     │  │  ├─ usage.proto
│  │     │  │  ├─ visibility_pb2.py
│  │     │  │  ├─ visibility_pb2.pyi
│  │     │  │  └─ visibility.proto
│  │     │  ├─ api_core/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _rest_streaming_base.cpython-312.pyc
│  │     │  │  │  ├─ bidi.cpython-312.pyc
│  │     │  │  │  ├─ client_info.cpython-312.pyc
│  │     │  │  │  ├─ client_logging.cpython-312.pyc
│  │     │  │  │  ├─ client_options.cpython-312.pyc
│  │     │  │  │  ├─ datetime_helpers.cpython-312.pyc
│  │     │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  ├─ extended_operation.cpython-312.pyc
│  │     │  │  │  ├─ general_helpers.cpython-312.pyc
│  │     │  │  │  ├─ grpc_helpers_async.cpython-312.pyc
│  │     │  │  │  ├─ grpc_helpers.cpython-312.pyc
│  │     │  │  │  ├─ iam.cpython-312.pyc
│  │     │  │  │  ├─ operation_async.cpython-312.pyc
│  │     │  │  │  ├─ operation.cpython-312.pyc
│  │     │  │  │  ├─ page_iterator_async.cpython-312.pyc
│  │     │  │  │  ├─ page_iterator.cpython-312.pyc
│  │     │  │  │  ├─ path_template.cpython-312.pyc
│  │     │  │  │  ├─ protobuf_helpers.cpython-312.pyc
│  │     │  │  │  ├─ rest_helpers.cpython-312.pyc
│  │     │  │  │  ├─ rest_streaming_async.cpython-312.pyc
│  │     │  │  │  ├─ rest_streaming.cpython-312.pyc
│  │     │  │  │  ├─ retry_async.cpython-312.pyc
│  │     │  │  │  ├─ timeout.cpython-312.pyc
│  │     │  │  │  ├─ universe.cpython-312.pyc
│  │     │  │  │  ├─ version_header.cpython-312.pyc
│  │     │  │  │  └─ version.cpython-312.pyc
│  │     │  │  ├─ future/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ async_future.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  └─ polling.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _helpers.py
│  │     │  │  │  ├─ async_future.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  └─ polling.py
│  │     │  │  ├─ gapic_v1/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ client_info.cpython-312.pyc
│  │     │  │  │  │  ├─ config_async.cpython-312.pyc
│  │     │  │  │  │  ├─ config.cpython-312.pyc
│  │     │  │  │  │  ├─ method_async.cpython-312.pyc
│  │     │  │  │  │  ├─ method.cpython-312.pyc
│  │     │  │  │  │  └─ routing_header.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ client_info.py
│  │     │  │  │  ├─ config_async.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ method_async.py
│  │     │  │  │  ├─ method.py
│  │     │  │  │  └─ routing_header.py
│  │     │  │  ├─ operations_v1/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ abstract_operations_base_client.cpython-312.pyc
│  │     │  │  │  │  ├─ abstract_operations_client.cpython-312.pyc
│  │     │  │  │  │  ├─ operations_async_client.cpython-312.pyc
│  │     │  │  │  │  ├─ operations_client_config.cpython-312.pyc
│  │     │  │  │  │  ├─ operations_client.cpython-312.pyc
│  │     │  │  │  │  ├─ operations_rest_client_async.cpython-312.pyc
│  │     │  │  │  │  ├─ pagers_async.cpython-312.pyc
│  │     │  │  │  │  ├─ pagers_base.cpython-312.pyc
│  │     │  │  │  │  └─ pagers.cpython-312.pyc
│  │     │  │  │  ├─ transports/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  │  ├─ rest_asyncio.cpython-312.pyc
│  │     │  │  │  │  │  └─ rest.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ rest_asyncio.py
│  │     │  │  │  │  └─ rest.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ abstract_operations_base_client.py
│  │     │  │  │  ├─ abstract_operations_client.py
│  │     │  │  │  ├─ operations_async_client.py
│  │     │  │  │  ├─ operations_client_config.py
│  │     │  │  │  ├─ operations_client.py
│  │     │  │  │  ├─ operations_rest_client_async.py
│  │     │  │  │  ├─ pagers_async.py
│  │     │  │  │  ├─ pagers_base.py
│  │     │  │  │  └─ pagers.py
│  │     │  │  ├─ retry/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ retry_base.cpython-312.pyc
│  │     │  │  │  │  ├─ retry_streaming_async.cpython-312.pyc
│  │     │  │  │  │  ├─ retry_streaming.cpython-312.pyc
│  │     │  │  │  │  ├─ retry_unary_async.cpython-312.pyc
│  │     │  │  │  │  └─ retry_unary.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ retry_base.py
│  │     │  │  │  ├─ retry_streaming_async.py
│  │     │  │  │  ├─ retry_streaming.py
│  │     │  │  │  ├─ retry_unary_async.py
│  │     │  │  │  └─ retry_unary.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _rest_streaming_base.py
│  │     │  │  ├─ bidi.py
│  │     │  │  ├─ client_info.py
│  │     │  │  ├─ client_logging.py
│  │     │  │  ├─ client_options.py
│  │     │  │  ├─ datetime_helpers.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ extended_operation.py
│  │     │  │  ├─ general_helpers.py
│  │     │  │  ├─ grpc_helpers_async.py
│  │     │  │  ├─ grpc_helpers.py
│  │     │  │  ├─ iam.py
│  │     │  │  ├─ operation_async.py
│  │     │  │  ├─ operation.py
│  │     │  │  ├─ page_iterator_async.py
│  │     │  │  ├─ page_iterator.py
│  │     │  │  ├─ path_template.py
│  │     │  │  ├─ protobuf_helpers.py
│  │     │  │  ├─ py.typed
│  │     │  │  ├─ rest_helpers.py
│  │     │  │  ├─ rest_streaming_async.py
│  │     │  │  ├─ rest_streaming.py
│  │     │  │  ├─ retry_async.py
│  │     │  │  ├─ timeout.py
│  │     │  │  ├─ universe.py
│  │     │  │  ├─ version_header.py
│  │     │  │  └─ version.py
│  │     │  ├─ auth/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _cloud_sdk.cpython-312.pyc
│  │     │  │  │  ├─ _credentials_async.cpython-312.pyc
│  │     │  │  │  ├─ _credentials_base.cpython-312.pyc
│  │     │  │  │  ├─ _default_async.cpython-312.pyc
│  │     │  │  │  ├─ _default.cpython-312.pyc
│  │     │  │  │  ├─ _exponential_backoff.cpython-312.pyc
│  │     │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  ├─ _jwt_async.cpython-312.pyc
│  │     │  │  │  ├─ _oauth2client.cpython-312.pyc
│  │     │  │  │  ├─ _refresh_worker.cpython-312.pyc
│  │     │  │  │  ├─ _service_account_info.cpython-312.pyc
│  │     │  │  │  ├─ api_key.cpython-312.pyc
│  │     │  │  │  ├─ app_engine.cpython-312.pyc
│  │     │  │  │  ├─ aws.cpython-312.pyc
│  │     │  │  │  ├─ credentials.cpython-312.pyc
│  │     │  │  │  ├─ downscoped.cpython-312.pyc
│  │     │  │  │  ├─ environment_vars.cpython-312.pyc
│  │     │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  ├─ external_account_authorized_user.cpython-312.pyc
│  │     │  │  │  ├─ external_account.cpython-312.pyc
│  │     │  │  │  ├─ iam.cpython-312.pyc
│  │     │  │  │  ├─ identity_pool.cpython-312.pyc
│  │     │  │  │  ├─ impersonated_credentials.cpython-312.pyc
│  │     │  │  │  ├─ jwt.cpython-312.pyc
│  │     │  │  │  ├─ metrics.cpython-312.pyc
│  │     │  │  │  ├─ pluggable.cpython-312.pyc
│  │     │  │  │  └─ version.cpython-312.pyc
│  │     │  │  ├─ aio/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  │  └─ credentials.cpython-312.pyc
│  │     │  │  │  ├─ transport/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ aiohttp.cpython-312.pyc
│  │     │  │  │  │  │  └─ sessions.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ aiohttp.py
│  │     │  │  │  │  └─ sessions.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _helpers.py
│  │     │  │  │  └─ credentials.py
│  │     │  │  ├─ compute_engine/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _metadata.cpython-312.pyc
│  │     │  │  │  │  └─ credentials.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _metadata.py
│  │     │  │  │  └─ credentials.py
│  │     │  │  ├─ crypt/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _cryptography_rsa.cpython-312.pyc
│  │     │  │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ _python_rsa.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ es256.cpython-312.pyc
│  │     │  │  │  │  └─ rsa.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _cryptography_rsa.py
│  │     │  │  │  ├─ _helpers.py
│  │     │  │  │  ├─ _python_rsa.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ es256.py
│  │     │  │  │  └─ rsa.py
│  │     │  │  ├─ transport/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _aiohttp_requests.cpython-312.pyc
│  │     │  │  │  │  ├─ _custom_tls_signer.cpython-312.pyc
│  │     │  │  │  │  ├─ _http_client.cpython-312.pyc
│  │     │  │  │  │  ├─ _mtls_helper.cpython-312.pyc
│  │     │  │  │  │  ├─ _requests_base.cpython-312.pyc
│  │     │  │  │  │  ├─ grpc.cpython-312.pyc
│  │     │  │  │  │  ├─ mtls.cpython-312.pyc
│  │     │  │  │  │  ├─ requests.cpython-312.pyc
│  │     │  │  │  │  └─ urllib3.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _aiohttp_requests.py
│  │     │  │  │  ├─ _custom_tls_signer.py
│  │     │  │  │  ├─ _http_client.py
│  │     │  │  │  ├─ _mtls_helper.py
│  │     │  │  │  ├─ _requests_base.py
│  │     │  │  │  ├─ grpc.py
│  │     │  │  │  ├─ mtls.py
│  │     │  │  │  ├─ requests.py
│  │     │  │  │  └─ urllib3.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _cloud_sdk.py
│  │     │  │  ├─ _credentials_async.py
│  │     │  │  ├─ _credentials_base.py
│  │     │  │  ├─ _default_async.py
│  │     │  │  ├─ _default.py
│  │     │  │  ├─ _exponential_backoff.py
│  │     │  │  ├─ _helpers.py
│  │     │  │  ├─ _jwt_async.py
│  │     │  │  ├─ _oauth2client.py
│  │     │  │  ├─ _refresh_worker.py
│  │     │  │  ├─ _service_account_info.py
│  │     │  │  ├─ api_key.py
│  │     │  │  ├─ app_engine.py
│  │     │  │  ├─ aws.py
│  │     │  │  ├─ credentials.py
│  │     │  │  ├─ downscoped.py
│  │     │  │  ├─ environment_vars.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ external_account_authorized_user.py
│  │     │  │  ├─ external_account.py
│  │     │  │  ├─ iam.py
│  │     │  │  ├─ identity_pool.py
│  │     │  │  ├─ impersonated_credentials.py
│  │     │  │  ├─ jwt.py
│  │     │  │  ├─ metrics.py
│  │     │  │  ├─ pluggable.py
│  │     │  │  ├─ py.typed
│  │     │  │  └─ version.py
│  │     │  ├─ cloud/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ extended_operations_pb2.cpython-312.pyc
│  │     │  │  │  └─ version.cpython-312.pyc
│  │     │  │  ├─ _helpers/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ _http/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ _testing/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ client/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ environment_vars/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ exceptions/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ location/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ locations_pb2.cpython-312.pyc
│  │     │  │  │  ├─ locations_pb2.py
│  │     │  │  │  ├─ locations_pb2.pyi
│  │     │  │  │  └─ locations.proto
│  │     │  │  ├─ obsolete/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ operation/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ storage/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ _http.cpython-312.pyc
│  │     │  │  │  │  ├─ _opentelemetry_tracing.cpython-312.pyc
│  │     │  │  │  │  ├─ _signing.cpython-312.pyc
│  │     │  │  │  │  ├─ acl.cpython-312.pyc
│  │     │  │  │  │  ├─ batch.cpython-312.pyc
│  │     │  │  │  │  ├─ blob.cpython-312.pyc
│  │     │  │  │  │  ├─ bucket.cpython-312.pyc
│  │     │  │  │  │  ├─ client.cpython-312.pyc
│  │     │  │  │  │  ├─ constants.cpython-312.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ fileio.cpython-312.pyc
│  │     │  │  │  │  ├─ hmac_key.cpython-312.pyc
│  │     │  │  │  │  ├─ iam.cpython-312.pyc
│  │     │  │  │  │  ├─ notification.cpython-312.pyc
│  │     │  │  │  │  ├─ retry.cpython-312.pyc
│  │     │  │  │  │  ├─ transfer_manager.cpython-312.pyc
│  │     │  │  │  │  └─ version.cpython-312.pyc
│  │     │  │  │  ├─ _media/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _download.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _upload.cpython-312.pyc
│  │     │  │  │  │  │  └─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ requests/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ _request_helpers.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ download.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ upload.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ _request_helpers.py
│  │     │  │  │  │  │  ├─ download.py
│  │     │  │  │  │  │  └─ upload.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _download.py
│  │     │  │  │  │  ├─ _helpers.py
│  │     │  │  │  │  ├─ _upload.py
│  │     │  │  │  │  ├─ common.py
│  │     │  │  │  │  └─ py.typed
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _helpers.py
│  │     │  │  │  ├─ _http.py
│  │     │  │  │  ├─ _opentelemetry_tracing.py
│  │     │  │  │  ├─ _signing.py
│  │     │  │  │  ├─ acl.py
│  │     │  │  │  ├─ batch.py
│  │     │  │  │  ├─ blob.py
│  │     │  │  │  ├─ bucket.py
│  │     │  │  │  ├─ client.py
│  │     │  │  │  ├─ constants.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fileio.py
│  │     │  │  │  ├─ hmac_key.py
│  │     │  │  │  ├─ iam.py
│  │     │  │  │  ├─ notification.py
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ transfer_manager.py
│  │     │  │  │  └─ version.py
│  │     │  │  ├─ extended_operations_pb2.py
│  │     │  │  ├─ extended_operations_pb2.pyi
│  │     │  │  ├─ extended_operations.proto
│  │     │  │  └─ version.py
│  │     │  ├─ gapic/
│  │     │  │  └─ metadata/
│  │     │  │     ├─ __pycache__/
│  │     │  │     │  └─ gapic_metadata_pb2.cpython-312.pyc
│  │     │  │     ├─ gapic_metadata_pb2.py
│  │     │  │     ├─ gapic_metadata_pb2.pyi
│  │     │  │     └─ gapic_metadata.proto
│  │     │  ├─ logging/
│  │     │  │  └─ type/
│  │     │  │     ├─ __pycache__/
│  │     │  │     │  ├─ http_request_pb2.cpython-312.pyc
│  │     │  │     │  └─ log_severity_pb2.cpython-312.pyc
│  │     │  │     ├─ http_request_pb2.py
│  │     │  │     ├─ http_request_pb2.pyi
│  │     │  │     ├─ http_request.proto
│  │     │  │     ├─ log_severity_pb2.py
│  │     │  │     ├─ log_severity_pb2.pyi
│  │     │  │     └─ log_severity.proto
│  │     │  ├─ longrunning/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ operations_grpc_pb2.cpython-312.pyc
│  │     │  │  │  ├─ operations_grpc.cpython-312.pyc
│  │     │  │  │  ├─ operations_pb2_grpc.cpython-312.pyc
│  │     │  │  │  ├─ operations_pb2.cpython-312.pyc
│  │     │  │  │  ├─ operations_proto_pb2.cpython-312.pyc
│  │     │  │  │  └─ operations_proto.cpython-312.pyc
│  │     │  │  ├─ operations_grpc_pb2.py
│  │     │  │  ├─ operations_grpc.py
│  │     │  │  ├─ operations_pb2_grpc.py
│  │     │  │  ├─ operations_pb2.py
│  │     │  │  ├─ operations_proto_pb2.py
│  │     │  │  ├─ operations_proto_pb2.pyi
│  │     │  │  ├─ operations_proto.proto
│  │     │  │  └─ operations_proto.py
│  │     │  ├─ oauth2/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _client_async.cpython-312.pyc
│  │     │  │  │  ├─ _client.cpython-312.pyc
│  │     │  │  │  ├─ _credentials_async.cpython-312.pyc
│  │     │  │  │  ├─ _id_token_async.cpython-312.pyc
│  │     │  │  │  ├─ _reauth_async.cpython-312.pyc
│  │     │  │  │  ├─ _service_account_async.cpython-312.pyc
│  │     │  │  │  ├─ challenges.cpython-312.pyc
│  │     │  │  │  ├─ credentials.cpython-312.pyc
│  │     │  │  │  ├─ gdch_credentials.cpython-312.pyc
│  │     │  │  │  ├─ id_token.cpython-312.pyc
│  │     │  │  │  ├─ reauth.cpython-312.pyc
│  │     │  │  │  ├─ service_account.cpython-312.pyc
│  │     │  │  │  ├─ sts.cpython-312.pyc
│  │     │  │  │  ├─ utils.cpython-312.pyc
│  │     │  │  │  ├─ webauthn_handler_factory.cpython-312.pyc
│  │     │  │  │  ├─ webauthn_handler.cpython-312.pyc
│  │     │  │  │  └─ webauthn_types.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _client_async.py
│  │     │  │  ├─ _client.py
│  │     │  │  ├─ _credentials_async.py
│  │     │  │  ├─ _id_token_async.py
│  │     │  │  ├─ _reauth_async.py
│  │     │  │  ├─ _service_account_async.py
│  │     │  │  ├─ challenges.py
│  │     │  │  ├─ credentials.py
│  │     │  │  ├─ gdch_credentials.py
│  │     │  │  ├─ id_token.py
│  │     │  │  ├─ py.typed
│  │     │  │  ├─ reauth.py
│  │     │  │  ├─ service_account.py
│  │     │  │  ├─ sts.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ webauthn_handler_factory.py
│  │     │  │  ├─ webauthn_handler.py
│  │     │  │  └─ webauthn_types.py
│  │     │  ├─ protobuf/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ any_pb2.cpython-312.pyc
│  │     │  │  │  ├─ any.cpython-312.pyc
│  │     │  │  │  ├─ api_pb2.cpython-312.pyc
│  │     │  │  │  ├─ descriptor_database.cpython-312.pyc
│  │     │  │  │  ├─ descriptor_pb2.cpython-312.pyc
│  │     │  │  │  ├─ descriptor_pool.cpython-312.pyc
│  │     │  │  │  ├─ descriptor.cpython-312.pyc
│  │     │  │  │  ├─ duration_pb2.cpython-312.pyc
│  │     │  │  │  ├─ duration.cpython-312.pyc
│  │     │  │  │  ├─ empty_pb2.cpython-312.pyc
│  │     │  │  │  ├─ field_mask_pb2.cpython-312.pyc
│  │     │  │  │  ├─ json_format.cpython-312.pyc
│  │     │  │  │  ├─ message_factory.cpython-312.pyc
│  │     │  │  │  ├─ message.cpython-312.pyc
│  │     │  │  │  ├─ proto_builder.cpython-312.pyc
│  │     │  │  │  ├─ proto_json.cpython-312.pyc
│  │     │  │  │  ├─ proto_text.cpython-312.pyc
│  │     │  │  │  ├─ proto.cpython-312.pyc
│  │     │  │  │  ├─ reflection.cpython-312.pyc
│  │     │  │  │  ├─ runtime_version.cpython-312.pyc
│  │     │  │  │  ├─ service_reflection.cpython-312.pyc
│  │     │  │  │  ├─ source_context_pb2.cpython-312.pyc
│  │     │  │  │  ├─ struct_pb2.cpython-312.pyc
│  │     │  │  │  ├─ symbol_database.cpython-312.pyc
│  │     │  │  │  ├─ text_encoding.cpython-312.pyc
│  │     │  │  │  ├─ text_format.cpython-312.pyc
│  │     │  │  │  ├─ timestamp_pb2.cpython-312.pyc
│  │     │  │  │  ├─ timestamp.cpython-312.pyc
│  │     │  │  │  ├─ type_pb2.cpython-312.pyc
│  │     │  │  │  ├─ unknown_fields.cpython-312.pyc
│  │     │  │  │  └─ wrappers_pb2.cpython-312.pyc
│  │     │  │  ├─ compiler/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ plugin_pb2.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ plugin_pb2.py
│  │     │  │  ├─ internal/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ api_implementation.cpython-312.pyc
│  │     │  │  │  │  ├─ builder.cpython-312.pyc
│  │     │  │  │  │  ├─ containers.cpython-312.pyc
│  │     │  │  │  │  ├─ decoder.cpython-312.pyc
│  │     │  │  │  │  ├─ encoder.cpython-312.pyc
│  │     │  │  │  │  ├─ enum_type_wrapper.cpython-312.pyc
│  │     │  │  │  │  ├─ extension_dict.cpython-312.pyc
│  │     │  │  │  │  ├─ field_mask.cpython-312.pyc
│  │     │  │  │  │  ├─ message_listener.cpython-312.pyc
│  │     │  │  │  │  ├─ python_edition_defaults.cpython-312.pyc
│  │     │  │  │  │  ├─ python_message.cpython-312.pyc
│  │     │  │  │  │  ├─ testing_refleaks.cpython-312.pyc
│  │     │  │  │  │  ├─ type_checkers.cpython-312.pyc
│  │     │  │  │  │  ├─ well_known_types.cpython-312.pyc
│  │     │  │  │  │  └─ wire_format.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ api_implementation.py
│  │     │  │  │  ├─ builder.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ decoder.py
│  │     │  │  │  ├─ encoder.py
│  │     │  │  │  ├─ enum_type_wrapper.py
│  │     │  │  │  ├─ extension_dict.py
│  │     │  │  │  ├─ field_mask.py
│  │     │  │  │  ├─ message_listener.py
│  │     │  │  │  ├─ python_edition_defaults.py
│  │     │  │  │  ├─ python_message.py
│  │     │  │  │  ├─ testing_refleaks.py
│  │     │  │  │  ├─ type_checkers.py
│  │     │  │  │  ├─ well_known_types.py
│  │     │  │  │  └─ wire_format.py
│  │     │  │  ├─ pyext/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ cpp_message.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ cpp_message.py
│  │     │  │  ├─ testdata/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ util/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ any_pb2.py
│  │     │  │  ├─ any.py
│  │     │  │  ├─ api_pb2.py
│  │     │  │  ├─ descriptor_database.py
│  │     │  │  ├─ descriptor_pb2.py
│  │     │  │  ├─ descriptor_pool.py
│  │     │  │  ├─ descriptor.py
│  │     │  │  ├─ duration_pb2.py
│  │     │  │  ├─ duration.py
│  │     │  │  ├─ empty_pb2.py
│  │     │  │  ├─ field_mask_pb2.py
│  │     │  │  ├─ json_format.py
│  │     │  │  ├─ message_factory.py
│  │     │  │  ├─ message.py
│  │     │  │  ├─ proto_builder.py
│  │     │  │  ├─ proto_json.py
│  │     │  │  ├─ proto_text.py
│  │     │  │  ├─ proto.py
│  │     │  │  ├─ reflection.py
│  │     │  │  ├─ runtime_version.py
│  │     │  │  ├─ service_reflection.py
│  │     │  │  ├─ source_context_pb2.py
│  │     │  │  ├─ struct_pb2.py
│  │     │  │  ├─ symbol_database.py
│  │     │  │  ├─ text_encoding.py
│  │     │  │  ├─ text_format.py
│  │     │  │  ├─ timestamp_pb2.py
│  │     │  │  ├─ timestamp.py
│  │     │  │  ├─ type_pb2.py
│  │     │  │  ├─ unknown_fields.py
│  │     │  │  └─ wrappers_pb2.py
│  │     │  ├─ resumable_media/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _download.cpython-312.pyc
│  │     │  │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  │  ├─ _upload.cpython-312.pyc
│  │     │  │  │  └─ common.cpython-312.pyc
│  │     │  │  ├─ requests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _request_helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ download.cpython-312.pyc
│  │     │  │  │  │  └─ upload.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _request_helpers.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  └─ upload.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _download.py
│  │     │  │  ├─ _helpers.py
│  │     │  │  ├─ _upload.py
│  │     │  │  ├─ common.py
│  │     │  │  └─ py.typed
│  │     │  ├─ rpc/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ code_pb2.cpython-312.pyc
│  │     │  │  │  ├─ error_details_pb2.cpython-312.pyc
│  │     │  │  │  ├─ http_pb2.cpython-312.pyc
│  │     │  │  │  └─ status_pb2.cpython-312.pyc
│  │     │  │  ├─ context/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ attribute_context_pb2.cpython-312.pyc
│  │     │  │  │  │  └─ audit_context_pb2.cpython-312.pyc
│  │     │  │  │  ├─ attribute_context_pb2.py
│  │     │  │  │  ├─ attribute_context_pb2.pyi
│  │     │  │  │  ├─ attribute_context.proto
│  │     │  │  │  ├─ audit_context_pb2.py
│  │     │  │  │  ├─ audit_context_pb2.pyi
│  │     │  │  │  └─ audit_context.proto
│  │     │  │  ├─ code_pb2.py
│  │     │  │  ├─ code_pb2.pyi
│  │     │  │  ├─ code.proto
│  │     │  │  ├─ error_details_pb2.py
│  │     │  │  ├─ error_details_pb2.pyi
│  │     │  │  ├─ error_details.proto
│  │     │  │  ├─ http_pb2.py
│  │     │  │  ├─ http_pb2.pyi
│  │     │  │  ├─ http.proto
│  │     │  │  ├─ status_pb2.py
│  │     │  │  ├─ status_pb2.pyi
│  │     │  │  └─ status.proto
│  │     │  └─ type/
│  │     │     ├─ __pycache__/
│  │     │     │  ├─ calendar_period_pb2.cpython-312.pyc
│  │     │     │  ├─ color_pb2.cpython-312.pyc
│  │     │     │  ├─ date_pb2.cpython-312.pyc
│  │     │     │  ├─ datetime_pb2.cpython-312.pyc
│  │     │     │  ├─ dayofweek_pb2.cpython-312.pyc
│  │     │     │  ├─ decimal_pb2.cpython-312.pyc
│  │     │     │  ├─ expr_pb2.cpython-312.pyc
│  │     │     │  ├─ fraction_pb2.cpython-312.pyc
│  │     │     │  ├─ interval_pb2.cpython-312.pyc
│  │     │     │  ├─ latlng_pb2.cpython-312.pyc
│  │     │     │  ├─ localized_text_pb2.cpython-312.pyc
│  │     │     │  ├─ money_pb2.cpython-312.pyc
│  │     │     │  ├─ month_pb2.cpython-312.pyc
│  │     │     │  ├─ phone_number_pb2.cpython-312.pyc
│  │     │     │  ├─ postal_address_pb2.cpython-312.pyc
│  │     │     │  ├─ quaternion_pb2.cpython-312.pyc
│  │     │     │  └─ timeofday_pb2.cpython-312.pyc
│  │     │     ├─ calendar_period_pb2.py
│  │     │     ├─ calendar_period_pb2.pyi
│  │     │     ├─ calendar_period.proto
│  │     │     ├─ color_pb2.py
│  │     │     ├─ color_pb2.pyi
│  │     │     ├─ color.proto
│  │     │     ├─ date_pb2.py
│  │     │     ├─ date_pb2.pyi
│  │     │     ├─ date.proto
│  │     │     ├─ datetime_pb2.py
│  │     │     ├─ datetime_pb2.pyi
│  │     │     ├─ datetime.proto
│  │     │     ├─ dayofweek_pb2.py
│  │     │     ├─ dayofweek_pb2.pyi
│  │     │     ├─ dayofweek.proto
│  │     │     ├─ decimal_pb2.py
│  │     │     ├─ decimal_pb2.pyi
│  │     │     ├─ decimal.proto
│  │     │     ├─ expr_pb2.py
│  │     │     ├─ expr_pb2.pyi
│  │     │     ├─ expr.proto
│  │     │     ├─ fraction_pb2.py
│  │     │     ├─ fraction_pb2.pyi
│  │     │     ├─ fraction.proto
│  │     │     ├─ interval_pb2.py
│  │     │     ├─ interval_pb2.pyi
│  │     │     ├─ interval.proto
│  │     │     ├─ latlng_pb2.py
│  │     │     ├─ latlng_pb2.pyi
│  │     │     ├─ latlng.proto
│  │     │     ├─ localized_text_pb2.py
│  │     │     ├─ localized_text_pb2.pyi
│  │     │     ├─ localized_text.proto
│  │     │     ├─ money_pb2.py
│  │     │     ├─ money_pb2.pyi
│  │     │     ├─ money.proto
│  │     │     ├─ month_pb2.py
│  │     │     ├─ month_pb2.pyi
│  │     │     ├─ month.proto
│  │     │     ├─ phone_number_pb2.py
│  │     │     ├─ phone_number_pb2.pyi
│  │     │     ├─ phone_number.proto
│  │     │     ├─ postal_address_pb2.py
│  │     │     ├─ postal_address_pb2.pyi
│  │     │     ├─ postal_address.proto
│  │     │     ├─ quaternion_pb2.py
│  │     │     ├─ quaternion_pb2.pyi
│  │     │     ├─ quaternion.proto
│  │     │     ├─ timeofday_pb2.py
│  │     │     ├─ timeofday_pb2.pyi
│  │     │     └─ timeofday.proto
│  │     ├─ google_api_core-2.25.1.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google_api_python_client-2.176.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google_auth_httplib2-0.2.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google_auth-2.40.3.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google_cloud_core-2.4.3.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google_cloud_storage-3.2.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ google_crc32c/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __config__.cpython-312.pyc
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _checksum.cpython-312.pyc
│  │     │  │  ├─ cext.cpython-312.pyc
│  │     │  │  └─ python.cpython-312.pyc
│  │     │  ├─ extra-dll/
│  │     │  │  └─ crc32c.dll
│  │     │  ├─ __config__.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _checksum.py
│  │     │  ├─ _crc32c.cp312-win_amd64.pyd
│  │     │  ├─ cext.py
│  │     │  ├─ py.typed
│  │     │  └─ python.py
│  │     ├─ google_crc32c-1.7.1.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ google_resumable_media-2.7.2.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ googleapiclient/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _auth.cpython-312.pyc
│  │     │  │  ├─ _helpers.cpython-312.pyc
│  │     │  │  ├─ channel.cpython-312.pyc
│  │     │  │  ├─ discovery.cpython-312.pyc
│  │     │  │  ├─ errors.cpython-312.pyc
│  │     │  │  ├─ http.cpython-312.pyc
│  │     │  │  ├─ mimeparse.cpython-312.pyc
│  │     │  │  ├─ model.cpython-312.pyc
│  │     │  │  ├─ sample_tools.cpython-312.pyc
│  │     │  │  ├─ schema.cpython-312.pyc
│  │     │  │  └─ version.cpython-312.pyc
│  │     │  ├─ discovery_cache/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ appengine_memcache.cpython-312.pyc
│  │     │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  └─ file_cache.cpython-312.pyc
│  │     │  │  ├─ documents/
│  │     │  │  │  ├─ abusiveexperiencereport.v1.json
│  │     │  │  │  ├─ acceleratedmobilepageurl.v1.json
│  │     │  │  │  ├─ accessapproval.v1.json
│  │     │  │  │  ├─ accesscontextmanager.v1.json
│  │     │  │  │  ├─ accesscontextmanager.v1beta.json
│  │     │  │  │  ├─ acmedns.v1.json
│  │     │  │  │  ├─ addressvalidation.v1.json
│  │     │  │  │  ├─ adexchangebuyer.v1.2.json
│  │     │  │  │  ├─ adexchangebuyer.v1.3.json
│  │     │  │  │  ├─ adexchangebuyer.v1.4.json
│  │     │  │  │  ├─ adexchangebuyer2.v2beta1.json
│  │     │  │  │  ├─ adexperiencereport.v1.json
│  │     │  │  │  ├─ admin.datatransfer_v1.json
│  │     │  │  │  ├─ admin.datatransferv1.json
│  │     │  │  │  ├─ admin.directory_v1.json
│  │     │  │  │  ├─ admin.directoryv1.json
│  │     │  │  │  ├─ admin.reports_v1.json
│  │     │  │  │  ├─ admin.reportsv1.json
│  │     │  │  │  ├─ admob.v1.json
│  │     │  │  │  ├─ admob.v1beta.json
│  │     │  │  │  ├─ adsense.v2.json
│  │     │  │  │  ├─ adsensehost.v4.1.json
│  │     │  │  │  ├─ adsenseplatform.v1.json
│  │     │  │  │  ├─ adsenseplatform.v1alpha.json
│  │     │  │  │  ├─ advisorynotifications.v1.json
│  │     │  │  │  ├─ aiplatform.v1.json
│  │     │  │  │  ├─ aiplatform.v1beta1.json
│  │     │  │  │  ├─ airquality.v1.json
│  │     │  │  │  ├─ alertcenter.v1beta1.json
│  │     │  │  │  ├─ alloydb.v1.json
│  │     │  │  │  ├─ alloydb.v1alpha.json
│  │     │  │  │  ├─ alloydb.v1beta.json
│  │     │  │  │  ├─ analytics.v3.json
│  │     │  │  │  ├─ analyticsadmin.v1alpha.json
│  │     │  │  │  ├─ analyticsadmin.v1beta.json
│  │     │  │  │  ├─ analyticsdata.v1alpha.json
│  │     │  │  │  ├─ analyticsdata.v1beta.json
│  │     │  │  │  ├─ analyticshub.v1.json
│  │     │  │  │  ├─ analyticshub.v1beta1.json
│  │     │  │  │  ├─ analyticsreporting.v4.json
│  │     │  │  │  ├─ androiddeviceprovisioning.v1.json
│  │     │  │  │  ├─ androidenterprise.v1.json
│  │     │  │  │  ├─ androidmanagement.v1.json
│  │     │  │  │  ├─ androidpublisher.v3.json
│  │     │  │  │  ├─ apigateway.v1.json
│  │     │  │  │  ├─ apigateway.v1beta.json
│  │     │  │  │  ├─ apigee.v1.json
│  │     │  │  │  ├─ apigeeregistry.v1.json
│  │     │  │  │  ├─ apihub.v1.json
│  │     │  │  │  ├─ apikeys.v2.json
│  │     │  │  │  ├─ apim.v1alpha.json
│  │     │  │  │  ├─ appengine.v1.json
│  │     │  │  │  ├─ appengine.v1alpha.json
│  │     │  │  │  ├─ appengine.v1beta.json
│  │     │  │  │  ├─ appengine.v1beta4.json
│  │     │  │  │  ├─ appengine.v1beta5.json
│  │     │  │  │  ├─ apphub.v1.json
│  │     │  │  │  ├─ apphub.v1alpha.json
│  │     │  │  │  ├─ area120tables.v1alpha1.json
│  │     │  │  │  ├─ areainsights.v1.json
│  │     │  │  │  ├─ artifactregistry.v1.json
│  │     │  │  │  ├─ artifactregistry.v1beta1.json
│  │     │  │  │  ├─ artifactregistry.v1beta2.json
│  │     │  │  │  ├─ assuredworkloads.v1.json
│  │     │  │  │  ├─ assuredworkloads.v1beta1.json
│  │     │  │  │  ├─ authorizedbuyersmarketplace.v1.json
│  │     │  │  │  ├─ authorizedbuyersmarketplace.v1alpha.json
│  │     │  │  │  ├─ authorizedbuyersmarketplace.v1beta.json
│  │     │  │  │  ├─ backupdr.v1.json
│  │     │  │  │  ├─ baremetalsolution.v1.json
│  │     │  │  │  ├─ baremetalsolution.v1alpha1.json
│  │     │  │  │  ├─ baremetalsolution.v2.json
│  │     │  │  │  ├─ batch.v1.json
│  │     │  │  │  ├─ beyondcorp.v1.json
│  │     │  │  │  ├─ beyondcorp.v1alpha.json
│  │     │  │  │  ├─ biglake.v1.json
│  │     │  │  │  ├─ bigquery.v2.json
│  │     │  │  │  ├─ bigqueryconnection.v1.json
│  │     │  │  │  ├─ bigqueryconnection.v1beta1.json
│  │     │  │  │  ├─ bigquerydatapolicy.v1.json
│  │     │  │  │  ├─ bigquerydatatransfer.v1.json
│  │     │  │  │  ├─ bigqueryreservation.v1.json
│  │     │  │  │  ├─ bigqueryreservation.v1alpha2.json
│  │     │  │  │  ├─ bigqueryreservation.v1beta1.json
│  │     │  │  │  ├─ bigtableadmin.v1.json
│  │     │  │  │  ├─ bigtableadmin.v2.json
│  │     │  │  │  ├─ billingbudgets.v1.json
│  │     │  │  │  ├─ billingbudgets.v1beta1.json
│  │     │  │  │  ├─ binaryauthorization.v1.json
│  │     │  │  │  ├─ binaryauthorization.v1beta1.json
│  │     │  │  │  ├─ blockchainnodeengine.v1.json
│  │     │  │  │  ├─ blogger.v2.json
│  │     │  │  │  ├─ blogger.v3.json
│  │     │  │  │  ├─ books.v1.json
│  │     │  │  │  ├─ businessprofileperformance.v1.json
│  │     │  │  │  ├─ calendar.v3.json
│  │     │  │  │  ├─ certificatemanager.v1.json
│  │     │  │  │  ├─ chat.v1.json
│  │     │  │  │  ├─ checks.v1alpha.json
│  │     │  │  │  ├─ chromemanagement.v1.json
│  │     │  │  │  ├─ chromepolicy.v1.json
│  │     │  │  │  ├─ chromeuxreport.v1.json
│  │     │  │  │  ├─ civicinfo.v2.json
│  │     │  │  │  ├─ classroom.v1.json
│  │     │  │  │  ├─ cloudasset.v1.json
│  │     │  │  │  ├─ cloudasset.v1beta1.json
│  │     │  │  │  ├─ cloudasset.v1p1beta1.json
│  │     │  │  │  ├─ cloudasset.v1p4beta1.json
│  │     │  │  │  ├─ cloudasset.v1p5beta1.json
│  │     │  │  │  ├─ cloudasset.v1p7beta1.json
│  │     │  │  │  ├─ cloudbilling.v1.json
│  │     │  │  │  ├─ cloudbilling.v1beta.json
│  │     │  │  │  ├─ cloudbuild.v1.json
│  │     │  │  │  ├─ cloudbuild.v1alpha1.json
│  │     │  │  │  ├─ cloudbuild.v1alpha2.json
│  │     │  │  │  ├─ cloudbuild.v1beta1.json
│  │     │  │  │  ├─ cloudbuild.v2.json
│  │     │  │  │  ├─ cloudchannel.v1.json
│  │     │  │  │  ├─ cloudcommerceprocurement.v1.json
│  │     │  │  │  ├─ cloudcontrolspartner.v1.json
│  │     │  │  │  ├─ cloudcontrolspartner.v1beta.json
│  │     │  │  │  ├─ clouddebugger.v2.json
│  │     │  │  │  ├─ clouddeploy.v1.json
│  │     │  │  │  ├─ clouderrorreporting.v1beta1.json
│  │     │  │  │  ├─ cloudfunctions.v1.json
│  │     │  │  │  ├─ cloudfunctions.v2.json
│  │     │  │  │  ├─ cloudfunctions.v2alpha.json
│  │     │  │  │  ├─ cloudfunctions.v2beta.json
│  │     │  │  │  ├─ cloudidentity.v1.json
│  │     │  │  │  ├─ cloudidentity.v1beta1.json
│  │     │  │  │  ├─ cloudiot.v1.json
│  │     │  │  │  ├─ cloudkms.v1.json
│  │     │  │  │  ├─ cloudlocationfinder.v1alpha.json
│  │     │  │  │  ├─ cloudprofiler.v2.json
│  │     │  │  │  ├─ cloudresourcemanager.v1.json
│  │     │  │  │  ├─ cloudresourcemanager.v1beta1.json
│  │     │  │  │  ├─ cloudresourcemanager.v2.json
│  │     │  │  │  ├─ cloudresourcemanager.v2beta1.json
│  │     │  │  │  ├─ cloudresourcemanager.v3.json
│  │     │  │  │  ├─ cloudscheduler.v1.json
│  │     │  │  │  ├─ cloudscheduler.v1beta1.json
│  │     │  │  │  ├─ cloudsearch.v1.json
│  │     │  │  │  ├─ cloudshell.v1.json
│  │     │  │  │  ├─ cloudshell.v1alpha1.json
│  │     │  │  │  ├─ cloudsupport.v2.json
│  │     │  │  │  ├─ cloudsupport.v2beta.json
│  │     │  │  │  ├─ cloudtasks.v2.json
│  │     │  │  │  ├─ cloudtasks.v2beta2.json
│  │     │  │  │  ├─ cloudtasks.v2beta3.json
│  │     │  │  │  ├─ cloudtrace.v1.json
│  │     │  │  │  ├─ cloudtrace.v2.json
│  │     │  │  │  ├─ cloudtrace.v2beta1.json
│  │     │  │  │  ├─ composer.v1.json
│  │     │  │  │  ├─ composer.v1beta1.json
│  │     │  │  │  ├─ compute.alpha.json
│  │     │  │  │  ├─ compute.beta.json
│  │     │  │  │  ├─ compute.v1.json
│  │     │  │  │  ├─ config.v1.json
│  │     │  │  │  ├─ connectors.v1.json
│  │     │  │  │  ├─ connectors.v2.json
│  │     │  │  │  ├─ contactcenteraiplatform.v1alpha1.json
│  │     │  │  │  ├─ contactcenterinsights.v1.json
│  │     │  │  │  ├─ container.v1.json
│  │     │  │  │  ├─ container.v1beta1.json
│  │     │  │  │  ├─ containeranalysis.v1.json
│  │     │  │  │  ├─ containeranalysis.v1alpha1.json
│  │     │  │  │  ├─ containeranalysis.v1beta1.json
│  │     │  │  │  ├─ content.v2.1.json
│  │     │  │  │  ├─ content.v2.json
│  │     │  │  │  ├─ contentwarehouse.v1.json
│  │     │  │  │  ├─ css.v1.json
│  │     │  │  │  ├─ customsearch.v1.json
│  │     │  │  │  ├─ datacatalog.v1.json
│  │     │  │  │  ├─ datacatalog.v1beta1.json
│  │     │  │  │  ├─ dataflow.v1b3.json
│  │     │  │  │  ├─ dataform.v1beta1.json
│  │     │  │  │  ├─ datafusion.v1.json
│  │     │  │  │  ├─ datafusion.v1beta1.json
│  │     │  │  │  ├─ datalabeling.v1beta1.json
│  │     │  │  │  ├─ datalineage.v1.json
│  │     │  │  │  ├─ datamigration.v1.json
│  │     │  │  │  ├─ datamigration.v1beta1.json
│  │     │  │  │  ├─ datapipelines.v1.json
│  │     │  │  │  ├─ dataplex.v1.json
│  │     │  │  │  ├─ dataportability.v1.json
│  │     │  │  │  ├─ dataportability.v1beta.json
│  │     │  │  │  ├─ dataproc.v1.json
│  │     │  │  │  ├─ dataproc.v1beta2.json
│  │     │  │  │  ├─ datastore.v1.json
│  │     │  │  │  ├─ datastore.v1beta1.json
│  │     │  │  │  ├─ datastore.v1beta3.json
│  │     │  │  │  ├─ datastream.v1.json
│  │     │  │  │  ├─ datastream.v1alpha1.json
│  │     │  │  │  ├─ deploymentmanager.alpha.json
│  │     │  │  │  ├─ deploymentmanager.v2.json
│  │     │  │  │  ├─ deploymentmanager.v2beta.json
│  │     │  │  │  ├─ developerconnect.v1.json
│  │     │  │  │  ├─ dfareporting.v3.3.json
│  │     │  │  │  ├─ dfareporting.v3.4.json
│  │     │  │  │  ├─ dfareporting.v3.5.json
│  │     │  │  │  ├─ dfareporting.v4.json
│  │     │  │  │  ├─ dialogflow.v2.json
│  │     │  │  │  ├─ dialogflow.v2beta1.json
│  │     │  │  │  ├─ dialogflow.v3.json
│  │     │  │  │  ├─ dialogflow.v3beta1.json
│  │     │  │  │  ├─ digitalassetlinks.v1.json
│  │     │  │  │  ├─ discovery.v1.json
│  │     │  │  │  ├─ discoveryengine.v1.json
│  │     │  │  │  ├─ discoveryengine.v1alpha.json
│  │     │  │  │  ├─ discoveryengine.v1beta.json
│  │     │  │  │  ├─ displayvideo.v1.json
│  │     │  │  │  ├─ displayvideo.v2.json
│  │     │  │  │  ├─ displayvideo.v3.json
│  │     │  │  │  ├─ displayvideo.v4.json
│  │     │  │  │  ├─ dlp.v2.json
│  │     │  │  │  ├─ dns.v1.json
│  │     │  │  │  ├─ dns.v1beta2.json
│  │     │  │  │  ├─ dns.v2.json
│  │     │  │  │  ├─ docs.v1.json
│  │     │  │  │  ├─ documentai.v1.json
│  │     │  │  │  ├─ documentai.v1beta2.json
│  │     │  │  │  ├─ documentai.v1beta3.json
│  │     │  │  │  ├─ domains.v1.json
│  │     │  │  │  ├─ domains.v1alpha2.json
│  │     │  │  │  ├─ domains.v1beta1.json
│  │     │  │  │  ├─ domainsrdap.v1.json
│  │     │  │  │  ├─ doubleclickbidmanager.v1.1.json
│  │     │  │  │  ├─ doubleclickbidmanager.v1.json
│  │     │  │  │  ├─ doubleclickbidmanager.v2.json
│  │     │  │  │  ├─ doubleclicksearch.v2.json
│  │     │  │  │  ├─ drive.v2.json
│  │     │  │  │  ├─ drive.v3.json
│  │     │  │  │  ├─ driveactivity.v2.json
│  │     │  │  │  ├─ drivelabels.v2.json
│  │     │  │  │  ├─ drivelabels.v2beta.json
│  │     │  │  │  ├─ essentialcontacts.v1.json
│  │     │  │  │  ├─ eventarc.v1.json
│  │     │  │  │  ├─ eventarc.v1beta1.json
│  │     │  │  │  ├─ factchecktools.v1alpha1.json
│  │     │  │  │  ├─ fcm.v1.json
│  │     │  │  │  ├─ fcmdata.v1beta1.json
│  │     │  │  │  ├─ file.v1.json
│  │     │  │  │  ├─ file.v1beta1.json
│  │     │  │  │  ├─ firebase.v1beta1.json
│  │     │  │  │  ├─ firebaseappcheck.v1.json
│  │     │  │  │  ├─ firebaseappcheck.v1beta.json
│  │     │  │  │  ├─ firebaseappdistribution.v1.json
│  │     │  │  │  ├─ firebaseappdistribution.v1alpha.json
│  │     │  │  │  ├─ firebaseapphosting.v1.json
│  │     │  │  │  ├─ firebaseapphosting.v1beta.json
│  │     │  │  │  ├─ firebasedatabase.v1beta.json
│  │     │  │  │  ├─ firebasedataconnect.v1.json
│  │     │  │  │  ├─ firebasedataconnect.v1beta.json
│  │     │  │  │  ├─ firebasedynamiclinks.v1.json
│  │     │  │  │  ├─ firebasehosting.v1.json
│  │     │  │  │  ├─ firebasehosting.v1beta1.json
│  │     │  │  │  ├─ firebaseml.v1.json
│  │     │  │  │  ├─ firebaseml.v1beta2.json
│  │     │  │  │  ├─ firebaseml.v2beta.json
│  │     │  │  │  ├─ firebaserules.v1.json
│  │     │  │  │  ├─ firebasestorage.v1beta.json
│  │     │  │  │  ├─ firestore.v1.json
│  │     │  │  │  ├─ firestore.v1beta1.json
│  │     │  │  │  ├─ firestore.v1beta2.json
│  │     │  │  │  ├─ fitness.v1.json
│  │     │  │  │  ├─ forms.v1.json
│  │     │  │  │  ├─ games.v1.json
│  │     │  │  │  ├─ gamesConfiguration.v1configuration.json
│  │     │  │  │  ├─ gameservices.v1.json
│  │     │  │  │  ├─ gameservices.v1beta.json
│  │     │  │  │  ├─ gamesManagement.v1management.json
│  │     │  │  │  ├─ genomics.v1.json
│  │     │  │  │  ├─ genomics.v1alpha2.json
│  │     │  │  │  ├─ genomics.v2alpha1.json
│  │     │  │  │  ├─ gkebackup.v1.json
│  │     │  │  │  ├─ gkehub.v1.json
│  │     │  │  │  ├─ gkehub.v1alpha.json
│  │     │  │  │  ├─ gkehub.v1alpha2.json
│  │     │  │  │  ├─ gkehub.v1beta.json
│  │     │  │  │  ├─ gkehub.v1beta1.json
│  │     │  │  │  ├─ gkehub.v2.json
│  │     │  │  │  ├─ gkehub.v2alpha.json
│  │     │  │  │  ├─ gkehub.v2beta.json
│  │     │  │  │  ├─ gkeonprem.v1.json
│  │     │  │  │  ├─ gmail.v1.json
│  │     │  │  │  ├─ gmailpostmastertools.v1.json
│  │     │  │  │  ├─ gmailpostmastertools.v1beta1.json
│  │     │  │  │  ├─ groupsmigration.v1.json
│  │     │  │  │  ├─ groupssettings.v1.json
│  │     │  │  │  ├─ healthcare.v1.json
│  │     │  │  │  ├─ healthcare.v1beta1.json
│  │     │  │  │  ├─ homegraph.v1.json
│  │     │  │  │  ├─ iam.v1.json
│  │     │  │  │  ├─ iam.v2.json
│  │     │  │  │  ├─ iam.v2beta.json
│  │     │  │  │  ├─ iamcredentials.v1.json
│  │     │  │  │  ├─ iap.v1.json
│  │     │  │  │  ├─ iap.v1beta1.json
│  │     │  │  │  ├─ ideahub.v1alpha.json
│  │     │  │  │  ├─ ideahub.v1beta.json
│  │     │  │  │  ├─ identitytoolkit.v1.json
│  │     │  │  │  ├─ identitytoolkit.v2.json
│  │     │  │  │  ├─ identitytoolkit.v3.json
│  │     │  │  │  ├─ ids.v1.json
│  │     │  │  │  ├─ index.json
│  │     │  │  │  ├─ indexing.v3.json
│  │     │  │  │  ├─ integrations.v1.json
│  │     │  │  │  ├─ integrations.v1alpha.json
│  │     │  │  │  ├─ jobs.v2.json
│  │     │  │  │  ├─ jobs.v3.json
│  │     │  │  │  ├─ jobs.v3p1beta1.json
│  │     │  │  │  ├─ jobs.v4.json
│  │     │  │  │  ├─ keep.v1.json
│  │     │  │  │  ├─ kgsearch.v1.json
│  │     │  │  │  ├─ kmsinventory.v1.json
│  │     │  │  │  ├─ language.v1.json
│  │     │  │  │  ├─ language.v1beta1.json
│  │     │  │  │  ├─ language.v1beta2.json
│  │     │  │  │  ├─ language.v2.json
│  │     │  │  │  ├─ libraryagent.v1.json
│  │     │  │  │  ├─ licensing.v1.json
│  │     │  │  │  ├─ lifesciences.v2beta.json
│  │     │  │  │  ├─ localservices.v1.json
│  │     │  │  │  ├─ logging.v2.json
│  │     │  │  │  ├─ looker.v1.json
│  │     │  │  │  ├─ managedidentities.v1.json
│  │     │  │  │  ├─ managedidentities.v1alpha1.json
│  │     │  │  │  ├─ managedidentities.v1beta1.json
│  │     │  │  │  ├─ managedkafka.v1.json
│  │     │  │  │  ├─ manufacturers.v1.json
│  │     │  │  │  ├─ marketingplatformadmin.v1alpha.json
│  │     │  │  │  ├─ meet.v2.json
│  │     │  │  │  ├─ memcache.v1.json
│  │     │  │  │  ├─ memcache.v1beta2.json
│  │     │  │  │  ├─ merchantapi.accounts_v1beta.json
│  │     │  │  │  ├─ merchantapi.conversions_v1beta.json
│  │     │  │  │  ├─ merchantapi.datasources_v1beta.json
│  │     │  │  │  ├─ merchantapi.inventories_v1beta.json
│  │     │  │  │  ├─ merchantapi.issueresolution_v1beta.json
│  │     │  │  │  ├─ merchantapi.lfp_v1beta.json
│  │     │  │  │  ├─ merchantapi.notifications_v1beta.json
│  │     │  │  │  ├─ merchantapi.ordertracking_v1beta.json
│  │     │  │  │  ├─ merchantapi.products_v1beta.json
│  │     │  │  │  ├─ merchantapi.promotions_v1beta.json
│  │     │  │  │  ├─ merchantapi.quota_v1beta.json
│  │     │  │  │  ├─ merchantapi.reports_v1beta.json
│  │     │  │  │  ├─ merchantapi.reviews_v1beta.json
│  │     │  │  │  ├─ metastore.v1.json
│  │     │  │  │  ├─ metastore.v1alpha.json
│  │     │  │  │  ├─ metastore.v1beta.json
│  │     │  │  │  ├─ metastore.v2.json
│  │     │  │  │  ├─ metastore.v2alpha.json
│  │     │  │  │  ├─ metastore.v2beta.json
│  │     │  │  │  ├─ migrationcenter.v1.json
│  │     │  │  │  ├─ migrationcenter.v1alpha1.json
│  │     │  │  │  ├─ ml.v1.json
│  │     │  │  │  ├─ monitoring.v1.json
│  │     │  │  │  ├─ monitoring.v3.json
│  │     │  │  │  ├─ mybusinessaccountmanagement.v1.json
│  │     │  │  │  ├─ mybusinessbusinesscalls.v1.json
│  │     │  │  │  ├─ mybusinessbusinessinformation.v1.json
│  │     │  │  │  ├─ mybusinesslodging.v1.json
│  │     │  │  │  ├─ mybusinessnotifications.v1.json
│  │     │  │  │  ├─ mybusinessplaceactions.v1.json
│  │     │  │  │  ├─ mybusinessqanda.v1.json
│  │     │  │  │  ├─ mybusinessverifications.v1.json
│  │     │  │  │  ├─ netapp.v1.json
│  │     │  │  │  ├─ netapp.v1beta1.json
│  │     │  │  │  ├─ networkconnectivity.v1.json
│  │     │  │  │  ├─ networkconnectivity.v1alpha1.json
│  │     │  │  │  ├─ networkmanagement.v1.json
│  │     │  │  │  ├─ networkmanagement.v1beta1.json
│  │     │  │  │  ├─ networksecurity.v1.json
│  │     │  │  │  ├─ networksecurity.v1beta1.json
│  │     │  │  │  ├─ networkservices.v1.json
│  │     │  │  │  ├─ networkservices.v1beta1.json
│  │     │  │  │  ├─ notebooks.v1.json
│  │     │  │  │  ├─ notebooks.v2.json
│  │     │  │  │  ├─ oauth2.v2.json
│  │     │  │  │  ├─ observability.v1.json
│  │     │  │  │  ├─ ondemandscanning.v1.json
│  │     │  │  │  ├─ ondemandscanning.v1beta1.json
│  │     │  │  │  ├─ oracledatabase.v1.json
│  │     │  │  │  ├─ orgpolicy.v2.json
│  │     │  │  │  ├─ osconfig.v1.json
│  │     │  │  │  ├─ osconfig.v1alpha.json
│  │     │  │  │  ├─ osconfig.v1beta.json
│  │     │  │  │  ├─ osconfig.v2.json
│  │     │  │  │  ├─ osconfig.v2beta.json
│  │     │  │  │  ├─ oslogin.v1.json
│  │     │  │  │  ├─ oslogin.v1alpha.json
│  │     │  │  │  ├─ oslogin.v1beta.json
│  │     │  │  │  ├─ pagespeedonline.v5.json
│  │     │  │  │  ├─ parallelstore.v1.json
│  │     │  │  │  ├─ parallelstore.v1beta.json
│  │     │  │  │  ├─ paymentsresellersubscription.v1.json
│  │     │  │  │  ├─ people.v1.json
│  │     │  │  │  ├─ places.v1.json
│  │     │  │  │  ├─ playablelocations.v3.json
│  │     │  │  │  ├─ playcustomapp.v1.json
│  │     │  │  │  ├─ playdeveloperreporting.v1alpha1.json
│  │     │  │  │  ├─ playdeveloperreporting.v1beta1.json
│  │     │  │  │  ├─ playgrouping.v1alpha1.json
│  │     │  │  │  ├─ playintegrity.v1.json
│  │     │  │  │  ├─ policyanalyzer.v1.json
│  │     │  │  │  ├─ policyanalyzer.v1beta1.json
│  │     │  │  │  ├─ policysimulator.v1.json
│  │     │  │  │  ├─ policysimulator.v1alpha.json
│  │     │  │  │  ├─ policysimulator.v1beta.json
│  │     │  │  │  ├─ policysimulator.v1beta1.json
│  │     │  │  │  ├─ policytroubleshooter.v1.json
│  │     │  │  │  ├─ policytroubleshooter.v1beta.json
│  │     │  │  │  ├─ pollen.v1.json
│  │     │  │  │  ├─ poly.v1.json
│  │     │  │  │  ├─ privateca.v1.json
│  │     │  │  │  ├─ privateca.v1beta1.json
│  │     │  │  │  ├─ prod_tt_sasportal.v1alpha1.json
│  │     │  │  │  ├─ publicca.v1.json
│  │     │  │  │  ├─ publicca.v1alpha1.json
│  │     │  │  │  ├─ publicca.v1beta1.json
│  │     │  │  │  ├─ pubsub.v1.json
│  │     │  │  │  ├─ pubsub.v1beta1a.json
│  │     │  │  │  ├─ pubsub.v1beta2.json
│  │     │  │  │  ├─ pubsublite.v1.json
│  │     │  │  │  ├─ rapidmigrationassessment.v1.json
│  │     │  │  │  ├─ readerrevenuesubscriptionlinking.v1.json
│  │     │  │  │  ├─ realtimebidding.v1.json
│  │     │  │  │  ├─ realtimebidding.v1alpha.json
│  │     │  │  │  ├─ recaptchaenterprise.v1.json
│  │     │  │  │  ├─ recommendationengine.v1beta1.json
│  │     │  │  │  ├─ recommender.v1.json
│  │     │  │  │  ├─ recommender.v1beta1.json
│  │     │  │  │  ├─ redis.v1.json
│  │     │  │  │  ├─ redis.v1beta1.json
│  │     │  │  │  ├─ remotebuildexecution.v1.json
│  │     │  │  │  ├─ remotebuildexecution.v1alpha.json
│  │     │  │  │  ├─ remotebuildexecution.v2.json
│  │     │  │  │  ├─ reseller.v1.json
│  │     │  │  │  ├─ resourcesettings.v1.json
│  │     │  │  │  ├─ retail.v2.json
│  │     │  │  │  ├─ retail.v2alpha.json
│  │     │  │  │  ├─ retail.v2beta.json
│  │     │  │  │  ├─ run.v1.json
│  │     │  │  │  ├─ run.v1alpha1.json
│  │     │  │  │  ├─ run.v1beta1.json
│  │     │  │  │  ├─ run.v2.json
│  │     │  │  │  ├─ runtimeconfig.v1.json
│  │     │  │  │  ├─ runtimeconfig.v1beta1.json
│  │     │  │  │  ├─ saasservicemgmt.v1beta1.json
│  │     │  │  │  ├─ safebrowsing.v4.json
│  │     │  │  │  ├─ safebrowsing.v5.json
│  │     │  │  │  ├─ sasportal.v1alpha1.json
│  │     │  │  │  ├─ script.v1.json
│  │     │  │  │  ├─ searchads360.v0.json
│  │     │  │  │  ├─ searchconsole.v1.json
│  │     │  │  │  ├─ secretmanager.v1.json
│  │     │  │  │  ├─ secretmanager.v1beta1.json
│  │     │  │  │  ├─ secretmanager.v1beta2.json
│  │     │  │  │  ├─ securitycenter.v1.json
│  │     │  │  │  ├─ securitycenter.v1beta1.json
│  │     │  │  │  ├─ securitycenter.v1beta2.json
│  │     │  │  │  ├─ securityposture.v1.json
│  │     │  │  │  ├─ serviceconsumermanagement.v1.json
│  │     │  │  │  ├─ serviceconsumermanagement.v1beta1.json
│  │     │  │  │  ├─ servicecontrol.v1.json
│  │     │  │  │  ├─ servicecontrol.v2.json
│  │     │  │  │  ├─ servicedirectory.v1.json
│  │     │  │  │  ├─ servicedirectory.v1beta1.json
│  │     │  │  │  ├─ servicemanagement.v1.json
│  │     │  │  │  ├─ servicenetworking.v1.json
│  │     │  │  │  ├─ servicenetworking.v1beta.json
│  │     │  │  │  ├─ serviceusage.v1.json
│  │     │  │  │  ├─ serviceusage.v1beta1.json
│  │     │  │  │  ├─ sheets.v4.json
│  │     │  │  │  ├─ siteVerification.v1.json
│  │     │  │  │  ├─ slides.v1.json
│  │     │  │  │  ├─ smartdevicemanagement.v1.json
│  │     │  │  │  ├─ solar.v1.json
│  │     │  │  │  ├─ sourcerepo.v1.json
│  │     │  │  │  ├─ spanner.v1.json
│  │     │  │  │  ├─ speech.v1.json
│  │     │  │  │  ├─ speech.v1p1beta1.json
│  │     │  │  │  ├─ speech.v2beta1.json
│  │     │  │  │  ├─ sqladmin.v1.json
│  │     │  │  │  ├─ sqladmin.v1beta4.json
│  │     │  │  │  ├─ storage.v1.json
│  │     │  │  │  ├─ storagebatchoperations.v1.json
│  │     │  │  │  ├─ storagetransfer.v1.json
│  │     │  │  │  ├─ streetviewpublish.v1.json
│  │     │  │  │  ├─ sts.v1.json
│  │     │  │  │  ├─ sts.v1beta.json
│  │     │  │  │  ├─ tagmanager.v1.json
│  │     │  │  │  ├─ tagmanager.v2.json
│  │     │  │  │  ├─ tasks.v1.json
│  │     │  │  │  ├─ testing.v1.json
│  │     │  │  │  ├─ texttospeech.v1.json
│  │     │  │  │  ├─ texttospeech.v1beta1.json
│  │     │  │  │  ├─ toolresults.v1beta3.json
│  │     │  │  │  ├─ tpu.v1.json
│  │     │  │  │  ├─ tpu.v1alpha1.json
│  │     │  │  │  ├─ tpu.v2.json
│  │     │  │  │  ├─ tpu.v2alpha1.json
│  │     │  │  │  ├─ trafficdirector.v2.json
│  │     │  │  │  ├─ trafficdirector.v3.json
│  │     │  │  │  ├─ transcoder.v1.json
│  │     │  │  │  ├─ transcoder.v1beta1.json
│  │     │  │  │  ├─ translate.v2.json
│  │     │  │  │  ├─ translate.v3.json
│  │     │  │  │  ├─ translate.v3beta1.json
│  │     │  │  │  ├─ travelimpactmodel.v1.json
│  │     │  │  │  ├─ vault.v1.json
│  │     │  │  │  ├─ vectortile.v1.json
│  │     │  │  │  ├─ verifiedaccess.v1.json
│  │     │  │  │  ├─ verifiedaccess.v2.json
│  │     │  │  │  ├─ versionhistory.v1.json
│  │     │  │  │  ├─ videointelligence.v1.json
│  │     │  │  │  ├─ videointelligence.v1beta2.json
│  │     │  │  │  ├─ videointelligence.v1p1beta1.json
│  │     │  │  │  ├─ videointelligence.v1p2beta1.json
│  │     │  │  │  ├─ videointelligence.v1p3beta1.json
│  │     │  │  │  ├─ vision.v1.json
│  │     │  │  │  ├─ vision.v1p1beta1.json
│  │     │  │  │  ├─ vision.v1p2beta1.json
│  │     │  │  │  ├─ vmmigration.v1.json
│  │     │  │  │  ├─ vmmigration.v1alpha1.json
│  │     │  │  │  ├─ vmwareengine.v1.json
│  │     │  │  │  ├─ vpcaccess.v1.json
│  │     │  │  │  ├─ vpcaccess.v1beta1.json
│  │     │  │  │  ├─ walletobjects.v1.json
│  │     │  │  │  ├─ webfonts.v1.json
│  │     │  │  │  ├─ webmasters.v3.json
│  │     │  │  │  ├─ webrisk.v1.json
│  │     │  │  │  ├─ websecurityscanner.v1.json
│  │     │  │  │  ├─ websecurityscanner.v1alpha.json
│  │     │  │  │  ├─ websecurityscanner.v1beta.json
│  │     │  │  │  ├─ workflowexecutions.v1.json
│  │     │  │  │  ├─ workflowexecutions.v1beta.json
│  │     │  │  │  ├─ workflows.v1.json
│  │     │  │  │  ├─ workflows.v1beta.json
│  │     │  │  │  ├─ workloadmanager.v1.json
│  │     │  │  │  ├─ workspaceevents.v1.json
│  │     │  │  │  ├─ workstations.v1.json
│  │     │  │  │  ├─ workstations.v1beta.json
│  │     │  │  │  ├─ youtube.v3.json
│  │     │  │  │  ├─ youtubeAnalytics.v1.json
│  │     │  │  │  ├─ youtubeAnalytics.v2.json
│  │     │  │  │  └─ youtubereporting.v1.json
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ appengine_memcache.py
│  │     │  │  ├─ base.py
│  │     │  │  └─ file_cache.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _auth.py
│  │     │  ├─ _helpers.py
│  │     │  ├─ channel.py
│  │     │  ├─ discovery.py
│  │     │  ├─ errors.py
│  │     │  ├─ http.py
│  │     │  ├─ mimeparse.py
│  │     │  ├─ model.py
│  │     │  ├─ sample_tools.py
│  │     │  ├─ schema.py
│  │     │  └─ version.py
│  │     ├─ googleapis_common_protos-1.70.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ httplib2/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ auth.cpython-312.pyc
│  │     │  │  ├─ certs.cpython-312.pyc
│  │     │  │  ├─ error.cpython-312.pyc
│  │     │  │  ├─ iri2uri.cpython-312.pyc
│  │     │  │  └─ socks.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ auth.py
│  │     │  ├─ cacerts.txt
│  │     │  ├─ certs.py
│  │     │  ├─ error.py
│  │     │  ├─ iri2uri.py
│  │     │  └─ socks.py
│  │     ├─ httplib2-0.22.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ idna/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ codec.cpython-312.pyc
│  │     │  │  ├─ compat.cpython-312.pyc
│  │     │  │  ├─ core.cpython-312.pyc
│  │     │  │  ├─ idnadata.cpython-312.pyc
│  │     │  │  ├─ intranges.cpython-312.pyc
│  │     │  │  ├─ package_data.cpython-312.pyc
│  │     │  │  └─ uts46data.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ codec.py
│  │     │  ├─ compat.py
│  │     │  ├─ core.py
│  │     │  ├─ idnadata.py
│  │     │  ├─ intranges.py
│  │     │  ├─ package_data.py
│  │     │  ├─ py.typed
│  │     │  └─ uts46data.py
│  │     ├─ idna-3.10.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.md
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ ipyevents/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  └─ events.cpython-312.pyc
│  │     │  ├─ labextension/
│  │     │  │  ├─ static/
│  │     │  │  │  ├─ 480.c423a222101c2195b83e.js
│  │     │  │  │  ├─ 568.1aede9119f40fe766541.js
│  │     │  │  │  ├─ 794.6b60fb863a746d89d5fd.js
│  │     │  │  │  ├─ remoteEntry.4d5ef87d14f03accc582.js
│  │     │  │  │  ├─ style.js
│  │     │  │  │  └─ third-party-licenses.json
│  │     │  │  └─ package.json
│  │     │  ├─ nbextension/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ static/
│  │     │  │  │  ├─ extension.js
│  │     │  │  │  ├─ index.js
│  │     │  │  │  └─ index.js.map
│  │     │  │  └─ __init__.py
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ test_events.cpython-312.pyc
│  │     │  │  └─ test_events.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  └─ events.py
│  │     ├─ ipyevents-2.0.2.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ ipyfilechooser/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ errors.cpython-312.pyc
│  │     │  │  ├─ filechooser.cpython-312.pyc
│  │     │  │  └─ utils.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ errors.py
│  │     │  ├─ filechooser.py
│  │     │  └─ utils.py
│  │     ├─ ipyfilechooser-0.6.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ipykernel/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ _eventloop_macos.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ compiler.cpython-312.pyc
│  │     │  │  ├─ connect.cpython-312.pyc
│  │     │  │  ├─ control.cpython-312.pyc
│  │     │  │  ├─ datapub.cpython-312.pyc
│  │     │  │  ├─ debugger.cpython-312.pyc
│  │     │  │  ├─ displayhook.cpython-312.pyc
│  │     │  │  ├─ embed.cpython-312.pyc
│  │     │  │  ├─ eventloops.cpython-312.pyc
│  │     │  │  ├─ heartbeat.cpython-312.pyc
│  │     │  │  ├─ iostream.cpython-312.pyc
│  │     │  │  ├─ ipkernel.cpython-312.pyc
│  │     │  │  ├─ jsonutil.cpython-312.pyc
│  │     │  │  ├─ kernelapp.cpython-312.pyc
│  │     │  │  ├─ kernelbase.cpython-312.pyc
│  │     │  │  ├─ kernelspec.cpython-312.pyc
│  │     │  │  ├─ log.cpython-312.pyc
│  │     │  │  ├─ parentpoller.cpython-312.pyc
│  │     │  │  ├─ pickleutil.cpython-312.pyc
│  │     │  │  ├─ serialize.cpython-312.pyc
│  │     │  │  ├─ trio_runner.cpython-312.pyc
│  │     │  │  └─ zmqshell.cpython-312.pyc
│  │     │  ├─ comm/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ comm.cpython-312.pyc
│  │     │  │  │  └─ manager.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ comm.py
│  │     │  │  └─ manager.py
│  │     │  ├─ gui/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ gtk3embed.cpython-312.pyc
│  │     │  │  │  └─ gtkembed.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ gtk3embed.py
│  │     │  │  └─ gtkembed.py
│  │     │  ├─ inprocess/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ blocking.cpython-312.pyc
│  │     │  │  │  ├─ channels.cpython-312.pyc
│  │     │  │  │  ├─ client.cpython-312.pyc
│  │     │  │  │  ├─ constants.cpython-312.pyc
│  │     │  │  │  ├─ ipkernel.cpython-312.pyc
│  │     │  │  │  ├─ manager.cpython-312.pyc
│  │     │  │  │  └─ socket.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ blocking.py
│  │     │  │  ├─ channels.py
│  │     │  │  ├─ client.py
│  │     │  │  ├─ constants.py
│  │     │  │  ├─ ipkernel.py
│  │     │  │  ├─ manager.py
│  │     │  │  └─ socket.py
│  │     │  ├─ pylab/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ backend_inline.cpython-312.pyc
│  │     │  │  │  └─ config.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ backend_inline.py
│  │     │  │  └─ config.py
│  │     │  ├─ resources/
│  │     │  │  ├─ logo-32x32.png
│  │     │  │  ├─ logo-64x64.png
│  │     │  │  └─ logo-svg.svg
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ _eventloop_macos.py
│  │     │  ├─ _version.py
│  │     │  ├─ compiler.py
│  │     │  ├─ connect.py
│  │     │  ├─ control.py
│  │     │  ├─ datapub.py
│  │     │  ├─ debugger.py
│  │     │  ├─ displayhook.py
│  │     │  ├─ embed.py
│  │     │  ├─ eventloops.py
│  │     │  ├─ heartbeat.py
│  │     │  ├─ iostream.py
│  │     │  ├─ ipkernel.py
│  │     │  ├─ jsonutil.py
│  │     │  ├─ kernelapp.py
│  │     │  ├─ kernelbase.py
│  │     │  ├─ kernelspec.py
│  │     │  ├─ log.py
│  │     │  ├─ parentpoller.py
│  │     │  ├─ pickleutil.py
│  │     │  ├─ py.typed
│  │     │  ├─ serialize.py
│  │     │  ├─ trio_runner.py
│  │     │  └─ zmqshell.py
│  │     ├─ ipykernel-6.29.5.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ ipyleaflet/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ basemaps.cpython-312.pyc
│  │     │  │  ├─ leaflet.cpython-312.pyc
│  │     │  │  ├─ projections.cpython-312.pyc
│  │     │  │  ├─ velocity.cpython-312.pyc
│  │     │  │  └─ xarray_ds.cpython-312.pyc
│  │     │  ├─ external/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ here.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ here.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  ├─ basemaps.py
│  │     │  ├─ leaflet.py
│  │     │  ├─ projections.py
│  │     │  ├─ velocity.py
│  │     │  └─ xarray_ds.py
│  │     ├─ ipyleaflet-0.20.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ IPython/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ display.cpython-312.pyc
│  │     │  │  └─ paths.cpython-312.pyc
│  │     │  ├─ core/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ alias.cpython-312.pyc
│  │     │  │  │  ├─ application.cpython-312.pyc
│  │     │  │  │  ├─ async_helpers.cpython-312.pyc
│  │     │  │  │  ├─ autocall.cpython-312.pyc
│  │     │  │  │  ├─ builtin_trap.cpython-312.pyc
│  │     │  │  │  ├─ compilerop.cpython-312.pyc
│  │     │  │  │  ├─ completer.cpython-312.pyc
│  │     │  │  │  ├─ completerlib.cpython-312.pyc
│  │     │  │  │  ├─ crashhandler.cpython-312.pyc
│  │     │  │  │  ├─ debugger_backport.cpython-312.pyc
│  │     │  │  │  ├─ debugger.cpython-312.pyc
│  │     │  │  │  ├─ display_functions.cpython-312.pyc
│  │     │  │  │  ├─ display_trap.cpython-312.pyc
│  │     │  │  │  ├─ display.cpython-312.pyc
│  │     │  │  │  ├─ displayhook.cpython-312.pyc
│  │     │  │  │  ├─ displaypub.cpython-312.pyc
│  │     │  │  │  ├─ doctb.cpython-312.pyc
│  │     │  │  │  ├─ error.cpython-312.pyc
│  │     │  │  │  ├─ events.cpython-312.pyc
│  │     │  │  │  ├─ extensions.cpython-312.pyc
│  │     │  │  │  ├─ formatters.cpython-312.pyc
│  │     │  │  │  ├─ getipython.cpython-312.pyc
│  │     │  │  │  ├─ guarded_eval.cpython-312.pyc
│  │     │  │  │  ├─ history.cpython-312.pyc
│  │     │  │  │  ├─ historyapp.cpython-312.pyc
│  │     │  │  │  ├─ hooks.cpython-312.pyc
│  │     │  │  │  ├─ inputtransformer2.cpython-312.pyc
│  │     │  │  │  ├─ interactiveshell.cpython-312.pyc
│  │     │  │  │  ├─ latex_symbols.cpython-312.pyc
│  │     │  │  │  ├─ logger.cpython-312.pyc
│  │     │  │  │  ├─ macro.cpython-312.pyc
│  │     │  │  │  ├─ magic_arguments.cpython-312.pyc
│  │     │  │  │  ├─ magic.cpython-312.pyc
│  │     │  │  │  ├─ oinspect.cpython-312.pyc
│  │     │  │  │  ├─ page.cpython-312.pyc
│  │     │  │  │  ├─ payload.cpython-312.pyc
│  │     │  │  │  ├─ payloadpage.cpython-312.pyc
│  │     │  │  │  ├─ prefilter.cpython-312.pyc
│  │     │  │  │  ├─ profileapp.cpython-312.pyc
│  │     │  │  │  ├─ profiledir.cpython-312.pyc
│  │     │  │  │  ├─ pylabtools.cpython-312.pyc
│  │     │  │  │  ├─ release.cpython-312.pyc
│  │     │  │  │  ├─ shellapp.cpython-312.pyc
│  │     │  │  │  ├─ splitinput.cpython-312.pyc
│  │     │  │  │  ├─ tbtools.cpython-312.pyc
│  │     │  │  │  ├─ tips.cpython-312.pyc
│  │     │  │  │  ├─ ultratb.cpython-312.pyc
│  │     │  │  │  └─ usage.cpython-312.pyc
│  │     │  │  ├─ magics/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ ast_mod.cpython-312.pyc
│  │     │  │  │  │  ├─ auto.cpython-312.pyc
│  │     │  │  │  │  ├─ basic.cpython-312.pyc
│  │     │  │  │  │  ├─ code.cpython-312.pyc
│  │     │  │  │  │  ├─ config.cpython-312.pyc
│  │     │  │  │  │  ├─ display.cpython-312.pyc
│  │     │  │  │  │  ├─ execution.cpython-312.pyc
│  │     │  │  │  │  ├─ extension.cpython-312.pyc
│  │     │  │  │  │  ├─ history.cpython-312.pyc
│  │     │  │  │  │  ├─ logging.cpython-312.pyc
│  │     │  │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  │  ├─ osm.cpython-312.pyc
│  │     │  │  │  │  ├─ packaging.cpython-312.pyc
│  │     │  │  │  │  ├─ pylab.cpython-312.pyc
│  │     │  │  │  │  └─ script.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ ast_mod.py
│  │     │  │  │  ├─ auto.py
│  │     │  │  │  ├─ basic.py
│  │     │  │  │  ├─ code.py
│  │     │  │  │  ├─ config.py
│  │     │  │  │  ├─ display.py
│  │     │  │  │  ├─ execution.py
│  │     │  │  │  ├─ extension.py
│  │     │  │  │  ├─ history.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ namespace.py
│  │     │  │  │  ├─ osm.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ pylab.py
│  │     │  │  │  └─ script.py
│  │     │  │  ├─ profile/
│  │     │  │  │  └─ README_STARTUP
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ alias.py
│  │     │  │  ├─ application.py
│  │     │  │  ├─ async_helpers.py
│  │     │  │  ├─ autocall.py
│  │     │  │  ├─ builtin_trap.py
│  │     │  │  ├─ compilerop.py
│  │     │  │  ├─ completer.py
│  │     │  │  ├─ completerlib.py
│  │     │  │  ├─ crashhandler.py
│  │     │  │  ├─ debugger_backport.py
│  │     │  │  ├─ debugger.py
│  │     │  │  ├─ display_functions.py
│  │     │  │  ├─ display_trap.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ displayhook.py
│  │     │  │  ├─ displaypub.py
│  │     │  │  ├─ doctb.py
│  │     │  │  ├─ error.py
│  │     │  │  ├─ events.py
│  │     │  │  ├─ extensions.py
│  │     │  │  ├─ formatters.py
│  │     │  │  ├─ getipython.py
│  │     │  │  ├─ guarded_eval.py
│  │     │  │  ├─ history.py
│  │     │  │  ├─ historyapp.py
│  │     │  │  ├─ hooks.py
│  │     │  │  ├─ inputtransformer2.py
│  │     │  │  ├─ interactiveshell.py
│  │     │  │  ├─ latex_symbols.py
│  │     │  │  ├─ logger.py
│  │     │  │  ├─ macro.py
│  │     │  │  ├─ magic_arguments.py
│  │     │  │  ├─ magic.py
│  │     │  │  ├─ oinspect.py
│  │     │  │  ├─ page.py
│  │     │  │  ├─ payload.py
│  │     │  │  ├─ payloadpage.py
│  │     │  │  ├─ prefilter.py
│  │     │  │  ├─ profileapp.py
│  │     │  │  ├─ profiledir.py
│  │     │  │  ├─ pylabtools.py
│  │     │  │  ├─ release.py
│  │     │  │  ├─ shellapp.py
│  │     │  │  ├─ splitinput.py
│  │     │  │  ├─ tbtools.py
│  │     │  │  ├─ tips.py
│  │     │  │  ├─ ultratb.py
│  │     │  │  └─ usage.py
│  │     │  ├─ extensions/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ autoreload.cpython-312.pyc
│  │     │  │  │  └─ storemagic.cpython-312.pyc
│  │     │  │  ├─ deduperreload/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ deduperreload_patching.cpython-312.pyc
│  │     │  │  │  │  └─ deduperreload.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ deduperreload_patching.py
│  │     │  │  │  └─ deduperreload.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ autoreload.py
│  │     │  │  └─ storemagic.py
│  │     │  ├─ external/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ pickleshare.cpython-312.pyc
│  │     │  │  │  ├─ qt_for_kernel.cpython-312.pyc
│  │     │  │  │  └─ qt_loaders.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ pickleshare.py
│  │     │  │  ├─ qt_for_kernel.py
│  │     │  │  └─ qt_loaders.py
│  │     │  ├─ lib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ backgroundjobs.cpython-312.pyc
│  │     │  │  │  ├─ clipboard.cpython-312.pyc
│  │     │  │  │  ├─ deepreload.cpython-312.pyc
│  │     │  │  │  ├─ demo.cpython-312.pyc
│  │     │  │  │  ├─ display.cpython-312.pyc
│  │     │  │  │  ├─ editorhooks.cpython-312.pyc
│  │     │  │  │  ├─ guisupport.cpython-312.pyc
│  │     │  │  │  ├─ latextools.cpython-312.pyc
│  │     │  │  │  ├─ lexers.cpython-312.pyc
│  │     │  │  │  └─ pretty.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ backgroundjobs.py
│  │     │  │  ├─ clipboard.py
│  │     │  │  ├─ deepreload.py
│  │     │  │  ├─ demo.py
│  │     │  │  ├─ display.py
│  │     │  │  ├─ editorhooks.py
│  │     │  │  ├─ guisupport.py
│  │     │  │  ├─ latextools.py
│  │     │  │  ├─ lexers.py
│  │     │  │  └─ pretty.py
│  │     │  ├─ sphinxext/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ custom_doctests.cpython-312.pyc
│  │     │  │  │  ├─ ipython_console_highlighting.cpython-312.pyc
│  │     │  │  │  └─ ipython_directive.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ custom_doctests.py
│  │     │  │  ├─ ipython_console_highlighting.py
│  │     │  │  └─ ipython_directive.py
│  │     │  ├─ terminal/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ debugger.cpython-312.pyc
│  │     │  │  │  ├─ embed.cpython-312.pyc
│  │     │  │  │  ├─ interactiveshell.cpython-312.pyc
│  │     │  │  │  ├─ ipapp.cpython-312.pyc
│  │     │  │  │  ├─ magics.cpython-312.pyc
│  │     │  │  │  ├─ prompts.cpython-312.pyc
│  │     │  │  │  └─ ptutils.cpython-312.pyc
│  │     │  │  ├─ pt_inputhooks/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ asyncio.cpython-312.pyc
│  │     │  │  │  │  ├─ glut.cpython-312.pyc
│  │     │  │  │  │  ├─ gtk.cpython-312.pyc
│  │     │  │  │  │  ├─ gtk3.cpython-312.pyc
│  │     │  │  │  │  ├─ gtk4.cpython-312.pyc
│  │     │  │  │  │  ├─ osx.cpython-312.pyc
│  │     │  │  │  │  ├─ pyglet.cpython-312.pyc
│  │     │  │  │  │  ├─ qt.cpython-312.pyc
│  │     │  │  │  │  ├─ tk.cpython-312.pyc
│  │     │  │  │  │  └─ wx.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ asyncio.py
│  │     │  │  │  ├─ glut.py
│  │     │  │  │  ├─ gtk.py
│  │     │  │  │  ├─ gtk3.py
│  │     │  │  │  ├─ gtk4.py
│  │     │  │  │  ├─ osx.py
│  │     │  │  │  ├─ pyglet.py
│  │     │  │  │  ├─ qt.py
│  │     │  │  │  ├─ tk.py
│  │     │  │  │  └─ wx.py
│  │     │  │  ├─ shortcuts/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ auto_match.cpython-312.pyc
│  │     │  │  │  │  ├─ auto_suggest.cpython-312.pyc
│  │     │  │  │  │  └─ filters.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ auto_match.py
│  │     │  │  │  ├─ auto_suggest.py
│  │     │  │  │  └─ filters.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ debugger.py
│  │     │  │  ├─ embed.py
│  │     │  │  ├─ interactiveshell.py
│  │     │  │  ├─ ipapp.py
│  │     │  │  ├─ magics.py
│  │     │  │  ├─ prompts.py
│  │     │  │  └─ ptutils.py
│  │     │  ├─ testing/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ decorators.cpython-312.pyc
│  │     │  │  │  ├─ globalipapp.cpython-312.pyc
│  │     │  │  │  ├─ ipunittest.cpython-312.pyc
│  │     │  │  │  ├─ skipdoctest.cpython-312.pyc
│  │     │  │  │  └─ tools.cpython-312.pyc
│  │     │  │  ├─ plugin/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ dtexample.cpython-312.pyc
│  │     │  │  │  │  ├─ ipdoctest.cpython-312.pyc
│  │     │  │  │  │  ├─ pytest_ipdoctest.cpython-312.pyc
│  │     │  │  │  │  ├─ setup.cpython-312.pyc
│  │     │  │  │  │  ├─ simple.cpython-312.pyc
│  │     │  │  │  │  ├─ simplevars.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ipdoctest.cpython-312.pyc
│  │     │  │  │  │  └─ test_refs.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ dtexample.py
│  │     │  │  │  ├─ ipdoctest.py
│  │     │  │  │  ├─ pytest_ipdoctest.py
│  │     │  │  │  ├─ setup.py
│  │     │  │  │  ├─ simple.py
│  │     │  │  │  ├─ simplevars.py
│  │     │  │  │  ├─ test_combo.txt
│  │     │  │  │  ├─ test_example.txt
│  │     │  │  │  ├─ test_exampleip.txt
│  │     │  │  │  ├─ test_ipdoctest.py
│  │     │  │  │  └─ test_refs.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ globalipapp.py
│  │     │  │  ├─ ipunittest.py
│  │     │  │  ├─ skipdoctest.py
│  │     │  │  └─ tools.py
│  │     │  ├─ utils/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _process_cli.cpython-312.pyc
│  │     │  │  │  ├─ _process_common.cpython-312.pyc
│  │     │  │  │  ├─ _process_emscripten.cpython-312.pyc
│  │     │  │  │  ├─ _process_posix.cpython-312.pyc
│  │     │  │  │  ├─ _process_win32_controller.cpython-312.pyc
│  │     │  │  │  ├─ _process_win32.cpython-312.pyc
│  │     │  │  │  ├─ _sysinfo.cpython-312.pyc
│  │     │  │  │  ├─ capture.cpython-312.pyc
│  │     │  │  │  ├─ coloransi.cpython-312.pyc
│  │     │  │  │  ├─ contexts.cpython-312.pyc
│  │     │  │  │  ├─ data.cpython-312.pyc
│  │     │  │  │  ├─ decorators.cpython-312.pyc
│  │     │  │  │  ├─ dir2.cpython-312.pyc
│  │     │  │  │  ├─ docs.cpython-312.pyc
│  │     │  │  │  ├─ encoding.cpython-312.pyc
│  │     │  │  │  ├─ eventful.cpython-312.pyc
│  │     │  │  │  ├─ frame.cpython-312.pyc
│  │     │  │  │  ├─ generics.cpython-312.pyc
│  │     │  │  │  ├─ importstring.cpython-312.pyc
│  │     │  │  │  ├─ io.cpython-312.pyc
│  │     │  │  │  ├─ ipstruct.cpython-312.pyc
│  │     │  │  │  ├─ jsonutil.cpython-312.pyc
│  │     │  │  │  ├─ log.cpython-312.pyc
│  │     │  │  │  ├─ module_paths.cpython-312.pyc
│  │     │  │  │  ├─ openpy.cpython-312.pyc
│  │     │  │  │  ├─ path.cpython-312.pyc
│  │     │  │  │  ├─ process.cpython-312.pyc
│  │     │  │  │  ├─ py3compat.cpython-312.pyc
│  │     │  │  │  ├─ PyColorize.cpython-312.pyc
│  │     │  │  │  ├─ sentinel.cpython-312.pyc
│  │     │  │  │  ├─ strdispatch.cpython-312.pyc
│  │     │  │  │  ├─ sysinfo.cpython-312.pyc
│  │     │  │  │  ├─ syspathcontext.cpython-312.pyc
│  │     │  │  │  ├─ tempdir.cpython-312.pyc
│  │     │  │  │  ├─ terminal.cpython-312.pyc
│  │     │  │  │  ├─ text.cpython-312.pyc
│  │     │  │  │  ├─ timing.cpython-312.pyc
│  │     │  │  │  ├─ tokenutil.cpython-312.pyc
│  │     │  │  │  └─ wildcard.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _process_cli.py
│  │     │  │  ├─ _process_common.py
│  │     │  │  ├─ _process_emscripten.py
│  │     │  │  ├─ _process_posix.py
│  │     │  │  ├─ _process_win32_controller.py
│  │     │  │  ├─ _process_win32.py
│  │     │  │  ├─ _sysinfo.py
│  │     │  │  ├─ capture.py
│  │     │  │  ├─ coloransi.py
│  │     │  │  ├─ contexts.py
│  │     │  │  ├─ data.py
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ dir2.py
│  │     │  │  ├─ docs.py
│  │     │  │  ├─ encoding.py
│  │     │  │  ├─ eventful.py
│  │     │  │  ├─ frame.py
│  │     │  │  ├─ generics.py
│  │     │  │  ├─ importstring.py
│  │     │  │  ├─ io.py
│  │     │  │  ├─ ipstruct.py
│  │     │  │  ├─ jsonutil.py
│  │     │  │  ├─ log.py
│  │     │  │  ├─ module_paths.py
│  │     │  │  ├─ openpy.py
│  │     │  │  ├─ path.py
│  │     │  │  ├─ process.py
│  │     │  │  ├─ py3compat.py
│  │     │  │  ├─ PyColorize.py
│  │     │  │  ├─ sentinel.py
│  │     │  │  ├─ strdispatch.py
│  │     │  │  ├─ sysinfo.py
│  │     │  │  ├─ syspathcontext.py
│  │     │  │  ├─ tempdir.py
│  │     │  │  ├─ terminal.py
│  │     │  │  ├─ text.py
│  │     │  │  ├─ timing.py
│  │     │  │  ├─ tokenutil.py
│  │     │  │  └─ wildcard.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ display.py
│  │     │  ├─ paths.py
│  │     │  └─ py.typed
│  │     ├─ ipython_pygments_lexers-1.1.1.dist-info/
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ ipython-9.4.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  ├─ COPYING.rst
│  │     │  │  └─ LICENSE
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ipytree/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  └─ tree.cpython-312.pyc
│  │     │  ├─ labextension/
│  │     │  │  ├─ static/
│  │     │  │  │  ├─ 261.4efb75b6352af894acb4.js
│  │     │  │  │  ├─ 287.fd063a1253f3266560f7.js
│  │     │  │  │  ├─ 287.fd063a1253f3266560f7.js.LICENSE.txt
│  │     │  │  │  ├─ 486.4c1ca47efc3790912711.js
│  │     │  │  │  ├─ 486.4c1ca47efc3790912711.js.LICENSE.txt
│  │     │  │  │  ├─ 568.c44c0ae4f70f7df0fe86.js
│  │     │  │  │  ├─ 755.71bcc770291b01d6ebaa.js
│  │     │  │  │  ├─ 755.71bcc770291b01d6ebaa.js.LICENSE.txt
│  │     │  │  │  ├─ remoteEntry.a322e5c11f9830cf62f6.js
│  │     │  │  │  ├─ style.js
│  │     │  │  │  └─ third-party-licenses.json
│  │     │  │  └─ package.json
│  │     │  ├─ nbextension/
│  │     │  │  ├─ extension.js
│  │     │  │  ├─ index.js
│  │     │  │  ├─ index.js.LICENSE.txt
│  │     │  │  └─ index.js.map
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  └─ tree.py
│  │     ├─ ipytree-0.2.2.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ ipywidgets/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ comm.cpython-312.pyc
│  │     │  │  └─ embed.cpython-312.pyc
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ test_embed.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ test_embed.py
│  │     │  ├─ widgets/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ docutils.cpython-312.pyc
│  │     │  │  │  ├─ domwidget.cpython-312.pyc
│  │     │  │  │  ├─ interaction.cpython-312.pyc
│  │     │  │  │  ├─ trait_types.cpython-312.pyc
│  │     │  │  │  ├─ utils.cpython-312.pyc
│  │     │  │  │  ├─ valuewidget.cpython-312.pyc
│  │     │  │  │  ├─ widget_bool.cpython-312.pyc
│  │     │  │  │  ├─ widget_box.cpython-312.pyc
│  │     │  │  │  ├─ widget_button.cpython-312.pyc
│  │     │  │  │  ├─ widget_color.cpython-312.pyc
│  │     │  │  │  ├─ widget_controller.cpython-312.pyc
│  │     │  │  │  ├─ widget_core.cpython-312.pyc
│  │     │  │  │  ├─ widget_date.cpython-312.pyc
│  │     │  │  │  ├─ widget_datetime.cpython-312.pyc
│  │     │  │  │  ├─ widget_description.cpython-312.pyc
│  │     │  │  │  ├─ widget_float.cpython-312.pyc
│  │     │  │  │  ├─ widget_int.cpython-312.pyc
│  │     │  │  │  ├─ widget_layout.cpython-312.pyc
│  │     │  │  │  ├─ widget_link.cpython-312.pyc
│  │     │  │  │  ├─ widget_media.cpython-312.pyc
│  │     │  │  │  ├─ widget_output.cpython-312.pyc
│  │     │  │  │  ├─ widget_selection.cpython-312.pyc
│  │     │  │  │  ├─ widget_selectioncontainer.cpython-312.pyc
│  │     │  │  │  ├─ widget_string.cpython-312.pyc
│  │     │  │  │  ├─ widget_style.cpython-312.pyc
│  │     │  │  │  ├─ widget_tagsinput.cpython-312.pyc
│  │     │  │  │  ├─ widget_templates.cpython-312.pyc
│  │     │  │  │  ├─ widget_time.cpython-312.pyc
│  │     │  │  │  ├─ widget_upload.cpython-312.pyc
│  │     │  │  │  └─ widget.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetime_serializers.cpython-312.pyc
│  │     │  │  │  │  ├─ test_docutils.cpython-312.pyc
│  │     │  │  │  │  ├─ test_interaction.cpython-312.pyc
│  │     │  │  │  │  ├─ test_link.cpython-312.pyc
│  │     │  │  │  │  ├─ test_selectioncontainer.cpython-312.pyc
│  │     │  │  │  │  ├─ test_send_state.cpython-312.pyc
│  │     │  │  │  │  ├─ test_set_state.cpython-312.pyc
│  │     │  │  │  │  ├─ test_traits.cpython-312.pyc
│  │     │  │  │  │  ├─ test_utils.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_box.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_button.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_float.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_image.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_naive_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_output.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_selection.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_string.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_templates.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_time.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget_upload.cpython-312.pyc
│  │     │  │  │  │  ├─ test_widget.cpython-312.pyc
│  │     │  │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  │  ├─ data/
│  │     │  │  │  │  └─ jupyter-logo-transparent.png
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_datetime_serializers.py
│  │     │  │  │  ├─ test_docutils.py
│  │     │  │  │  ├─ test_interaction.py
│  │     │  │  │  ├─ test_link.py
│  │     │  │  │  ├─ test_selectioncontainer.py
│  │     │  │  │  ├─ test_send_state.py
│  │     │  │  │  ├─ test_set_state.py
│  │     │  │  │  ├─ test_traits.py
│  │     │  │  │  ├─ test_utils.py
│  │     │  │  │  ├─ test_widget_box.py
│  │     │  │  │  ├─ test_widget_button.py
│  │     │  │  │  ├─ test_widget_datetime.py
│  │     │  │  │  ├─ test_widget_float.py
│  │     │  │  │  ├─ test_widget_image.py
│  │     │  │  │  ├─ test_widget_naive_datetime.py
│  │     │  │  │  ├─ test_widget_output.py
│  │     │  │  │  ├─ test_widget_selection.py
│  │     │  │  │  ├─ test_widget_string.py
│  │     │  │  │  ├─ test_widget_templates.py
│  │     │  │  │  ├─ test_widget_time.py
│  │     │  │  │  ├─ test_widget_upload.py
│  │     │  │  │  ├─ test_widget.py
│  │     │  │  │  └─ utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ docutils.py
│  │     │  │  ├─ domwidget.py
│  │     │  │  ├─ interaction.py
│  │     │  │  ├─ trait_types.py
│  │     │  │  ├─ utils.py
│  │     │  │  ├─ valuewidget.py
│  │     │  │  ├─ widget_bool.py
│  │     │  │  ├─ widget_box.py
│  │     │  │  ├─ widget_button.py
│  │     │  │  ├─ widget_color.py
│  │     │  │  ├─ widget_controller.py
│  │     │  │  ├─ widget_core.py
│  │     │  │  ├─ widget_date.py
│  │     │  │  ├─ widget_datetime.py
│  │     │  │  ├─ widget_description.py
│  │     │  │  ├─ widget_float.py
│  │     │  │  ├─ widget_int.py
│  │     │  │  ├─ widget_layout.py
│  │     │  │  ├─ widget_link.py
│  │     │  │  ├─ widget_media.py
│  │     │  │  ├─ widget_output.py
│  │     │  │  ├─ widget_selection.py
│  │     │  │  ├─ widget_selectioncontainer.py
│  │     │  │  ├─ widget_string.py
│  │     │  │  ├─ widget_style.py
│  │     │  │  ├─ widget_tagsinput.py
│  │     │  │  ├─ widget_templates.py
│  │     │  │  ├─ widget_time.py
│  │     │  │  ├─ widget_upload.py
│  │     │  │  └─ widget.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  ├─ comm.py
│  │     │  ├─ embed.py
│  │     │  ├─ state.schema.json
│  │     │  └─ view.schema.json
│  │     ├─ ipywidgets-8.1.7.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ isapi/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ install.cpython-312.pyc
│  │     │  │  ├─ isapicon.cpython-312.pyc
│  │     │  │  ├─ simple.cpython-312.pyc
│  │     │  │  └─ threaded_extension.cpython-312.pyc
│  │     │  ├─ doc/
│  │     │  │  └─ isapi.html
│  │     │  ├─ samples/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ advanced.cpython-312.pyc
│  │     │  │  │  ├─ redirector_asynch.cpython-312.pyc
│  │     │  │  │  ├─ redirector_with_filter.cpython-312.pyc
│  │     │  │  │  ├─ redirector.cpython-312.pyc
│  │     │  │  │  └─ test.cpython-312.pyc
│  │     │  │  ├─ advanced.py
│  │     │  │  ├─ README.txt
│  │     │  │  ├─ redirector_asynch.py
│  │     │  │  ├─ redirector_with_filter.py
│  │     │  │  ├─ redirector.py
│  │     │  │  └─ test.py
│  │     │  ├─ test/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ extension_simple.cpython-312.pyc
│  │     │  │  ├─ extension_simple.py
│  │     │  │  └─ README.txt
│  │     │  ├─ __init__.py
│  │     │  ├─ install.py
│  │     │  ├─ isapicon.py
│  │     │  ├─ PyISAPI_loader.dll
│  │     │  ├─ README.txt
│  │     │  ├─ simple.py
│  │     │  └─ threaded_extension.py
│  │     ├─ jedi/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ _compatibility.cpython-312.pyc
│  │     │  │  ├─ cache.cpython-312.pyc
│  │     │  │  ├─ common.cpython-312.pyc
│  │     │  │  ├─ debug.cpython-312.pyc
│  │     │  │  ├─ file_io.cpython-312.pyc
│  │     │  │  ├─ parser_utils.cpython-312.pyc
│  │     │  │  ├─ settings.cpython-312.pyc
│  │     │  │  └─ utils.cpython-312.pyc
│  │     │  ├─ api/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ classes.cpython-312.pyc
│  │     │  │  │  ├─ completion_cache.cpython-312.pyc
│  │     │  │  │  ├─ completion.cpython-312.pyc
│  │     │  │  │  ├─ environment.cpython-312.pyc
│  │     │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  ├─ file_name.cpython-312.pyc
│  │     │  │  │  ├─ helpers.cpython-312.pyc
│  │     │  │  │  ├─ interpreter.cpython-312.pyc
│  │     │  │  │  ├─ keywords.cpython-312.pyc
│  │     │  │  │  ├─ project.cpython-312.pyc
│  │     │  │  │  ├─ replstartup.cpython-312.pyc
│  │     │  │  │  └─ strings.cpython-312.pyc
│  │     │  │  ├─ refactoring/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ extract.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ extract.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ classes.py
│  │     │  │  ├─ completion_cache.py
│  │     │  │  ├─ completion.py
│  │     │  │  ├─ environment.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ file_name.py
│  │     │  │  ├─ helpers.py
│  │     │  │  ├─ interpreter.py
│  │     │  │  ├─ keywords.py
│  │     │  │  ├─ project.py
│  │     │  │  ├─ replstartup.py
│  │     │  │  └─ strings.py
│  │     │  ├─ inference/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ analysis.cpython-312.pyc
│  │     │  │  │  ├─ arguments.cpython-312.pyc
│  │     │  │  │  ├─ base_value.cpython-312.pyc
│  │     │  │  │  ├─ cache.cpython-312.pyc
│  │     │  │  │  ├─ context.cpython-312.pyc
│  │     │  │  │  ├─ docstring_utils.cpython-312.pyc
│  │     │  │  │  ├─ docstrings.cpython-312.pyc
│  │     │  │  │  ├─ dynamic_params.cpython-312.pyc
│  │     │  │  │  ├─ filters.cpython-312.pyc
│  │     │  │  │  ├─ finder.cpython-312.pyc
│  │     │  │  │  ├─ flow_analysis.cpython-312.pyc
│  │     │  │  │  ├─ helpers.cpython-312.pyc
│  │     │  │  │  ├─ imports.cpython-312.pyc
│  │     │  │  │  ├─ lazy_value.cpython-312.pyc
│  │     │  │  │  ├─ names.cpython-312.pyc
│  │     │  │  │  ├─ param.cpython-312.pyc
│  │     │  │  │  ├─ parser_cache.cpython-312.pyc
│  │     │  │  │  ├─ recursion.cpython-312.pyc
│  │     │  │  │  ├─ references.cpython-312.pyc
│  │     │  │  │  ├─ signature.cpython-312.pyc
│  │     │  │  │  ├─ star_args.cpython-312.pyc
│  │     │  │  │  ├─ syntax_tree.cpython-312.pyc
│  │     │  │  │  ├─ sys_path.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ compiled/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ access.cpython-312.pyc
│  │     │  │  │  │  ├─ getattr_static.cpython-312.pyc
│  │     │  │  │  │  ├─ mixed.cpython-312.pyc
│  │     │  │  │  │  └─ value.cpython-312.pyc
│  │     │  │  │  ├─ subprocess/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  │  └─ functions.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ __main__.py
│  │     │  │  │  │  └─ functions.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ access.py
│  │     │  │  │  ├─ getattr_static.py
│  │     │  │  │  ├─ mixed.py
│  │     │  │  │  └─ value.py
│  │     │  │  ├─ gradual/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ annotation.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ conversion.cpython-312.pyc
│  │     │  │  │  │  ├─ generics.cpython-312.pyc
│  │     │  │  │  │  ├─ stub_value.cpython-312.pyc
│  │     │  │  │  │  ├─ type_var.cpython-312.pyc
│  │     │  │  │  │  ├─ typeshed.cpython-312.pyc
│  │     │  │  │  │  ├─ typing.cpython-312.pyc
│  │     │  │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ annotation.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ conversion.py
│  │     │  │  │  ├─ generics.py
│  │     │  │  │  ├─ stub_value.py
│  │     │  │  │  ├─ type_var.py
│  │     │  │  │  ├─ typeshed.py
│  │     │  │  │  ├─ typing.py
│  │     │  │  │  └─ utils.py
│  │     │  │  ├─ value/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ decorator.cpython-312.pyc
│  │     │  │  │  │  ├─ dynamic_arrays.cpython-312.pyc
│  │     │  │  │  │  ├─ function.cpython-312.pyc
│  │     │  │  │  │  ├─ instance.cpython-312.pyc
│  │     │  │  │  │  ├─ iterable.cpython-312.pyc
│  │     │  │  │  │  ├─ klass.cpython-312.pyc
│  │     │  │  │  │  ├─ module.cpython-312.pyc
│  │     │  │  │  │  └─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ decorator.py
│  │     │  │  │  ├─ dynamic_arrays.py
│  │     │  │  │  ├─ function.py
│  │     │  │  │  ├─ instance.py
│  │     │  │  │  ├─ iterable.py
│  │     │  │  │  ├─ klass.py
│  │     │  │  │  ├─ module.py
│  │     │  │  │  └─ namespace.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ analysis.py
│  │     │  │  ├─ arguments.py
│  │     │  │  ├─ base_value.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ context.py
│  │     │  │  ├─ docstring_utils.py
│  │     │  │  ├─ docstrings.py
│  │     │  │  ├─ dynamic_params.py
│  │     │  │  ├─ filters.py
│  │     │  │  ├─ finder.py
│  │     │  │  ├─ flow_analysis.py
│  │     │  │  ├─ helpers.py
│  │     │  │  ├─ imports.py
│  │     │  │  ├─ lazy_value.py
│  │     │  │  ├─ names.py
│  │     │  │  ├─ param.py
│  │     │  │  ├─ parser_cache.py
│  │     │  │  ├─ recursion.py
│  │     │  │  ├─ references.py
│  │     │  │  ├─ signature.py
│  │     │  │  ├─ star_args.py
│  │     │  │  ├─ syntax_tree.py
│  │     │  │  ├─ sys_path.py
│  │     │  │  └─ utils.py
│  │     │  ├─ plugins/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ django.cpython-312.pyc
│  │     │  │  │  ├─ flask.cpython-312.pyc
│  │     │  │  │  ├─ pytest.cpython-312.pyc
│  │     │  │  │  ├─ registry.cpython-312.pyc
│  │     │  │  │  └─ stdlib.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ django.py
│  │     │  │  ├─ flask.py
│  │     │  │  ├─ pytest.py
│  │     │  │  ├─ registry.py
│  │     │  │  └─ stdlib.py
│  │     │  ├─ third_party/
│  │     │  │  ├─ django-stubs/
│  │     │  │  │  ├─ django-stubs/
│  │     │  │  │  │  ├─ apps/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ config.pyi
│  │     │  │  │  │  │  └─ registry.pyi
│  │     │  │  │  │  ├─ conf/
│  │     │  │  │  │  │  ├─ locale/
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ urls/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ i18n.pyi
│  │     │  │  │  │  │  │  └─ static.pyi
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  └─ global_settings.pyi
│  │     │  │  │  │  ├─ contrib/
│  │     │  │  │  │  │  ├─ admin/
│  │     │  │  │  │  │  │  ├─ templatetags/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ admin_list.pyi
│  │     │  │  │  │  │  │  │  ├─ admin_modify.pyi
│  │     │  │  │  │  │  │  │  ├─ admin_static.pyi
│  │     │  │  │  │  │  │  │  ├─ admin_urls.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  └─ log.pyi
│  │     │  │  │  │  │  │  ├─ views/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ autocomplete.pyi
│  │     │  │  │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  │  │  └─ main.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ actions.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  │  ├─ filters.pyi
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ helpers.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ options.pyi
│  │     │  │  │  │  │  │  ├─ sites.pyi
│  │     │  │  │  │  │  │  ├─ tests.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ widgets.pyi
│  │     │  │  │  │  │  ├─ admindocs/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  ├─ auth/
│  │     │  │  │  │  │  │  ├─ handlers/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ modwsgi.pyi
│  │     │  │  │  │  │  │  ├─ management/
│  │     │  │  │  │  │  │  │  ├─ commands/
│  │     │  │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  │  ├─ changepassword.pyi
│  │     │  │  │  │  │  │  │  │  └─ createsuperuser.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ admin.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ backends.pyi
│  │     │  │  │  │  │  │  ├─ base_user.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ context_processors.pyi
│  │     │  │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ hashers.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ password_validation.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  ├─ tokens.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  ├─ validators.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  ├─ contenttypes/
│  │     │  │  │  │  │  │  ├─ management/
│  │     │  │  │  │  │  │  │  ├─ commands/
│  │     │  │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  │  └─ remove_stale_contenttypes.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ admin.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ fields.pyi
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  ├─ flatpages/
│  │     │  │  │  │  │  │  ├─ templatetags/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ flatpages.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ sitemaps.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  ├─ gis/
│  │     │  │  │  │  │  │  ├─ db/
│  │     │  │  │  │  │  │  │  ├─ models/
│  │     │  │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  │  └─ fields.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ humanize/
│  │     │  │  │  │  │  │  ├─ templatetags/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ humanize.pyi
│  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  ├─ messages/
│  │     │  │  │  │  │  │  ├─ storage/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ cookie.pyi
│  │     │  │  │  │  │  │  │  ├─ fallback.pyi
│  │     │  │  │  │  │  │  │  └─ session.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ api.pyi
│  │     │  │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  │  ├─ context_processors.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  ├─ postgres/
│  │     │  │  │  │  │  │  ├─ aggregates/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ general.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  └─ statistics.pyi
│  │     │  │  │  │  │  │  ├─ fields/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ array.pyi
│  │     │  │  │  │  │  │  │  ├─ citext.pyi
│  │     │  │  │  │  │  │  │  ├─ hstore.pyi
│  │     │  │  │  │  │  │  │  ├─ jsonb.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  └─ ranges.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ constraints.pyi
│  │     │  │  │  │  │  │  ├─ functions.pyi
│  │     │  │  │  │  │  │  ├─ indexes.pyi
│  │     │  │  │  │  │  │  ├─ lookups.pyi
│  │     │  │  │  │  │  │  ├─ operations.pyi
│  │     │  │  │  │  │  │  ├─ search.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  └─ validators.pyi
│  │     │  │  │  │  │  ├─ redirects/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  └─ models.pyi
│  │     │  │  │  │  │  ├─ sessions/
│  │     │  │  │  │  │  │  ├─ backends/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  │  │  ├─ cached_db.pyi
│  │     │  │  │  │  │  │  │  ├─ db.pyi
│  │     │  │  │  │  │  │  │  ├─ file.pyi
│  │     │  │  │  │  │  │  │  └─ signed_cookies.pyi
│  │     │  │  │  │  │  │  ├─ management/
│  │     │  │  │  │  │  │  │  ├─ commands/
│  │     │  │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  │  └─ clearsessions.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base_session.pyi
│  │     │  │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  └─ serializers.pyi
│  │     │  │  │  │  │  ├─ sitemaps/
│  │     │  │  │  │  │  │  ├─ management/
│  │     │  │  │  │  │  │  │  ├─ commands/
│  │     │  │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  │  └─ ping_google.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  ├─ sites/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ management.pyi
│  │     │  │  │  │  │  │  ├─ managers.pyi
│  │     │  │  │  │  │  │  ├─ middleware.pyi
│  │     │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  ├─ requests.pyi
│  │     │  │  │  │  │  │  └─ shortcuts.pyi
│  │     │  │  │  │  │  ├─ staticfiles/
│  │     │  │  │  │  │  │  ├─ management/
│  │     │  │  │  │  │  │  │  ├─ commands/
│  │     │  │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  │  ├─ collectstatic.pyi
│  │     │  │  │  │  │  │  │  │  ├─ findstatic.pyi
│  │     │  │  │  │  │  │  │  │  └─ runserver.pyi
│  │     │  │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ templatetags/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ staticfiles.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ apps.pyi
│  │     │  │  │  │  │  │  ├─ checks.pyi
│  │     │  │  │  │  │  │  ├─ finders.pyi
│  │     │  │  │  │  │  │  ├─ handlers.pyi
│  │     │  │  │  │  │  │  ├─ storage.pyi
│  │     │  │  │  │  │  │  ├─ testing.pyi
│  │     │  │  │  │  │  │  ├─ urls.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  ├─ syndication/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  └─ views.pyi
│  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │  │  │  ├─ core/
│  │     │  │  │  │  │  ├─ cache/
│  │     │  │  │  │  │  │  ├─ backends/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ db.pyi
│  │     │  │  │  │  │  │  │  ├─ dummy.pyi
│  │     │  │  │  │  │  │  │  ├─ filebased.pyi
│  │     │  │  │  │  │  │  │  ├─ locmem.pyi
│  │     │  │  │  │  │  │  │  └─ memcached.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  ├─ checks/
│  │     │  │  │  │  │  │  ├─ security/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  │  │  └─ sessions.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ caches.pyi
│  │     │  │  │  │  │  │  ├─ database.pyi
│  │     │  │  │  │  │  │  ├─ messages.pyi
│  │     │  │  │  │  │  │  ├─ model_checks.pyi
│  │     │  │  │  │  │  │  ├─ registry.pyi
│  │     │  │  │  │  │  │  ├─ templates.pyi
│  │     │  │  │  │  │  │  ├─ translation.pyi
│  │     │  │  │  │  │  │  └─ urls.pyi
│  │     │  │  │  │  │  ├─ files/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ images.pyi
│  │     │  │  │  │  │  │  ├─ locks.pyi
│  │     │  │  │  │  │  │  ├─ move.pyi
│  │     │  │  │  │  │  │  ├─ storage.pyi
│  │     │  │  │  │  │  │  ├─ temp.pyi
│  │     │  │  │  │  │  │  ├─ uploadedfile.pyi
│  │     │  │  │  │  │  │  ├─ uploadhandler.pyi
│  │     │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  ├─ handlers/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ exception.pyi
│  │     │  │  │  │  │  │  └─ wsgi.pyi
│  │     │  │  │  │  │  ├─ mail/
│  │     │  │  │  │  │  │  ├─ backends/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ console.pyi
│  │     │  │  │  │  │  │  │  ├─ dummy.pyi
│  │     │  │  │  │  │  │  │  ├─ filebased.pyi
│  │     │  │  │  │  │  │  │  ├─ locmem.pyi
│  │     │  │  │  │  │  │  │  └─ smtp.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ message.pyi
│  │     │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  ├─ management/
│  │     │  │  │  │  │  │  ├─ commands/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ dumpdata.pyi
│  │     │  │  │  │  │  │  │  ├─ loaddata.pyi
│  │     │  │  │  │  │  │  │  ├─ makemessages.pyi
│  │     │  │  │  │  │  │  │  ├─ runserver.pyi
│  │     │  │  │  │  │  │  │  └─ testserver.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ color.pyi
│  │     │  │  │  │  │  │  ├─ sql.pyi
│  │     │  │  │  │  │  │  ├─ templates.pyi
│  │     │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  ├─ serializers/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ json.pyi
│  │     │  │  │  │  │  │  └─ python.pyi
│  │     │  │  │  │  │  ├─ servers/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  └─ basehttp.pyi
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  ├─ paginator.pyi
│  │     │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  ├─ signing.pyi
│  │     │  │  │  │  │  ├─ validators.pyi
│  │     │  │  │  │  │  └─ wsgi.pyi
│  │     │  │  │  │  ├─ db/
│  │     │  │  │  │  │  ├─ backends/
│  │     │  │  │  │  │  │  ├─ base/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ client.pyi
│  │     │  │  │  │  │  │  │  ├─ creation.pyi
│  │     │  │  │  │  │  │  │  ├─ features.pyi
│  │     │  │  │  │  │  │  │  ├─ introspection.pyi
│  │     │  │  │  │  │  │  │  ├─ operations.pyi
│  │     │  │  │  │  │  │  │  ├─ schema.pyi
│  │     │  │  │  │  │  │  │  └─ validation.pyi
│  │     │  │  │  │  │  │  ├─ dummy/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ base.pyi
│  │     │  │  │  │  │  │  ├─ mysql/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  └─ client.pyi
│  │     │  │  │  │  │  │  ├─ postgresql/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ client.pyi
│  │     │  │  │  │  │  │  │  ├─ creation.pyi
│  │     │  │  │  │  │  │  │  └─ operations.pyi
│  │     │  │  │  │  │  │  ├─ sqlite3/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ creation.pyi
│  │     │  │  │  │  │  │  │  ├─ features.pyi
│  │     │  │  │  │  │  │  │  ├─ introspection.pyi
│  │     │  │  │  │  │  │  │  ├─ operations.pyi
│  │     │  │  │  │  │  │  │  └─ schema.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ ddl_references.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  ├─ migrations/
│  │     │  │  │  │  │  │  ├─ operations/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  │  ├─ fields.pyi
│  │     │  │  │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  │  │  ├─ special.pyi
│  │     │  │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ autodetector.pyi
│  │     │  │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  │  ├─ executor.pyi
│  │     │  │  │  │  │  │  ├─ graph.pyi
│  │     │  │  │  │  │  │  ├─ loader.pyi
│  │     │  │  │  │  │  │  ├─ migration.pyi
│  │     │  │  │  │  │  │  ├─ optimizer.pyi
│  │     │  │  │  │  │  │  ├─ questioner.pyi
│  │     │  │  │  │  │  │  ├─ recorder.pyi
│  │     │  │  │  │  │  │  ├─ serializer.pyi
│  │     │  │  │  │  │  │  ├─ state.pyi
│  │     │  │  │  │  │  │  ├─ topological_sort.pyi
│  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  │  └─ writer.pyi
│  │     │  │  │  │  │  ├─ models/
│  │     │  │  │  │  │  │  ├─ fields/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ files.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  ├─ proxy.pyi
│  │     │  │  │  │  │  │  │  ├─ related_descriptors.pyi
│  │     │  │  │  │  │  │  │  ├─ related_lookups.pyi
│  │     │  │  │  │  │  │  │  ├─ related.pyi
│  │     │  │  │  │  │  │  │  └─ reverse_related.pyi
│  │     │  │  │  │  │  │  ├─ functions/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ comparison.pyi
│  │     │  │  │  │  │  │  │  ├─ datetime.pyi
│  │     │  │  │  │  │  │  │  ├─ math.pyi
│  │     │  │  │  │  │  │  │  ├─ mixins.pyi
│  │     │  │  │  │  │  │  │  ├─ text.pyi
│  │     │  │  │  │  │  │  │  └─ window.pyi
│  │     │  │  │  │  │  │  ├─ sql/
│  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  │  ├─ compiler.pyi
│  │     │  │  │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  │  │  ├─ datastructures.pyi
│  │     │  │  │  │  │  │  │  ├─ query.pyi
│  │     │  │  │  │  │  │  │  ├─ subqueries.pyi
│  │     │  │  │  │  │  │  │  └─ where.pyi
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ aggregates.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ constraints.pyi
│  │     │  │  │  │  │  │  ├─ deletion.pyi
│  │     │  │  │  │  │  │  ├─ enums.pyi
│  │     │  │  │  │  │  │  ├─ expressions.pyi
│  │     │  │  │  │  │  │  ├─ indexes.pyi
│  │     │  │  │  │  │  │  ├─ lookups.pyi
│  │     │  │  │  │  │  │  ├─ manager.pyi
│  │     │  │  │  │  │  │  ├─ options.pyi
│  │     │  │  │  │  │  │  ├─ query_utils.pyi
│  │     │  │  │  │  │  │  ├─ query.pyi
│  │     │  │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ transaction.pyi
│  │     │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  ├─ dispatch/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  └─ dispatcher.pyi
│  │     │  │  │  │  ├─ forms/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ boundfield.pyi
│  │     │  │  │  │  │  ├─ fields.pyi
│  │     │  │  │  │  │  ├─ forms.pyi
│  │     │  │  │  │  │  ├─ formsets.pyi
│  │     │  │  │  │  │  ├─ models.pyi
│  │     │  │  │  │  │  ├─ renderers.pyi
│  │     │  │  │  │  │  ├─ utils.pyi
│  │     │  │  │  │  │  └─ widgets.pyi
│  │     │  │  │  │  ├─ http/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ cookie.pyi
│  │     │  │  │  │  │  ├─ multipartparser.pyi
│  │     │  │  │  │  │  ├─ request.pyi
│  │     │  │  │  │  │  └─ response.pyi
│  │     │  │  │  │  ├─ middleware/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  ├─ clickjacking.pyi
│  │     │  │  │  │  │  ├─ common.pyi
│  │     │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  ├─ gzip.pyi
│  │     │  │  │  │  │  ├─ http.pyi
│  │     │  │  │  │  │  ├─ locale.pyi
│  │     │  │  │  │  │  └─ security.pyi
│  │     │  │  │  │  ├─ template/
│  │     │  │  │  │  │  ├─ backends/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ django.pyi
│  │     │  │  │  │  │  │  ├─ dummy.pyi
│  │     │  │  │  │  │  │  ├─ jinja2.pyi
│  │     │  │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  │  ├─ loaders/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ app_directories.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ cached.pyi
│  │     │  │  │  │  │  │  ├─ filesystem.pyi
│  │     │  │  │  │  │  │  └─ locmem.pyi
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  ├─ context_processors.pyi
│  │     │  │  │  │  │  ├─ context.pyi
│  │     │  │  │  │  │  ├─ defaultfilters.pyi
│  │     │  │  │  │  │  ├─ defaulttags.pyi
│  │     │  │  │  │  │  ├─ engine.pyi
│  │     │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  ├─ library.pyi
│  │     │  │  │  │  │  ├─ loader_tags.pyi
│  │     │  │  │  │  │  ├─ loader.pyi
│  │     │  │  │  │  │  ├─ response.pyi
│  │     │  │  │  │  │  ├─ smartif.pyi
│  │     │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  ├─ templatetags/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  ├─ i18n.pyi
│  │     │  │  │  │  │  ├─ l10n.pyi
│  │     │  │  │  │  │  ├─ static.pyi
│  │     │  │  │  │  │  └─ tz.pyi
│  │     │  │  │  │  ├─ test/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ client.pyi
│  │     │  │  │  │  │  ├─ html.pyi
│  │     │  │  │  │  │  ├─ runner.pyi
│  │     │  │  │  │  │  ├─ selenium.pyi
│  │     │  │  │  │  │  ├─ signals.pyi
│  │     │  │  │  │  │  ├─ testcases.pyi
│  │     │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  ├─ urls/
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  ├─ conf.pyi
│  │     │  │  │  │  │  ├─ converters.pyi
│  │     │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │  │  │  │  ├─ resolvers.pyi
│  │     │  │  │  │  │  └─ utils.pyi
│  │     │  │  │  │  ├─ utils/
│  │     │  │  │  │  │  ├─ translation/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ reloader.pyi
│  │     │  │  │  │  │  │  ├─ template.pyi
│  │     │  │  │  │  │  │  ├─ trans_null.pyi
│  │     │  │  │  │  │  │  └─ trans_real.pyi
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ _os.pyi
│  │     │  │  │  │  │  ├─ archive.pyi
│  │     │  │  │  │  │  ├─ autoreload.pyi
│  │     │  │  │  │  │  ├─ baseconv.pyi
│  │     │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  ├─ crypto.pyi
│  │     │  │  │  │  │  ├─ datastructures.pyi
│  │     │  │  │  │  │  ├─ dateformat.pyi
│  │     │  │  │  │  │  ├─ dateparse.pyi
│  │     │  │  │  │  │  ├─ dates.pyi
│  │     │  │  │  │  │  ├─ datetime_safe.pyi
│  │     │  │  │  │  │  ├─ deconstruct.pyi
│  │     │  │  │  │  │  ├─ decorators.pyi
│  │     │  │  │  │  │  ├─ deprecation.pyi
│  │     │  │  │  │  │  ├─ duration.pyi
│  │     │  │  │  │  │  ├─ encoding.pyi
│  │     │  │  │  │  │  ├─ feedgenerator.pyi
│  │     │  │  │  │  │  ├─ formats.pyi
│  │     │  │  │  │  │  ├─ functional.pyi
│  │     │  │  │  │  │  ├─ hashable.pyi
│  │     │  │  │  │  │  ├─ html.pyi
│  │     │  │  │  │  │  ├─ http.pyi
│  │     │  │  │  │  │  ├─ inspect.pyi
│  │     │  │  │  │  │  ├─ ipv6.pyi
│  │     │  │  │  │  │  ├─ itercompat.pyi
│  │     │  │  │  │  │  ├─ jslex.pyi
│  │     │  │  │  │  │  ├─ log.pyi
│  │     │  │  │  │  │  ├─ lorem_ipsum.pyi
│  │     │  │  │  │  │  ├─ module_loading.pyi
│  │     │  │  │  │  │  ├─ numberformat.pyi
│  │     │  │  │  │  │  ├─ regex_helper.pyi
│  │     │  │  │  │  │  ├─ safestring.pyi
│  │     │  │  │  │  │  ├─ six.pyi
│  │     │  │  │  │  │  ├─ termcolors.pyi
│  │     │  │  │  │  │  ├─ text.pyi
│  │     │  │  │  │  │  ├─ timesince.pyi
│  │     │  │  │  │  │  ├─ timezone.pyi
│  │     │  │  │  │  │  ├─ topological_sort.pyi
│  │     │  │  │  │  │  ├─ tree.pyi
│  │     │  │  │  │  │  ├─ version.pyi
│  │     │  │  │  │  │  └─ xmlutils.pyi
│  │     │  │  │  │  ├─ views/
│  │     │  │  │  │  │  ├─ decorators/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ cache.pyi
│  │     │  │  │  │  │  │  ├─ clickjacking.pyi
│  │     │  │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  │  ├─ debug.pyi
│  │     │  │  │  │  │  │  ├─ gzip.pyi
│  │     │  │  │  │  │  │  ├─ http.pyi
│  │     │  │  │  │  │  │  └─ vary.pyi
│  │     │  │  │  │  │  ├─ generic/
│  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  │  ├─ base.pyi
│  │     │  │  │  │  │  │  ├─ dates.pyi
│  │     │  │  │  │  │  │  ├─ detail.pyi
│  │     │  │  │  │  │  │  ├─ edit.pyi
│  │     │  │  │  │  │  │  └─ list.pyi
│  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  │  ├─ csrf.pyi
│  │     │  │  │  │  │  ├─ debug.pyi
│  │     │  │  │  │  │  ├─ defaults.pyi
│  │     │  │  │  │  │  ├─ i18n.pyi
│  │     │  │  │  │  │  └─ static.pyi
│  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │  │  │  └─ shortcuts.pyi
│  │     │  │  │  └─ LICENSE.txt
│  │     │  │  └─ typeshed/
│  │     │  │     ├─ stdlib/
│  │     │  │     │  ├─ 2/
│  │     │  │     │  │  ├─ distutils/
│  │     │  │     │  │  │  ├─ command/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ bdist_dumb.pyi
│  │     │  │     │  │  │  │  ├─ bdist_msi.pyi
│  │     │  │     │  │  │  │  ├─ bdist_packager.pyi
│  │     │  │     │  │  │  │  ├─ bdist_rpm.pyi
│  │     │  │     │  │  │  │  ├─ bdist_wininst.pyi
│  │     │  │     │  │  │  │  ├─ bdist.pyi
│  │     │  │     │  │  │  │  ├─ build_clib.pyi
│  │     │  │     │  │  │  │  ├─ build_ext.pyi
│  │     │  │     │  │  │  │  ├─ build_py.pyi
│  │     │  │     │  │  │  │  ├─ build_scripts.pyi
│  │     │  │     │  │  │  │  ├─ build.pyi
│  │     │  │     │  │  │  │  ├─ check.pyi
│  │     │  │     │  │  │  │  ├─ clean.pyi
│  │     │  │     │  │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  │  ├─ install_data.pyi
│  │     │  │     │  │  │  │  ├─ install_egg_info.pyi
│  │     │  │     │  │  │  │  ├─ install_headers.pyi
│  │     │  │     │  │  │  │  ├─ install_lib.pyi
│  │     │  │     │  │  │  │  ├─ install_scripts.pyi
│  │     │  │     │  │  │  │  ├─ install.pyi
│  │     │  │     │  │  │  │  ├─ register.pyi
│  │     │  │     │  │  │  │  ├─ sdist.pyi
│  │     │  │     │  │  │  │  └─ upload.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ archive_util.pyi
│  │     │  │     │  │  │  ├─ bcppcompiler.pyi
│  │     │  │     │  │  │  ├─ ccompiler.pyi
│  │     │  │     │  │  │  ├─ cmd.pyi
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  ├─ core.pyi
│  │     │  │     │  │  │  ├─ cygwinccompiler.pyi
│  │     │  │     │  │  │  ├─ debug.pyi
│  │     │  │     │  │  │  ├─ dep_util.pyi
│  │     │  │     │  │  │  ├─ dir_util.pyi
│  │     │  │     │  │  │  ├─ dist.pyi
│  │     │  │     │  │  │  ├─ emxccompiler.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ extension.pyi
│  │     │  │     │  │  │  ├─ fancy_getopt.pyi
│  │     │  │     │  │  │  ├─ file_util.pyi
│  │     │  │     │  │  │  ├─ filelist.pyi
│  │     │  │     │  │  │  ├─ log.pyi
│  │     │  │     │  │  │  ├─ msvccompiler.pyi
│  │     │  │     │  │  │  ├─ spawn.pyi
│  │     │  │     │  │  │  ├─ sysconfig.pyi
│  │     │  │     │  │  │  ├─ text_file.pyi
│  │     │  │     │  │  │  ├─ unixccompiler.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ version.pyi
│  │     │  │     │  │  ├─ email/
│  │     │  │     │  │  │  ├─ mime/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ application.pyi
│  │     │  │     │  │  │  │  ├─ audio.pyi
│  │     │  │     │  │  │  │  ├─ base.pyi
│  │     │  │     │  │  │  │  ├─ image.pyi
│  │     │  │     │  │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  │  ├─ multipart.pyi
│  │     │  │     │  │  │  │  ├─ nonmultipart.pyi
│  │     │  │     │  │  │  │  └─ text.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _parseaddr.pyi
│  │     │  │     │  │  │  ├─ base64mime.pyi
│  │     │  │     │  │  │  ├─ charset.pyi
│  │     │  │     │  │  │  ├─ encoders.pyi
│  │     │  │     │  │  │  ├─ feedparser.pyi
│  │     │  │     │  │  │  ├─ generator.pyi
│  │     │  │     │  │  │  ├─ header.pyi
│  │     │  │     │  │  │  ├─ iterators.pyi
│  │     │  │     │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  ├─ MIMEText.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ quoprimime.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ encodings/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ utf_8.pyi
│  │     │  │     │  │  ├─ multiprocessing/
│  │     │  │     │  │  │  ├─ dummy/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  └─ connection.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ pool.pyi
│  │     │  │     │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  └─ util.pyi
│  │     │  │     │  │  ├─ os/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ path.pyi
│  │     │  │     │  │  ├─ __builtin__.pyi
│  │     │  │     │  │  ├─ _ast.pyi
│  │     │  │     │  │  ├─ _collections.pyi
│  │     │  │     │  │  ├─ _functools.pyi
│  │     │  │     │  │  ├─ _hotshot.pyi
│  │     │  │     │  │  ├─ _io.pyi
│  │     │  │     │  │  ├─ _json.pyi
│  │     │  │     │  │  ├─ _md5.pyi
│  │     │  │     │  │  ├─ _sha.pyi
│  │     │  │     │  │  ├─ _sha256.pyi
│  │     │  │     │  │  ├─ _sha512.pyi
│  │     │  │     │  │  ├─ _socket.pyi
│  │     │  │     │  │  ├─ _sre.pyi
│  │     │  │     │  │  ├─ _struct.pyi
│  │     │  │     │  │  ├─ _symtable.pyi
│  │     │  │     │  │  ├─ _threading_local.pyi
│  │     │  │     │  │  ├─ _winreg.pyi
│  │     │  │     │  │  ├─ abc.pyi
│  │     │  │     │  │  ├─ ast.pyi
│  │     │  │     │  │  ├─ atexit.pyi
│  │     │  │     │  │  ├─ BaseHTTPServer.pyi
│  │     │  │     │  │  ├─ builtins.pyi
│  │     │  │     │  │  ├─ CGIHTTPServer.pyi
│  │     │  │     │  │  ├─ collections.pyi
│  │     │  │     │  │  ├─ commands.pyi
│  │     │  │     │  │  ├─ compileall.pyi
│  │     │  │     │  │  ├─ ConfigParser.pyi
│  │     │  │     │  │  ├─ Cookie.pyi
│  │     │  │     │  │  ├─ cookielib.pyi
│  │     │  │     │  │  ├─ copy_reg.pyi
│  │     │  │     │  │  ├─ cPickle.pyi
│  │     │  │     │  │  ├─ cStringIO.pyi
│  │     │  │     │  │  ├─ dircache.pyi
│  │     │  │     │  │  ├─ dummy_thread.pyi
│  │     │  │     │  │  ├─ exceptions.pyi
│  │     │  │     │  │  ├─ fcntl.pyi
│  │     │  │     │  │  ├─ fnmatch.pyi
│  │     │  │     │  │  ├─ functools.pyi
│  │     │  │     │  │  ├─ future_builtins.pyi
│  │     │  │     │  │  ├─ gc.pyi
│  │     │  │     │  │  ├─ getopt.pyi
│  │     │  │     │  │  ├─ getpass.pyi
│  │     │  │     │  │  ├─ gettext.pyi
│  │     │  │     │  │  ├─ glob.pyi
│  │     │  │     │  │  ├─ gzip.pyi
│  │     │  │     │  │  ├─ hashlib.pyi
│  │     │  │     │  │  ├─ heapq.pyi
│  │     │  │     │  │  ├─ htmlentitydefs.pyi
│  │     │  │     │  │  ├─ HTMLParser.pyi
│  │     │  │     │  │  ├─ httplib.pyi
│  │     │  │     │  │  ├─ imp.pyi
│  │     │  │     │  │  ├─ importlib.pyi
│  │     │  │     │  │  ├─ inspect.pyi
│  │     │  │     │  │  ├─ io.pyi
│  │     │  │     │  │  ├─ itertools.pyi
│  │     │  │     │  │  ├─ json.pyi
│  │     │  │     │  │  ├─ markupbase.pyi
│  │     │  │     │  │  ├─ md5.pyi
│  │     │  │     │  │  ├─ mimetools.pyi
│  │     │  │     │  │  ├─ mutex.pyi
│  │     │  │     │  │  ├─ ntpath.pyi
│  │     │  │     │  │  ├─ nturl2path.pyi
│  │     │  │     │  │  ├─ os2emxpath.pyi
│  │     │  │     │  │  ├─ pipes.pyi
│  │     │  │     │  │  ├─ platform.pyi
│  │     │  │     │  │  ├─ popen2.pyi
│  │     │  │     │  │  ├─ posix.pyi
│  │     │  │     │  │  ├─ posixpath.pyi
│  │     │  │     │  │  ├─ Queue.pyi
│  │     │  │     │  │  ├─ random.pyi
│  │     │  │     │  │  ├─ re.pyi
│  │     │  │     │  │  ├─ repr.pyi
│  │     │  │     │  │  ├─ resource.pyi
│  │     │  │     │  │  ├─ rfc822.pyi
│  │     │  │     │  │  ├─ robotparser.pyi
│  │     │  │     │  │  ├─ runpy.pyi
│  │     │  │     │  │  ├─ sets.pyi
│  │     │  │     │  │  ├─ sha.pyi
│  │     │  │     │  │  ├─ shelve.pyi
│  │     │  │     │  │  ├─ shlex.pyi
│  │     │  │     │  │  ├─ signal.pyi
│  │     │  │     │  │  ├─ SimpleHTTPServer.pyi
│  │     │  │     │  │  ├─ smtplib.pyi
│  │     │  │     │  │  ├─ SocketServer.pyi
│  │     │  │     │  │  ├─ spwd.pyi
│  │     │  │     │  │  ├─ sre_constants.pyi
│  │     │  │     │  │  ├─ sre_parse.pyi
│  │     │  │     │  │  ├─ stat.pyi
│  │     │  │     │  │  ├─ string.pyi
│  │     │  │     │  │  ├─ StringIO.pyi
│  │     │  │     │  │  ├─ stringold.pyi
│  │     │  │     │  │  ├─ strop.pyi
│  │     │  │     │  │  ├─ subprocess.pyi
│  │     │  │     │  │  ├─ symbol.pyi
│  │     │  │     │  │  ├─ sys.pyi
│  │     │  │     │  │  ├─ tempfile.pyi
│  │     │  │     │  │  ├─ textwrap.pyi
│  │     │  │     │  │  ├─ thread.pyi
│  │     │  │     │  │  ├─ toaiff.pyi
│  │     │  │     │  │  ├─ tokenize.pyi
│  │     │  │     │  │  ├─ types.pyi
│  │     │  │     │  │  ├─ typing.pyi
│  │     │  │     │  │  ├─ unittest.pyi
│  │     │  │     │  │  ├─ urllib.pyi
│  │     │  │     │  │  ├─ urllib2.pyi
│  │     │  │     │  │  ├─ urlparse.pyi
│  │     │  │     │  │  ├─ user.pyi
│  │     │  │     │  │  ├─ UserDict.pyi
│  │     │  │     │  │  ├─ UserList.pyi
│  │     │  │     │  │  ├─ UserString.pyi
│  │     │  │     │  │  ├─ whichdb.pyi
│  │     │  │     │  │  └─ xmlrpclib.pyi
│  │     │  │     │  ├─ 2and3/
│  │     │  │     │  │  ├─ _typeshed/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ wsgi.pyi
│  │     │  │     │  │  │  └─ xml.pyi
│  │     │  │     │  │  ├─ ctypes/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ wintypes.pyi
│  │     │  │     │  │  ├─ curses/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ ascii.pyi
│  │     │  │     │  │  │  ├─ panel.pyi
│  │     │  │     │  │  │  └─ textpad.pyi
│  │     │  │     │  │  ├─ ensurepip/
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ lib2to3/
│  │     │  │     │  │  │  ├─ pgen2/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ driver.pyi
│  │     │  │     │  │  │  │  ├─ grammar.pyi
│  │     │  │     │  │  │  │  ├─ literals.pyi
│  │     │  │     │  │  │  │  ├─ parse.pyi
│  │     │  │     │  │  │  │  ├─ pgen.pyi
│  │     │  │     │  │  │  │  ├─ token.pyi
│  │     │  │     │  │  │  │  └─ tokenize.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ pygram.pyi
│  │     │  │     │  │  │  └─ pytree.pyi
│  │     │  │     │  │  ├─ logging/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  └─ handlers.pyi
│  │     │  │     │  │  ├─ msilib/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ schema.pyi
│  │     │  │     │  │  │  ├─ sequence.pyi
│  │     │  │     │  │  │  └─ text.pyi
│  │     │  │     │  │  ├─ pydoc_data/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ topics.pyi
│  │     │  │     │  │  ├─ pyexpat/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  └─ model.pyi
│  │     │  │     │  │  ├─ sqlite3/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ dbapi2.pyi
│  │     │  │     │  │  ├─ wsgiref/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ handlers.pyi
│  │     │  │     │  │  │  ├─ headers.pyi
│  │     │  │     │  │  │  ├─ simple_server.pyi
│  │     │  │     │  │  │  ├─ types.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ validate.pyi
│  │     │  │     │  │  ├─ xml/
│  │     │  │     │  │  │  ├─ dom/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ domreg.pyi
│  │     │  │     │  │  │  │  ├─ expatbuilder.pyi
│  │     │  │     │  │  │  │  ├─ minicompat.pyi
│  │     │  │     │  │  │  │  ├─ minidom.pyi
│  │     │  │     │  │  │  │  ├─ NodeFilter.pyi
│  │     │  │     │  │  │  │  ├─ pulldom.pyi
│  │     │  │     │  │  │  │  └─ xmlbuilder.pyi
│  │     │  │     │  │  │  ├─ etree/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ cElementTree.pyi
│  │     │  │     │  │  │  │  ├─ ElementInclude.pyi
│  │     │  │     │  │  │  │  ├─ ElementPath.pyi
│  │     │  │     │  │  │  │  └─ ElementTree.pyi
│  │     │  │     │  │  │  ├─ parsers/
│  │     │  │     │  │  │  │  ├─ expat/
│  │     │  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  │  │  └─ model.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ sax/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ handler.pyi
│  │     │  │     │  │  │  │  ├─ saxutils.pyi
│  │     │  │     │  │  │  │  └─ xmlreader.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ __future__.pyi
│  │     │  │     │  │  ├─ _bisect.pyi
│  │     │  │     │  │  ├─ _codecs.pyi
│  │     │  │     │  │  ├─ _csv.pyi
│  │     │  │     │  │  ├─ _curses.pyi
│  │     │  │     │  │  ├─ _dummy_threading.pyi
│  │     │  │     │  │  ├─ _heapq.pyi
│  │     │  │     │  │  ├─ _msi.pyi
│  │     │  │     │  │  ├─ _random.pyi
│  │     │  │     │  │  ├─ _warnings.pyi
│  │     │  │     │  │  ├─ _weakref.pyi
│  │     │  │     │  │  ├─ _weakrefset.pyi
│  │     │  │     │  │  ├─ aifc.pyi
│  │     │  │     │  │  ├─ antigravity.pyi
│  │     │  │     │  │  ├─ argparse.pyi
│  │     │  │     │  │  ├─ array.pyi
│  │     │  │     │  │  ├─ asynchat.pyi
│  │     │  │     │  │  ├─ asyncore.pyi
│  │     │  │     │  │  ├─ audioop.pyi
│  │     │  │     │  │  ├─ base64.pyi
│  │     │  │     │  │  ├─ bdb.pyi
│  │     │  │     │  │  ├─ binascii.pyi
│  │     │  │     │  │  ├─ binhex.pyi
│  │     │  │     │  │  ├─ bisect.pyi
│  │     │  │     │  │  ├─ bz2.pyi
│  │     │  │     │  │  ├─ calendar.pyi
│  │     │  │     │  │  ├─ cgi.pyi
│  │     │  │     │  │  ├─ cgitb.pyi
│  │     │  │     │  │  ├─ chunk.pyi
│  │     │  │     │  │  ├─ cmath.pyi
│  │     │  │     │  │  ├─ cmd.pyi
│  │     │  │     │  │  ├─ code.pyi
│  │     │  │     │  │  ├─ codecs.pyi
│  │     │  │     │  │  ├─ codeop.pyi
│  │     │  │     │  │  ├─ colorsys.pyi
│  │     │  │     │  │  ├─ contextlib.pyi
│  │     │  │     │  │  ├─ copy.pyi
│  │     │  │     │  │  ├─ cProfile.pyi
│  │     │  │     │  │  ├─ crypt.pyi
│  │     │  │     │  │  ├─ csv.pyi
│  │     │  │     │  │  ├─ datetime.pyi
│  │     │  │     │  │  ├─ decimal.pyi
│  │     │  │     │  │  ├─ difflib.pyi
│  │     │  │     │  │  ├─ dis.pyi
│  │     │  │     │  │  ├─ doctest.pyi
│  │     │  │     │  │  ├─ dummy_threading.pyi
│  │     │  │     │  │  ├─ errno.pyi
│  │     │  │     │  │  ├─ filecmp.pyi
│  │     │  │     │  │  ├─ fileinput.pyi
│  │     │  │     │  │  ├─ formatter.pyi
│  │     │  │     │  │  ├─ fractions.pyi
│  │     │  │     │  │  ├─ ftplib.pyi
│  │     │  │     │  │  ├─ genericpath.pyi
│  │     │  │     │  │  ├─ grp.pyi
│  │     │  │     │  │  ├─ hmac.pyi
│  │     │  │     │  │  ├─ imaplib.pyi
│  │     │  │     │  │  ├─ imghdr.pyi
│  │     │  │     │  │  ├─ keyword.pyi
│  │     │  │     │  │  ├─ linecache.pyi
│  │     │  │     │  │  ├─ locale.pyi
│  │     │  │     │  │  ├─ macpath.pyi
│  │     │  │     │  │  ├─ mailbox.pyi
│  │     │  │     │  │  ├─ mailcap.pyi
│  │     │  │     │  │  ├─ marshal.pyi
│  │     │  │     │  │  ├─ math.pyi
│  │     │  │     │  │  ├─ mimetypes.pyi
│  │     │  │     │  │  ├─ mmap.pyi
│  │     │  │     │  │  ├─ modulefinder.pyi
│  │     │  │     │  │  ├─ msvcrt.pyi
│  │     │  │     │  │  ├─ netrc.pyi
│  │     │  │     │  │  ├─ nis.pyi
│  │     │  │     │  │  ├─ numbers.pyi
│  │     │  │     │  │  ├─ opcode.pyi
│  │     │  │     │  │  ├─ operator.pyi
│  │     │  │     │  │  ├─ optparse.pyi
│  │     │  │     │  │  ├─ parser.pyi
│  │     │  │     │  │  ├─ pdb.pyi
│  │     │  │     │  │  ├─ pickle.pyi
│  │     │  │     │  │  ├─ pickletools.pyi
│  │     │  │     │  │  ├─ pkgutil.pyi
│  │     │  │     │  │  ├─ plistlib.pyi
│  │     │  │     │  │  ├─ poplib.pyi
│  │     │  │     │  │  ├─ pprint.pyi
│  │     │  │     │  │  ├─ profile.pyi
│  │     │  │     │  │  ├─ pstats.pyi
│  │     │  │     │  │  ├─ pty.pyi
│  │     │  │     │  │  ├─ pwd.pyi
│  │     │  │     │  │  ├─ py_compile.pyi
│  │     │  │     │  │  ├─ pyclbr.pyi
│  │     │  │     │  │  ├─ pydoc.pyi
│  │     │  │     │  │  ├─ quopri.pyi
│  │     │  │     │  │  ├─ readline.pyi
│  │     │  │     │  │  ├─ rlcompleter.pyi
│  │     │  │     │  │  ├─ sched.pyi
│  │     │  │     │  │  ├─ select.pyi
│  │     │  │     │  │  ├─ shutil.pyi
│  │     │  │     │  │  ├─ site.pyi
│  │     │  │     │  │  ├─ smtpd.pyi
│  │     │  │     │  │  ├─ sndhdr.pyi
│  │     │  │     │  │  ├─ socket.pyi
│  │     │  │     │  │  ├─ sre_compile.pyi
│  │     │  │     │  │  ├─ ssl.pyi
│  │     │  │     │  │  ├─ stringprep.pyi
│  │     │  │     │  │  ├─ struct.pyi
│  │     │  │     │  │  ├─ sunau.pyi
│  │     │  │     │  │  ├─ symtable.pyi
│  │     │  │     │  │  ├─ sysconfig.pyi
│  │     │  │     │  │  ├─ syslog.pyi
│  │     │  │     │  │  ├─ tabnanny.pyi
│  │     │  │     │  │  ├─ tarfile.pyi
│  │     │  │     │  │  ├─ telnetlib.pyi
│  │     │  │     │  │  ├─ termios.pyi
│  │     │  │     │  │  ├─ this.pyi
│  │     │  │     │  │  ├─ threading.pyi
│  │     │  │     │  │  ├─ time.pyi
│  │     │  │     │  │  ├─ timeit.pyi
│  │     │  │     │  │  ├─ token.pyi
│  │     │  │     │  │  ├─ trace.pyi
│  │     │  │     │  │  ├─ traceback.pyi
│  │     │  │     │  │  ├─ tty.pyi
│  │     │  │     │  │  ├─ turtle.pyi
│  │     │  │     │  │  ├─ unicodedata.pyi
│  │     │  │     │  │  ├─ uu.pyi
│  │     │  │     │  │  ├─ uuid.pyi
│  │     │  │     │  │  ├─ warnings.pyi
│  │     │  │     │  │  ├─ wave.pyi
│  │     │  │     │  │  ├─ weakref.pyi
│  │     │  │     │  │  ├─ webbrowser.pyi
│  │     │  │     │  │  ├─ winsound.pyi
│  │     │  │     │  │  ├─ xdrlib.pyi
│  │     │  │     │  │  ├─ zipfile.pyi
│  │     │  │     │  │  ├─ zipimport.pyi
│  │     │  │     │  │  └─ zlib.pyi
│  │     │  │     │  ├─ 3/
│  │     │  │     │  │  ├─ asyncio/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ base_events.pyi
│  │     │  │     │  │  │  ├─ base_futures.pyi
│  │     │  │     │  │  │  ├─ base_subprocess.pyi
│  │     │  │     │  │  │  ├─ base_tasks.pyi
│  │     │  │     │  │  │  ├─ compat.pyi
│  │     │  │     │  │  │  ├─ constants.pyi
│  │     │  │     │  │  │  ├─ coroutines.pyi
│  │     │  │     │  │  │  ├─ events.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ format_helpers.pyi
│  │     │  │     │  │  │  ├─ futures.pyi
│  │     │  │     │  │  │  ├─ locks.pyi
│  │     │  │     │  │  │  ├─ log.pyi
│  │     │  │     │  │  │  ├─ proactor_events.pyi
│  │     │  │     │  │  │  ├─ protocols.pyi
│  │     │  │     │  │  │  ├─ queues.pyi
│  │     │  │     │  │  │  ├─ runners.pyi
│  │     │  │     │  │  │  ├─ selector_events.pyi
│  │     │  │     │  │  │  ├─ sslproto.pyi
│  │     │  │     │  │  │  ├─ staggered.pyi
│  │     │  │     │  │  │  ├─ streams.pyi
│  │     │  │     │  │  │  ├─ subprocess.pyi
│  │     │  │     │  │  │  ├─ tasks.pyi
│  │     │  │     │  │  │  ├─ threads.pyi
│  │     │  │     │  │  │  ├─ transports.pyi
│  │     │  │     │  │  │  ├─ trsock.pyi
│  │     │  │     │  │  │  ├─ unix_events.pyi
│  │     │  │     │  │  │  ├─ windows_events.pyi
│  │     │  │     │  │  │  └─ windows_utils.pyi
│  │     │  │     │  │  ├─ collections/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ abc.pyi
│  │     │  │     │  │  ├─ concurrent/
│  │     │  │     │  │  │  ├─ futures/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ _base.pyi
│  │     │  │     │  │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  │  └─ thread.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ dbm/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ dumb.pyi
│  │     │  │     │  │  │  ├─ gnu.pyi
│  │     │  │     │  │  │  └─ ndbm.pyi
│  │     │  │     │  │  ├─ distutils/
│  │     │  │     │  │  │  ├─ command/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ bdist_dumb.pyi
│  │     │  │     │  │  │  │  ├─ bdist_msi.pyi
│  │     │  │     │  │  │  │  ├─ bdist_packager.pyi
│  │     │  │     │  │  │  │  ├─ bdist_rpm.pyi
│  │     │  │     │  │  │  │  ├─ bdist_wininst.pyi
│  │     │  │     │  │  │  │  ├─ bdist.pyi
│  │     │  │     │  │  │  │  ├─ build_clib.pyi
│  │     │  │     │  │  │  │  ├─ build_ext.pyi
│  │     │  │     │  │  │  │  ├─ build_py.pyi
│  │     │  │     │  │  │  │  ├─ build_scripts.pyi
│  │     │  │     │  │  │  │  ├─ build.pyi
│  │     │  │     │  │  │  │  ├─ check.pyi
│  │     │  │     │  │  │  │  ├─ clean.pyi
│  │     │  │     │  │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  │  ├─ install_data.pyi
│  │     │  │     │  │  │  │  ├─ install_egg_info.pyi
│  │     │  │     │  │  │  │  ├─ install_headers.pyi
│  │     │  │     │  │  │  │  ├─ install_lib.pyi
│  │     │  │     │  │  │  │  ├─ install_scripts.pyi
│  │     │  │     │  │  │  │  ├─ install.pyi
│  │     │  │     │  │  │  │  ├─ register.pyi
│  │     │  │     │  │  │  │  ├─ sdist.pyi
│  │     │  │     │  │  │  │  └─ upload.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ archive_util.pyi
│  │     │  │     │  │  │  ├─ bcppcompiler.pyi
│  │     │  │     │  │  │  ├─ ccompiler.pyi
│  │     │  │     │  │  │  ├─ cmd.pyi
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  ├─ core.pyi
│  │     │  │     │  │  │  ├─ cygwinccompiler.pyi
│  │     │  │     │  │  │  ├─ debug.pyi
│  │     │  │     │  │  │  ├─ dep_util.pyi
│  │     │  │     │  │  │  ├─ dir_util.pyi
│  │     │  │     │  │  │  ├─ dist.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ extension.pyi
│  │     │  │     │  │  │  ├─ fancy_getopt.pyi
│  │     │  │     │  │  │  ├─ file_util.pyi
│  │     │  │     │  │  │  ├─ filelist.pyi
│  │     │  │     │  │  │  ├─ log.pyi
│  │     │  │     │  │  │  ├─ msvccompiler.pyi
│  │     │  │     │  │  │  ├─ spawn.pyi
│  │     │  │     │  │  │  ├─ sysconfig.pyi
│  │     │  │     │  │  │  ├─ text_file.pyi
│  │     │  │     │  │  │  ├─ unixccompiler.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ version.pyi
│  │     │  │     │  │  ├─ email/
│  │     │  │     │  │  │  ├─ mime/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ application.pyi
│  │     │  │     │  │  │  │  ├─ audio.pyi
│  │     │  │     │  │  │  │  ├─ base.pyi
│  │     │  │     │  │  │  │  ├─ image.pyi
│  │     │  │     │  │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  │  ├─ multipart.pyi
│  │     │  │     │  │  │  │  ├─ nonmultipart.pyi
│  │     │  │     │  │  │  │  └─ text.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ charset.pyi
│  │     │  │     │  │  │  ├─ contentmanager.pyi
│  │     │  │     │  │  │  ├─ encoders.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ feedparser.pyi
│  │     │  │     │  │  │  ├─ generator.pyi
│  │     │  │     │  │  │  ├─ header.pyi
│  │     │  │     │  │  │  ├─ headerregistry.pyi
│  │     │  │     │  │  │  ├─ iterators.pyi
│  │     │  │     │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ policy.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ encodings/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ utf_8.pyi
│  │     │  │     │  │  ├─ html/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ entities.pyi
│  │     │  │     │  │  │  └─ parser.pyi
│  │     │  │     │  │  ├─ http/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ client.pyi
│  │     │  │     │  │  │  ├─ cookiejar.pyi
│  │     │  │     │  │  │  ├─ cookies.pyi
│  │     │  │     │  │  │  └─ server.pyi
│  │     │  │     │  │  ├─ importlib/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ abc.pyi
│  │     │  │     │  │  │  ├─ machinery.pyi
│  │     │  │     │  │  │  ├─ metadata.pyi
│  │     │  │     │  │  │  ├─ resources.pyi
│  │     │  │     │  │  │  └─ util.pyi
│  │     │  │     │  │  ├─ json/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ decoder.pyi
│  │     │  │     │  │  │  ├─ encoder.pyi
│  │     │  │     │  │  │  └─ tool.pyi
│  │     │  │     │  │  ├─ multiprocessing/
│  │     │  │     │  │  │  ├─ dummy/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  └─ connection.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  ├─ context.pyi
│  │     │  │     │  │  │  ├─ managers.pyi
│  │     │  │     │  │  │  ├─ pool.pyi
│  │     │  │     │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  ├─ queues.pyi
│  │     │  │     │  │  │  ├─ shared_memory.pyi
│  │     │  │     │  │  │  ├─ sharedctypes.pyi
│  │     │  │     │  │  │  ├─ spawn.pyi
│  │     │  │     │  │  │  └─ synchronize.pyi
│  │     │  │     │  │  ├─ os/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ path.pyi
│  │     │  │     │  │  ├─ tkinter/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ commondialog.pyi
│  │     │  │     │  │  │  ├─ constants.pyi
│  │     │  │     │  │  │  ├─ dialog.pyi
│  │     │  │     │  │  │  ├─ filedialog.pyi
│  │     │  │     │  │  │  ├─ font.pyi
│  │     │  │     │  │  │  ├─ messagebox.pyi
│  │     │  │     │  │  │  └─ ttk.pyi
│  │     │  │     │  │  ├─ unittest/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ async_case.pyi
│  │     │  │     │  │  │  ├─ case.pyi
│  │     │  │     │  │  │  ├─ loader.pyi
│  │     │  │     │  │  │  ├─ main.pyi
│  │     │  │     │  │  │  ├─ mock.pyi
│  │     │  │     │  │  │  ├─ result.pyi
│  │     │  │     │  │  │  ├─ runner.pyi
│  │     │  │     │  │  │  ├─ signals.pyi
│  │     │  │     │  │  │  ├─ suite.pyi
│  │     │  │     │  │  │  └─ util.pyi
│  │     │  │     │  │  ├─ urllib/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ error.pyi
│  │     │  │     │  │  │  ├─ parse.pyi
│  │     │  │     │  │  │  ├─ request.pyi
│  │     │  │     │  │  │  ├─ response.pyi
│  │     │  │     │  │  │  └─ robotparser.pyi
│  │     │  │     │  │  ├─ venv/
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ xmlrpc/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ client.pyi
│  │     │  │     │  │  │  └─ server.pyi
│  │     │  │     │  │  ├─ _ast.pyi
│  │     │  │     │  │  ├─ _bootlocale.pyi
│  │     │  │     │  │  ├─ _compat_pickle.pyi
│  │     │  │     │  │  ├─ _compression.pyi
│  │     │  │     │  │  ├─ _decimal.pyi
│  │     │  │     │  │  ├─ _dummy_thread.pyi
│  │     │  │     │  │  ├─ _imp.pyi
│  │     │  │     │  │  ├─ _importlib_modulespec.pyi
│  │     │  │     │  │  ├─ _json.pyi
│  │     │  │     │  │  ├─ _markupbase.pyi
│  │     │  │     │  │  ├─ _operator.pyi
│  │     │  │     │  │  ├─ _osx_support.pyi
│  │     │  │     │  │  ├─ _posixsubprocess.pyi
│  │     │  │     │  │  ├─ _pydecimal.pyi
│  │     │  │     │  │  ├─ _sitebuiltins.pyi
│  │     │  │     │  │  ├─ _stat.pyi
│  │     │  │     │  │  ├─ _thread.pyi
│  │     │  │     │  │  ├─ _threading_local.pyi
│  │     │  │     │  │  ├─ _tkinter.pyi
│  │     │  │     │  │  ├─ _tracemalloc.pyi
│  │     │  │     │  │  ├─ _winapi.pyi
│  │     │  │     │  │  ├─ abc.pyi
│  │     │  │     │  │  ├─ ast.pyi
│  │     │  │     │  │  ├─ atexit.pyi
│  │     │  │     │  │  ├─ builtins.pyi
│  │     │  │     │  │  ├─ compileall.pyi
│  │     │  │     │  │  ├─ configparser.pyi
│  │     │  │     │  │  ├─ copyreg.pyi
│  │     │  │     │  │  ├─ enum.pyi
│  │     │  │     │  │  ├─ faulthandler.pyi
│  │     │  │     │  │  ├─ fcntl.pyi
│  │     │  │     │  │  ├─ fnmatch.pyi
│  │     │  │     │  │  ├─ functools.pyi
│  │     │  │     │  │  ├─ gc.pyi
│  │     │  │     │  │  ├─ getopt.pyi
│  │     │  │     │  │  ├─ getpass.pyi
│  │     │  │     │  │  ├─ gettext.pyi
│  │     │  │     │  │  ├─ glob.pyi
│  │     │  │     │  │  ├─ gzip.pyi
│  │     │  │     │  │  ├─ hashlib.pyi
│  │     │  │     │  │  ├─ heapq.pyi
│  │     │  │     │  │  ├─ imp.pyi
│  │     │  │     │  │  ├─ inspect.pyi
│  │     │  │     │  │  ├─ io.pyi
│  │     │  │     │  │  ├─ ipaddress.pyi
│  │     │  │     │  │  ├─ itertools.pyi
│  │     │  │     │  │  ├─ lzma.pyi
│  │     │  │     │  │  ├─ macurl2path.pyi
│  │     │  │     │  │  ├─ nntplib.pyi
│  │     │  │     │  │  ├─ ntpath.pyi
│  │     │  │     │  │  ├─ nturl2path.pyi
│  │     │  │     │  │  ├─ pathlib.pyi
│  │     │  │     │  │  ├─ pipes.pyi
│  │     │  │     │  │  ├─ platform.pyi
│  │     │  │     │  │  ├─ posix.pyi
│  │     │  │     │  │  ├─ posixpath.pyi
│  │     │  │     │  │  ├─ queue.pyi
│  │     │  │     │  │  ├─ random.pyi
│  │     │  │     │  │  ├─ re.pyi
│  │     │  │     │  │  ├─ reprlib.pyi
│  │     │  │     │  │  ├─ resource.pyi
│  │     │  │     │  │  ├─ runpy.pyi
│  │     │  │     │  │  ├─ secrets.pyi
│  │     │  │     │  │  ├─ selectors.pyi
│  │     │  │     │  │  ├─ shelve.pyi
│  │     │  │     │  │  ├─ shlex.pyi
│  │     │  │     │  │  ├─ signal.pyi
│  │     │  │     │  │  ├─ smtplib.pyi
│  │     │  │     │  │  ├─ socketserver.pyi
│  │     │  │     │  │  ├─ spwd.pyi
│  │     │  │     │  │  ├─ sre_constants.pyi
│  │     │  │     │  │  ├─ sre_parse.pyi
│  │     │  │     │  │  ├─ stat.pyi
│  │     │  │     │  │  ├─ statistics.pyi
│  │     │  │     │  │  ├─ string.pyi
│  │     │  │     │  │  ├─ subprocess.pyi
│  │     │  │     │  │  ├─ symbol.pyi
│  │     │  │     │  │  ├─ sys.pyi
│  │     │  │     │  │  ├─ tempfile.pyi
│  │     │  │     │  │  ├─ textwrap.pyi
│  │     │  │     │  │  ├─ tokenize.pyi
│  │     │  │     │  │  ├─ tracemalloc.pyi
│  │     │  │     │  │  ├─ types.pyi
│  │     │  │     │  │  ├─ typing.pyi
│  │     │  │     │  │  ├─ winreg.pyi
│  │     │  │     │  │  ├─ xxlimited.pyi
│  │     │  │     │  │  └─ zipapp.pyi
│  │     │  │     │  ├─ 3.7/
│  │     │  │     │  │  ├─ _py_abc.pyi
│  │     │  │     │  │  ├─ contextvars.pyi
│  │     │  │     │  │  └─ dataclasses.pyi
│  │     │  │     │  └─ 3.9/
│  │     │  │     │     ├─ zoneinfo/
│  │     │  │     │     │  └─ __init__.pyi
│  │     │  │     │     └─ graphlib.pyi
│  │     │  │     ├─ third_party/
│  │     │  │     │  ├─ 2/
│  │     │  │     │  │  ├─ concurrent/
│  │     │  │     │  │  │  ├─ futures/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ _base.pyi
│  │     │  │     │  │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  │  └─ thread.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ fb303/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ FacebookService.pyi
│  │     │  │     │  │  ├─ kazoo/
│  │     │  │     │  │  │  ├─ recipe/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  └─ watchers.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ client.pyi
│  │     │  │     │  │  │  └─ exceptions.pyi
│  │     │  │     │  │  ├─ OpenSSL/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ crypto.pyi
│  │     │  │     │  │  ├─ routes/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ mapper.pyi
│  │     │  │     │  │  │  └─ util.pyi
│  │     │  │     │  │  ├─ scribe/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ scribe.pyi
│  │     │  │     │  │  │  └─ ttypes.pyi
│  │     │  │     │  │  ├─ six/
│  │     │  │     │  │  │  ├─ moves/
│  │     │  │     │  │  │  │  ├─ urllib/
│  │     │  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  ├─ error.pyi
│  │     │  │     │  │  │  │  │  ├─ parse.pyi
│  │     │  │     │  │  │  │  │  ├─ request.pyi
│  │     │  │     │  │  │  │  │  ├─ response.pyi
│  │     │  │     │  │  │  │  │  └─ robotparser.pyi
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ _dummy_thread.pyi
│  │     │  │     │  │  │  │  ├─ _thread.pyi
│  │     │  │     │  │  │  │  ├─ BaseHTTPServer.pyi
│  │     │  │     │  │  │  │  ├─ CGIHTTPServer.pyi
│  │     │  │     │  │  │  │  ├─ collections_abc.pyi
│  │     │  │     │  │  │  │  ├─ configparser.pyi
│  │     │  │     │  │  │  │  ├─ cPickle.pyi
│  │     │  │     │  │  │  │  ├─ email_mime_base.pyi
│  │     │  │     │  │  │  │  ├─ email_mime_multipart.pyi
│  │     │  │     │  │  │  │  ├─ email_mime_nonmultipart.pyi
│  │     │  │     │  │  │  │  ├─ email_mime_text.pyi
│  │     │  │     │  │  │  │  ├─ html_entities.pyi
│  │     │  │     │  │  │  │  ├─ html_parser.pyi
│  │     │  │     │  │  │  │  ├─ http_client.pyi
│  │     │  │     │  │  │  │  ├─ http_cookiejar.pyi
│  │     │  │     │  │  │  │  ├─ http_cookies.pyi
│  │     │  │     │  │  │  │  ├─ queue.pyi
│  │     │  │     │  │  │  │  ├─ reprlib.pyi
│  │     │  │     │  │  │  │  ├─ SimpleHTTPServer.pyi
│  │     │  │     │  │  │  │  ├─ socketserver.pyi
│  │     │  │     │  │  │  │  ├─ urllib_error.pyi
│  │     │  │     │  │  │  │  ├─ urllib_parse.pyi
│  │     │  │     │  │  │  │  ├─ urllib_request.pyi
│  │     │  │     │  │  │  │  ├─ urllib_response.pyi
│  │     │  │     │  │  │  │  ├─ urllib_robotparser.pyi
│  │     │  │     │  │  │  │  └─ xmlrpc_client.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ tornado/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ concurrent.pyi
│  │     │  │     │  │  │  ├─ gen.pyi
│  │     │  │     │  │  │  ├─ httpclient.pyi
│  │     │  │     │  │  │  ├─ httpserver.pyi
│  │     │  │     │  │  │  ├─ httputil.pyi
│  │     │  │     │  │  │  ├─ ioloop.pyi
│  │     │  │     │  │  │  ├─ locks.pyi
│  │     │  │     │  │  │  ├─ netutil.pyi
│  │     │  │     │  │  │  ├─ process.pyi
│  │     │  │     │  │  │  ├─ tcpserver.pyi
│  │     │  │     │  │  │  ├─ testing.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ web.pyi
│  │     │  │     │  │  ├─ enum.pyi
│  │     │  │     │  │  ├─ ipaddress.pyi
│  │     │  │     │  │  ├─ pathlib2.pyi
│  │     │  │     │  │  └─ pymssql.pyi
│  │     │  │     │  ├─ 2and3/
│  │     │  │     │  │  ├─ atomicwrites/
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ attr/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _version_info.pyi
│  │     │  │     │  │  │  ├─ converters.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ filters.pyi
│  │     │  │     │  │  │  └─ validators.pyi
│  │     │  │     │  │  ├─ backports/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ ssl_match_hostname.pyi
│  │     │  │     │  │  ├─ bleach/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ callbacks.pyi
│  │     │  │     │  │  │  ├─ linkifier.pyi
│  │     │  │     │  │  │  ├─ sanitizer.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ boto/
│  │     │  │     │  │  │  ├─ ec2/
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ elb/
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ kms/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  │  └─ layer1.pyi
│  │     │  │     │  │  │  ├─ s3/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ acl.pyi
│  │     │  │     │  │  │  │  ├─ bucket.pyi
│  │     │  │     │  │  │  │  ├─ bucketlistresultset.pyi
│  │     │  │     │  │  │  │  ├─ bucketlogging.pyi
│  │     │  │     │  │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  │  ├─ cors.pyi
│  │     │  │     │  │  │  │  ├─ deletemarker.pyi
│  │     │  │     │  │  │  │  ├─ key.pyi
│  │     │  │     │  │  │  │  ├─ keyfile.pyi
│  │     │  │     │  │  │  │  ├─ lifecycle.pyi
│  │     │  │     │  │  │  │  ├─ multidelete.pyi
│  │     │  │     │  │  │  │  ├─ multipart.pyi
│  │     │  │     │  │  │  │  ├─ prefix.pyi
│  │     │  │     │  │  │  │  ├─ tagging.pyi
│  │     │  │     │  │  │  │  ├─ user.pyi
│  │     │  │     │  │  │  │  └─ website.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ auth_handler.pyi
│  │     │  │     │  │  │  ├─ auth.pyi
│  │     │  │     │  │  │  ├─ compat.pyi
│  │     │  │     │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  ├─ exception.pyi
│  │     │  │     │  │  │  ├─ plugin.pyi
│  │     │  │     │  │  │  ├─ regioninfo.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ cachetools/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ abc.pyi
│  │     │  │     │  │  │  ├─ cache.pyi
│  │     │  │     │  │  │  ├─ decorators.pyi
│  │     │  │     │  │  │  ├─ func.pyi
│  │     │  │     │  │  │  ├─ lfu.pyi
│  │     │  │     │  │  │  ├─ lru.pyi
│  │     │  │     │  │  │  ├─ rr.pyi
│  │     │  │     │  │  │  └─ ttl.pyi
│  │     │  │     │  │  ├─ characteristic/
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ chardet/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ enums.pyi
│  │     │  │     │  │  │  ├─ langbulgarianmodel.pyi
│  │     │  │     │  │  │  ├─ langcyrillicmodel.pyi
│  │     │  │     │  │  │  ├─ langgreekmodel.pyi
│  │     │  │     │  │  │  ├─ langhebrewmodel.pyi
│  │     │  │     │  │  │  ├─ langhungarianmodel.pyi
│  │     │  │     │  │  │  ├─ langthaimodel.pyi
│  │     │  │     │  │  │  ├─ langturkishmodel.pyi
│  │     │  │     │  │  │  ├─ universaldetector.pyi
│  │     │  │     │  │  │  └─ version.pyi
│  │     │  │     │  │  ├─ click/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _termui_impl.pyi
│  │     │  │     │  │  │  ├─ core.pyi
│  │     │  │     │  │  │  ├─ decorators.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ formatting.pyi
│  │     │  │     │  │  │  ├─ globals.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ termui.pyi
│  │     │  │     │  │  │  ├─ testing.pyi
│  │     │  │     │  │  │  ├─ types.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ cryptography/
│  │     │  │     │  │  │  ├─ hazmat/
│  │     │  │     │  │  │  │  ├─ backends/
│  │     │  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  └─ interfaces.pyi
│  │     │  │     │  │  │  │  ├─ bindings/
│  │     │  │     │  │  │  │  │  ├─ openssl/
│  │     │  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  └─ binding.pyi
│  │     │  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ primitives/
│  │     │  │     │  │  │  │  │  ├─ asymmetric/
│  │     │  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  ├─ dh.pyi
│  │     │  │     │  │  │  │  │  │  ├─ dsa.pyi
│  │     │  │     │  │  │  │  │  │  ├─ ec.pyi
│  │     │  │     │  │  │  │  │  │  ├─ ed25519.pyi
│  │     │  │     │  │  │  │  │  │  ├─ ed448.pyi
│  │     │  │     │  │  │  │  │  │  ├─ padding.pyi
│  │     │  │     │  │  │  │  │  │  ├─ rsa.pyi
│  │     │  │     │  │  │  │  │  │  ├─ utils.pyi
│  │     │  │     │  │  │  │  │  │  ├─ x25519.pyi
│  │     │  │     │  │  │  │  │  │  └─ x448.pyi
│  │     │  │     │  │  │  │  │  ├─ ciphers/
│  │     │  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  ├─ aead.pyi
│  │     │  │     │  │  │  │  │  │  ├─ algorithms.pyi
│  │     │  │     │  │  │  │  │  │  └─ modes.pyi
│  │     │  │     │  │  │  │  │  ├─ kdf/
│  │     │  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  ├─ concatkdf.pyi
│  │     │  │     │  │  │  │  │  │  ├─ hkdf.pyi
│  │     │  │     │  │  │  │  │  │  ├─ kbkdf.pyi
│  │     │  │     │  │  │  │  │  │  ├─ pbkdf2.pyi
│  │     │  │     │  │  │  │  │  │  ├─ scrypt.pyi
│  │     │  │     │  │  │  │  │  │  └─ x963kdf.pyi
│  │     │  │     │  │  │  │  │  ├─ serialization/
│  │     │  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  └─ pkcs12.pyi
│  │     │  │     │  │  │  │  │  ├─ twofactor/
│  │     │  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  ├─ hotp.pyi
│  │     │  │     │  │  │  │  │  │  └─ totp.pyi
│  │     │  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  ├─ cmac.pyi
│  │     │  │     │  │  │  │  │  ├─ constant_time.pyi
│  │     │  │     │  │  │  │  │  ├─ hashes.pyi
│  │     │  │     │  │  │  │  │  ├─ hmac.pyi
│  │     │  │     │  │  │  │  │  ├─ keywrap.pyi
│  │     │  │     │  │  │  │  │  ├─ padding.pyi
│  │     │  │     │  │  │  │  │  └─ poly1305.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ x509/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ extensions.pyi
│  │     │  │     │  │  │  │  └─ oid.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  └─ fernet.pyi
│  │     │  │     │  │  ├─ datetimerange/
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ dateutil/
│  │     │  │     │  │  │  ├─ tz/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ _common.pyi
│  │     │  │     │  │  │  │  └─ tz.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _common.pyi
│  │     │  │     │  │  │  ├─ easter.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ relativedelta.pyi
│  │     │  │     │  │  │  ├─ rrule.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ deprecated/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ classic.pyi
│  │     │  │     │  │  │  └─ sphinx.pyi
│  │     │  │     │  │  ├─ emoji/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ core.pyi
│  │     │  │     │  │  │  └─ unicode_codes.pyi
│  │     │  │     │  │  ├─ flask/
│  │     │  │     │  │  │  ├─ json/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  └─ tag.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ app.pyi
│  │     │  │     │  │  │  ├─ blueprints.pyi
│  │     │  │     │  │  │  ├─ cli.pyi
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  ├─ ctx.pyi
│  │     │  │     │  │  │  ├─ debughelpers.pyi
│  │     │  │     │  │  │  ├─ globals.pyi
│  │     │  │     │  │  │  ├─ helpers.pyi
│  │     │  │     │  │  │  ├─ logging.pyi
│  │     │  │     │  │  │  ├─ sessions.pyi
│  │     │  │     │  │  │  ├─ signals.pyi
│  │     │  │     │  │  │  ├─ templating.pyi
│  │     │  │     │  │  │  ├─ testing.pyi
│  │     │  │     │  │  │  ├─ views.pyi
│  │     │  │     │  │  │  └─ wrappers.pyi
│  │     │  │     │  │  ├─ geoip2/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ database.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ mixins.pyi
│  │     │  │     │  │  │  ├─ models.pyi
│  │     │  │     │  │  │  └─ records.pyi
│  │     │  │     │  │  ├─ google/
│  │     │  │     │  │  │  ├─ protobuf/
│  │     │  │     │  │  │  │  ├─ compiler/
│  │     │  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  └─ plugin_pb2.pyi
│  │     │  │     │  │  │  │  ├─ internal/
│  │     │  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  ├─ containers.pyi
│  │     │  │     │  │  │  │  │  ├─ decoder.pyi
│  │     │  │     │  │  │  │  │  ├─ encoder.pyi
│  │     │  │     │  │  │  │  │  ├─ enum_type_wrapper.pyi
│  │     │  │     │  │  │  │  │  ├─ extension_dict.pyi
│  │     │  │     │  │  │  │  │  ├─ message_listener.pyi
│  │     │  │     │  │  │  │  │  ├─ python_message.pyi
│  │     │  │     │  │  │  │  │  ├─ well_known_types.pyi
│  │     │  │     │  │  │  │  │  └─ wire_format.pyi
│  │     │  │     │  │  │  │  ├─ util/
│  │     │  │     │  │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ any_pb2.pyi
│  │     │  │     │  │  │  │  ├─ api_pb2.pyi
│  │     │  │     │  │  │  │  ├─ descriptor_pb2.pyi
│  │     │  │     │  │  │  │  ├─ descriptor_pool.pyi
│  │     │  │     │  │  │  │  ├─ descriptor.pyi
│  │     │  │     │  │  │  │  ├─ duration_pb2.pyi
│  │     │  │     │  │  │  │  ├─ empty_pb2.pyi
│  │     │  │     │  │  │  │  ├─ field_mask_pb2.pyi
│  │     │  │     │  │  │  │  ├─ json_format.pyi
│  │     │  │     │  │  │  │  ├─ message_factory.pyi
│  │     │  │     │  │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  │  ├─ reflection.pyi
│  │     │  │     │  │  │  │  ├─ service.pyi
│  │     │  │     │  │  │  │  ├─ source_context_pb2.pyi
│  │     │  │     │  │  │  │  ├─ struct_pb2.pyi
│  │     │  │     │  │  │  │  ├─ symbol_database.pyi
│  │     │  │     │  │  │  │  ├─ timestamp_pb2.pyi
│  │     │  │     │  │  │  │  ├─ type_pb2.pyi
│  │     │  │     │  │  │  │  └─ wrappers_pb2.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ jinja2/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _compat.pyi
│  │     │  │     │  │  │  ├─ _stringdefs.pyi
│  │     │  │     │  │  │  ├─ bccache.pyi
│  │     │  │     │  │  │  ├─ compiler.pyi
│  │     │  │     │  │  │  ├─ constants.pyi
│  │     │  │     │  │  │  ├─ debug.pyi
│  │     │  │     │  │  │  ├─ defaults.pyi
│  │     │  │     │  │  │  ├─ environment.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ ext.pyi
│  │     │  │     │  │  │  ├─ filters.pyi
│  │     │  │     │  │  │  ├─ lexer.pyi
│  │     │  │     │  │  │  ├─ loaders.pyi
│  │     │  │     │  │  │  ├─ meta.pyi
│  │     │  │     │  │  │  ├─ nodes.pyi
│  │     │  │     │  │  │  ├─ optimizer.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ runtime.pyi
│  │     │  │     │  │  │  ├─ sandbox.pyi
│  │     │  │     │  │  │  ├─ tests.pyi
│  │     │  │     │  │  │  ├─ utils.pyi
│  │     │  │     │  │  │  └─ visitor.pyi
│  │     │  │     │  │  ├─ markdown/
│  │     │  │     │  │  │  ├─ extensions/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ abbr.pyi
│  │     │  │     │  │  │  │  ├─ admonition.pyi
│  │     │  │     │  │  │  │  ├─ attr_list.pyi
│  │     │  │     │  │  │  │  ├─ codehilite.pyi
│  │     │  │     │  │  │  │  ├─ def_list.pyi
│  │     │  │     │  │  │  │  ├─ extra.pyi
│  │     │  │     │  │  │  │  ├─ fenced_code.pyi
│  │     │  │     │  │  │  │  ├─ footnotes.pyi
│  │     │  │     │  │  │  │  ├─ legacy_attrs.pyi
│  │     │  │     │  │  │  │  ├─ legacy_em.pyi
│  │     │  │     │  │  │  │  ├─ md_in_html.pyi
│  │     │  │     │  │  │  │  ├─ meta.pyi
│  │     │  │     │  │  │  │  ├─ nl2br.pyi
│  │     │  │     │  │  │  │  ├─ sane_lists.pyi
│  │     │  │     │  │  │  │  ├─ smarty.pyi
│  │     │  │     │  │  │  │  ├─ tables.pyi
│  │     │  │     │  │  │  │  ├─ toc.pyi
│  │     │  │     │  │  │  │  └─ wikilinks.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ __meta__.pyi
│  │     │  │     │  │  │  ├─ blockparser.pyi
│  │     │  │     │  │  │  ├─ blockprocessors.pyi
│  │     │  │     │  │  │  ├─ core.pyi
│  │     │  │     │  │  │  ├─ inlinepatterns.pyi
│  │     │  │     │  │  │  ├─ pep562.pyi
│  │     │  │     │  │  │  ├─ postprocessors.pyi
│  │     │  │     │  │  │  ├─ preprocessors.pyi
│  │     │  │     │  │  │  ├─ serializers.pyi
│  │     │  │     │  │  │  ├─ treeprocessors.pyi
│  │     │  │     │  │  │  └─ util.pyi
│  │     │  │     │  │  ├─ markupsafe/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _compat.pyi
│  │     │  │     │  │  │  ├─ _constants.pyi
│  │     │  │     │  │  │  ├─ _native.pyi
│  │     │  │     │  │  │  └─ _speedups.pyi
│  │     │  │     │  │  ├─ maxminddb/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ compat.pyi
│  │     │  │     │  │  │  ├─ const.pyi
│  │     │  │     │  │  │  ├─ decoder.pyi
│  │     │  │     │  │  │  ├─ errors.pyi
│  │     │  │     │  │  │  ├─ extension.pyi
│  │     │  │     │  │  │  └─ reader.pyi
│  │     │  │     │  │  ├─ nmap/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ nmap.pyi
│  │     │  │     │  │  ├─ paramiko/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _version.pyi
│  │     │  │     │  │  │  ├─ _winapi.pyi
│  │     │  │     │  │  │  ├─ agent.pyi
│  │     │  │     │  │  │  ├─ auth_handler.pyi
│  │     │  │     │  │  │  ├─ ber.pyi
│  │     │  │     │  │  │  ├─ buffered_pipe.pyi
│  │     │  │     │  │  │  ├─ channel.pyi
│  │     │  │     │  │  │  ├─ client.pyi
│  │     │  │     │  │  │  ├─ common.pyi
│  │     │  │     │  │  │  ├─ compress.pyi
│  │     │  │     │  │  │  ├─ config.pyi
│  │     │  │     │  │  │  ├─ dsskey.pyi
│  │     │  │     │  │  │  ├─ ecdsakey.pyi
│  │     │  │     │  │  │  ├─ ed25519key.pyi
│  │     │  │     │  │  │  ├─ file.pyi
│  │     │  │     │  │  │  ├─ hostkeys.pyi
│  │     │  │     │  │  │  ├─ kex_curve25519.pyi
│  │     │  │     │  │  │  ├─ kex_ecdh_nist.pyi
│  │     │  │     │  │  │  ├─ kex_gex.pyi
│  │     │  │     │  │  │  ├─ kex_group1.pyi
│  │     │  │     │  │  │  ├─ kex_group14.pyi
│  │     │  │     │  │  │  ├─ kex_group16.pyi
│  │     │  │     │  │  │  ├─ kex_gss.pyi
│  │     │  │     │  │  │  ├─ message.pyi
│  │     │  │     │  │  │  ├─ packet.pyi
│  │     │  │     │  │  │  ├─ pipe.pyi
│  │     │  │     │  │  │  ├─ pkey.pyi
│  │     │  │     │  │  │  ├─ primes.pyi
│  │     │  │     │  │  │  ├─ proxy.pyi
│  │     │  │     │  │  │  ├─ py3compat.pyi
│  │     │  │     │  │  │  ├─ rsakey.pyi
│  │     │  │     │  │  │  ├─ server.pyi
│  │     │  │     │  │  │  ├─ sftp_attr.pyi
│  │     │  │     │  │  │  ├─ sftp_client.pyi
│  │     │  │     │  │  │  ├─ sftp_file.pyi
│  │     │  │     │  │  │  ├─ sftp_handle.pyi
│  │     │  │     │  │  │  ├─ sftp_server.pyi
│  │     │  │     │  │  │  ├─ sftp_si.pyi
│  │     │  │     │  │  │  ├─ sftp.pyi
│  │     │  │     │  │  │  ├─ ssh_exception.pyi
│  │     │  │     │  │  │  ├─ ssh_gss.pyi
│  │     │  │     │  │  │  ├─ transport.pyi
│  │     │  │     │  │  │  ├─ util.pyi
│  │     │  │     │  │  │  └─ win_pageant.pyi
│  │     │  │     │  │  ├─ pymysql/
│  │     │  │     │  │  │  ├─ constants/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ CLIENT.pyi
│  │     │  │     │  │  │  │  ├─ COMMAND.pyi
│  │     │  │     │  │  │  │  ├─ ER.pyi
│  │     │  │     │  │  │  │  ├─ FIELD_TYPE.pyi
│  │     │  │     │  │  │  │  ├─ FLAG.pyi
│  │     │  │     │  │  │  │  └─ SERVER_STATUS.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ charset.pyi
│  │     │  │     │  │  │  ├─ connections.pyi
│  │     │  │     │  │  │  ├─ converters.pyi
│  │     │  │     │  │  │  ├─ cursors.pyi
│  │     │  │     │  │  │  ├─ err.pyi
│  │     │  │     │  │  │  ├─ times.pyi
│  │     │  │     │  │  │  └─ util.pyi
│  │     │  │     │  │  ├─ pynamodb/
│  │     │  │     │  │  │  ├─ connection/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ base.pyi
│  │     │  │     │  │  │  │  ├─ table.pyi
│  │     │  │     │  │  │  │  └─ util.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ attributes.pyi
│  │     │  │     │  │  │  ├─ constants.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ indexes.pyi
│  │     │  │     │  │  │  ├─ models.pyi
│  │     │  │     │  │  │  ├─ settings.pyi
│  │     │  │     │  │  │  ├─ throttle.pyi
│  │     │  │     │  │  │  └─ types.pyi
│  │     │  │     │  │  ├─ pytz/
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ pyVmomi/
│  │     │  │     │  │  │  ├─ vim/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ event.pyi
│  │     │  │     │  │  │  │  ├─ fault.pyi
│  │     │  │     │  │  │  │  ├─ option.pyi
│  │     │  │     │  │  │  │  └─ view.pyi
│  │     │  │     │  │  │  ├─ vmodl/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ fault.pyi
│  │     │  │     │  │  │  │  └─ query.pyi
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ redis/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ client.pyi
│  │     │  │     │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ requests/
│  │     │  │     │  │  │  ├─ packages/
│  │     │  │     │  │  │  │  ├─ urllib3/
│  │     │  │     │  │  │  │  │  ├─ contrib/
│  │     │  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  │  │  ├─ packages/
│  │     │  │     │  │  │  │  │  │  ├─ ssl_match_hostname/
│  │     │  │     │  │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  │  └─ _implementation.pyi
│  │     │  │     │  │  │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  │  │  ├─ util/
│  │     │  │     │  │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  │  │  │  ├─ request.pyi
│  │     │  │     │  │  │  │  │  │  ├─ response.pyi
│  │     │  │     │  │  │  │  │  │  ├─ retry.pyi
│  │     │  │     │  │  │  │  │  │  ├─ ssl_.pyi
│  │     │  │     │  │  │  │  │  │  ├─ timeout.pyi
│  │     │  │     │  │  │  │  │  │  └─ url.pyi
│  │     │  │     │  │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  │  ├─ _collections.pyi
│  │     │  │     │  │  │  │  │  ├─ connection.pyi
│  │     │  │     │  │  │  │  │  ├─ connectionpool.pyi
│  │     │  │     │  │  │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  │  │  ├─ fields.pyi
│  │     │  │     │  │  │  │  │  ├─ filepost.pyi
│  │     │  │     │  │  │  │  │  ├─ poolmanager.pyi
│  │     │  │     │  │  │  │  │  ├─ request.pyi
│  │     │  │     │  │  │  │  │  └─ response.pyi
│  │     │  │     │  │  │  │  └─ __init__.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ adapters.pyi
│  │     │  │     │  │  │  ├─ api.pyi
│  │     │  │     │  │  │  ├─ auth.pyi
│  │     │  │     │  │  │  ├─ compat.pyi
│  │     │  │     │  │  │  ├─ cookies.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ hooks.pyi
│  │     │  │     │  │  │  ├─ models.pyi
│  │     │  │     │  │  │  ├─ sessions.pyi
│  │     │  │     │  │  │  ├─ status_codes.pyi
│  │     │  │     │  │  │  ├─ structures.pyi
│  │     │  │     │  │  │  └─ utils.pyi
│  │     │  │     │  │  ├─ retry/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  └─ api.pyi
│  │     │  │     │  │  ├─ simplejson/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ decoder.pyi
│  │     │  │     │  │  │  ├─ encoder.pyi
│  │     │  │     │  │  │  └─ scanner.pyi
│  │     │  │     │  │  ├─ slugify/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ slugify.pyi
│  │     │  │     │  │  │  └─ special.pyi
│  │     │  │     │  │  ├─ tzlocal/
│  │     │  │     │  │  │  └─ __init__.pyi
│  │     │  │     │  │  ├─ werkzeug/
│  │     │  │     │  │  │  ├─ contrib/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ atom.pyi
│  │     │  │     │  │  │  │  ├─ cache.pyi
│  │     │  │     │  │  │  │  ├─ fixers.pyi
│  │     │  │     │  │  │  │  ├─ iterio.pyi
│  │     │  │     │  │  │  │  ├─ jsrouting.pyi
│  │     │  │     │  │  │  │  ├─ limiter.pyi
│  │     │  │     │  │  │  │  ├─ lint.pyi
│  │     │  │     │  │  │  │  ├─ profiler.pyi
│  │     │  │     │  │  │  │  ├─ securecookie.pyi
│  │     │  │     │  │  │  │  ├─ sessions.pyi
│  │     │  │     │  │  │  │  ├─ testtools.pyi
│  │     │  │     │  │  │  │  └─ wrappers.pyi
│  │     │  │     │  │  │  ├─ debug/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ console.pyi
│  │     │  │     │  │  │  │  ├─ repr.pyi
│  │     │  │     │  │  │  │  └─ tbtools.pyi
│  │     │  │     │  │  │  ├─ middleware/
│  │     │  │     │  │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  │  ├─ dispatcher.pyi
│  │     │  │     │  │  │  │  ├─ http_proxy.pyi
│  │     │  │     │  │  │  │  ├─ lint.pyi
│  │     │  │     │  │  │  │  ├─ profiler.pyi
│  │     │  │     │  │  │  │  ├─ proxy_fix.pyi
│  │     │  │     │  │  │  │  └─ shared_data.pyi
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ _compat.pyi
│  │     │  │     │  │  │  ├─ _internal.pyi
│  │     │  │     │  │  │  ├─ _reloader.pyi
│  │     │  │     │  │  │  ├─ datastructures.pyi
│  │     │  │     │  │  │  ├─ exceptions.pyi
│  │     │  │     │  │  │  ├─ filesystem.pyi
│  │     │  │     │  │  │  ├─ formparser.pyi
│  │     │  │     │  │  │  ├─ http.pyi
│  │     │  │     │  │  │  ├─ local.pyi
│  │     │  │     │  │  │  ├─ posixemulation.pyi
│  │     │  │     │  │  │  ├─ routing.pyi
│  │     │  │     │  │  │  ├─ script.pyi
│  │     │  │     │  │  │  ├─ security.pyi
│  │     │  │     │  │  │  ├─ serving.pyi
│  │     │  │     │  │  │  ├─ test.pyi
│  │     │  │     │  │  │  ├─ testapp.pyi
│  │     │  │     │  │  │  ├─ urls.pyi
│  │     │  │     │  │  │  ├─ useragents.pyi
│  │     │  │     │  │  │  ├─ utils.pyi
│  │     │  │     │  │  │  ├─ wrappers.pyi
│  │     │  │     │  │  │  └─ wsgi.pyi
│  │     │  │     │  │  ├─ yaml/
│  │     │  │     │  │  │  ├─ __init__.pyi
│  │     │  │     │  │  │  ├─ composer.pyi
│  │     │  │     │  │  │  ├─ constructor.pyi
│  │     │  │     │  │  │  ├─ cyaml.pyi
│  │     │  │     │  │  │  ├─ dumper.pyi
│  │     │  │     │  │  │  ├─ emitter.pyi
│  │     │  │     │  │  │  ├─ error.pyi
│  │     │  │     │  │  │  ├─ events.pyi
│  │     │  │     │  │  │  ├─ loader.pyi
│  │     │  │     │  │  │  ├─ nodes.pyi
│  │     │  │     │  │  │  ├─ parser.pyi
│  │     │  │     │  │  │  ├─ reader.pyi
│  │     │  │     │  │  │  ├─ representer.pyi
│  │     │  │     │  │  │  ├─ resolver.pyi
│  │     │  │     │  │  │  ├─ scanner.pyi
│  │     │  │     │  │  │  ├─ serializer.pyi
│  │     │  │     │  │  │  └─ tokens.pyi
│  │     │  │     │  │  ├─ backports_abc.pyi
│  │     │  │     │  │  ├─ certifi.pyi
│  │     │  │     │  │  ├─ croniter.pyi
│  │     │  │     │  │  ├─ dateparser.pyi
│  │     │  │     │  │  ├─ decorator.pyi
│  │     │  │     │  │  ├─ first.pyi
│  │     │  │     │  │  ├─ gflags.pyi
│  │     │  │     │  │  ├─ itsdangerous.pyi
│  │     │  │     │  │  ├─ mock.pyi
│  │     │  │     │  │  ├─ mypy_extensions.pyi
│  │     │  │     │  │  ├─ polib.pyi
│  │     │  │     │  │  ├─ pycurl.pyi
│  │     │  │     │  │  ├─ pyre_extensions.pyi
│  │     │  │     │  │  ├─ singledispatch.pyi
│  │     │  │     │  │  ├─ tabulate.pyi
│  │     │  │     │  │  ├─ termcolor.pyi
│  │     │  │     │  │  ├─ toml.pyi
│  │     │  │     │  │  ├─ typing_extensions.pyi
│  │     │  │     │  │  └─ ujson.pyi
│  │     │  │     │  └─ 3/
│  │     │  │     │     ├─ aiofiles/
│  │     │  │     │     │  ├─ threadpool/
│  │     │  │     │     │  │  ├─ __init__.pyi
│  │     │  │     │     │  │  ├─ binary.pyi
│  │     │  │     │     │  │  └─ text.pyi
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  ├─ base.pyi
│  │     │  │     │     │  └─ os.pyi
│  │     │  │     │     ├─ docutils/
│  │     │  │     │     │  ├─ parsers/
│  │     │  │     │     │  │  ├─ rst/
│  │     │  │     │     │  │  │  ├─ __init__.pyi
│  │     │  │     │     │  │  │  ├─ nodes.pyi
│  │     │  │     │     │  │  │  ├─ roles.pyi
│  │     │  │     │     │  │  │  └─ states.pyi
│  │     │  │     │     │  │  └─ __init__.pyi
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  ├─ examples.pyi
│  │     │  │     │     │  └─ nodes.pyi
│  │     │  │     │     ├─ filelock/
│  │     │  │     │     │  └─ __init__.pyi
│  │     │  │     │     ├─ freezegun/
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  └─ api.pyi
│  │     │  │     │     ├─ jwt/
│  │     │  │     │     │  ├─ contrib/
│  │     │  │     │     │  │  ├─ algorithms/
│  │     │  │     │     │  │  │  ├─ __init__.pyi
│  │     │  │     │     │  │  │  ├─ py_ecdsa.pyi
│  │     │  │     │     │  │  │  └─ pycrypto.pyi
│  │     │  │     │     │  │  └─ __init__.pyi
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  └─ algorithms.pyi
│  │     │  │     │     ├─ pkg_resources/
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  └─ py31compat.pyi
│  │     │  │     │     ├─ pyrfc3339/
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  ├─ generator.pyi
│  │     │  │     │     │  ├─ parser.pyi
│  │     │  │     │     │  └─ utils.pyi
│  │     │  │     │     ├─ six/
│  │     │  │     │     │  ├─ moves/
│  │     │  │     │     │  │  ├─ urllib/
│  │     │  │     │     │  │  │  ├─ __init__.pyi
│  │     │  │     │     │  │  │  ├─ error.pyi
│  │     │  │     │     │  │  │  ├─ parse.pyi
│  │     │  │     │     │  │  │  ├─ request.pyi
│  │     │  │     │     │  │  │  ├─ response.pyi
│  │     │  │     │     │  │  │  └─ robotparser.pyi
│  │     │  │     │     │  │  ├─ __init__.pyi
│  │     │  │     │     │  │  ├─ _dummy_thread.pyi
│  │     │  │     │     │  │  ├─ _thread.pyi
│  │     │  │     │     │  │  ├─ BaseHTTPServer.pyi
│  │     │  │     │     │  │  ├─ builtins.pyi
│  │     │  │     │     │  │  ├─ CGIHTTPServer.pyi
│  │     │  │     │     │  │  ├─ collections_abc.pyi
│  │     │  │     │     │  │  ├─ configparser.pyi
│  │     │  │     │     │  │  ├─ cPickle.pyi
│  │     │  │     │     │  │  ├─ email_mime_base.pyi
│  │     │  │     │     │  │  ├─ email_mime_multipart.pyi
│  │     │  │     │     │  │  ├─ email_mime_nonmultipart.pyi
│  │     │  │     │     │  │  ├─ email_mime_text.pyi
│  │     │  │     │     │  │  ├─ html_entities.pyi
│  │     │  │     │     │  │  ├─ html_parser.pyi
│  │     │  │     │     │  │  ├─ http_client.pyi
│  │     │  │     │     │  │  ├─ http_cookiejar.pyi
│  │     │  │     │     │  │  ├─ http_cookies.pyi
│  │     │  │     │     │  │  ├─ queue.pyi
│  │     │  │     │     │  │  ├─ reprlib.pyi
│  │     │  │     │     │  │  ├─ SimpleHTTPServer.pyi
│  │     │  │     │     │  │  ├─ socketserver.pyi
│  │     │  │     │     │  │  ├─ tkinter_commondialog.pyi
│  │     │  │     │     │  │  ├─ tkinter_constants.pyi
│  │     │  │     │     │  │  ├─ tkinter_dialog.pyi
│  │     │  │     │     │  │  ├─ tkinter_filedialog.pyi
│  │     │  │     │     │  │  ├─ tkinter_tkfiledialog.pyi
│  │     │  │     │     │  │  ├─ tkinter_ttk.pyi
│  │     │  │     │     │  │  ├─ tkinter.pyi
│  │     │  │     │     │  │  ├─ urllib_error.pyi
│  │     │  │     │     │  │  ├─ urllib_parse.pyi
│  │     │  │     │     │  │  ├─ urllib_request.pyi
│  │     │  │     │     │  │  ├─ urllib_response.pyi
│  │     │  │     │     │  │  └─ urllib_robotparser.pyi
│  │     │  │     │     │  └─ __init__.pyi
│  │     │  │     │     ├─ typed_ast/
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  ├─ ast27.pyi
│  │     │  │     │     │  ├─ ast3.pyi
│  │     │  │     │     │  └─ conversions.pyi
│  │     │  │     │     ├─ waitress/
│  │     │  │     │     │  ├─ __init__.pyi
│  │     │  │     │     │  ├─ adjustments.pyi
│  │     │  │     │     │  ├─ buffers.pyi
│  │     │  │     │     │  ├─ channel.pyi
│  │     │  │     │     │  ├─ compat.pyi
│  │     │  │     │     │  ├─ parser.pyi
│  │     │  │     │     │  ├─ proxy_headers.pyi
│  │     │  │     │     │  ├─ receiver.pyi
│  │     │  │     │     │  ├─ rfc7230.pyi
│  │     │  │     │     │  ├─ runner.pyi
│  │     │  │     │     │  ├─ server.pyi
│  │     │  │     │     │  ├─ task.pyi
│  │     │  │     │     │  ├─ trigger.pyi
│  │     │  │     │     │  ├─ utilities.pyi
│  │     │  │     │     │  └─ wasyncore.pyi
│  │     │  │     │     ├─ contextvars.pyi
│  │     │  │     │     ├─ dataclasses.pyi
│  │     │  │     │     ├─ frozendict.pyi
│  │     │  │     │     └─ orjson.pyi
│  │     │  │     └─ LICENSE
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ _compatibility.py
│  │     │  ├─ cache.py
│  │     │  ├─ common.py
│  │     │  ├─ debug.py
│  │     │  ├─ file_io.py
│  │     │  ├─ parser_utils.py
│  │     │  ├─ settings.py
│  │     │  └─ utils.py
│  │     ├─ jedi-0.19.2.dist-info/
│  │     │  ├─ AUTHORS.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ jinja2/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _identifier.cpython-312.pyc
│  │     │  │  ├─ async_utils.cpython-312.pyc
│  │     │  │  ├─ bccache.cpython-312.pyc
│  │     │  │  ├─ compiler.cpython-312.pyc
│  │     │  │  ├─ constants.cpython-312.pyc
│  │     │  │  ├─ debug.cpython-312.pyc
│  │     │  │  ├─ defaults.cpython-312.pyc
│  │     │  │  ├─ environment.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ ext.cpython-312.pyc
│  │     │  │  ├─ filters.cpython-312.pyc
│  │     │  │  ├─ idtracking.cpython-312.pyc
│  │     │  │  ├─ lexer.cpython-312.pyc
│  │     │  │  ├─ loaders.cpython-312.pyc
│  │     │  │  ├─ meta.cpython-312.pyc
│  │     │  │  ├─ nativetypes.cpython-312.pyc
│  │     │  │  ├─ nodes.cpython-312.pyc
│  │     │  │  ├─ optimizer.cpython-312.pyc
│  │     │  │  ├─ parser.cpython-312.pyc
│  │     │  │  ├─ runtime.cpython-312.pyc
│  │     │  │  ├─ sandbox.cpython-312.pyc
│  │     │  │  ├─ tests.cpython-312.pyc
│  │     │  │  ├─ utils.cpython-312.pyc
│  │     │  │  └─ visitor.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ _identifier.py
│  │     │  ├─ async_utils.py
│  │     │  ├─ bccache.py
│  │     │  ├─ compiler.py
│  │     │  ├─ constants.py
│  │     │  ├─ debug.py
│  │     │  ├─ defaults.py
│  │     │  ├─ environment.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ ext.py
│  │     │  ├─ filters.py
│  │     │  ├─ idtracking.py
│  │     │  ├─ lexer.py
│  │     │  ├─ loaders.py
│  │     │  ├─ meta.py
│  │     │  ├─ nativetypes.py
│  │     │  ├─ nodes.py
│  │     │  ├─ optimizer.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ runtime.py
│  │     │  ├─ sandbox.py
│  │     │  ├─ tests.py
│  │     │  ├─ utils.py
│  │     │  └─ visitor.py
│  │     ├─ jinja2-3.1.6.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jupyter_client/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ adapter.cpython-312.pyc
│  │     │  │  ├─ channels.cpython-312.pyc
│  │     │  │  ├─ channelsabc.cpython-312.pyc
│  │     │  │  ├─ client.cpython-312.pyc
│  │     │  │  ├─ clientabc.cpython-312.pyc
│  │     │  │  ├─ connect.cpython-312.pyc
│  │     │  │  ├─ consoleapp.cpython-312.pyc
│  │     │  │  ├─ jsonutil.cpython-312.pyc
│  │     │  │  ├─ kernelapp.cpython-312.pyc
│  │     │  │  ├─ kernelspec.cpython-312.pyc
│  │     │  │  ├─ kernelspecapp.cpython-312.pyc
│  │     │  │  ├─ launcher.cpython-312.pyc
│  │     │  │  ├─ localinterfaces.cpython-312.pyc
│  │     │  │  ├─ manager.cpython-312.pyc
│  │     │  │  ├─ managerabc.cpython-312.pyc
│  │     │  │  ├─ multikernelmanager.cpython-312.pyc
│  │     │  │  ├─ restarter.cpython-312.pyc
│  │     │  │  ├─ runapp.cpython-312.pyc
│  │     │  │  ├─ session.cpython-312.pyc
│  │     │  │  ├─ threaded.cpython-312.pyc
│  │     │  │  ├─ utils.cpython-312.pyc
│  │     │  │  └─ win_interrupt.cpython-312.pyc
│  │     │  ├─ asynchronous/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ client.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ client.py
│  │     │  ├─ blocking/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ client.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ client.py
│  │     │  ├─ ioloop/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ manager.cpython-312.pyc
│  │     │  │  │  └─ restarter.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ manager.py
│  │     │  │  └─ restarter.py
│  │     │  ├─ provisioning/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ factory.cpython-312.pyc
│  │     │  │  │  ├─ local_provisioner.cpython-312.pyc
│  │     │  │  │  └─ provisioner_base.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ factory.py
│  │     │  │  ├─ local_provisioner.py
│  │     │  │  └─ provisioner_base.py
│  │     │  ├─ ssh/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ forward.cpython-312.pyc
│  │     │  │  │  └─ tunnel.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ forward.py
│  │     │  │  └─ tunnel.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  ├─ adapter.py
│  │     │  ├─ channels.py
│  │     │  ├─ channelsabc.py
│  │     │  ├─ client.py
│  │     │  ├─ clientabc.py
│  │     │  ├─ connect.py
│  │     │  ├─ consoleapp.py
│  │     │  ├─ jsonutil.py
│  │     │  ├─ kernelapp.py
│  │     │  ├─ kernelspec.py
│  │     │  ├─ kernelspecapp.py
│  │     │  ├─ launcher.py
│  │     │  ├─ localinterfaces.py
│  │     │  ├─ manager.py
│  │     │  ├─ managerabc.py
│  │     │  ├─ multikernelmanager.py
│  │     │  ├─ py.typed
│  │     │  ├─ restarter.py
│  │     │  ├─ runapp.py
│  │     │  ├─ session.py
│  │     │  ├─ threaded.py
│  │     │  ├─ utils.py
│  │     │  └─ win_interrupt.py
│  │     ├─ jupyter_client-8.6.3.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jupyter_core/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ application.cpython-312.pyc
│  │     │  │  ├─ command.cpython-312.pyc
│  │     │  │  ├─ migrate.cpython-312.pyc
│  │     │  │  ├─ paths.cpython-312.pyc
│  │     │  │  ├─ troubleshoot.cpython-312.pyc
│  │     │  │  └─ version.cpython-312.pyc
│  │     │  ├─ utils/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ application.py
│  │     │  ├─ command.py
│  │     │  ├─ migrate.py
│  │     │  ├─ paths.py
│  │     │  ├─ py.typed
│  │     │  ├─ troubleshoot.py
│  │     │  └─ version.py
│  │     ├─ jupyter_core-5.8.1.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jupyter_leaflet/
│  │     │  ├─ __pycache__/
│  │     │  │  └─ __init__.cpython-312.pyc
│  │     │  └─ __init__.py
│  │     ├─ jupyter_leaflet-0.20.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ jupyterlab_widgets/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ _version.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ _version.py
│  │     │  └─ .gitignore
│  │     ├─ jupyterlab_widgets-3.0.15.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ kiwisolver/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ exceptions.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ _cext.cp312-win_amd64.pyd
│  │     │  ├─ _cext.pyi
│  │     │  ├─ exceptions.py
│  │     │  └─ py.typed
│  │     ├─ kiwisolver-1.4.8.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ libfuturize/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ fixer_util.cpython-312.pyc
│  │     │  │  └─ main.cpython-312.pyc
│  │     │  ├─ fixes/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ fix_absolute_import.cpython-312.pyc
│  │     │  │  │  ├─ fix_add__future__imports_except_unicode_literals.cpython-312.pyc
│  │     │  │  │  ├─ fix_basestring.cpython-312.pyc
│  │     │  │  │  ├─ fix_bytes.cpython-312.pyc
│  │     │  │  │  ├─ fix_cmp.cpython-312.pyc
│  │     │  │  │  ├─ fix_division_safe.cpython-312.pyc
│  │     │  │  │  ├─ fix_division.cpython-312.pyc
│  │     │  │  │  ├─ fix_execfile.cpython-312.pyc
│  │     │  │  │  ├─ fix_future_builtins.cpython-312.pyc
│  │     │  │  │  ├─ fix_future_standard_library_urllib.cpython-312.pyc
│  │     │  │  │  ├─ fix_future_standard_library.cpython-312.pyc
│  │     │  │  │  ├─ fix_input.cpython-312.pyc
│  │     │  │  │  ├─ fix_metaclass.cpython-312.pyc
│  │     │  │  │  ├─ fix_next_call.cpython-312.pyc
│  │     │  │  │  ├─ fix_object.cpython-312.pyc
│  │     │  │  │  ├─ fix_oldstr_wrap.cpython-312.pyc
│  │     │  │  │  ├─ fix_order___future__imports.cpython-312.pyc
│  │     │  │  │  ├─ fix_print_with_import.cpython-312.pyc
│  │     │  │  │  ├─ fix_print.cpython-312.pyc
│  │     │  │  │  ├─ fix_raise.cpython-312.pyc
│  │     │  │  │  ├─ fix_remove_old__future__imports.cpython-312.pyc
│  │     │  │  │  ├─ fix_unicode_keep_u.cpython-312.pyc
│  │     │  │  │  ├─ fix_unicode_literals_import.cpython-312.pyc
│  │     │  │  │  ├─ fix_UserDict.cpython-312.pyc
│  │     │  │  │  └─ fix_xrange_with_import.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ fix_absolute_import.py
│  │     │  │  ├─ fix_add__future__imports_except_unicode_literals.py
│  │     │  │  ├─ fix_basestring.py
│  │     │  │  ├─ fix_bytes.py
│  │     │  │  ├─ fix_cmp.py
│  │     │  │  ├─ fix_division_safe.py
│  │     │  │  ├─ fix_division.py
│  │     │  │  ├─ fix_execfile.py
│  │     │  │  ├─ fix_future_builtins.py
│  │     │  │  ├─ fix_future_standard_library_urllib.py
│  │     │  │  ├─ fix_future_standard_library.py
│  │     │  │  ├─ fix_input.py
│  │     │  │  ├─ fix_metaclass.py
│  │     │  │  ├─ fix_next_call.py
│  │     │  │  ├─ fix_object.py
│  │     │  │  ├─ fix_oldstr_wrap.py
│  │     │  │  ├─ fix_order___future__imports.py
│  │     │  │  ├─ fix_print_with_import.py
│  │     │  │  ├─ fix_print.py
│  │     │  │  ├─ fix_raise.py
│  │     │  │  ├─ fix_remove_old__future__imports.py
│  │     │  │  ├─ fix_unicode_keep_u.py
│  │     │  │  ├─ fix_unicode_literals_import.py
│  │     │  │  ├─ fix_UserDict.py
│  │     │  │  └─ fix_xrange_with_import.py
│  │     │  ├─ __init__.py
│  │     │  ├─ fixer_util.py
│  │     │  └─ main.py
│  │     ├─ libpasteurize/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ main.cpython-312.pyc
│  │     │  ├─ fixes/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ feature_base.cpython-312.pyc
│  │     │  │  │  ├─ fix_add_all__future__imports.cpython-312.pyc
│  │     │  │  │  ├─ fix_add_all_future_builtins.cpython-312.pyc
│  │     │  │  │  ├─ fix_add_future_standard_library_import.cpython-312.pyc
│  │     │  │  │  ├─ fix_annotations.cpython-312.pyc
│  │     │  │  │  ├─ fix_division.cpython-312.pyc
│  │     │  │  │  ├─ fix_features.cpython-312.pyc
│  │     │  │  │  ├─ fix_fullargspec.cpython-312.pyc
│  │     │  │  │  ├─ fix_future_builtins.cpython-312.pyc
│  │     │  │  │  ├─ fix_getcwd.cpython-312.pyc
│  │     │  │  │  ├─ fix_imports.cpython-312.pyc
│  │     │  │  │  ├─ fix_imports2.cpython-312.pyc
│  │     │  │  │  ├─ fix_kwargs.cpython-312.pyc
│  │     │  │  │  ├─ fix_memoryview.cpython-312.pyc
│  │     │  │  │  ├─ fix_metaclass.cpython-312.pyc
│  │     │  │  │  ├─ fix_newstyle.cpython-312.pyc
│  │     │  │  │  ├─ fix_next.cpython-312.pyc
│  │     │  │  │  ├─ fix_printfunction.cpython-312.pyc
│  │     │  │  │  ├─ fix_raise_.cpython-312.pyc
│  │     │  │  │  ├─ fix_raise.cpython-312.pyc
│  │     │  │  │  ├─ fix_throw.cpython-312.pyc
│  │     │  │  │  └─ fix_unpacking.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ feature_base.py
│  │     │  │  ├─ fix_add_all__future__imports.py
│  │     │  │  ├─ fix_add_all_future_builtins.py
│  │     │  │  ├─ fix_add_future_standard_library_import.py
│  │     │  │  ├─ fix_annotations.py
│  │     │  │  ├─ fix_division.py
│  │     │  │  ├─ fix_features.py
│  │     │  │  ├─ fix_fullargspec.py
│  │     │  │  ├─ fix_future_builtins.py
│  │     │  │  ├─ fix_getcwd.py
│  │     │  │  ├─ fix_imports.py
│  │     │  │  ├─ fix_imports2.py
│  │     │  │  ├─ fix_kwargs.py
│  │     │  │  ├─ fix_memoryview.py
│  │     │  │  ├─ fix_metaclass.py
│  │     │  │  ├─ fix_newstyle.py
│  │     │  │  ├─ fix_next.py
│  │     │  │  ├─ fix_printfunction.py
│  │     │  │  ├─ fix_raise_.py
│  │     │  │  ├─ fix_raise.py
│  │     │  │  ├─ fix_throw.py
│  │     │  │  └─ fix_unpacking.py
│  │     │  ├─ __init__.py
│  │     │  └─ main.py
│  │     ├─ markupsafe/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  └─ _native.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ _native.py
│  │     │  ├─ _speedups.c
│  │     │  ├─ _speedups.cp312-win_amd64.pyd
│  │     │  ├─ _speedups.pyi
│  │     │  └─ py.typed
│  │     ├─ MarkupSafe-3.0.2.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ matplotlib/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _afm.cpython-312.pyc
│  │     │  │  ├─ _animation_data.cpython-312.pyc
│  │     │  │  ├─ _blocking_input.cpython-312.pyc
│  │     │  │  ├─ _cm_bivar.cpython-312.pyc
│  │     │  │  ├─ _cm_listed.cpython-312.pyc
│  │     │  │  ├─ _cm_multivar.cpython-312.pyc
│  │     │  │  ├─ _cm.cpython-312.pyc
│  │     │  │  ├─ _color_data.cpython-312.pyc
│  │     │  │  ├─ _constrained_layout.cpython-312.pyc
│  │     │  │  ├─ _docstring.cpython-312.pyc
│  │     │  │  ├─ _enums.cpython-312.pyc
│  │     │  │  ├─ _fontconfig_pattern.cpython-312.pyc
│  │     │  │  ├─ _internal_utils.cpython-312.pyc
│  │     │  │  ├─ _layoutgrid.cpython-312.pyc
│  │     │  │  ├─ _mathtext_data.cpython-312.pyc
│  │     │  │  ├─ _mathtext.cpython-312.pyc
│  │     │  │  ├─ _pylab_helpers.cpython-312.pyc
│  │     │  │  ├─ _text_helpers.cpython-312.pyc
│  │     │  │  ├─ _tight_bbox.cpython-312.pyc
│  │     │  │  ├─ _tight_layout.cpython-312.pyc
│  │     │  │  ├─ _type1font.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ animation.cpython-312.pyc
│  │     │  │  ├─ artist.cpython-312.pyc
│  │     │  │  ├─ axis.cpython-312.pyc
│  │     │  │  ├─ backend_bases.cpython-312.pyc
│  │     │  │  ├─ backend_managers.cpython-312.pyc
│  │     │  │  ├─ backend_tools.cpython-312.pyc
│  │     │  │  ├─ bezier.cpython-312.pyc
│  │     │  │  ├─ category.cpython-312.pyc
│  │     │  │  ├─ cbook.cpython-312.pyc
│  │     │  │  ├─ cm.cpython-312.pyc
│  │     │  │  ├─ collections.cpython-312.pyc
│  │     │  │  ├─ colorbar.cpython-312.pyc
│  │     │  │  ├─ colorizer.cpython-312.pyc
│  │     │  │  ├─ colors.cpython-312.pyc
│  │     │  │  ├─ container.cpython-312.pyc
│  │     │  │  ├─ contour.cpython-312.pyc
│  │     │  │  ├─ dates.cpython-312.pyc
│  │     │  │  ├─ dviread.cpython-312.pyc
│  │     │  │  ├─ figure.cpython-312.pyc
│  │     │  │  ├─ font_manager.cpython-312.pyc
│  │     │  │  ├─ gridspec.cpython-312.pyc
│  │     │  │  ├─ hatch.cpython-312.pyc
│  │     │  │  ├─ image.cpython-312.pyc
│  │     │  │  ├─ inset.cpython-312.pyc
│  │     │  │  ├─ layout_engine.cpython-312.pyc
│  │     │  │  ├─ legend_handler.cpython-312.pyc
│  │     │  │  ├─ legend.cpython-312.pyc
│  │     │  │  ├─ lines.cpython-312.pyc
│  │     │  │  ├─ markers.cpython-312.pyc
│  │     │  │  ├─ mathtext.cpython-312.pyc
│  │     │  │  ├─ mlab.cpython-312.pyc
│  │     │  │  ├─ offsetbox.cpython-312.pyc
│  │     │  │  ├─ patches.cpython-312.pyc
│  │     │  │  ├─ path.cpython-312.pyc
│  │     │  │  ├─ patheffects.cpython-312.pyc
│  │     │  │  ├─ pylab.cpython-312.pyc
│  │     │  │  ├─ pyplot.cpython-312.pyc
│  │     │  │  ├─ quiver.cpython-312.pyc
│  │     │  │  ├─ rcsetup.cpython-312.pyc
│  │     │  │  ├─ sankey.cpython-312.pyc
│  │     │  │  ├─ scale.cpython-312.pyc
│  │     │  │  ├─ spines.cpython-312.pyc
│  │     │  │  ├─ stackplot.cpython-312.pyc
│  │     │  │  ├─ streamplot.cpython-312.pyc
│  │     │  │  ├─ table.cpython-312.pyc
│  │     │  │  ├─ texmanager.cpython-312.pyc
│  │     │  │  ├─ text.cpython-312.pyc
│  │     │  │  ├─ textpath.cpython-312.pyc
│  │     │  │  ├─ ticker.cpython-312.pyc
│  │     │  │  ├─ transforms.cpython-312.pyc
│  │     │  │  ├─ typing.cpython-312.pyc
│  │     │  │  ├─ units.cpython-312.pyc
│  │     │  │  └─ widgets.cpython-312.pyc
│  │     │  ├─ _api/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ deprecation.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ deprecation.py
│  │     │  │  └─ deprecation.pyi
│  │     │  ├─ axes/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _axes.cpython-312.pyc
│  │     │  │  │  ├─ _base.cpython-312.pyc
│  │     │  │  │  └─ _secondary_axes.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _axes.py
│  │     │  │  ├─ _axes.pyi
│  │     │  │  ├─ _base.py
│  │     │  │  ├─ _base.pyi
│  │     │  │  ├─ _secondary_axes.py
│  │     │  │  └─ _secondary_axes.pyi
│  │     │  ├─ backends/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _backend_gtk.cpython-312.pyc
│  │     │  │  │  ├─ _backend_pdf_ps.cpython-312.pyc
│  │     │  │  │  ├─ _backend_tk.cpython-312.pyc
│  │     │  │  │  ├─ backend_agg.cpython-312.pyc
│  │     │  │  │  ├─ backend_cairo.cpython-312.pyc
│  │     │  │  │  ├─ backend_gtk3.cpython-312.pyc
│  │     │  │  │  ├─ backend_gtk3agg.cpython-312.pyc
│  │     │  │  │  ├─ backend_gtk3cairo.cpython-312.pyc
│  │     │  │  │  ├─ backend_gtk4.cpython-312.pyc
│  │     │  │  │  ├─ backend_gtk4agg.cpython-312.pyc
│  │     │  │  │  ├─ backend_gtk4cairo.cpython-312.pyc
│  │     │  │  │  ├─ backend_macosx.cpython-312.pyc
│  │     │  │  │  ├─ backend_mixed.cpython-312.pyc
│  │     │  │  │  ├─ backend_nbagg.cpython-312.pyc
│  │     │  │  │  ├─ backend_pdf.cpython-312.pyc
│  │     │  │  │  ├─ backend_pgf.cpython-312.pyc
│  │     │  │  │  ├─ backend_ps.cpython-312.pyc
│  │     │  │  │  ├─ backend_qt.cpython-312.pyc
│  │     │  │  │  ├─ backend_qt5.cpython-312.pyc
│  │     │  │  │  ├─ backend_qt5agg.cpython-312.pyc
│  │     │  │  │  ├─ backend_qt5cairo.cpython-312.pyc
│  │     │  │  │  ├─ backend_qtagg.cpython-312.pyc
│  │     │  │  │  ├─ backend_qtcairo.cpython-312.pyc
│  │     │  │  │  ├─ backend_svg.cpython-312.pyc
│  │     │  │  │  ├─ backend_template.cpython-312.pyc
│  │     │  │  │  ├─ backend_tkagg.cpython-312.pyc
│  │     │  │  │  ├─ backend_tkcairo.cpython-312.pyc
│  │     │  │  │  ├─ backend_webagg_core.cpython-312.pyc
│  │     │  │  │  ├─ backend_webagg.cpython-312.pyc
│  │     │  │  │  ├─ backend_wx.cpython-312.pyc
│  │     │  │  │  ├─ backend_wxagg.cpython-312.pyc
│  │     │  │  │  ├─ backend_wxcairo.cpython-312.pyc
│  │     │  │  │  ├─ qt_compat.cpython-312.pyc
│  │     │  │  │  └─ registry.cpython-312.pyc
│  │     │  │  ├─ qt_editor/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _formlayout.cpython-312.pyc
│  │     │  │  │  │  └─ figureoptions.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _formlayout.py
│  │     │  │  │  └─ figureoptions.py
│  │     │  │  ├─ web_backend/
│  │     │  │  │  ├─ css/
│  │     │  │  │  │  ├─ boilerplate.css
│  │     │  │  │  │  ├─ fbm.css
│  │     │  │  │  │  ├─ mpl.css
│  │     │  │  │  │  └─ page.css
│  │     │  │  │  ├─ js/
│  │     │  │  │  │  ├─ mpl_tornado.js
│  │     │  │  │  │  ├─ mpl.js
│  │     │  │  │  │  └─ nbagg_mpl.js
│  │     │  │  │  ├─ all_figures.html
│  │     │  │  │  ├─ ipython_inline_figure.html
│  │     │  │  │  └─ single_figure.html
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _backend_agg.cp312-win_amd64.pyd
│  │     │  │  ├─ _backend_agg.pyi
│  │     │  │  ├─ _backend_gtk.py
│  │     │  │  ├─ _backend_pdf_ps.py
│  │     │  │  ├─ _backend_tk.py
│  │     │  │  ├─ _macosx.pyi
│  │     │  │  ├─ _tkagg.cp312-win_amd64.pyd
│  │     │  │  ├─ _tkagg.pyi
│  │     │  │  ├─ backend_agg.py
│  │     │  │  ├─ backend_cairo.py
│  │     │  │  ├─ backend_gtk3.py
│  │     │  │  ├─ backend_gtk3agg.py
│  │     │  │  ├─ backend_gtk3cairo.py
│  │     │  │  ├─ backend_gtk4.py
│  │     │  │  ├─ backend_gtk4agg.py
│  │     │  │  ├─ backend_gtk4cairo.py
│  │     │  │  ├─ backend_macosx.py
│  │     │  │  ├─ backend_mixed.py
│  │     │  │  ├─ backend_nbagg.py
│  │     │  │  ├─ backend_pdf.py
│  │     │  │  ├─ backend_pgf.py
│  │     │  │  ├─ backend_ps.py
│  │     │  │  ├─ backend_qt.py
│  │     │  │  ├─ backend_qt5.py
│  │     │  │  ├─ backend_qt5agg.py
│  │     │  │  ├─ backend_qt5cairo.py
│  │     │  │  ├─ backend_qtagg.py
│  │     │  │  ├─ backend_qtcairo.py
│  │     │  │  ├─ backend_svg.py
│  │     │  │  ├─ backend_template.py
│  │     │  │  ├─ backend_tkagg.py
│  │     │  │  ├─ backend_tkcairo.py
│  │     │  │  ├─ backend_webagg_core.py
│  │     │  │  ├─ backend_webagg.py
│  │     │  │  ├─ backend_wx.py
│  │     │  │  ├─ backend_wxagg.py
│  │     │  │  ├─ backend_wxcairo.py
│  │     │  │  ├─ qt_compat.py
│  │     │  │  └─ registry.py
│  │     │  ├─ mpl-data/
│  │     │  │  ├─ fonts/
│  │     │  │  │  ├─ afm/
│  │     │  │  │  │  ├─ cmex10.afm
│  │     │  │  │  │  ├─ cmmi10.afm
│  │     │  │  │  │  ├─ cmr10.afm
│  │     │  │  │  │  ├─ cmsy10.afm
│  │     │  │  │  │  ├─ cmtt10.afm
│  │     │  │  │  │  ├─ pagd8a.afm
│  │     │  │  │  │  ├─ pagdo8a.afm
│  │     │  │  │  │  ├─ pagk8a.afm
│  │     │  │  │  │  ├─ pagko8a.afm
│  │     │  │  │  │  ├─ pbkd8a.afm
│  │     │  │  │  │  ├─ pbkdi8a.afm
│  │     │  │  │  │  ├─ pbkl8a.afm
│  │     │  │  │  │  ├─ pbkli8a.afm
│  │     │  │  │  │  ├─ pcrb8a.afm
│  │     │  │  │  │  ├─ pcrbo8a.afm
│  │     │  │  │  │  ├─ pcrr8a.afm
│  │     │  │  │  │  ├─ pcrro8a.afm
│  │     │  │  │  │  ├─ phvb8a.afm
│  │     │  │  │  │  ├─ phvb8an.afm
│  │     │  │  │  │  ├─ phvbo8a.afm
│  │     │  │  │  │  ├─ phvbo8an.afm
│  │     │  │  │  │  ├─ phvl8a.afm
│  │     │  │  │  │  ├─ phvlo8a.afm
│  │     │  │  │  │  ├─ phvr8a.afm
│  │     │  │  │  │  ├─ phvr8an.afm
│  │     │  │  │  │  ├─ phvro8a.afm
│  │     │  │  │  │  ├─ phvro8an.afm
│  │     │  │  │  │  ├─ pncb8a.afm
│  │     │  │  │  │  ├─ pncbi8a.afm
│  │     │  │  │  │  ├─ pncr8a.afm
│  │     │  │  │  │  ├─ pncri8a.afm
│  │     │  │  │  │  ├─ pplb8a.afm
│  │     │  │  │  │  ├─ pplbi8a.afm
│  │     │  │  │  │  ├─ pplr8a.afm
│  │     │  │  │  │  ├─ pplri8a.afm
│  │     │  │  │  │  ├─ psyr.afm
│  │     │  │  │  │  ├─ ptmb8a.afm
│  │     │  │  │  │  ├─ ptmbi8a.afm
│  │     │  │  │  │  ├─ ptmr8a.afm
│  │     │  │  │  │  ├─ ptmri8a.afm
│  │     │  │  │  │  ├─ putb8a.afm
│  │     │  │  │  │  ├─ putbi8a.afm
│  │     │  │  │  │  ├─ putr8a.afm
│  │     │  │  │  │  ├─ putri8a.afm
│  │     │  │  │  │  ├─ pzcmi8a.afm
│  │     │  │  │  │  └─ pzdr.afm
│  │     │  │  │  ├─ pdfcorefonts/
│  │     │  │  │  │  ├─ Courier-Bold.afm
│  │     │  │  │  │  ├─ Courier-BoldOblique.afm
│  │     │  │  │  │  ├─ Courier-Oblique.afm
│  │     │  │  │  │  ├─ Courier.afm
│  │     │  │  │  │  ├─ Helvetica-Bold.afm
│  │     │  │  │  │  ├─ Helvetica-BoldOblique.afm
│  │     │  │  │  │  ├─ Helvetica-Oblique.afm
│  │     │  │  │  │  ├─ Helvetica.afm
│  │     │  │  │  │  ├─ readme.txt
│  │     │  │  │  │  ├─ Symbol.afm
│  │     │  │  │  │  ├─ Times-Bold.afm
│  │     │  │  │  │  ├─ Times-BoldItalic.afm
│  │     │  │  │  │  ├─ Times-Italic.afm
│  │     │  │  │  │  ├─ Times-Roman.afm
│  │     │  │  │  │  └─ ZapfDingbats.afm
│  │     │  │  │  └─ ttf/
│  │     │  │  │     ├─ cmb10.ttf
│  │     │  │  │     ├─ cmex10.ttf
│  │     │  │  │     ├─ cmmi10.ttf
│  │     │  │  │     ├─ cmr10.ttf
│  │     │  │  │     ├─ cmss10.ttf
│  │     │  │  │     ├─ cmsy10.ttf
│  │     │  │  │     ├─ cmtt10.ttf
│  │     │  │  │     ├─ DejaVuSans-Bold.ttf
│  │     │  │  │     ├─ DejaVuSans-BoldOblique.ttf
│  │     │  │  │     ├─ DejaVuSans-Oblique.ttf
│  │     │  │  │     ├─ DejaVuSans.ttf
│  │     │  │  │     ├─ DejaVuSansDisplay.ttf
│  │     │  │  │     ├─ DejaVuSansMono-Bold.ttf
│  │     │  │  │     ├─ DejaVuSansMono-BoldOblique.ttf
│  │     │  │  │     ├─ DejaVuSansMono-Oblique.ttf
│  │     │  │  │     ├─ DejaVuSansMono.ttf
│  │     │  │  │     ├─ DejaVuSerif-Bold.ttf
│  │     │  │  │     ├─ DejaVuSerif-BoldItalic.ttf
│  │     │  │  │     ├─ DejaVuSerif-Italic.ttf
│  │     │  │  │     ├─ DejaVuSerif.ttf
│  │     │  │  │     ├─ DejaVuSerifDisplay.ttf
│  │     │  │  │     ├─ LICENSE_DEJAVU
│  │     │  │  │     ├─ LICENSE_STIX
│  │     │  │  │     ├─ STIXGeneral.ttf
│  │     │  │  │     ├─ STIXGeneralBol.ttf
│  │     │  │  │     ├─ STIXGeneralBolIta.ttf
│  │     │  │  │     ├─ STIXGeneralItalic.ttf
│  │     │  │  │     ├─ STIXNonUni.ttf
│  │     │  │  │     ├─ STIXNonUniBol.ttf
│  │     │  │  │     ├─ STIXNonUniBolIta.ttf
│  │     │  │  │     ├─ STIXNonUniIta.ttf
│  │     │  │  │     ├─ STIXSizFiveSymReg.ttf
│  │     │  │  │     ├─ STIXSizFourSymBol.ttf
│  │     │  │  │     ├─ STIXSizFourSymReg.ttf
│  │     │  │  │     ├─ STIXSizOneSymBol.ttf
│  │     │  │  │     ├─ STIXSizOneSymReg.ttf
│  │     │  │  │     ├─ STIXSizThreeSymBol.ttf
│  │     │  │  │     ├─ STIXSizThreeSymReg.ttf
│  │     │  │  │     ├─ STIXSizTwoSymBol.ttf
│  │     │  │  │     └─ STIXSizTwoSymReg.ttf
│  │     │  │  ├─ images/
│  │     │  │  │  ├─ back_large.png
│  │     │  │  │  ├─ back-symbolic.svg
│  │     │  │  │  ├─ back.pdf
│  │     │  │  │  ├─ back.png
│  │     │  │  │  ├─ back.svg
│  │     │  │  │  ├─ filesave_large.png
│  │     │  │  │  ├─ filesave-symbolic.svg
│  │     │  │  │  ├─ filesave.pdf
│  │     │  │  │  ├─ filesave.png
│  │     │  │  │  ├─ filesave.svg
│  │     │  │  │  ├─ forward_large.png
│  │     │  │  │  ├─ forward-symbolic.svg
│  │     │  │  │  ├─ forward.pdf
│  │     │  │  │  ├─ forward.png
│  │     │  │  │  ├─ forward.svg
│  │     │  │  │  ├─ hand.pdf
│  │     │  │  │  ├─ hand.png
│  │     │  │  │  ├─ hand.svg
│  │     │  │  │  ├─ help_large.png
│  │     │  │  │  ├─ help-symbolic.svg
│  │     │  │  │  ├─ help.pdf
│  │     │  │  │  ├─ help.png
│  │     │  │  │  ├─ help.svg
│  │     │  │  │  ├─ home_large.png
│  │     │  │  │  ├─ home-symbolic.svg
│  │     │  │  │  ├─ home.pdf
│  │     │  │  │  ├─ home.png
│  │     │  │  │  ├─ home.svg
│  │     │  │  │  ├─ matplotlib_large.png
│  │     │  │  │  ├─ matplotlib.pdf
│  │     │  │  │  ├─ matplotlib.png
│  │     │  │  │  ├─ matplotlib.svg
│  │     │  │  │  ├─ move_large.png
│  │     │  │  │  ├─ move-symbolic.svg
│  │     │  │  │  ├─ move.pdf
│  │     │  │  │  ├─ move.png
│  │     │  │  │  ├─ move.svg
│  │     │  │  │  ├─ qt4_editor_options_large.png
│  │     │  │  │  ├─ qt4_editor_options.pdf
│  │     │  │  │  ├─ qt4_editor_options.png
│  │     │  │  │  ├─ qt4_editor_options.svg
│  │     │  │  │  ├─ subplots_large.png
│  │     │  │  │  ├─ subplots-symbolic.svg
│  │     │  │  │  ├─ subplots.pdf
│  │     │  │  │  ├─ subplots.png
│  │     │  │  │  ├─ subplots.svg
│  │     │  │  │  ├─ zoom_to_rect_large.png
│  │     │  │  │  ├─ zoom_to_rect-symbolic.svg
│  │     │  │  │  ├─ zoom_to_rect.pdf
│  │     │  │  │  ├─ zoom_to_rect.png
│  │     │  │  │  └─ zoom_to_rect.svg
│  │     │  │  ├─ plot_directive/
│  │     │  │  │  └─ plot_directive.css
│  │     │  │  ├─ sample_data/
│  │     │  │  │  ├─ axes_grid/
│  │     │  │  │  │  └─ bivariate_normal.npy
│  │     │  │  │  ├─ data_x_x2_x3.csv
│  │     │  │  │  ├─ eeg.dat
│  │     │  │  │  ├─ embedding_in_wx3.xrc
│  │     │  │  │  ├─ goog.npz
│  │     │  │  │  ├─ grace_hopper.jpg
│  │     │  │  │  ├─ jacksboro_fault_dem.npz
│  │     │  │  │  ├─ logo2.png
│  │     │  │  │  ├─ membrane.dat
│  │     │  │  │  ├─ Minduka_Present_Blue_Pack.png
│  │     │  │  │  ├─ msft.csv
│  │     │  │  │  ├─ README.txt
│  │     │  │  │  ├─ s1045.ima.gz
│  │     │  │  │  ├─ Stocks.csv
│  │     │  │  │  └─ topobathy.npz
│  │     │  │  ├─ stylelib/
│  │     │  │  │  ├─ _classic_test_patch.mplstyle
│  │     │  │  │  ├─ _mpl-gallery-nogrid.mplstyle
│  │     │  │  │  ├─ _mpl-gallery.mplstyle
│  │     │  │  │  ├─ bmh.mplstyle
│  │     │  │  │  ├─ classic.mplstyle
│  │     │  │  │  ├─ dark_background.mplstyle
│  │     │  │  │  ├─ fast.mplstyle
│  │     │  │  │  ├─ fivethirtyeight.mplstyle
│  │     │  │  │  ├─ ggplot.mplstyle
│  │     │  │  │  ├─ grayscale.mplstyle
│  │     │  │  │  ├─ petroff10.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-bright.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-colorblind.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-dark-palette.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-dark.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-darkgrid.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-deep.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-muted.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-notebook.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-paper.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-pastel.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-poster.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-talk.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-ticks.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-white.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8-whitegrid.mplstyle
│  │     │  │  │  ├─ seaborn-v0_8.mplstyle
│  │     │  │  │  ├─ Solarize_Light2.mplstyle
│  │     │  │  │  └─ tableau-colorblind10.mplstyle
│  │     │  │  ├─ kpsewhich.lua
│  │     │  │  └─ matplotlibrc
│  │     │  ├─ projections/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ geo.cpython-312.pyc
│  │     │  │  │  └─ polar.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ geo.py
│  │     │  │  ├─ geo.pyi
│  │     │  │  ├─ polar.py
│  │     │  │  └─ polar.pyi
│  │     │  ├─ sphinxext/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ figmpl_directive.cpython-312.pyc
│  │     │  │  │  ├─ mathmpl.cpython-312.pyc
│  │     │  │  │  ├─ plot_directive.cpython-312.pyc
│  │     │  │  │  └─ roles.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ figmpl_directive.py
│  │     │  │  ├─ mathmpl.py
│  │     │  │  ├─ plot_directive.py
│  │     │  │  └─ roles.py
│  │     │  ├─ style/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ core.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ core.py
│  │     │  │  └─ core.pyi
│  │     │  ├─ testing/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _markers.cpython-312.pyc
│  │     │  │  │  ├─ compare.cpython-312.pyc
│  │     │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  ├─ decorators.cpython-312.pyc
│  │     │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  └─ widgets.cpython-312.pyc
│  │     │  │  ├─ jpl_units/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ Duration.cpython-312.pyc
│  │     │  │  │  │  ├─ Epoch.cpython-312.pyc
│  │     │  │  │  │  ├─ EpochConverter.cpython-312.pyc
│  │     │  │  │  │  ├─ StrConverter.cpython-312.pyc
│  │     │  │  │  │  ├─ UnitDbl.cpython-312.pyc
│  │     │  │  │  │  ├─ UnitDblConverter.cpython-312.pyc
│  │     │  │  │  │  └─ UnitDblFormatter.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ Duration.py
│  │     │  │  │  ├─ Epoch.py
│  │     │  │  │  ├─ EpochConverter.py
│  │     │  │  │  ├─ StrConverter.py
│  │     │  │  │  ├─ UnitDbl.py
│  │     │  │  │  ├─ UnitDblConverter.py
│  │     │  │  │  └─ UnitDblFormatter.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _markers.py
│  │     │  │  ├─ compare.py
│  │     │  │  ├─ compare.pyi
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ conftest.pyi
│  │     │  │  ├─ decorators.py
│  │     │  │  ├─ decorators.pyi
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ widgets.py
│  │     │  │  └─ widgets.pyi
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  ├─ test_afm.cpython-312.pyc
│  │     │  │  │  ├─ test_agg_filter.cpython-312.pyc
│  │     │  │  │  ├─ test_agg.cpython-312.pyc
│  │     │  │  │  ├─ test_animation.cpython-312.pyc
│  │     │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  ├─ test_arrow_patches.cpython-312.pyc
│  │     │  │  │  ├─ test_artist.cpython-312.pyc
│  │     │  │  │  ├─ test_axes.cpython-312.pyc
│  │     │  │  │  ├─ test_axis.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_bases.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_cairo.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_gtk3.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_inline.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_macosx.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_nbagg.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_pdf.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_pgf.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_ps.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_qt.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_registry.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_svg.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_template.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_tk.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_tools.cpython-312.pyc
│  │     │  │  │  ├─ test_backend_webagg.cpython-312.pyc
│  │     │  │  │  ├─ test_backends_interactive.cpython-312.pyc
│  │     │  │  │  ├─ test_basic.cpython-312.pyc
│  │     │  │  │  ├─ test_bbox_tight.cpython-312.pyc
│  │     │  │  │  ├─ test_bezier.cpython-312.pyc
│  │     │  │  │  ├─ test_category.cpython-312.pyc
│  │     │  │  │  ├─ test_cbook.cpython-312.pyc
│  │     │  │  │  ├─ test_collections.cpython-312.pyc
│  │     │  │  │  ├─ test_colorbar.cpython-312.pyc
│  │     │  │  │  ├─ test_colors.cpython-312.pyc
│  │     │  │  │  ├─ test_compare_images.cpython-312.pyc
│  │     │  │  │  ├─ test_constrainedlayout.cpython-312.pyc
│  │     │  │  │  ├─ test_container.cpython-312.pyc
│  │     │  │  │  ├─ test_contour.cpython-312.pyc
│  │     │  │  │  ├─ test_cycles.cpython-312.pyc
│  │     │  │  │  ├─ test_dates.cpython-312.pyc
│  │     │  │  │  ├─ test_datetime.cpython-312.pyc
│  │     │  │  │  ├─ test_determinism.cpython-312.pyc
│  │     │  │  │  ├─ test_doc.cpython-312.pyc
│  │     │  │  │  ├─ test_dviread.cpython-312.pyc
│  │     │  │  │  ├─ test_figure.cpython-312.pyc
│  │     │  │  │  ├─ test_font_manager.cpython-312.pyc
│  │     │  │  │  ├─ test_fontconfig_pattern.cpython-312.pyc
│  │     │  │  │  ├─ test_ft2font.cpython-312.pyc
│  │     │  │  │  ├─ test_getattr.cpython-312.pyc
│  │     │  │  │  ├─ test_gridspec.cpython-312.pyc
│  │     │  │  │  ├─ test_image.cpython-312.pyc
│  │     │  │  │  ├─ test_legend.cpython-312.pyc
│  │     │  │  │  ├─ test_lines.cpython-312.pyc
│  │     │  │  │  ├─ test_marker.cpython-312.pyc
│  │     │  │  │  ├─ test_mathtext.cpython-312.pyc
│  │     │  │  │  ├─ test_matplotlib.cpython-312.pyc
│  │     │  │  │  ├─ test_mlab.cpython-312.pyc
│  │     │  │  │  ├─ test_multivariate_colormaps.cpython-312.pyc
│  │     │  │  │  ├─ test_offsetbox.cpython-312.pyc
│  │     │  │  │  ├─ test_patches.cpython-312.pyc
│  │     │  │  │  ├─ test_path.cpython-312.pyc
│  │     │  │  │  ├─ test_patheffects.cpython-312.pyc
│  │     │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  ├─ test_png.cpython-312.pyc
│  │     │  │  │  ├─ test_polar.cpython-312.pyc
│  │     │  │  │  ├─ test_preprocess_data.cpython-312.pyc
│  │     │  │  │  ├─ test_pyplot.cpython-312.pyc
│  │     │  │  │  ├─ test_quiver.cpython-312.pyc
│  │     │  │  │  ├─ test_rcparams.cpython-312.pyc
│  │     │  │  │  ├─ test_sankey.cpython-312.pyc
│  │     │  │  │  ├─ test_scale.cpython-312.pyc
│  │     │  │  │  ├─ test_simplification.cpython-312.pyc
│  │     │  │  │  ├─ test_skew.cpython-312.pyc
│  │     │  │  │  ├─ test_sphinxext.cpython-312.pyc
│  │     │  │  │  ├─ test_spines.cpython-312.pyc
│  │     │  │  │  ├─ test_streamplot.cpython-312.pyc
│  │     │  │  │  ├─ test_style.cpython-312.pyc
│  │     │  │  │  ├─ test_subplots.cpython-312.pyc
│  │     │  │  │  ├─ test_table.cpython-312.pyc
│  │     │  │  │  ├─ test_testing.cpython-312.pyc
│  │     │  │  │  ├─ test_texmanager.cpython-312.pyc
│  │     │  │  │  ├─ test_text.cpython-312.pyc
│  │     │  │  │  ├─ test_textpath.cpython-312.pyc
│  │     │  │  │  ├─ test_ticker.cpython-312.pyc
│  │     │  │  │  ├─ test_tightlayout.cpython-312.pyc
│  │     │  │  │  ├─ test_transforms.cpython-312.pyc
│  │     │  │  │  ├─ test_triangulation.cpython-312.pyc
│  │     │  │  │  ├─ test_type1font.cpython-312.pyc
│  │     │  │  │  ├─ test_units.cpython-312.pyc
│  │     │  │  │  ├─ test_usetex.cpython-312.pyc
│  │     │  │  │  └─ test_widgets.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ conftest.py
│  │     │  │  ├─ test_afm.py
│  │     │  │  ├─ test_agg_filter.py
│  │     │  │  ├─ test_agg.py
│  │     │  │  ├─ test_animation.py
│  │     │  │  ├─ test_api.py
│  │     │  │  ├─ test_arrow_patches.py
│  │     │  │  ├─ test_artist.py
│  │     │  │  ├─ test_axes.py
│  │     │  │  ├─ test_axis.py
│  │     │  │  ├─ test_backend_bases.py
│  │     │  │  ├─ test_backend_cairo.py
│  │     │  │  ├─ test_backend_gtk3.py
│  │     │  │  ├─ test_backend_inline.py
│  │     │  │  ├─ test_backend_macosx.py
│  │     │  │  ├─ test_backend_nbagg.py
│  │     │  │  ├─ test_backend_pdf.py
│  │     │  │  ├─ test_backend_pgf.py
│  │     │  │  ├─ test_backend_ps.py
│  │     │  │  ├─ test_backend_qt.py
│  │     │  │  ├─ test_backend_registry.py
│  │     │  │  ├─ test_backend_svg.py
│  │     │  │  ├─ test_backend_template.py
│  │     │  │  ├─ test_backend_tk.py
│  │     │  │  ├─ test_backend_tools.py
│  │     │  │  ├─ test_backend_webagg.py
│  │     │  │  ├─ test_backends_interactive.py
│  │     │  │  ├─ test_basic.py
│  │     │  │  ├─ test_bbox_tight.py
│  │     │  │  ├─ test_bezier.py
│  │     │  │  ├─ test_category.py
│  │     │  │  ├─ test_cbook.py
│  │     │  │  ├─ test_collections.py
│  │     │  │  ├─ test_colorbar.py
│  │     │  │  ├─ test_colors.py
│  │     │  │  ├─ test_compare_images.py
│  │     │  │  ├─ test_constrainedlayout.py
│  │     │  │  ├─ test_container.py
│  │     │  │  ├─ test_contour.py
│  │     │  │  ├─ test_cycles.py
│  │     │  │  ├─ test_dates.py
│  │     │  │  ├─ test_datetime.py
│  │     │  │  ├─ test_determinism.py
│  │     │  │  ├─ test_doc.py
│  │     │  │  ├─ test_dviread.py
│  │     │  │  ├─ test_figure.py
│  │     │  │  ├─ test_font_manager.py
│  │     │  │  ├─ test_fontconfig_pattern.py
│  │     │  │  ├─ test_ft2font.py
│  │     │  │  ├─ test_getattr.py
│  │     │  │  ├─ test_gridspec.py
│  │     │  │  ├─ test_image.py
│  │     │  │  ├─ test_legend.py
│  │     │  │  ├─ test_lines.py
│  │     │  │  ├─ test_marker.py
│  │     │  │  ├─ test_mathtext.py
│  │     │  │  ├─ test_matplotlib.py
│  │     │  │  ├─ test_mlab.py
│  │     │  │  ├─ test_multivariate_colormaps.py
│  │     │  │  ├─ test_offsetbox.py
│  │     │  │  ├─ test_patches.py
│  │     │  │  ├─ test_path.py
│  │     │  │  ├─ test_patheffects.py
│  │     │  │  ├─ test_pickle.py
│  │     │  │  ├─ test_png.py
│  │     │  │  ├─ test_polar.py
│  │     │  │  ├─ test_preprocess_data.py
│  │     │  │  ├─ test_pyplot.py
│  │     │  │  ├─ test_quiver.py
│  │     │  │  ├─ test_rcparams.py
│  │     │  │  ├─ test_sankey.py
│  │     │  │  ├─ test_scale.py
│  │     │  │  ├─ test_simplification.py
│  │     │  │  ├─ test_skew.py
│  │     │  │  ├─ test_sphinxext.py
│  │     │  │  ├─ test_spines.py
│  │     │  │  ├─ test_streamplot.py
│  │     │  │  ├─ test_style.py
│  │     │  │  ├─ test_subplots.py
│  │     │  │  ├─ test_table.py
│  │     │  │  ├─ test_testing.py
│  │     │  │  ├─ test_texmanager.py
│  │     │  │  ├─ test_text.py
│  │     │  │  ├─ test_textpath.py
│  │     │  │  ├─ test_ticker.py
│  │     │  │  ├─ test_tightlayout.py
│  │     │  │  ├─ test_transforms.py
│  │     │  │  ├─ test_triangulation.py
│  │     │  │  ├─ test_type1font.py
│  │     │  │  ├─ test_units.py
│  │     │  │  ├─ test_usetex.py
│  │     │  │  └─ test_widgets.py
│  │     │  ├─ tri/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _triangulation.cpython-312.pyc
│  │     │  │  │  ├─ _tricontour.cpython-312.pyc
│  │     │  │  │  ├─ _trifinder.cpython-312.pyc
│  │     │  │  │  ├─ _triinterpolate.cpython-312.pyc
│  │     │  │  │  ├─ _tripcolor.cpython-312.pyc
│  │     │  │  │  ├─ _triplot.cpython-312.pyc
│  │     │  │  │  ├─ _trirefine.cpython-312.pyc
│  │     │  │  │  └─ _tritools.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _triangulation.py
│  │     │  │  ├─ _triangulation.pyi
│  │     │  │  ├─ _tricontour.py
│  │     │  │  ├─ _tricontour.pyi
│  │     │  │  ├─ _trifinder.py
│  │     │  │  ├─ _trifinder.pyi
│  │     │  │  ├─ _triinterpolate.py
│  │     │  │  ├─ _triinterpolate.pyi
│  │     │  │  ├─ _tripcolor.py
│  │     │  │  ├─ _tripcolor.pyi
│  │     │  │  ├─ _triplot.py
│  │     │  │  ├─ _triplot.pyi
│  │     │  │  ├─ _trirefine.py
│  │     │  │  ├─ _trirefine.pyi
│  │     │  │  ├─ _tritools.py
│  │     │  │  └─ _tritools.pyi
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  ├─ _afm.py
│  │     │  ├─ _animation_data.py
│  │     │  ├─ _blocking_input.py
│  │     │  ├─ _c_internal_utils.cp312-win_amd64.pyd
│  │     │  ├─ _c_internal_utils.pyi
│  │     │  ├─ _cm_bivar.py
│  │     │  ├─ _cm_listed.py
│  │     │  ├─ _cm_multivar.py
│  │     │  ├─ _cm.py
│  │     │  ├─ _color_data.py
│  │     │  ├─ _color_data.pyi
│  │     │  ├─ _constrained_layout.py
│  │     │  ├─ _docstring.py
│  │     │  ├─ _docstring.pyi
│  │     │  ├─ _enums.py
│  │     │  ├─ _enums.pyi
│  │     │  ├─ _fontconfig_pattern.py
│  │     │  ├─ _image.cp312-win_amd64.pyd
│  │     │  ├─ _image.pyi
│  │     │  ├─ _internal_utils.py
│  │     │  ├─ _layoutgrid.py
│  │     │  ├─ _mathtext_data.py
│  │     │  ├─ _mathtext.py
│  │     │  ├─ _path.cp312-win_amd64.pyd
│  │     │  ├─ _path.pyi
│  │     │  ├─ _pylab_helpers.py
│  │     │  ├─ _pylab_helpers.pyi
│  │     │  ├─ _qhull.cp312-win_amd64.pyd
│  │     │  ├─ _qhull.pyi
│  │     │  ├─ _text_helpers.py
│  │     │  ├─ _tight_bbox.py
│  │     │  ├─ _tight_layout.py
│  │     │  ├─ _tri.cp312-win_amd64.pyd
│  │     │  ├─ _tri.pyi
│  │     │  ├─ _type1font.py
│  │     │  ├─ _version.py
│  │     │  ├─ animation.py
│  │     │  ├─ animation.pyi
│  │     │  ├─ artist.py
│  │     │  ├─ artist.pyi
│  │     │  ├─ axis.py
│  │     │  ├─ axis.pyi
│  │     │  ├─ backend_bases.py
│  │     │  ├─ backend_bases.pyi
│  │     │  ├─ backend_managers.py
│  │     │  ├─ backend_managers.pyi
│  │     │  ├─ backend_tools.py
│  │     │  ├─ backend_tools.pyi
│  │     │  ├─ bezier.py
│  │     │  ├─ bezier.pyi
│  │     │  ├─ category.py
│  │     │  ├─ cbook.py
│  │     │  ├─ cbook.pyi
│  │     │  ├─ cm.py
│  │     │  ├─ cm.pyi
│  │     │  ├─ collections.py
│  │     │  ├─ collections.pyi
│  │     │  ├─ colorbar.py
│  │     │  ├─ colorbar.pyi
│  │     │  ├─ colorizer.py
│  │     │  ├─ colorizer.pyi
│  │     │  ├─ colors.py
│  │     │  ├─ colors.pyi
│  │     │  ├─ container.py
│  │     │  ├─ container.pyi
│  │     │  ├─ contour.py
│  │     │  ├─ contour.pyi
│  │     │  ├─ dates.py
│  │     │  ├─ dviread.py
│  │     │  ├─ dviread.pyi
│  │     │  ├─ figure.py
│  │     │  ├─ figure.pyi
│  │     │  ├─ font_manager.py
│  │     │  ├─ font_manager.pyi
│  │     │  ├─ ft2font.cp312-win_amd64.pyd
│  │     │  ├─ ft2font.pyi
│  │     │  ├─ gridspec.py
│  │     │  ├─ gridspec.pyi
│  │     │  ├─ hatch.py
│  │     │  ├─ hatch.pyi
│  │     │  ├─ image.py
│  │     │  ├─ image.pyi
│  │     │  ├─ inset.py
│  │     │  ├─ inset.pyi
│  │     │  ├─ layout_engine.py
│  │     │  ├─ layout_engine.pyi
│  │     │  ├─ legend_handler.py
│  │     │  ├─ legend_handler.pyi
│  │     │  ├─ legend.py
│  │     │  ├─ legend.pyi
│  │     │  ├─ lines.py
│  │     │  ├─ lines.pyi
│  │     │  ├─ markers.py
│  │     │  ├─ markers.pyi
│  │     │  ├─ mathtext.py
│  │     │  ├─ mathtext.pyi
│  │     │  ├─ mlab.py
│  │     │  ├─ mlab.pyi
│  │     │  ├─ offsetbox.py
│  │     │  ├─ offsetbox.pyi
│  │     │  ├─ patches.py
│  │     │  ├─ patches.pyi
│  │     │  ├─ path.py
│  │     │  ├─ path.pyi
│  │     │  ├─ patheffects.py
│  │     │  ├─ patheffects.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ pylab.py
│  │     │  ├─ pyplot.py
│  │     │  ├─ quiver.py
│  │     │  ├─ quiver.pyi
│  │     │  ├─ rcsetup.py
│  │     │  ├─ rcsetup.pyi
│  │     │  ├─ sankey.py
│  │     │  ├─ sankey.pyi
│  │     │  ├─ scale.py
│  │     │  ├─ scale.pyi
│  │     │  ├─ spines.py
│  │     │  ├─ spines.pyi
│  │     │  ├─ stackplot.py
│  │     │  ├─ stackplot.pyi
│  │     │  ├─ streamplot.py
│  │     │  ├─ streamplot.pyi
│  │     │  ├─ table.py
│  │     │  ├─ table.pyi
│  │     │  ├─ texmanager.py
│  │     │  ├─ texmanager.pyi
│  │     │  ├─ text.py
│  │     │  ├─ text.pyi
│  │     │  ├─ textpath.py
│  │     │  ├─ textpath.pyi
│  │     │  ├─ ticker.py
│  │     │  ├─ ticker.pyi
│  │     │  ├─ transforms.py
│  │     │  ├─ transforms.pyi
│  │     │  ├─ typing.py
│  │     │  ├─ units.py
│  │     │  ├─ widgets.py
│  │     │  └─ widgets.pyi
│  │     ├─ matplotlib_inline/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ backend_inline.cpython-312.pyc
│  │     │  │  └─ config.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ backend_inline.py
│  │     │  └─ config.py
│  │     ├─ matplotlib_inline-0.1.7.dist-info/
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ matplotlib-3.10.3.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ mpl_toolkits/
│  │     │  ├─ axes_grid1/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ anchored_artists.cpython-312.pyc
│  │     │  │  │  ├─ axes_divider.cpython-312.pyc
│  │     │  │  │  ├─ axes_grid.cpython-312.pyc
│  │     │  │  │  ├─ axes_rgb.cpython-312.pyc
│  │     │  │  │  ├─ axes_size.cpython-312.pyc
│  │     │  │  │  ├─ inset_locator.cpython-312.pyc
│  │     │  │  │  ├─ mpl_axes.cpython-312.pyc
│  │     │  │  │  └─ parasite_axes.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  └─ test_axes_grid1.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  └─ test_axes_grid1.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ anchored_artists.py
│  │     │  │  ├─ axes_divider.py
│  │     │  │  ├─ axes_grid.py
│  │     │  │  ├─ axes_rgb.py
│  │     │  │  ├─ axes_size.py
│  │     │  │  ├─ inset_locator.py
│  │     │  │  ├─ mpl_axes.py
│  │     │  │  └─ parasite_axes.py
│  │     │  ├─ axisartist/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ angle_helper.cpython-312.pyc
│  │     │  │  │  ├─ axes_divider.cpython-312.pyc
│  │     │  │  │  ├─ axis_artist.cpython-312.pyc
│  │     │  │  │  ├─ axisline_style.cpython-312.pyc
│  │     │  │  │  ├─ axislines.cpython-312.pyc
│  │     │  │  │  ├─ floating_axes.cpython-312.pyc
│  │     │  │  │  ├─ grid_finder.cpython-312.pyc
│  │     │  │  │  ├─ grid_helper_curvelinear.cpython-312.pyc
│  │     │  │  │  └─ parasite_axes.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_angle_helper.cpython-312.pyc
│  │     │  │  │  │  ├─ test_axis_artist.cpython-312.pyc
│  │     │  │  │  │  ├─ test_axislines.cpython-312.pyc
│  │     │  │  │  │  ├─ test_floating_axes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_grid_finder.cpython-312.pyc
│  │     │  │  │  │  └─ test_grid_helper_curvelinear.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_angle_helper.py
│  │     │  │  │  ├─ test_axis_artist.py
│  │     │  │  │  ├─ test_axislines.py
│  │     │  │  │  ├─ test_floating_axes.py
│  │     │  │  │  ├─ test_grid_finder.py
│  │     │  │  │  └─ test_grid_helper_curvelinear.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ angle_helper.py
│  │     │  │  ├─ axes_divider.py
│  │     │  │  ├─ axis_artist.py
│  │     │  │  ├─ axisline_style.py
│  │     │  │  ├─ axislines.py
│  │     │  │  ├─ floating_axes.py
│  │     │  │  ├─ grid_finder.py
│  │     │  │  ├─ grid_helper_curvelinear.py
│  │     │  │  └─ parasite_axes.py
│  │     │  └─ mplot3d/
│  │     │     ├─ __pycache__/
│  │     │     │  ├─ __init__.cpython-312.pyc
│  │     │     │  ├─ art3d.cpython-312.pyc
│  │     │     │  ├─ axes3d.cpython-312.pyc
│  │     │     │  ├─ axis3d.cpython-312.pyc
│  │     │     │  └─ proj3d.cpython-312.pyc
│  │     │     ├─ tests/
│  │     │     │  ├─ __pycache__/
│  │     │     │  │  ├─ __init__.cpython-312.pyc
│  │     │     │  │  ├─ conftest.cpython-312.pyc
│  │     │     │  │  ├─ test_art3d.cpython-312.pyc
│  │     │     │  │  ├─ test_axes3d.cpython-312.pyc
│  │     │     │  │  └─ test_legend3d.cpython-312.pyc
│  │     │     │  ├─ __init__.py
│  │     │     │  ├─ conftest.py
│  │     │     │  ├─ test_art3d.py
│  │     │     │  ├─ test_axes3d.py
│  │     │     │  └─ test_legend3d.py
│  │     │     ├─ __init__.py
│  │     │     ├─ art3d.py
│  │     │     ├─ axes3d.py
│  │     │     ├─ axis3d.py
│  │     │     └─ proj3d.py
│  │     ├─ narwhals/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _constants.cpython-312.pyc
│  │     │  │  ├─ _duration.cpython-312.pyc
│  │     │  │  ├─ _enum.cpython-312.pyc
│  │     │  │  ├─ _expression_parsing.cpython-312.pyc
│  │     │  │  ├─ _namespace.cpython-312.pyc
│  │     │  │  ├─ _translate.cpython-312.pyc
│  │     │  │  ├─ _typing_compat.cpython-312.pyc
│  │     │  │  ├─ _utils.cpython-312.pyc
│  │     │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  ├─ dependencies.cpython-312.pyc
│  │     │  │  ├─ dtypes.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ expr_cat.cpython-312.pyc
│  │     │  │  ├─ expr_dt.cpython-312.pyc
│  │     │  │  ├─ expr_list.cpython-312.pyc
│  │     │  │  ├─ expr_name.cpython-312.pyc
│  │     │  │  ├─ expr_str.cpython-312.pyc
│  │     │  │  ├─ expr_struct.cpython-312.pyc
│  │     │  │  ├─ expr.cpython-312.pyc
│  │     │  │  ├─ functions.cpython-312.pyc
│  │     │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  ├─ schema.cpython-312.pyc
│  │     │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  ├─ series_cat.cpython-312.pyc
│  │     │  │  ├─ series_dt.cpython-312.pyc
│  │     │  │  ├─ series_list.cpython-312.pyc
│  │     │  │  ├─ series_str.cpython-312.pyc
│  │     │  │  ├─ series_struct.cpython-312.pyc
│  │     │  │  ├─ series.cpython-312.pyc
│  │     │  │  ├─ this.cpython-312.pyc
│  │     │  │  ├─ translate.cpython-312.pyc
│  │     │  │  ├─ typing.cpython-312.pyc
│  │     │  │  └─ utils.cpython-312.pyc
│  │     │  ├─ _arrow/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  ├─ series_cat.cpython-312.pyc
│  │     │  │  │  ├─ series_dt.cpython-312.pyc
│  │     │  │  │  ├─ series_list.cpython-312.pyc
│  │     │  │  │  ├─ series_str.cpython-312.pyc
│  │     │  │  │  ├─ series_struct.cpython-312.pyc
│  │     │  │  │  ├─ series.cpython-312.pyc
│  │     │  │  │  ├─ typing.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series_cat.py
│  │     │  │  ├─ series_dt.py
│  │     │  │  ├─ series_list.py
│  │     │  │  ├─ series_str.py
│  │     │  │  ├─ series_struct.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  └─ utils.py
│  │     │  ├─ _compliant/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ any_namespace.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  ├─ series.cpython-312.pyc
│  │     │  │  │  ├─ typing.cpython-312.pyc
│  │     │  │  │  ├─ when_then.cpython-312.pyc
│  │     │  │  │  └─ window.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ any_namespace.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  ├─ when_then.py
│  │     │  │  └─ window.py
│  │     │  ├─ _dask/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr_dt.cpython-312.pyc
│  │     │  │  │  ├─ expr_str.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  └─ utils.py
│  │     │  ├─ _duckdb/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr_dt.cpython-312.pyc
│  │     │  │  │  ├─ expr_list.cpython-312.pyc
│  │     │  │  │  ├─ expr_str.cpython-312.pyc
│  │     │  │  │  ├─ expr_struct.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  ├─ series.cpython-312.pyc
│  │     │  │  │  ├─ typing.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_list.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ expr_struct.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  └─ utils.py
│  │     │  ├─ _ibis/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr_dt.cpython-312.pyc
│  │     │  │  │  ├─ expr_list.cpython-312.pyc
│  │     │  │  │  ├─ expr_str.cpython-312.pyc
│  │     │  │  │  ├─ expr_struct.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  ├─ series.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_list.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ expr_struct.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series.py
│  │     │  │  └─ utils.py
│  │     │  ├─ _interchange/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  └─ series.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  └─ series.py
│  │     │  ├─ _pandas_like/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  ├─ series_cat.cpython-312.pyc
│  │     │  │  │  ├─ series_dt.cpython-312.pyc
│  │     │  │  │  ├─ series_list.cpython-312.pyc
│  │     │  │  │  ├─ series_str.cpython-312.pyc
│  │     │  │  │  ├─ series_struct.cpython-312.pyc
│  │     │  │  │  ├─ series.cpython-312.pyc
│  │     │  │  │  ├─ typing.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  ├─ series_cat.py
│  │     │  │  ├─ series_dt.py
│  │     │  │  ├─ series_list.py
│  │     │  │  ├─ series_str.py
│  │     │  │  ├─ series_struct.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  └─ utils.py
│  │     │  ├─ _polars/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ series.cpython-312.pyc
│  │     │  │  │  ├─ typing.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ typing.py
│  │     │  │  └─ utils.py
│  │     │  ├─ _spark_like/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  ├─ expr_dt.cpython-312.pyc
│  │     │  │  │  ├─ expr_list.cpython-312.pyc
│  │     │  │  │  ├─ expr_str.cpython-312.pyc
│  │     │  │  │  ├─ expr_struct.cpython-312.pyc
│  │     │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  ├─ group_by.cpython-312.pyc
│  │     │  │  │  ├─ namespace.cpython-312.pyc
│  │     │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ dataframe.py
│  │     │  │  ├─ expr_dt.py
│  │     │  │  ├─ expr_list.py
│  │     │  │  ├─ expr_str.py
│  │     │  │  ├─ expr_struct.py
│  │     │  │  ├─ expr.py
│  │     │  │  ├─ group_by.py
│  │     │  │  ├─ namespace.py
│  │     │  │  ├─ selectors.py
│  │     │  │  └─ utils.py
│  │     │  ├─ stable/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ v1/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _dtypes.cpython-312.pyc
│  │     │  │  │  │  ├─ _namespace.cpython-312.pyc
│  │     │  │  │  │  ├─ dependencies.cpython-312.pyc
│  │     │  │  │  │  ├─ dtypes.cpython-312.pyc
│  │     │  │  │  │  ├─ selectors.cpython-312.pyc
│  │     │  │  │  │  └─ typing.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _dtypes.py
│  │     │  │  │  ├─ _namespace.py
│  │     │  │  │  ├─ dependencies.py
│  │     │  │  │  ├─ dtypes.py
│  │     │  │  │  ├─ selectors.py
│  │     │  │  │  └─ typing.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _constants.py
│  │     │  ├─ _duration.py
│  │     │  ├─ _enum.py
│  │     │  ├─ _expression_parsing.py
│  │     │  ├─ _namespace.py
│  │     │  ├─ _translate.py
│  │     │  ├─ _typing_compat.py
│  │     │  ├─ _utils.py
│  │     │  ├─ dataframe.py
│  │     │  ├─ dependencies.py
│  │     │  ├─ dtypes.py
│  │     │  ├─ exceptions.py
│  │     │  ├─ expr_cat.py
│  │     │  ├─ expr_dt.py
│  │     │  ├─ expr_list.py
│  │     │  ├─ expr_name.py
│  │     │  ├─ expr_str.py
│  │     │  ├─ expr_struct.py
│  │     │  ├─ expr.py
│  │     │  ├─ functions.py
│  │     │  ├─ group_by.py
│  │     │  ├─ py.typed
│  │     │  ├─ schema.py
│  │     │  ├─ selectors.py
│  │     │  ├─ series_cat.py
│  │     │  ├─ series_dt.py
│  │     │  ├─ series_list.py
│  │     │  ├─ series_str.py
│  │     │  ├─ series_struct.py
│  │     │  ├─ series.py
│  │     │  ├─ this.py
│  │     │  ├─ translate.py
│  │     │  ├─ typing.py
│  │     │  └─ utils.py
│  │     ├─ narwhals-1.46.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE.md
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ nest_asyncio-1.6.0.dist-info/
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ numpy/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __config__.cpython-312.pyc
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _array_api_info.cpython-312.pyc
│  │     │  │  ├─ _configtool.cpython-312.pyc
│  │     │  │  ├─ _distributor_init.cpython-312.pyc
│  │     │  │  ├─ _expired_attrs_2_0.cpython-312.pyc
│  │     │  │  ├─ _globals.cpython-312.pyc
│  │     │  │  ├─ _pytesttester.cpython-312.pyc
│  │     │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  ├─ dtypes.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ matlib.cpython-312.pyc
│  │     │  │  └─ version.cpython-312.pyc
│  │     │  ├─ _core/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _add_newdocs_scalars.cpython-312.pyc
│  │     │  │  │  ├─ _add_newdocs.cpython-312.pyc
│  │     │  │  │  ├─ _asarray.cpython-312.pyc
│  │     │  │  │  ├─ _dtype_ctypes.cpython-312.pyc
│  │     │  │  │  ├─ _dtype.cpython-312.pyc
│  │     │  │  │  ├─ _exceptions.cpython-312.pyc
│  │     │  │  │  ├─ _internal.cpython-312.pyc
│  │     │  │  │  ├─ _machar.cpython-312.pyc
│  │     │  │  │  ├─ _methods.cpython-312.pyc
│  │     │  │  │  ├─ _string_helpers.cpython-312.pyc
│  │     │  │  │  ├─ _type_aliases.cpython-312.pyc
│  │     │  │  │  ├─ _ufunc_config.cpython-312.pyc
│  │     │  │  │  ├─ arrayprint.cpython-312.pyc
│  │     │  │  │  ├─ cversions.cpython-312.pyc
│  │     │  │  │  ├─ defchararray.cpython-312.pyc
│  │     │  │  │  ├─ einsumfunc.cpython-312.pyc
│  │     │  │  │  ├─ fromnumeric.cpython-312.pyc
│  │     │  │  │  ├─ function_base.cpython-312.pyc
│  │     │  │  │  ├─ getlimits.cpython-312.pyc
│  │     │  │  │  ├─ memmap.cpython-312.pyc
│  │     │  │  │  ├─ multiarray.cpython-312.pyc
│  │     │  │  │  ├─ numeric.cpython-312.pyc
│  │     │  │  │  ├─ numerictypes.cpython-312.pyc
│  │     │  │  │  ├─ overrides.cpython-312.pyc
│  │     │  │  │  ├─ printoptions.cpython-312.pyc
│  │     │  │  │  ├─ records.cpython-312.pyc
│  │     │  │  │  ├─ shape_base.cpython-312.pyc
│  │     │  │  │  ├─ strings.cpython-312.pyc
│  │     │  │  │  └─ umath.cpython-312.pyc
│  │     │  │  ├─ include/
│  │     │  │  │  └─ numpy/
│  │     │  │  │     ├─ random/
│  │     │  │  │     │  ├─ bitgen.h
│  │     │  │  │     │  ├─ distributions.h
│  │     │  │  │     │  ├─ libdivide.h
│  │     │  │  │     │  └─ LICENSE.txt
│  │     │  │  │     ├─ __multiarray_api.c
│  │     │  │  │     ├─ __multiarray_api.h
│  │     │  │  │     ├─ __ufunc_api.c
│  │     │  │  │     ├─ __ufunc_api.h
│  │     │  │  │     ├─ _neighborhood_iterator_imp.h
│  │     │  │  │     ├─ _numpyconfig.h
│  │     │  │  │     ├─ _public_dtype_api_table.h
│  │     │  │  │     ├─ arrayobject.h
│  │     │  │  │     ├─ arrayscalars.h
│  │     │  │  │     ├─ dtype_api.h
│  │     │  │  │     ├─ halffloat.h
│  │     │  │  │     ├─ ndarrayobject.h
│  │     │  │  │     ├─ ndarraytypes.h
│  │     │  │  │     ├─ npy_2_compat.h
│  │     │  │  │     ├─ npy_2_complexcompat.h
│  │     │  │  │     ├─ npy_3kcompat.h
│  │     │  │  │     ├─ npy_common.h
│  │     │  │  │     ├─ npy_cpu.h
│  │     │  │  │     ├─ npy_endian.h
│  │     │  │  │     ├─ npy_math.h
│  │     │  │  │     ├─ npy_no_deprecated_api.h
│  │     │  │  │     ├─ npy_os.h
│  │     │  │  │     ├─ numpyconfig.h
│  │     │  │  │     ├─ ufuncobject.h
│  │     │  │  │     └─ utils.h
│  │     │  │  ├─ lib/
│  │     │  │  │  ├─ npy-pkg-config/
│  │     │  │  │  │  ├─ mlib.ini
│  │     │  │  │  │  └─ npymath.ini
│  │     │  │  │  ├─ pkgconfig/
│  │     │  │  │  │  └─ numpy.pc
│  │     │  │  │  └─ npymath.lib
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ _locales.cpython-312.pyc
│  │     │  │  │  │  ├─ _natype.cpython-312.pyc
│  │     │  │  │  │  ├─ test__exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_abc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_argparse.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array_api_info.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array_coercion.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array_interface.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arraymethod.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arrayobject.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arrayprint.cpython-312.pyc
│  │     │  │  │  │  ├─ test_casting_floatingpoint_errors.cpython-312.pyc
│  │     │  │  │  │  ├─ test_casting_unittests.cpython-312.pyc
│  │     │  │  │  │  ├─ test_conversion_utils.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cpu_dispatcher.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cpu_features.cpython-312.pyc
│  │     │  │  │  │  ├─ test_custom_dtypes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cython.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_defchararray.cpython-312.pyc
│  │     │  │  │  │  ├─ test_deprecations.cpython-312.pyc
│  │     │  │  │  │  ├─ test_dlpack.cpython-312.pyc
│  │     │  │  │  │  ├─ test_dtype.cpython-312.pyc
│  │     │  │  │  │  ├─ test_einsum.cpython-312.pyc
│  │     │  │  │  │  ├─ test_errstate.cpython-312.pyc
│  │     │  │  │  │  ├─ test_extint128.cpython-312.pyc
│  │     │  │  │  │  ├─ test_function_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_getlimits.cpython-312.pyc
│  │     │  │  │  │  ├─ test_half.cpython-312.pyc
│  │     │  │  │  │  ├─ test_hashtable.cpython-312.pyc
│  │     │  │  │  │  ├─ test_indexerrors.cpython-312.pyc
│  │     │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_item_selection.cpython-312.pyc
│  │     │  │  │  │  ├─ test_limited_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_longdouble.cpython-312.pyc
│  │     │  │  │  │  ├─ test_machar.cpython-312.pyc
│  │     │  │  │  │  ├─ test_mem_overlap.cpython-312.pyc
│  │     │  │  │  │  ├─ test_mem_policy.cpython-312.pyc
│  │     │  │  │  │  ├─ test_memmap.cpython-312.pyc
│  │     │  │  │  │  ├─ test_multiarray.cpython-312.pyc
│  │     │  │  │  │  ├─ test_multithreading.cpython-312.pyc
│  │     │  │  │  │  ├─ test_nditer.cpython-312.pyc
│  │     │  │  │  │  ├─ test_nep50_promotions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numeric.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numerictypes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_overrides.cpython-312.pyc
│  │     │  │  │  │  ├─ test_print.cpython-312.pyc
│  │     │  │  │  │  ├─ test_protocols.cpython-312.pyc
│  │     │  │  │  │  ├─ test_records.cpython-312.pyc
│  │     │  │  │  │  ├─ test_regression.cpython-312.pyc
│  │     │  │  │  │  ├─ test_scalar_ctors.cpython-312.pyc
│  │     │  │  │  │  ├─ test_scalar_methods.cpython-312.pyc
│  │     │  │  │  │  ├─ test_scalarbuffer.cpython-312.pyc
│  │     │  │  │  │  ├─ test_scalarinherit.cpython-312.pyc
│  │     │  │  │  │  ├─ test_scalarmath.cpython-312.pyc
│  │     │  │  │  │  ├─ test_scalarprint.cpython-312.pyc
│  │     │  │  │  │  ├─ test_shape_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_simd_module.cpython-312.pyc
│  │     │  │  │  │  ├─ test_simd.cpython-312.pyc
│  │     │  │  │  │  ├─ test_stringdtype.cpython-312.pyc
│  │     │  │  │  │  ├─ test_strings.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ufunc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_umath_accuracy.cpython-312.pyc
│  │     │  │  │  │  ├─ test_umath_complex.cpython-312.pyc
│  │     │  │  │  │  ├─ test_umath.cpython-312.pyc
│  │     │  │  │  │  └─ test_unicode.cpython-312.pyc
│  │     │  │  │  ├─ data/
│  │     │  │  │  │  ├─ astype_copy.pkl
│  │     │  │  │  │  ├─ generate_umath_validation_data.cpp
│  │     │  │  │  │  ├─ recarray_from_file.fits
│  │     │  │  │  │  ├─ umath-validation-set-arccos.csv
│  │     │  │  │  │  ├─ umath-validation-set-arccosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsin.csv
│  │     │  │  │  │  ├─ umath-validation-set-arcsinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctan.csv
│  │     │  │  │  │  ├─ umath-validation-set-arctanh.csv
│  │     │  │  │  │  ├─ umath-validation-set-cbrt.csv
│  │     │  │  │  │  ├─ umath-validation-set-cos.csv
│  │     │  │  │  │  ├─ umath-validation-set-cosh.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp.csv
│  │     │  │  │  │  ├─ umath-validation-set-exp2.csv
│  │     │  │  │  │  ├─ umath-validation-set-expm1.csv
│  │     │  │  │  │  ├─ umath-validation-set-log.csv
│  │     │  │  │  │  ├─ umath-validation-set-log10.csv
│  │     │  │  │  │  ├─ umath-validation-set-log1p.csv
│  │     │  │  │  │  ├─ umath-validation-set-log2.csv
│  │     │  │  │  │  ├─ umath-validation-set-README.txt
│  │     │  │  │  │  ├─ umath-validation-set-sin.csv
│  │     │  │  │  │  ├─ umath-validation-set-sinh.csv
│  │     │  │  │  │  ├─ umath-validation-set-tan.csv
│  │     │  │  │  │  └─ umath-validation-set-tanh.csv
│  │     │  │  │  ├─ examples/
│  │     │  │  │  │  ├─ cython/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  └─ setup.cpython-312.pyc
│  │     │  │  │  │  │  ├─ checks.pyx
│  │     │  │  │  │  │  ├─ meson.build
│  │     │  │  │  │  │  └─ setup.py
│  │     │  │  │  │  └─ limited_api/
│  │     │  │  │  │     ├─ __pycache__/
│  │     │  │  │  │     │  └─ setup.cpython-312.pyc
│  │     │  │  │  │     ├─ limited_api_latest.c
│  │     │  │  │  │     ├─ limited_api1.c
│  │     │  │  │  │     ├─ limited_api2.pyx
│  │     │  │  │  │     ├─ meson.build
│  │     │  │  │  │     └─ setup.py
│  │     │  │  │  ├─ _locales.py
│  │     │  │  │  ├─ _natype.py
│  │     │  │  │  ├─ test__exceptions.py
│  │     │  │  │  ├─ test_abc.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_argparse.py
│  │     │  │  │  ├─ test_array_api_info.py
│  │     │  │  │  ├─ test_array_coercion.py
│  │     │  │  │  ├─ test_array_interface.py
│  │     │  │  │  ├─ test_arraymethod.py
│  │     │  │  │  ├─ test_arrayobject.py
│  │     │  │  │  ├─ test_arrayprint.py
│  │     │  │  │  ├─ test_casting_floatingpoint_errors.py
│  │     │  │  │  ├─ test_casting_unittests.py
│  │     │  │  │  ├─ test_conversion_utils.py
│  │     │  │  │  ├─ test_cpu_dispatcher.py
│  │     │  │  │  ├─ test_cpu_features.py
│  │     │  │  │  ├─ test_custom_dtypes.py
│  │     │  │  │  ├─ test_cython.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_defchararray.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_dlpack.py
│  │     │  │  │  ├─ test_dtype.py
│  │     │  │  │  ├─ test_einsum.py
│  │     │  │  │  ├─ test_errstate.py
│  │     │  │  │  ├─ test_extint128.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_getlimits.py
│  │     │  │  │  ├─ test_half.py
│  │     │  │  │  ├─ test_hashtable.py
│  │     │  │  │  ├─ test_indexerrors.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_item_selection.py
│  │     │  │  │  ├─ test_limited_api.py
│  │     │  │  │  ├─ test_longdouble.py
│  │     │  │  │  ├─ test_machar.py
│  │     │  │  │  ├─ test_mem_overlap.py
│  │     │  │  │  ├─ test_mem_policy.py
│  │     │  │  │  ├─ test_memmap.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_multithreading.py
│  │     │  │  │  ├─ test_nditer.py
│  │     │  │  │  ├─ test_nep50_promotions.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_numerictypes.py
│  │     │  │  │  ├─ test_overrides.py
│  │     │  │  │  ├─ test_print.py
│  │     │  │  │  ├─ test_protocols.py
│  │     │  │  │  ├─ test_records.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_scalar_ctors.py
│  │     │  │  │  ├─ test_scalar_methods.py
│  │     │  │  │  ├─ test_scalarbuffer.py
│  │     │  │  │  ├─ test_scalarinherit.py
│  │     │  │  │  ├─ test_scalarmath.py
│  │     │  │  │  ├─ test_scalarprint.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_simd_module.py
│  │     │  │  │  ├─ test_simd.py
│  │     │  │  │  ├─ test_stringdtype.py
│  │     │  │  │  ├─ test_strings.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_umath_accuracy.py
│  │     │  │  │  ├─ test_umath_complex.py
│  │     │  │  │  ├─ test_umath.py
│  │     │  │  │  └─ test_unicode.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _add_newdocs_scalars.py
│  │     │  │  ├─ _add_newdocs_scalars.pyi
│  │     │  │  ├─ _add_newdocs.py
│  │     │  │  ├─ _add_newdocs.pyi
│  │     │  │  ├─ _asarray.py
│  │     │  │  ├─ _asarray.pyi
│  │     │  │  ├─ _dtype_ctypes.py
│  │     │  │  ├─ _dtype_ctypes.pyi
│  │     │  │  ├─ _dtype.py
│  │     │  │  ├─ _dtype.pyi
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _exceptions.pyi
│  │     │  │  ├─ _internal.py
│  │     │  │  ├─ _internal.pyi
│  │     │  │  ├─ _machar.py
│  │     │  │  ├─ _machar.pyi
│  │     │  │  ├─ _methods.py
│  │     │  │  ├─ _methods.pyi
│  │     │  │  ├─ _multiarray_tests.cp312-win_amd64.lib
│  │     │  │  ├─ _multiarray_tests.cp312-win_amd64.pyd
│  │     │  │  ├─ _multiarray_umath.cp312-win_amd64.lib
│  │     │  │  ├─ _multiarray_umath.cp312-win_amd64.pyd
│  │     │  │  ├─ _operand_flag_tests.cp312-win_amd64.lib
│  │     │  │  ├─ _operand_flag_tests.cp312-win_amd64.pyd
│  │     │  │  ├─ _rational_tests.cp312-win_amd64.lib
│  │     │  │  ├─ _rational_tests.cp312-win_amd64.pyd
│  │     │  │  ├─ _simd.cp312-win_amd64.lib
│  │     │  │  ├─ _simd.cp312-win_amd64.pyd
│  │     │  │  ├─ _simd.pyi
│  │     │  │  ├─ _string_helpers.py
│  │     │  │  ├─ _string_helpers.pyi
│  │     │  │  ├─ _struct_ufunc_tests.cp312-win_amd64.lib
│  │     │  │  ├─ _struct_ufunc_tests.cp312-win_amd64.pyd
│  │     │  │  ├─ _type_aliases.py
│  │     │  │  ├─ _type_aliases.pyi
│  │     │  │  ├─ _ufunc_config.py
│  │     │  │  ├─ _ufunc_config.pyi
│  │     │  │  ├─ _umath_tests.cp312-win_amd64.lib
│  │     │  │  ├─ _umath_tests.cp312-win_amd64.pyd
│  │     │  │  ├─ arrayprint.py
│  │     │  │  ├─ arrayprint.pyi
│  │     │  │  ├─ cversions.py
│  │     │  │  ├─ defchararray.py
│  │     │  │  ├─ defchararray.pyi
│  │     │  │  ├─ einsumfunc.py
│  │     │  │  ├─ einsumfunc.pyi
│  │     │  │  ├─ fromnumeric.py
│  │     │  │  ├─ fromnumeric.pyi
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ function_base.pyi
│  │     │  │  ├─ getlimits.py
│  │     │  │  ├─ getlimits.pyi
│  │     │  │  ├─ memmap.py
│  │     │  │  ├─ memmap.pyi
│  │     │  │  ├─ multiarray.py
│  │     │  │  ├─ multiarray.pyi
│  │     │  │  ├─ numeric.py
│  │     │  │  ├─ numeric.pyi
│  │     │  │  ├─ numerictypes.py
│  │     │  │  ├─ numerictypes.pyi
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ overrides.pyi
│  │     │  │  ├─ printoptions.py
│  │     │  │  ├─ printoptions.pyi
│  │     │  │  ├─ records.py
│  │     │  │  ├─ records.pyi
│  │     │  │  ├─ shape_base.py
│  │     │  │  ├─ shape_base.pyi
│  │     │  │  ├─ strings.py
│  │     │  │  ├─ strings.pyi
│  │     │  │  ├─ umath.py
│  │     │  │  └─ umath.pyi
│  │     │  ├─ _pyinstaller/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ hook-numpy.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ pyinstaller-smoke.cpython-312.pyc
│  │     │  │  │  │  └─ test_pyinstaller.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ pyinstaller-smoke.py
│  │     │  │  │  └─ test_pyinstaller.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ hook-numpy.py
│  │     │  │  └─ hook-numpy.pyi
│  │     │  ├─ _typing/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _add_docstring.cpython-312.pyc
│  │     │  │  │  ├─ _array_like.cpython-312.pyc
│  │     │  │  │  ├─ _char_codes.cpython-312.pyc
│  │     │  │  │  ├─ _dtype_like.cpython-312.pyc
│  │     │  │  │  ├─ _extended_precision.cpython-312.pyc
│  │     │  │  │  ├─ _nbit_base.cpython-312.pyc
│  │     │  │  │  ├─ _nbit.cpython-312.pyc
│  │     │  │  │  ├─ _nested_sequence.cpython-312.pyc
│  │     │  │  │  ├─ _scalars.cpython-312.pyc
│  │     │  │  │  ├─ _shape.cpython-312.pyc
│  │     │  │  │  └─ _ufunc.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _add_docstring.py
│  │     │  │  ├─ _array_like.py
│  │     │  │  ├─ _callable.pyi
│  │     │  │  ├─ _char_codes.py
│  │     │  │  ├─ _dtype_like.py
│  │     │  │  ├─ _extended_precision.py
│  │     │  │  ├─ _nbit_base.py
│  │     │  │  ├─ _nbit_base.pyi
│  │     │  │  ├─ _nbit.py
│  │     │  │  ├─ _nested_sequence.py
│  │     │  │  ├─ _scalars.py
│  │     │  │  ├─ _shape.py
│  │     │  │  ├─ _ufunc.py
│  │     │  │  └─ _ufunc.pyi
│  │     │  ├─ _utils/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _convertions.cpython-312.pyc
│  │     │  │  │  ├─ _inspect.cpython-312.pyc
│  │     │  │  │  └─ _pep440.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _convertions.py
│  │     │  │  ├─ _convertions.pyi
│  │     │  │  ├─ _inspect.py
│  │     │  │  ├─ _inspect.pyi
│  │     │  │  ├─ _pep440.py
│  │     │  │  └─ _pep440.pyi
│  │     │  ├─ char/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ core/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _dtype_ctypes.cpython-312.pyc
│  │     │  │  │  ├─ _dtype.cpython-312.pyc
│  │     │  │  │  ├─ _internal.cpython-312.pyc
│  │     │  │  │  ├─ _multiarray_umath.cpython-312.pyc
│  │     │  │  │  ├─ _utils.cpython-312.pyc
│  │     │  │  │  ├─ arrayprint.cpython-312.pyc
│  │     │  │  │  ├─ defchararray.cpython-312.pyc
│  │     │  │  │  ├─ einsumfunc.cpython-312.pyc
│  │     │  │  │  ├─ fromnumeric.cpython-312.pyc
│  │     │  │  │  ├─ function_base.cpython-312.pyc
│  │     │  │  │  ├─ getlimits.cpython-312.pyc
│  │     │  │  │  ├─ multiarray.cpython-312.pyc
│  │     │  │  │  ├─ numeric.cpython-312.pyc
│  │     │  │  │  ├─ numerictypes.cpython-312.pyc
│  │     │  │  │  ├─ overrides.cpython-312.pyc
│  │     │  │  │  ├─ records.cpython-312.pyc
│  │     │  │  │  ├─ shape_base.cpython-312.pyc
│  │     │  │  │  └─ umath.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _dtype_ctypes.py
│  │     │  │  ├─ _dtype_ctypes.pyi
│  │     │  │  ├─ _dtype.py
│  │     │  │  ├─ _dtype.pyi
│  │     │  │  ├─ _internal.py
│  │     │  │  ├─ _multiarray_umath.py
│  │     │  │  ├─ _utils.py
│  │     │  │  ├─ arrayprint.py
│  │     │  │  ├─ defchararray.py
│  │     │  │  ├─ einsumfunc.py
│  │     │  │  ├─ fromnumeric.py
│  │     │  │  ├─ function_base.py
│  │     │  │  ├─ getlimits.py
│  │     │  │  ├─ multiarray.py
│  │     │  │  ├─ numeric.py
│  │     │  │  ├─ numerictypes.py
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ overrides.pyi
│  │     │  │  ├─ records.py
│  │     │  │  ├─ shape_base.py
│  │     │  │  └─ umath.py
│  │     │  ├─ ctypeslib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ _ctypeslib.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _ctypeslib.py
│  │     │  │  └─ _ctypeslib.pyi
│  │     │  ├─ doc/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ ufuncs.cpython-312.pyc
│  │     │  │  └─ ufuncs.py
│  │     │  ├─ f2py/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  ├─ __version__.cpython-312.pyc
│  │     │  │  │  ├─ _isocbind.cpython-312.pyc
│  │     │  │  │  ├─ _src_pyf.cpython-312.pyc
│  │     │  │  │  ├─ auxfuncs.cpython-312.pyc
│  │     │  │  │  ├─ capi_maps.cpython-312.pyc
│  │     │  │  │  ├─ cb_rules.cpython-312.pyc
│  │     │  │  │  ├─ cfuncs.cpython-312.pyc
│  │     │  │  │  ├─ common_rules.cpython-312.pyc
│  │     │  │  │  ├─ crackfortran.cpython-312.pyc
│  │     │  │  │  ├─ diagnose.cpython-312.pyc
│  │     │  │  │  ├─ f2py2e.cpython-312.pyc
│  │     │  │  │  ├─ f90mod_rules.cpython-312.pyc
│  │     │  │  │  ├─ func2subr.cpython-312.pyc
│  │     │  │  │  ├─ rules.cpython-312.pyc
│  │     │  │  │  ├─ symbolic.cpython-312.pyc
│  │     │  │  │  └─ use_rules.cpython-312.pyc
│  │     │  │  ├─ _backends/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _backend.cpython-312.pyc
│  │     │  │  │  │  ├─ _distutils.cpython-312.pyc
│  │     │  │  │  │  └─ _meson.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __init__.pyi
│  │     │  │  │  ├─ _backend.py
│  │     │  │  │  ├─ _backend.pyi
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _distutils.pyi
│  │     │  │  │  ├─ _meson.py
│  │     │  │  │  ├─ _meson.pyi
│  │     │  │  │  └─ meson.build.template
│  │     │  │  ├─ src/
│  │     │  │  │  ├─ fortranobject.c
│  │     │  │  │  └─ fortranobject.h
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_abstract_interface.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array_from_pyobj.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assumed_shape.cpython-312.pyc
│  │     │  │  │  │  ├─ test_block_docstring.cpython-312.pyc
│  │     │  │  │  │  ├─ test_callback.cpython-312.pyc
│  │     │  │  │  │  ├─ test_character.cpython-312.pyc
│  │     │  │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_crackfortran.cpython-312.pyc
│  │     │  │  │  │  ├─ test_data.cpython-312.pyc
│  │     │  │  │  │  ├─ test_docs.cpython-312.pyc
│  │     │  │  │  │  ├─ test_f2cmap.cpython-312.pyc
│  │     │  │  │  │  ├─ test_f2py2e.cpython-312.pyc
│  │     │  │  │  │  ├─ test_isoc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_kind.cpython-312.pyc
│  │     │  │  │  │  ├─ test_mixed.cpython-312.pyc
│  │     │  │  │  │  ├─ test_modules.cpython-312.pyc
│  │     │  │  │  │  ├─ test_parameter.cpython-312.pyc
│  │     │  │  │  │  ├─ test_pyf_src.cpython-312.pyc
│  │     │  │  │  │  ├─ test_quoted_character.cpython-312.pyc
│  │     │  │  │  │  ├─ test_regression.cpython-312.pyc
│  │     │  │  │  │  ├─ test_return_character.cpython-312.pyc
│  │     │  │  │  │  ├─ test_return_complex.cpython-312.pyc
│  │     │  │  │  │  ├─ test_return_integer.cpython-312.pyc
│  │     │  │  │  │  ├─ test_return_logical.cpython-312.pyc
│  │     │  │  │  │  ├─ test_return_real.cpython-312.pyc
│  │     │  │  │  │  ├─ test_routines.cpython-312.pyc
│  │     │  │  │  │  ├─ test_semicolon_split.cpython-312.pyc
│  │     │  │  │  │  ├─ test_size.cpython-312.pyc
│  │     │  │  │  │  ├─ test_string.cpython-312.pyc
│  │     │  │  │  │  ├─ test_symbolic.cpython-312.pyc
│  │     │  │  │  │  ├─ test_value_attrspec.cpython-312.pyc
│  │     │  │  │  │  └─ util.cpython-312.pyc
│  │     │  │  │  ├─ src/
│  │     │  │  │  │  ├─ abstract_interface/
│  │     │  │  │  │  │  ├─ foo.f90
│  │     │  │  │  │  │  └─ gh18403_mod.f90
│  │     │  │  │  │  ├─ array_from_pyobj/
│  │     │  │  │  │  │  └─ wrapmodule.c
│  │     │  │  │  │  ├─ assumed_shape/
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  ├─ foo_free.f90
│  │     │  │  │  │  │  ├─ foo_mod.f90
│  │     │  │  │  │  │  ├─ foo_use.f90
│  │     │  │  │  │  │  └─ precision.f90
│  │     │  │  │  │  ├─ block_docstring/
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ callback/
│  │     │  │  │  │  │  ├─ foo.f
│  │     │  │  │  │  │  ├─ gh17797.f90
│  │     │  │  │  │  │  ├─ gh18335.f90
│  │     │  │  │  │  │  ├─ gh25211.f
│  │     │  │  │  │  │  ├─ gh25211.pyf
│  │     │  │  │  │  │  └─ gh26681.f90
│  │     │  │  │  │  ├─ cli/
│  │     │  │  │  │  │  ├─ gh_22819.pyf
│  │     │  │  │  │  │  ├─ hi77.f
│  │     │  │  │  │  │  └─ hiworld.f90
│  │     │  │  │  │  ├─ common/
│  │     │  │  │  │  │  ├─ block.f
│  │     │  │  │  │  │  └─ gh19161.f90
│  │     │  │  │  │  ├─ crackfortran/
│  │     │  │  │  │  │  ├─ accesstype.f90
│  │     │  │  │  │  │  ├─ common_with_division.f
│  │     │  │  │  │  │  ├─ data_common.f
│  │     │  │  │  │  │  ├─ data_multiplier.f
│  │     │  │  │  │  │  ├─ data_stmts.f90
│  │     │  │  │  │  │  ├─ data_with_comments.f
│  │     │  │  │  │  │  ├─ foo_deps.f90
│  │     │  │  │  │  │  ├─ gh15035.f
│  │     │  │  │  │  │  ├─ gh17859.f
│  │     │  │  │  │  │  ├─ gh22648.pyf
│  │     │  │  │  │  │  ├─ gh23533.f
│  │     │  │  │  │  │  ├─ gh23598.f90
│  │     │  │  │  │  │  ├─ gh23598Warn.f90
│  │     │  │  │  │  │  ├─ gh23879.f90
│  │     │  │  │  │  │  ├─ gh27697.f90
│  │     │  │  │  │  │  ├─ gh2848.f90
│  │     │  │  │  │  │  ├─ operators.f90
│  │     │  │  │  │  │  ├─ privatemod.f90
│  │     │  │  │  │  │  ├─ publicmod.f90
│  │     │  │  │  │  │  ├─ pubprivmod.f90
│  │     │  │  │  │  │  └─ unicode_comment.f90
│  │     │  │  │  │  ├─ f2cmap/
│  │     │  │  │  │  │  ├─ .f2py_f2cmap
│  │     │  │  │  │  │  └─ isoFortranEnvMap.f90
│  │     │  │  │  │  ├─ isocintrin/
│  │     │  │  │  │  │  └─ isoCtests.f90
│  │     │  │  │  │  ├─ kind/
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ mixed/
│  │     │  │  │  │  │  ├─ foo_fixed.f90
│  │     │  │  │  │  │  ├─ foo_free.f90
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ modules/
│  │     │  │  │  │  │  ├─ gh25337/
│  │     │  │  │  │  │  │  ├─ data.f90
│  │     │  │  │  │  │  │  └─ use_data.f90
│  │     │  │  │  │  │  ├─ gh26920/
│  │     │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
│  │     │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
│  │     │  │  │  │  │  ├─ module_data_docstring.f90
│  │     │  │  │  │  │  └─ use_modules.f90
│  │     │  │  │  │  ├─ negative_bounds/
│  │     │  │  │  │  │  └─ issue_20853.f90
│  │     │  │  │  │  ├─ parameter/
│  │     │  │  │  │  │  ├─ constant_array.f90
│  │     │  │  │  │  │  ├─ constant_both.f90
│  │     │  │  │  │  │  ├─ constant_compound.f90
│  │     │  │  │  │  │  ├─ constant_integer.f90
│  │     │  │  │  │  │  ├─ constant_non_compound.f90
│  │     │  │  │  │  │  └─ constant_real.f90
│  │     │  │  │  │  ├─ quoted_character/
│  │     │  │  │  │  │  └─ foo.f
│  │     │  │  │  │  ├─ regression/
│  │     │  │  │  │  │  ├─ AB.inc
│  │     │  │  │  │  │  ├─ assignOnlyModule.f90
│  │     │  │  │  │  │  ├─ datonly.f90
│  │     │  │  │  │  │  ├─ f77comments.f
│  │     │  │  │  │  │  ├─ f77fixedform.f95
│  │     │  │  │  │  │  ├─ f90continuation.f90
│  │     │  │  │  │  │  ├─ incfile.f90
│  │     │  │  │  │  │  ├─ inout.f90
│  │     │  │  │  │  │  ├─ lower_f2py_fortran.f90
│  │     │  │  │  │  │  └─ mod_derived_types.f90
│  │     │  │  │  │  ├─ return_character/
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_complex/
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_integer/
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_logical/
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ return_real/
│  │     │  │  │  │  │  ├─ foo77.f
│  │     │  │  │  │  │  └─ foo90.f90
│  │     │  │  │  │  ├─ routines/
│  │     │  │  │  │  │  ├─ funcfortranname.f
│  │     │  │  │  │  │  ├─ funcfortranname.pyf
│  │     │  │  │  │  │  ├─ subrout.f
│  │     │  │  │  │  │  └─ subrout.pyf
│  │     │  │  │  │  ├─ size/
│  │     │  │  │  │  │  └─ foo.f90
│  │     │  │  │  │  ├─ string/
│  │     │  │  │  │  │  ├─ char.f90
│  │     │  │  │  │  │  ├─ fixed_string.f90
│  │     │  │  │  │  │  ├─ gh24008.f
│  │     │  │  │  │  │  ├─ gh24662.f90
│  │     │  │  │  │  │  ├─ gh25286_bc.pyf
│  │     │  │  │  │  │  ├─ gh25286.f90
│  │     │  │  │  │  │  ├─ gh25286.pyf
│  │     │  │  │  │  │  ├─ scalar_string.f90
│  │     │  │  │  │  │  └─ string.f
│  │     │  │  │  │  └─ value_attrspec/
│  │     │  │  │  │     └─ gh21665.f90
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_abstract_interface.py
│  │     │  │  │  ├─ test_array_from_pyobj.py
│  │     │  │  │  ├─ test_assumed_shape.py
│  │     │  │  │  ├─ test_block_docstring.py
│  │     │  │  │  ├─ test_callback.py
│  │     │  │  │  ├─ test_character.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_crackfortran.py
│  │     │  │  │  ├─ test_data.py
│  │     │  │  │  ├─ test_docs.py
│  │     │  │  │  ├─ test_f2cmap.py
│  │     │  │  │  ├─ test_f2py2e.py
│  │     │  │  │  ├─ test_isoc.py
│  │     │  │  │  ├─ test_kind.py
│  │     │  │  │  ├─ test_mixed.py
│  │     │  │  │  ├─ test_modules.py
│  │     │  │  │  ├─ test_parameter.py
│  │     │  │  │  ├─ test_pyf_src.py
│  │     │  │  │  ├─ test_quoted_character.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_return_character.py
│  │     │  │  │  ├─ test_return_complex.py
│  │     │  │  │  ├─ test_return_integer.py
│  │     │  │  │  ├─ test_return_logical.py
│  │     │  │  │  ├─ test_return_real.py
│  │     │  │  │  ├─ test_routines.py
│  │     │  │  │  ├─ test_semicolon_split.py
│  │     │  │  │  ├─ test_size.py
│  │     │  │  │  ├─ test_string.py
│  │     │  │  │  ├─ test_symbolic.py
│  │     │  │  │  ├─ test_value_attrspec.py
│  │     │  │  │  └─ util.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ __main__.py
│  │     │  │  ├─ __version__.py
│  │     │  │  ├─ __version__.pyi
│  │     │  │  ├─ _isocbind.py
│  │     │  │  ├─ _isocbind.pyi
│  │     │  │  ├─ _src_pyf.py
│  │     │  │  ├─ _src_pyf.pyi
│  │     │  │  ├─ auxfuncs.py
│  │     │  │  ├─ auxfuncs.pyi
│  │     │  │  ├─ capi_maps.py
│  │     │  │  ├─ capi_maps.pyi
│  │     │  │  ├─ cb_rules.py
│  │     │  │  ├─ cb_rules.pyi
│  │     │  │  ├─ cfuncs.py
│  │     │  │  ├─ cfuncs.pyi
│  │     │  │  ├─ common_rules.py
│  │     │  │  ├─ common_rules.pyi
│  │     │  │  ├─ crackfortran.py
│  │     │  │  ├─ crackfortran.pyi
│  │     │  │  ├─ diagnose.py
│  │     │  │  ├─ diagnose.pyi
│  │     │  │  ├─ f2py2e.py
│  │     │  │  ├─ f2py2e.pyi
│  │     │  │  ├─ f90mod_rules.py
│  │     │  │  ├─ f90mod_rules.pyi
│  │     │  │  ├─ func2subr.py
│  │     │  │  ├─ func2subr.pyi
│  │     │  │  ├─ rules.py
│  │     │  │  ├─ rules.pyi
│  │     │  │  ├─ setup.cfg
│  │     │  │  ├─ symbolic.py
│  │     │  │  ├─ symbolic.pyi
│  │     │  │  ├─ use_rules.py
│  │     │  │  └─ use_rules.pyi
│  │     │  ├─ fft/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _helper.cpython-312.pyc
│  │     │  │  │  ├─ _pocketfft.cpython-312.pyc
│  │     │  │  │  └─ helper.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_helper.cpython-312.pyc
│  │     │  │  │  │  └─ test_pocketfft.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_helper.py
│  │     │  │  │  └─ test_pocketfft.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _helper.py
│  │     │  │  ├─ _helper.pyi
│  │     │  │  ├─ _pocketfft_umath.cp312-win_amd64.lib
│  │     │  │  ├─ _pocketfft_umath.cp312-win_amd64.pyd
│  │     │  │  ├─ _pocketfft.py
│  │     │  │  ├─ _pocketfft.pyi
│  │     │  │  ├─ helper.py
│  │     │  │  └─ helper.pyi
│  │     │  ├─ lib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _array_utils_impl.cpython-312.pyc
│  │     │  │  │  ├─ _arraypad_impl.cpython-312.pyc
│  │     │  │  │  ├─ _arraysetops_impl.cpython-312.pyc
│  │     │  │  │  ├─ _arrayterator_impl.cpython-312.pyc
│  │     │  │  │  ├─ _datasource.cpython-312.pyc
│  │     │  │  │  ├─ _format_impl.cpython-312.pyc
│  │     │  │  │  ├─ _function_base_impl.cpython-312.pyc
│  │     │  │  │  ├─ _histograms_impl.cpython-312.pyc
│  │     │  │  │  ├─ _index_tricks_impl.cpython-312.pyc
│  │     │  │  │  ├─ _iotools.cpython-312.pyc
│  │     │  │  │  ├─ _nanfunctions_impl.cpython-312.pyc
│  │     │  │  │  ├─ _npyio_impl.cpython-312.pyc
│  │     │  │  │  ├─ _polynomial_impl.cpython-312.pyc
│  │     │  │  │  ├─ _scimath_impl.cpython-312.pyc
│  │     │  │  │  ├─ _shape_base_impl.cpython-312.pyc
│  │     │  │  │  ├─ _stride_tricks_impl.cpython-312.pyc
│  │     │  │  │  ├─ _twodim_base_impl.cpython-312.pyc
│  │     │  │  │  ├─ _type_check_impl.cpython-312.pyc
│  │     │  │  │  ├─ _ufunclike_impl.cpython-312.pyc
│  │     │  │  │  ├─ _user_array_impl.cpython-312.pyc
│  │     │  │  │  ├─ _utils_impl.cpython-312.pyc
│  │     │  │  │  ├─ _version.cpython-312.pyc
│  │     │  │  │  ├─ array_utils.cpython-312.pyc
│  │     │  │  │  ├─ format.cpython-312.pyc
│  │     │  │  │  ├─ introspect.cpython-312.pyc
│  │     │  │  │  ├─ mixins.cpython-312.pyc
│  │     │  │  │  ├─ npyio.cpython-312.pyc
│  │     │  │  │  ├─ recfunctions.cpython-312.pyc
│  │     │  │  │  ├─ scimath.cpython-312.pyc
│  │     │  │  │  ├─ stride_tricks.cpython-312.pyc
│  │     │  │  │  └─ user_array.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test__datasource.cpython-312.pyc
│  │     │  │  │  │  ├─ test__iotools.cpython-312.pyc
│  │     │  │  │  │  ├─ test__version.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array_utils.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arraypad.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arraysetops.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arrayterator.cpython-312.pyc
│  │     │  │  │  │  ├─ test_format.cpython-312.pyc
│  │     │  │  │  │  ├─ test_function_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_histograms.cpython-312.pyc
│  │     │  │  │  │  ├─ test_index_tricks.cpython-312.pyc
│  │     │  │  │  │  ├─ test_io.cpython-312.pyc
│  │     │  │  │  │  ├─ test_loadtxt.cpython-312.pyc
│  │     │  │  │  │  ├─ test_mixins.cpython-312.pyc
│  │     │  │  │  │  ├─ test_nanfunctions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_packbits.cpython-312.pyc
│  │     │  │  │  │  ├─ test_polynomial.cpython-312.pyc
│  │     │  │  │  │  ├─ test_recfunctions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_regression.cpython-312.pyc
│  │     │  │  │  │  ├─ test_shape_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_stride_tricks.cpython-312.pyc
│  │     │  │  │  │  ├─ test_twodim_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_type_check.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ufunclike.cpython-312.pyc
│  │     │  │  │  │  └─ test_utils.cpython-312.pyc
│  │     │  │  │  ├─ data/
│  │     │  │  │  │  ├─ py2-np0-objarr.npy
│  │     │  │  │  │  ├─ py2-objarr.npy
│  │     │  │  │  │  ├─ py2-objarr.npz
│  │     │  │  │  │  ├─ py3-objarr.npy
│  │     │  │  │  │  ├─ py3-objarr.npz
│  │     │  │  │  │  ├─ python3.npy
│  │     │  │  │  │  └─ win64python2.npy
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test__datasource.py
│  │     │  │  │  ├─ test__iotools.py
│  │     │  │  │  ├─ test__version.py
│  │     │  │  │  ├─ test_array_utils.py
│  │     │  │  │  ├─ test_arraypad.py
│  │     │  │  │  ├─ test_arraysetops.py
│  │     │  │  │  ├─ test_arrayterator.py
│  │     │  │  │  ├─ test_format.py
│  │     │  │  │  ├─ test_function_base.py
│  │     │  │  │  ├─ test_histograms.py
│  │     │  │  │  ├─ test_index_tricks.py
│  │     │  │  │  ├─ test_io.py
│  │     │  │  │  ├─ test_loadtxt.py
│  │     │  │  │  ├─ test_mixins.py
│  │     │  │  │  ├─ test_nanfunctions.py
│  │     │  │  │  ├─ test_packbits.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_recfunctions.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_shape_base.py
│  │     │  │  │  ├─ test_stride_tricks.py
│  │     │  │  │  ├─ test_twodim_base.py
│  │     │  │  │  ├─ test_type_check.py
│  │     │  │  │  ├─ test_ufunclike.py
│  │     │  │  │  └─ test_utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _array_utils_impl.py
│  │     │  │  ├─ _array_utils_impl.pyi
│  │     │  │  ├─ _arraypad_impl.py
│  │     │  │  ├─ _arraypad_impl.pyi
│  │     │  │  ├─ _arraysetops_impl.py
│  │     │  │  ├─ _arraysetops_impl.pyi
│  │     │  │  ├─ _arrayterator_impl.py
│  │     │  │  ├─ _arrayterator_impl.pyi
│  │     │  │  ├─ _datasource.py
│  │     │  │  ├─ _datasource.pyi
│  │     │  │  ├─ _format_impl.py
│  │     │  │  ├─ _format_impl.pyi
│  │     │  │  ├─ _function_base_impl.py
│  │     │  │  ├─ _function_base_impl.pyi
│  │     │  │  ├─ _histograms_impl.py
│  │     │  │  ├─ _histograms_impl.pyi
│  │     │  │  ├─ _index_tricks_impl.py
│  │     │  │  ├─ _index_tricks_impl.pyi
│  │     │  │  ├─ _iotools.py
│  │     │  │  ├─ _iotools.pyi
│  │     │  │  ├─ _nanfunctions_impl.py
│  │     │  │  ├─ _nanfunctions_impl.pyi
│  │     │  │  ├─ _npyio_impl.py
│  │     │  │  ├─ _npyio_impl.pyi
│  │     │  │  ├─ _polynomial_impl.py
│  │     │  │  ├─ _polynomial_impl.pyi
│  │     │  │  ├─ _scimath_impl.py
│  │     │  │  ├─ _scimath_impl.pyi
│  │     │  │  ├─ _shape_base_impl.py
│  │     │  │  ├─ _shape_base_impl.pyi
│  │     │  │  ├─ _stride_tricks_impl.py
│  │     │  │  ├─ _stride_tricks_impl.pyi
│  │     │  │  ├─ _twodim_base_impl.py
│  │     │  │  ├─ _twodim_base_impl.pyi
│  │     │  │  ├─ _type_check_impl.py
│  │     │  │  ├─ _type_check_impl.pyi
│  │     │  │  ├─ _ufunclike_impl.py
│  │     │  │  ├─ _ufunclike_impl.pyi
│  │     │  │  ├─ _user_array_impl.py
│  │     │  │  ├─ _user_array_impl.pyi
│  │     │  │  ├─ _utils_impl.py
│  │     │  │  ├─ _utils_impl.pyi
│  │     │  │  ├─ _version.py
│  │     │  │  ├─ _version.pyi
│  │     │  │  ├─ array_utils.py
│  │     │  │  ├─ array_utils.pyi
│  │     │  │  ├─ format.py
│  │     │  │  ├─ format.pyi
│  │     │  │  ├─ introspect.py
│  │     │  │  ├─ introspect.pyi
│  │     │  │  ├─ mixins.py
│  │     │  │  ├─ mixins.pyi
│  │     │  │  ├─ npyio.py
│  │     │  │  ├─ npyio.pyi
│  │     │  │  ├─ recfunctions.py
│  │     │  │  ├─ recfunctions.pyi
│  │     │  │  ├─ scimath.py
│  │     │  │  ├─ scimath.pyi
│  │     │  │  ├─ stride_tricks.py
│  │     │  │  ├─ stride_tricks.pyi
│  │     │  │  ├─ user_array.py
│  │     │  │  └─ user_array.pyi
│  │     │  ├─ linalg/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _linalg.cpython-312.pyc
│  │     │  │  │  └─ linalg.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_deprecations.cpython-312.pyc
│  │     │  │  │  │  ├─ test_linalg.cpython-312.pyc
│  │     │  │  │  │  └─ test_regression.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_linalg.py
│  │     │  │  │  └─ test_regression.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _linalg.py
│  │     │  │  ├─ _linalg.pyi
│  │     │  │  ├─ _umath_linalg.cp312-win_amd64.lib
│  │     │  │  ├─ _umath_linalg.cp312-win_amd64.pyd
│  │     │  │  ├─ _umath_linalg.pyi
│  │     │  │  ├─ lapack_lite.cp312-win_amd64.lib
│  │     │  │  ├─ lapack_lite.cp312-win_amd64.pyd
│  │     │  │  ├─ lapack_lite.pyi
│  │     │  │  ├─ linalg.py
│  │     │  │  └─ linalg.pyi
│  │     │  ├─ ma/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ core.cpython-312.pyc
│  │     │  │  │  ├─ extras.cpython-312.pyc
│  │     │  │  │  ├─ mrecords.cpython-312.pyc
│  │     │  │  │  └─ testutils.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arrayobject.cpython-312.pyc
│  │     │  │  │  │  ├─ test_core.cpython-312.pyc
│  │     │  │  │  │  ├─ test_deprecations.cpython-312.pyc
│  │     │  │  │  │  ├─ test_extras.cpython-312.pyc
│  │     │  │  │  │  ├─ test_mrecords.cpython-312.pyc
│  │     │  │  │  │  ├─ test_old_ma.cpython-312.pyc
│  │     │  │  │  │  ├─ test_regression.cpython-312.pyc
│  │     │  │  │  │  └─ test_subclassing.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_arrayobject.py
│  │     │  │  │  ├─ test_core.py
│  │     │  │  │  ├─ test_deprecations.py
│  │     │  │  │  ├─ test_extras.py
│  │     │  │  │  ├─ test_mrecords.py
│  │     │  │  │  ├─ test_old_ma.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  └─ test_subclassing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ API_CHANGES.txt
│  │     │  │  ├─ core.py
│  │     │  │  ├─ core.pyi
│  │     │  │  ├─ extras.py
│  │     │  │  ├─ extras.pyi
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ mrecords.py
│  │     │  │  ├─ mrecords.pyi
│  │     │  │  ├─ README.rst
│  │     │  │  └─ testutils.py
│  │     │  ├─ matrixlib/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ defmatrix.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_defmatrix.cpython-312.pyc
│  │     │  │  │  │  ├─ test_interaction.cpython-312.pyc
│  │     │  │  │  │  ├─ test_masked_matrix.cpython-312.pyc
│  │     │  │  │  │  ├─ test_matrix_linalg.cpython-312.pyc
│  │     │  │  │  │  ├─ test_multiarray.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numeric.cpython-312.pyc
│  │     │  │  │  │  └─ test_regression.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_defmatrix.py
│  │     │  │  │  ├─ test_interaction.py
│  │     │  │  │  ├─ test_masked_matrix.py
│  │     │  │  │  ├─ test_matrix_linalg.py
│  │     │  │  │  ├─ test_multiarray.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  └─ test_regression.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ defmatrix.py
│  │     │  │  └─ defmatrix.pyi
│  │     │  ├─ polynomial/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _polybase.cpython-312.pyc
│  │     │  │  │  ├─ chebyshev.cpython-312.pyc
│  │     │  │  │  ├─ hermite_e.cpython-312.pyc
│  │     │  │  │  ├─ hermite.cpython-312.pyc
│  │     │  │  │  ├─ laguerre.cpython-312.pyc
│  │     │  │  │  ├─ legendre.cpython-312.pyc
│  │     │  │  │  ├─ polynomial.cpython-312.pyc
│  │     │  │  │  └─ polyutils.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_chebyshev.cpython-312.pyc
│  │     │  │  │  │  ├─ test_classes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_hermite_e.cpython-312.pyc
│  │     │  │  │  │  ├─ test_hermite.cpython-312.pyc
│  │     │  │  │  │  ├─ test_laguerre.cpython-312.pyc
│  │     │  │  │  │  ├─ test_legendre.cpython-312.pyc
│  │     │  │  │  │  ├─ test_polynomial.cpython-312.pyc
│  │     │  │  │  │  ├─ test_polyutils.cpython-312.pyc
│  │     │  │  │  │  ├─ test_printing.cpython-312.pyc
│  │     │  │  │  │  └─ test_symbol.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_chebyshev.py
│  │     │  │  │  ├─ test_classes.py
│  │     │  │  │  ├─ test_hermite_e.py
│  │     │  │  │  ├─ test_hermite.py
│  │     │  │  │  ├─ test_laguerre.py
│  │     │  │  │  ├─ test_legendre.py
│  │     │  │  │  ├─ test_polynomial.py
│  │     │  │  │  ├─ test_polyutils.py
│  │     │  │  │  ├─ test_printing.py
│  │     │  │  │  └─ test_symbol.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _polybase.py
│  │     │  │  ├─ _polybase.pyi
│  │     │  │  ├─ _polytypes.pyi
│  │     │  │  ├─ chebyshev.py
│  │     │  │  ├─ chebyshev.pyi
│  │     │  │  ├─ hermite_e.py
│  │     │  │  ├─ hermite_e.pyi
│  │     │  │  ├─ hermite.py
│  │     │  │  ├─ hermite.pyi
│  │     │  │  ├─ laguerre.py
│  │     │  │  ├─ laguerre.pyi
│  │     │  │  ├─ legendre.py
│  │     │  │  ├─ legendre.pyi
│  │     │  │  ├─ polynomial.py
│  │     │  │  ├─ polynomial.pyi
│  │     │  │  ├─ polyutils.py
│  │     │  │  └─ polyutils.pyi
│  │     │  ├─ random/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ _pickle.cpython-312.pyc
│  │     │  │  ├─ _examples/
│  │     │  │  │  ├─ cffi/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ extending.cpython-312.pyc
│  │     │  │  │  │  │  └─ parse.cpython-312.pyc
│  │     │  │  │  │  ├─ extending.py
│  │     │  │  │  │  └─ parse.py
│  │     │  │  │  ├─ cython/
│  │     │  │  │  │  ├─ extending_distributions.pyx
│  │     │  │  │  │  ├─ extending.pyx
│  │     │  │  │  │  └─ meson.build
│  │     │  │  │  └─ numba/
│  │     │  │  │     ├─ __pycache__/
│  │     │  │  │     │  ├─ extending_distributions.cpython-312.pyc
│  │     │  │  │     │  └─ extending.cpython-312.pyc
│  │     │  │  │     ├─ extending_distributions.py
│  │     │  │  │     └─ extending.py
│  │     │  │  ├─ lib/
│  │     │  │  │  └─ npyrandom.lib
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_direct.cpython-312.pyc
│  │     │  │  │  │  ├─ test_extending.cpython-312.pyc
│  │     │  │  │  │  ├─ test_generator_mt19937_regressions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_generator_mt19937.cpython-312.pyc
│  │     │  │  │  │  ├─ test_random.cpython-312.pyc
│  │     │  │  │  │  ├─ test_randomstate_regression.cpython-312.pyc
│  │     │  │  │  │  ├─ test_randomstate.cpython-312.pyc
│  │     │  │  │  │  ├─ test_regression.cpython-312.pyc
│  │     │  │  │  │  ├─ test_seed_sequence.cpython-312.pyc
│  │     │  │  │  │  └─ test_smoke.cpython-312.pyc
│  │     │  │  │  ├─ data/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ generator_pcg64_np121.pkl.gz
│  │     │  │  │  │  ├─ generator_pcg64_np126.pkl.gz
│  │     │  │  │  │  ├─ mt19937-testset-1.csv
│  │     │  │  │  │  ├─ mt19937-testset-2.csv
│  │     │  │  │  │  ├─ pcg64-testset-1.csv
│  │     │  │  │  │  ├─ pcg64-testset-2.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-1.csv
│  │     │  │  │  │  ├─ pcg64dxsm-testset-2.csv
│  │     │  │  │  │  ├─ philox-testset-1.csv
│  │     │  │  │  │  ├─ philox-testset-2.csv
│  │     │  │  │  │  ├─ sfc64_np126.pkl.gz
│  │     │  │  │  │  ├─ sfc64-testset-1.csv
│  │     │  │  │  │  └─ sfc64-testset-2.csv
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_direct.py
│  │     │  │  │  ├─ test_extending.py
│  │     │  │  │  ├─ test_generator_mt19937_regressions.py
│  │     │  │  │  ├─ test_generator_mt19937.py
│  │     │  │  │  ├─ test_random.py
│  │     │  │  │  ├─ test_randomstate_regression.py
│  │     │  │  │  ├─ test_randomstate.py
│  │     │  │  │  ├─ test_regression.py
│  │     │  │  │  ├─ test_seed_sequence.py
│  │     │  │  │  └─ test_smoke.py
│  │     │  │  ├─ __init__.pxd
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ _bounded_integers.cp312-win_amd64.lib
│  │     │  │  ├─ _bounded_integers.cp312-win_amd64.pyd
│  │     │  │  ├─ _bounded_integers.pxd
│  │     │  │  ├─ _bounded_integers.pyi
│  │     │  │  ├─ _common.cp312-win_amd64.lib
│  │     │  │  ├─ _common.cp312-win_amd64.pyd
│  │     │  │  ├─ _common.pxd
│  │     │  │  ├─ _common.pyi
│  │     │  │  ├─ _generator.cp312-win_amd64.lib
│  │     │  │  ├─ _generator.cp312-win_amd64.pyd
│  │     │  │  ├─ _generator.pyi
│  │     │  │  ├─ _mt19937.cp312-win_amd64.lib
│  │     │  │  ├─ _mt19937.cp312-win_amd64.pyd
│  │     │  │  ├─ _mt19937.pyi
│  │     │  │  ├─ _pcg64.cp312-win_amd64.lib
│  │     │  │  ├─ _pcg64.cp312-win_amd64.pyd
│  │     │  │  ├─ _pcg64.pyi
│  │     │  │  ├─ _philox.cp312-win_amd64.lib
│  │     │  │  ├─ _philox.cp312-win_amd64.pyd
│  │     │  │  ├─ _philox.pyi
│  │     │  │  ├─ _pickle.py
│  │     │  │  ├─ _pickle.pyi
│  │     │  │  ├─ _sfc64.cp312-win_amd64.lib
│  │     │  │  ├─ _sfc64.cp312-win_amd64.pyd
│  │     │  │  ├─ _sfc64.pyi
│  │     │  │  ├─ bit_generator.cp312-win_amd64.lib
│  │     │  │  ├─ bit_generator.cp312-win_amd64.pyd
│  │     │  │  ├─ bit_generator.pxd
│  │     │  │  ├─ bit_generator.pyi
│  │     │  │  ├─ c_distributions.pxd
│  │     │  │  ├─ LICENSE.md
│  │     │  │  ├─ mtrand.cp312-win_amd64.lib
│  │     │  │  ├─ mtrand.cp312-win_amd64.pyd
│  │     │  │  └─ mtrand.pyi
│  │     │  ├─ rec/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ strings/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ __init__.pyi
│  │     │  ├─ testing/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ overrides.cpython-312.pyc
│  │     │  │  │  └─ print_coercion_tables.cpython-312.pyc
│  │     │  │  ├─ _private/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ extbuild.cpython-312.pyc
│  │     │  │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __init__.pyi
│  │     │  │  │  ├─ extbuild.py
│  │     │  │  │  ├─ extbuild.pyi
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ utils.pyi
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ test_utils.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ test_utils.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ __init__.pyi
│  │     │  │  ├─ overrides.py
│  │     │  │  ├─ overrides.pyi
│  │     │  │  ├─ print_coercion_tables.py
│  │     │  │  └─ print_coercion_tables.pyi
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ test__all__.cpython-312.pyc
│  │     │  │  │  ├─ test_configtool.cpython-312.pyc
│  │     │  │  │  ├─ test_ctypeslib.cpython-312.pyc
│  │     │  │  │  ├─ test_lazyloading.cpython-312.pyc
│  │     │  │  │  ├─ test_matlib.cpython-312.pyc
│  │     │  │  │  ├─ test_numpy_config.cpython-312.pyc
│  │     │  │  │  ├─ test_numpy_version.cpython-312.pyc
│  │     │  │  │  ├─ test_public_api.cpython-312.pyc
│  │     │  │  │  ├─ test_reloading.cpython-312.pyc
│  │     │  │  │  ├─ test_scripts.cpython-312.pyc
│  │     │  │  │  └─ test_warnings.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ test__all__.py
│  │     │  │  ├─ test_configtool.py
│  │     │  │  ├─ test_ctypeslib.py
│  │     │  │  ├─ test_lazyloading.py
│  │     │  │  ├─ test_matlib.py
│  │     │  │  ├─ test_numpy_config.py
│  │     │  │  ├─ test_numpy_version.py
│  │     │  │  ├─ test_public_api.py
│  │     │  │  ├─ test_reloading.py
│  │     │  │  ├─ test_scripts.py
│  │     │  │  └─ test_warnings.py
│  │     │  ├─ typing/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ mypy_plugin.cpython-312.pyc
│  │     │  │  ├─ tests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_isfile.cpython-312.pyc
│  │     │  │  │  │  ├─ test_runtime.cpython-312.pyc
│  │     │  │  │  │  └─ test_typing.cpython-312.pyc
│  │     │  │  │  ├─ data/
│  │     │  │  │  │  ├─ fail/
│  │     │  │  │  │  │  ├─ arithmetic.pyi
│  │     │  │  │  │  │  ├─ array_constructors.pyi
│  │     │  │  │  │  │  ├─ array_like.pyi
│  │     │  │  │  │  │  ├─ array_pad.pyi
│  │     │  │  │  │  │  ├─ arrayprint.pyi
│  │     │  │  │  │  │  ├─ arrayterator.pyi
│  │     │  │  │  │  │  ├─ bitwise_ops.pyi
│  │     │  │  │  │  │  ├─ char.pyi
│  │     │  │  │  │  │  ├─ chararray.pyi
│  │     │  │  │  │  │  ├─ comparisons.pyi
│  │     │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  ├─ datasource.pyi
│  │     │  │  │  │  │  ├─ dtype.pyi
│  │     │  │  │  │  │  ├─ einsumfunc.pyi
│  │     │  │  │  │  │  ├─ flatiter.pyi
│  │     │  │  │  │  │  ├─ fromnumeric.pyi
│  │     │  │  │  │  │  ├─ histograms.pyi
│  │     │  │  │  │  │  ├─ index_tricks.pyi
│  │     │  │  │  │  │  ├─ lib_function_base.pyi
│  │     │  │  │  │  │  ├─ lib_polynomial.pyi
│  │     │  │  │  │  │  ├─ lib_utils.pyi
│  │     │  │  │  │  │  ├─ lib_version.pyi
│  │     │  │  │  │  │  ├─ linalg.pyi
│  │     │  │  │  │  │  ├─ ma.pyi
│  │     │  │  │  │  │  ├─ memmap.pyi
│  │     │  │  │  │  │  ├─ modules.pyi
│  │     │  │  │  │  │  ├─ multiarray.pyi
│  │     │  │  │  │  │  ├─ ndarray_misc.pyi
│  │     │  │  │  │  │  ├─ ndarray.pyi
│  │     │  │  │  │  │  ├─ nditer.pyi
│  │     │  │  │  │  │  ├─ nested_sequence.pyi
│  │     │  │  │  │  │  ├─ npyio.pyi
│  │     │  │  │  │  │  ├─ numerictypes.pyi
│  │     │  │  │  │  │  ├─ random.pyi
│  │     │  │  │  │  │  ├─ rec.pyi
│  │     │  │  │  │  │  ├─ scalars.pyi
│  │     │  │  │  │  │  ├─ shape_base.pyi
│  │     │  │  │  │  │  ├─ shape.pyi
│  │     │  │  │  │  │  ├─ stride_tricks.pyi
│  │     │  │  │  │  │  ├─ strings.pyi
│  │     │  │  │  │  │  ├─ testing.pyi
│  │     │  │  │  │  │  ├─ twodim_base.pyi
│  │     │  │  │  │  │  ├─ type_check.pyi
│  │     │  │  │  │  │  ├─ ufunc_config.pyi
│  │     │  │  │  │  │  ├─ ufunclike.pyi
│  │     │  │  │  │  │  ├─ ufuncs.pyi
│  │     │  │  │  │  │  └─ warnings_and_errors.pyi
│  │     │  │  │  │  ├─ misc/
│  │     │  │  │  │  │  └─ extended_precision.pyi
│  │     │  │  │  │  ├─ pass/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ array_constructors.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ array_like.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ arrayprint.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ arrayterator.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ bitwise_ops.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ comparisons.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ dtype.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ einsumfunc.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ flatiter.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ fromnumeric.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ index_tricks.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ lib_user_array.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ lib_utils.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ lib_version.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ literal.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ ma.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ mod.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ modules.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ multiarray.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ ndarray_conversion.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ ndarray_misc.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ ndarray_shape_manipulation.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ nditer.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ numeric.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ numerictypes.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ random.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ recfunctions.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ scalars.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ shape.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ simple_py3.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ simple.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ ufunc_config.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ ufunclike.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ ufuncs.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ warnings_and_errors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ arithmetic.py
│  │     │  │  │  │  │  ├─ array_constructors.py
│  │     │  │  │  │  │  ├─ array_like.py
│  │     │  │  │  │  │  ├─ arrayprint.py
│  │     │  │  │  │  │  ├─ arrayterator.py
│  │     │  │  │  │  │  ├─ bitwise_ops.py
│  │     │  │  │  │  │  ├─ comparisons.py
│  │     │  │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  │  ├─ einsumfunc.py
│  │     │  │  │  │  │  ├─ flatiter.py
│  │     │  │  │  │  │  ├─ fromnumeric.py
│  │     │  │  │  │  │  ├─ index_tricks.py
│  │     │  │  │  │  │  ├─ lib_user_array.py
│  │     │  │  │  │  │  ├─ lib_utils.py
│  │     │  │  │  │  │  ├─ lib_version.py
│  │     │  │  │  │  │  ├─ literal.py
│  │     │  │  │  │  │  ├─ ma.py
│  │     │  │  │  │  │  ├─ mod.py
│  │     │  │  │  │  │  ├─ modules.py
│  │     │  │  │  │  │  ├─ multiarray.py
│  │     │  │  │  │  │  ├─ ndarray_conversion.py
│  │     │  │  │  │  │  ├─ ndarray_misc.py
│  │     │  │  │  │  │  ├─ ndarray_shape_manipulation.py
│  │     │  │  │  │  │  ├─ nditer.py
│  │     │  │  │  │  │  ├─ numeric.py
│  │     │  │  │  │  │  ├─ numerictypes.py
│  │     │  │  │  │  │  ├─ random.py
│  │     │  │  │  │  │  ├─ recfunctions.py
│  │     │  │  │  │  │  ├─ scalars.py
│  │     │  │  │  │  │  ├─ shape.py
│  │     │  │  │  │  │  ├─ simple_py3.py
│  │     │  │  │  │  │  ├─ simple.py
│  │     │  │  │  │  │  ├─ ufunc_config.py
│  │     │  │  │  │  │  ├─ ufunclike.py
│  │     │  │  │  │  │  ├─ ufuncs.py
│  │     │  │  │  │  │  └─ warnings_and_errors.py
│  │     │  │  │  │  ├─ reveal/
│  │     │  │  │  │  │  ├─ arithmetic.pyi
│  │     │  │  │  │  │  ├─ array_api_info.pyi
│  │     │  │  │  │  │  ├─ array_constructors.pyi
│  │     │  │  │  │  │  ├─ arraypad.pyi
│  │     │  │  │  │  │  ├─ arrayprint.pyi
│  │     │  │  │  │  │  ├─ arraysetops.pyi
│  │     │  │  │  │  │  ├─ arrayterator.pyi
│  │     │  │  │  │  │  ├─ bitwise_ops.pyi
│  │     │  │  │  │  │  ├─ char.pyi
│  │     │  │  │  │  │  ├─ chararray.pyi
│  │     │  │  │  │  │  ├─ comparisons.pyi
│  │     │  │  │  │  │  ├─ constants.pyi
│  │     │  │  │  │  │  ├─ ctypeslib.pyi
│  │     │  │  │  │  │  ├─ datasource.pyi
│  │     │  │  │  │  │  ├─ dtype.pyi
│  │     │  │  │  │  │  ├─ einsumfunc.pyi
│  │     │  │  │  │  │  ├─ emath.pyi
│  │     │  │  │  │  │  ├─ fft.pyi
│  │     │  │  │  │  │  ├─ flatiter.pyi
│  │     │  │  │  │  │  ├─ fromnumeric.pyi
│  │     │  │  │  │  │  ├─ getlimits.pyi
│  │     │  │  │  │  │  ├─ histograms.pyi
│  │     │  │  │  │  │  ├─ index_tricks.pyi
│  │     │  │  │  │  │  ├─ lib_function_base.pyi
│  │     │  │  │  │  │  ├─ lib_polynomial.pyi
│  │     │  │  │  │  │  ├─ lib_utils.pyi
│  │     │  │  │  │  │  ├─ lib_version.pyi
│  │     │  │  │  │  │  ├─ linalg.pyi
│  │     │  │  │  │  │  ├─ ma.pyi
│  │     │  │  │  │  │  ├─ matrix.pyi
│  │     │  │  │  │  │  ├─ memmap.pyi
│  │     │  │  │  │  │  ├─ mod.pyi
│  │     │  │  │  │  │  ├─ modules.pyi
│  │     │  │  │  │  │  ├─ multiarray.pyi
│  │     │  │  │  │  │  ├─ nbit_base_example.pyi
│  │     │  │  │  │  │  ├─ ndarray_assignability.pyi
│  │     │  │  │  │  │  ├─ ndarray_conversion.pyi
│  │     │  │  │  │  │  ├─ ndarray_misc.pyi
│  │     │  │  │  │  │  ├─ ndarray_shape_manipulation.pyi
│  │     │  │  │  │  │  ├─ nditer.pyi
│  │     │  │  │  │  │  ├─ nested_sequence.pyi
│  │     │  │  │  │  │  ├─ npyio.pyi
│  │     │  │  │  │  │  ├─ numeric.pyi
│  │     │  │  │  │  │  ├─ numerictypes.pyi
│  │     │  │  │  │  │  ├─ polynomial_polybase.pyi
│  │     │  │  │  │  │  ├─ polynomial_polyutils.pyi
│  │     │  │  │  │  │  ├─ polynomial_series.pyi
│  │     │  │  │  │  │  ├─ random.pyi
│  │     │  │  │  │  │  ├─ rec.pyi
│  │     │  │  │  │  │  ├─ scalars.pyi
│  │     │  │  │  │  │  ├─ shape_base.pyi
│  │     │  │  │  │  │  ├─ shape.pyi
│  │     │  │  │  │  │  ├─ stride_tricks.pyi
│  │     │  │  │  │  │  ├─ strings.pyi
│  │     │  │  │  │  │  ├─ testing.pyi
│  │     │  │  │  │  │  ├─ twodim_base.pyi
│  │     │  │  │  │  │  ├─ type_check.pyi
│  │     │  │  │  │  │  ├─ ufunc_config.pyi
│  │     │  │  │  │  │  ├─ ufunclike.pyi
│  │     │  │  │  │  │  ├─ ufuncs.pyi
│  │     │  │  │  │  │  └─ warnings_and_errors.pyi
│  │     │  │  │  │  └─ mypy.ini
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_isfile.py
│  │     │  │  │  ├─ test_runtime.py
│  │     │  │  │  └─ test_typing.py
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ mypy_plugin.py
│  │     │  ├─ __config__.py
│  │     │  ├─ __config__.pyi
│  │     │  ├─ __init__.cython-30.pxd
│  │     │  ├─ __init__.pxd
│  │     │  ├─ __init__.py
│  │     │  ├─ __init__.pyi
│  │     │  ├─ _array_api_info.py
│  │     │  ├─ _array_api_info.pyi
│  │     │  ├─ _configtool.py
│  │     │  ├─ _configtool.pyi
│  │     │  ├─ _distributor_init.py
│  │     │  ├─ _distributor_init.pyi
│  │     │  ├─ _expired_attrs_2_0.py
│  │     │  ├─ _expired_attrs_2_0.pyi
│  │     │  ├─ _globals.py
│  │     │  ├─ _globals.pyi
│  │     │  ├─ _pytesttester.py
│  │     │  ├─ _pytesttester.pyi
│  │     │  ├─ conftest.py
│  │     │  ├─ dtypes.py
│  │     │  ├─ dtypes.pyi
│  │     │  ├─ exceptions.py
│  │     │  ├─ exceptions.pyi
│  │     │  ├─ matlib.py
│  │     │  ├─ matlib.pyi
│  │     │  ├─ py.typed
│  │     │  ├─ version.py
│  │     │  └─ version.pyi
│  │     ├─ numpy-2.3.1.dist-info/
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ numpy.libs/
│  │     │  ├─ libscipy_openblas64_-13e2df515630b4a41f92893938845698.dll
│  │     │  └─ msvcp140-263139962577ecda4cd9469ca360a746.dll
│  │     ├─ packaging/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _elffile.cpython-312.pyc
│  │     │  │  ├─ _manylinux.cpython-312.pyc
│  │     │  │  ├─ _musllinux.cpython-312.pyc
│  │     │  │  ├─ _parser.cpython-312.pyc
│  │     │  │  ├─ _structures.cpython-312.pyc
│  │     │  │  ├─ _tokenizer.cpython-312.pyc
│  │     │  │  ├─ markers.cpython-312.pyc
│  │     │  │  ├─ metadata.cpython-312.pyc
│  │     │  │  ├─ requirements.cpython-312.pyc
│  │     │  │  ├─ specifiers.cpython-312.pyc
│  │     │  │  ├─ tags.cpython-312.pyc
│  │     │  │  ├─ utils.cpython-312.pyc
│  │     │  │  └─ version.cpython-312.pyc
│  │     │  ├─ licenses/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ _spdx.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  └─ _spdx.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _elffile.py
│  │     │  ├─ _manylinux.py
│  │     │  ├─ _musllinux.py
│  │     │  ├─ _parser.py
│  │     │  ├─ _structures.py
│  │     │  ├─ _tokenizer.py
│  │     │  ├─ markers.py
│  │     │  ├─ metadata.py
│  │     │  ├─ py.typed
│  │     │  ├─ requirements.py
│  │     │  ├─ specifiers.py
│  │     │  ├─ tags.py
│  │     │  ├─ utils.py
│  │     │  └─ version.py
│  │     ├─ packaging-25.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  ├─ LICENSE
│  │     │  │  ├─ LICENSE.APACHE
│  │     │  │  └─ LICENSE.BSD
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ pandas/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _typing.cpython-312.pyc
│  │     │  │  ├─ _version_meson.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  └─ testing.cpython-312.pyc
│  │     │  ├─ _config/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ config.cpython-312.pyc
│  │     │  │  │  ├─ dates.cpython-312.pyc
│  │     │  │  │  ├─ display.cpython-312.pyc
│  │     │  │  │  └─ localization.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ config.py
│  │     │  │  ├─ dates.py
│  │     │  │  ├─ display.py
│  │     │  │  └─ localization.py
│  │     │  ├─ _libs/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ tslibs/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ base.cp312-win_amd64.lib
│  │     │  │  │  ├─ base.cp312-win_amd64.pyd
│  │     │  │  │  ├─ ccalendar.cp312-win_amd64.lib
│  │     │  │  │  ├─ ccalendar.cp312-win_amd64.pyd
│  │     │  │  │  ├─ ccalendar.pyi
│  │     │  │  │  ├─ conversion.cp312-win_amd64.lib
│  │     │  │  │  ├─ conversion.cp312-win_amd64.pyd
│  │     │  │  │  ├─ conversion.pyi
│  │     │  │  │  ├─ dtypes.cp312-win_amd64.lib
│  │     │  │  │  ├─ dtypes.cp312-win_amd64.pyd
│  │     │  │  │  ├─ dtypes.pyi
│  │     │  │  │  ├─ fields.cp312-win_amd64.lib
│  │     │  │  │  ├─ fields.cp312-win_amd64.pyd
│  │     │  │  │  ├─ fields.pyi
│  │     │  │  │  ├─ nattype.cp312-win_amd64.lib
│  │     │  │  │  ├─ nattype.cp312-win_amd64.pyd
│  │     │  │  │  ├─ nattype.pyi
│  │     │  │  │  ├─ np_datetime.cp312-win_amd64.lib
│  │     │  │  │  ├─ np_datetime.cp312-win_amd64.pyd
│  │     │  │  │  ├─ np_datetime.pyi
│  │     │  │  │  ├─ offsets.cp312-win_amd64.lib
│  │     │  │  │  ├─ offsets.cp312-win_amd64.pyd
│  │     │  │  │  ├─ offsets.pyi
│  │     │  │  │  ├─ parsing.cp312-win_amd64.lib
│  │     │  │  │  ├─ parsing.cp312-win_amd64.pyd
│  │     │  │  │  ├─ parsing.pyi
│  │     │  │  │  ├─ period.cp312-win_amd64.lib
│  │     │  │  │  ├─ period.cp312-win_amd64.pyd
│  │     │  │  │  ├─ period.pyi
│  │     │  │  │  ├─ strptime.cp312-win_amd64.lib
│  │     │  │  │  ├─ strptime.cp312-win_amd64.pyd
│  │     │  │  │  ├─ strptime.pyi
│  │     │  │  │  ├─ timedeltas.cp312-win_amd64.lib
│  │     │  │  │  ├─ timedeltas.cp312-win_amd64.pyd
│  │     │  │  │  ├─ timedeltas.pyi
│  │     │  │  │  ├─ timestamps.cp312-win_amd64.lib
│  │     │  │  │  ├─ timestamps.cp312-win_amd64.pyd
│  │     │  │  │  ├─ timestamps.pyi
│  │     │  │  │  ├─ timezones.cp312-win_amd64.lib
│  │     │  │  │  ├─ timezones.cp312-win_amd64.pyd
│  │     │  │  │  ├─ timezones.pyi
│  │     │  │  │  ├─ tzconversion.cp312-win_amd64.lib
│  │     │  │  │  ├─ tzconversion.cp312-win_amd64.pyd
│  │     │  │  │  ├─ tzconversion.pyi
│  │     │  │  │  ├─ vectorized.cp312-win_amd64.lib
│  │     │  │  │  ├─ vectorized.cp312-win_amd64.pyd
│  │     │  │  │  └─ vectorized.pyi
│  │     │  │  ├─ window/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ aggregations.cp312-win_amd64.lib
│  │     │  │  │  ├─ aggregations.cp312-win_amd64.pyd
│  │     │  │  │  ├─ aggregations.pyi
│  │     │  │  │  ├─ indexers.cp312-win_amd64.lib
│  │     │  │  │  ├─ indexers.cp312-win_amd64.pyd
│  │     │  │  │  └─ indexers.pyi
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ algos.cp312-win_amd64.lib
│  │     │  │  ├─ algos.cp312-win_amd64.pyd
│  │     │  │  ├─ algos.pyi
│  │     │  │  ├─ arrays.cp312-win_amd64.lib
│  │     │  │  ├─ arrays.cp312-win_amd64.pyd
│  │     │  │  ├─ arrays.pyi
│  │     │  │  ├─ byteswap.cp312-win_amd64.lib
│  │     │  │  ├─ byteswap.cp312-win_amd64.pyd
│  │     │  │  ├─ byteswap.pyi
│  │     │  │  ├─ groupby.cp312-win_amd64.lib
│  │     │  │  ├─ groupby.cp312-win_amd64.pyd
│  │     │  │  ├─ groupby.pyi
│  │     │  │  ├─ hashing.cp312-win_amd64.lib
│  │     │  │  ├─ hashing.cp312-win_amd64.pyd
│  │     │  │  ├─ hashing.pyi
│  │     │  │  ├─ hashtable.cp312-win_amd64.lib
│  │     │  │  ├─ hashtable.cp312-win_amd64.pyd
│  │     │  │  ├─ hashtable.pyi
│  │     │  │  ├─ index.cp312-win_amd64.lib
│  │     │  │  ├─ index.cp312-win_amd64.pyd
│  │     │  │  ├─ index.pyi
│  │     │  │  ├─ indexing.cp312-win_amd64.lib
│  │     │  │  ├─ indexing.cp312-win_amd64.pyd
│  │     │  │  ├─ indexing.pyi
│  │     │  │  ├─ internals.cp312-win_amd64.lib
│  │     │  │  ├─ internals.cp312-win_amd64.pyd
│  │     │  │  ├─ internals.pyi
│  │     │  │  ├─ interval.cp312-win_amd64.lib
│  │     │  │  ├─ interval.cp312-win_amd64.pyd
│  │     │  │  ├─ interval.pyi
│  │     │  │  ├─ join.cp312-win_amd64.lib
│  │     │  │  ├─ join.cp312-win_amd64.pyd
│  │     │  │  ├─ join.pyi
│  │     │  │  ├─ json.cp312-win_amd64.lib
│  │     │  │  ├─ json.cp312-win_amd64.pyd
│  │     │  │  ├─ json.pyi
│  │     │  │  ├─ lib.cp312-win_amd64.lib
│  │     │  │  ├─ lib.cp312-win_amd64.pyd
│  │     │  │  ├─ lib.pyi
│  │     │  │  ├─ missing.cp312-win_amd64.lib
│  │     │  │  ├─ missing.cp312-win_amd64.pyd
│  │     │  │  ├─ missing.pyi
│  │     │  │  ├─ ops_dispatch.cp312-win_amd64.lib
│  │     │  │  ├─ ops_dispatch.cp312-win_amd64.pyd
│  │     │  │  ├─ ops_dispatch.pyi
│  │     │  │  ├─ ops.cp312-win_amd64.lib
│  │     │  │  ├─ ops.cp312-win_amd64.pyd
│  │     │  │  ├─ ops.pyi
│  │     │  │  ├─ pandas_datetime.cp312-win_amd64.lib
│  │     │  │  ├─ pandas_datetime.cp312-win_amd64.pyd
│  │     │  │  ├─ pandas_parser.cp312-win_amd64.lib
│  │     │  │  ├─ pandas_parser.cp312-win_amd64.pyd
│  │     │  │  ├─ parsers.cp312-win_amd64.lib
│  │     │  │  ├─ parsers.cp312-win_amd64.pyd
│  │     │  │  ├─ parsers.pyi
│  │     │  │  ├─ properties.cp312-win_amd64.lib
│  │     │  │  ├─ properties.cp312-win_amd64.pyd
│  │     │  │  ├─ properties.pyi
│  │     │  │  ├─ reshape.cp312-win_amd64.lib
│  │     │  │  ├─ reshape.cp312-win_amd64.pyd
│  │     │  │  ├─ reshape.pyi
│  │     │  │  ├─ sas.cp312-win_amd64.lib
│  │     │  │  ├─ sas.cp312-win_amd64.pyd
│  │     │  │  ├─ sas.pyi
│  │     │  │  ├─ sparse.cp312-win_amd64.lib
│  │     │  │  ├─ sparse.cp312-win_amd64.pyd
│  │     │  │  ├─ sparse.pyi
│  │     │  │  ├─ testing.cp312-win_amd64.lib
│  │     │  │  ├─ testing.cp312-win_amd64.pyd
│  │     │  │  ├─ testing.pyi
│  │     │  │  ├─ tslib.cp312-win_amd64.lib
│  │     │  │  ├─ tslib.cp312-win_amd64.pyd
│  │     │  │  ├─ tslib.pyi
│  │     │  │  ├─ writers.cp312-win_amd64.lib
│  │     │  │  ├─ writers.cp312-win_amd64.pyd
│  │     │  │  └─ writers.pyi
│  │     │  ├─ _testing/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _hypothesis.cpython-312.pyc
│  │     │  │  │  ├─ _io.cpython-312.pyc
│  │     │  │  │  ├─ _warnings.cpython-312.pyc
│  │     │  │  │  ├─ asserters.cpython-312.pyc
│  │     │  │  │  ├─ compat.cpython-312.pyc
│  │     │  │  │  └─ contexts.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _hypothesis.py
│  │     │  │  ├─ _io.py
│  │     │  │  ├─ _warnings.py
│  │     │  │  ├─ asserters.py
│  │     │  │  ├─ compat.py
│  │     │  │  └─ contexts.py
│  │     │  ├─ api/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  ├─ extensions/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ indexers/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ interchange/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ types/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ typing/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  └─ __init__.py
│  │     │  ├─ arrays/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ compat/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _constants.cpython-312.pyc
│  │     │  │  │  ├─ _optional.cpython-312.pyc
│  │     │  │  │  ├─ compressors.cpython-312.pyc
│  │     │  │  │  ├─ pickle_compat.cpython-312.pyc
│  │     │  │  │  └─ pyarrow.cpython-312.pyc
│  │     │  │  ├─ numpy/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ function.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ function.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _constants.py
│  │     │  │  ├─ _optional.py
│  │     │  │  ├─ compressors.py
│  │     │  │  ├─ pickle_compat.py
│  │     │  │  └─ pyarrow.py
│  │     │  ├─ core/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ accessor.cpython-312.pyc
│  │     │  │  │  ├─ algorithms.cpython-312.pyc
│  │     │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  ├─ apply.cpython-312.pyc
│  │     │  │  │  ├─ arraylike.cpython-312.pyc
│  │     │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  ├─ config_init.cpython-312.pyc
│  │     │  │  │  ├─ construction.cpython-312.pyc
│  │     │  │  │  ├─ flags.cpython-312.pyc
│  │     │  │  │  ├─ frame.cpython-312.pyc
│  │     │  │  │  ├─ generic.cpython-312.pyc
│  │     │  │  │  ├─ indexing.cpython-312.pyc
│  │     │  │  │  ├─ missing.cpython-312.pyc
│  │     │  │  │  ├─ nanops.cpython-312.pyc
│  │     │  │  │  ├─ resample.cpython-312.pyc
│  │     │  │  │  ├─ roperator.cpython-312.pyc
│  │     │  │  │  ├─ sample.cpython-312.pyc
│  │     │  │  │  ├─ series.cpython-312.pyc
│  │     │  │  │  ├─ shared_docs.cpython-312.pyc
│  │     │  │  │  └─ sorting.cpython-312.pyc
│  │     │  │  ├─ _numba/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ executor.cpython-312.pyc
│  │     │  │  │  │  └─ extensions.cpython-312.pyc
│  │     │  │  │  ├─ kernels/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ mean_.cpython-312.pyc
│  │     │  │  │  │  │  ├─ min_max_.cpython-312.pyc
│  │     │  │  │  │  │  ├─ shared.cpython-312.pyc
│  │     │  │  │  │  │  ├─ sum_.cpython-312.pyc
│  │     │  │  │  │  │  └─ var_.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ mean_.py
│  │     │  │  │  │  ├─ min_max_.py
│  │     │  │  │  │  ├─ shared.py
│  │     │  │  │  │  ├─ sum_.py
│  │     │  │  │  │  └─ var_.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ executor.py
│  │     │  │  │  └─ extensions.py
│  │     │  │  ├─ array_algos/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ datetimelike_accumulations.cpython-312.pyc
│  │     │  │  │  │  ├─ masked_accumulations.cpython-312.pyc
│  │     │  │  │  │  ├─ masked_reductions.cpython-312.pyc
│  │     │  │  │  │  ├─ putmask.cpython-312.pyc
│  │     │  │  │  │  ├─ quantile.cpython-312.pyc
│  │     │  │  │  │  ├─ replace.cpython-312.pyc
│  │     │  │  │  │  ├─ take.cpython-312.pyc
│  │     │  │  │  │  └─ transforms.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ datetimelike_accumulations.py
│  │     │  │  │  ├─ masked_accumulations.py
│  │     │  │  │  ├─ masked_reductions.py
│  │     │  │  │  ├─ putmask.py
│  │     │  │  │  ├─ quantile.py
│  │     │  │  │  ├─ replace.py
│  │     │  │  │  ├─ take.py
│  │     │  │  │  └─ transforms.py
│  │     │  │  ├─ arrays/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _arrow_string_mixins.cpython-312.pyc
│  │     │  │  │  │  ├─ _mixins.cpython-312.pyc
│  │     │  │  │  │  ├─ _ranges.cpython-312.pyc
│  │     │  │  │  │  ├─ _utils.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ boolean.cpython-312.pyc
│  │     │  │  │  │  ├─ categorical.cpython-312.pyc
│  │     │  │  │  │  ├─ datetimelike.cpython-312.pyc
│  │     │  │  │  │  ├─ datetimes.cpython-312.pyc
│  │     │  │  │  │  ├─ floating.cpython-312.pyc
│  │     │  │  │  │  ├─ integer.cpython-312.pyc
│  │     │  │  │  │  ├─ interval.cpython-312.pyc
│  │     │  │  │  │  ├─ masked.cpython-312.pyc
│  │     │  │  │  │  ├─ numeric.cpython-312.pyc
│  │     │  │  │  │  ├─ numpy_.cpython-312.pyc
│  │     │  │  │  │  ├─ period.cpython-312.pyc
│  │     │  │  │  │  ├─ string_.cpython-312.pyc
│  │     │  │  │  │  ├─ string_arrow.cpython-312.pyc
│  │     │  │  │  │  └─ timedeltas.cpython-312.pyc
│  │     │  │  │  ├─ arrow/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _arrow_utils.cpython-312.pyc
│  │     │  │  │  │  │  ├─ accessors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ array.cpython-312.pyc
│  │     │  │  │  │  │  └─ extension_types.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _arrow_utils.py
│  │     │  │  │  │  ├─ accessors.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  └─ extension_types.py
│  │     │  │  │  ├─ sparse/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ accessor.cpython-312.pyc
│  │     │  │  │  │  │  ├─ array.cpython-312.pyc
│  │     │  │  │  │  │  └─ scipy_sparse.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ accessor.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  └─ scipy_sparse.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _arrow_string_mixins.py
│  │     │  │  │  ├─ _mixins.py
│  │     │  │  │  ├─ _ranges.py
│  │     │  │  │  ├─ _utils.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ boolean.py
│  │     │  │  │  ├─ categorical.py
│  │     │  │  │  ├─ datetimelike.py
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ floating.py
│  │     │  │  │  ├─ integer.py
│  │     │  │  │  ├─ interval.py
│  │     │  │  │  ├─ masked.py
│  │     │  │  │  ├─ numeric.py
│  │     │  │  │  ├─ numpy_.py
│  │     │  │  │  ├─ period.py
│  │     │  │  │  ├─ string_.py
│  │     │  │  │  ├─ string_arrow.py
│  │     │  │  │  └─ timedeltas.py
│  │     │  │  ├─ computation/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ align.cpython-312.pyc
│  │     │  │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  │  ├─ check.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ engines.cpython-312.pyc
│  │     │  │  │  │  ├─ eval.cpython-312.pyc
│  │     │  │  │  │  ├─ expr.cpython-312.pyc
│  │     │  │  │  │  ├─ expressions.cpython-312.pyc
│  │     │  │  │  │  ├─ ops.cpython-312.pyc
│  │     │  │  │  │  ├─ parsing.cpython-312.pyc
│  │     │  │  │  │  ├─ pytables.cpython-312.pyc
│  │     │  │  │  │  └─ scope.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ engines.py
│  │     │  │  │  ├─ eval.py
│  │     │  │  │  ├─ expr.py
│  │     │  │  │  ├─ expressions.py
│  │     │  │  │  ├─ ops.py
│  │     │  │  │  ├─ parsing.py
│  │     │  │  │  ├─ pytables.py
│  │     │  │  │  └─ scope.py
│  │     │  │  ├─ dtypes/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  │  ├─ astype.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ cast.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ concat.cpython-312.pyc
│  │     │  │  │  │  ├─ dtypes.cpython-312.pyc
│  │     │  │  │  │  ├─ generic.cpython-312.pyc
│  │     │  │  │  │  ├─ inference.cpython-312.pyc
│  │     │  │  │  │  └─ missing.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ astype.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ cast.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ dtypes.py
│  │     │  │  │  ├─ generic.py
│  │     │  │  │  ├─ inference.py
│  │     │  │  │  └─ missing.py
│  │     │  │  ├─ groupby/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ categorical.cpython-312.pyc
│  │     │  │  │  │  ├─ generic.cpython-312.pyc
│  │     │  │  │  │  ├─ groupby.cpython-312.pyc
│  │     │  │  │  │  ├─ grouper.cpython-312.pyc
│  │     │  │  │  │  ├─ indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ numba_.cpython-312.pyc
│  │     │  │  │  │  └─ ops.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ categorical.py
│  │     │  │  │  ├─ generic.py
│  │     │  │  │  ├─ groupby.py
│  │     │  │  │  ├─ grouper.py
│  │     │  │  │  ├─ indexing.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  └─ ops.py
│  │     │  │  ├─ indexers/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ objects.cpython-312.pyc
│  │     │  │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ objects.py
│  │     │  │  │  └─ utils.py
│  │     │  │  ├─ indexes/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ accessors.cpython-312.pyc
│  │     │  │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ category.cpython-312.pyc
│  │     │  │  │  │  ├─ datetimelike.cpython-312.pyc
│  │     │  │  │  │  ├─ datetimes.cpython-312.pyc
│  │     │  │  │  │  ├─ extension.cpython-312.pyc
│  │     │  │  │  │  ├─ frozen.cpython-312.pyc
│  │     │  │  │  │  ├─ interval.cpython-312.pyc
│  │     │  │  │  │  ├─ multi.cpython-312.pyc
│  │     │  │  │  │  ├─ period.cpython-312.pyc
│  │     │  │  │  │  ├─ range.cpython-312.pyc
│  │     │  │  │  │  └─ timedeltas.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ accessors.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ category.py
│  │     │  │  │  ├─ datetimelike.py
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ extension.py
│  │     │  │  │  ├─ frozen.py
│  │     │  │  │  ├─ interval.py
│  │     │  │  │  ├─ multi.py
│  │     │  │  │  ├─ period.py
│  │     │  │  │  ├─ range.py
│  │     │  │  │  └─ timedeltas.py
│  │     │  │  ├─ interchange/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ buffer.cpython-312.pyc
│  │     │  │  │  │  ├─ column.cpython-312.pyc
│  │     │  │  │  │  ├─ dataframe_protocol.cpython-312.pyc
│  │     │  │  │  │  ├─ dataframe.cpython-312.pyc
│  │     │  │  │  │  ├─ from_dataframe.cpython-312.pyc
│  │     │  │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ buffer.py
│  │     │  │  │  ├─ column.py
│  │     │  │  │  ├─ dataframe_protocol.py
│  │     │  │  │  ├─ dataframe.py
│  │     │  │  │  ├─ from_dataframe.py
│  │     │  │  │  └─ utils.py
│  │     │  │  ├─ internals/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  │  ├─ array_manager.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ blocks.cpython-312.pyc
│  │     │  │  │  │  ├─ concat.cpython-312.pyc
│  │     │  │  │  │  ├─ construction.cpython-312.pyc
│  │     │  │  │  │  ├─ managers.cpython-312.pyc
│  │     │  │  │  │  └─ ops.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ array_manager.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ blocks.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ construction.py
│  │     │  │  │  ├─ managers.py
│  │     │  │  │  └─ ops.py
│  │     │  │  ├─ methods/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ describe.cpython-312.pyc
│  │     │  │  │  │  ├─ selectn.cpython-312.pyc
│  │     │  │  │  │  └─ to_dict.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ describe.py
│  │     │  │  │  ├─ selectn.py
│  │     │  │  │  └─ to_dict.py
│  │     │  │  ├─ ops/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ array_ops.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ dispatch.cpython-312.pyc
│  │     │  │  │  │  ├─ docstrings.cpython-312.pyc
│  │     │  │  │  │  ├─ invalid.cpython-312.pyc
│  │     │  │  │  │  ├─ mask_ops.cpython-312.pyc
│  │     │  │  │  │  └─ missing.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ array_ops.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ dispatch.py
│  │     │  │  │  ├─ docstrings.py
│  │     │  │  │  ├─ invalid.py
│  │     │  │  │  ├─ mask_ops.py
│  │     │  │  │  └─ missing.py
│  │     │  │  ├─ reshape/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  │  ├─ concat.cpython-312.pyc
│  │     │  │  │  │  ├─ encoding.cpython-312.pyc
│  │     │  │  │  │  ├─ melt.cpython-312.pyc
│  │     │  │  │  │  ├─ merge.cpython-312.pyc
│  │     │  │  │  │  ├─ pivot.cpython-312.pyc
│  │     │  │  │  │  ├─ reshape.cpython-312.pyc
│  │     │  │  │  │  ├─ tile.cpython-312.pyc
│  │     │  │  │  │  └─ util.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ concat.py
│  │     │  │  │  ├─ encoding.py
│  │     │  │  │  ├─ melt.py
│  │     │  │  │  ├─ merge.py
│  │     │  │  │  ├─ pivot.py
│  │     │  │  │  ├─ reshape.py
│  │     │  │  │  ├─ tile.py
│  │     │  │  │  └─ util.py
│  │     │  │  ├─ sparse/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ api.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ api.py
│  │     │  │  ├─ strings/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ accessor.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  └─ object_array.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ accessor.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  └─ object_array.py
│  │     │  │  ├─ tools/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ datetimes.cpython-312.pyc
│  │     │  │  │  │  ├─ numeric.cpython-312.pyc
│  │     │  │  │  │  ├─ timedeltas.cpython-312.pyc
│  │     │  │  │  │  └─ times.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ datetimes.py
│  │     │  │  │  ├─ numeric.py
│  │     │  │  │  ├─ timedeltas.py
│  │     │  │  │  └─ times.py
│  │     │  │  ├─ util/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ hashing.cpython-312.pyc
│  │     │  │  │  │  └─ numba_.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ hashing.py
│  │     │  │  │  └─ numba_.py
│  │     │  │  ├─ window/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ doc.cpython-312.pyc
│  │     │  │  │  │  ├─ ewm.cpython-312.pyc
│  │     │  │  │  │  ├─ expanding.cpython-312.pyc
│  │     │  │  │  │  ├─ numba_.cpython-312.pyc
│  │     │  │  │  │  ├─ online.cpython-312.pyc
│  │     │  │  │  │  └─ rolling.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ doc.py
│  │     │  │  │  ├─ ewm.py
│  │     │  │  │  ├─ expanding.py
│  │     │  │  │  ├─ numba_.py
│  │     │  │  │  ├─ online.py
│  │     │  │  │  └─ rolling.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ accessor.py
│  │     │  │  ├─ algorithms.py
│  │     │  │  ├─ api.py
│  │     │  │  ├─ apply.py
│  │     │  │  ├─ arraylike.py
│  │     │  │  ├─ base.py
│  │     │  │  ├─ common.py
│  │     │  │  ├─ config_init.py
│  │     │  │  ├─ construction.py
│  │     │  │  ├─ flags.py
│  │     │  │  ├─ frame.py
│  │     │  │  ├─ generic.py
│  │     │  │  ├─ indexing.py
│  │     │  │  ├─ missing.py
│  │     │  │  ├─ nanops.py
│  │     │  │  ├─ resample.py
│  │     │  │  ├─ roperator.py
│  │     │  │  ├─ sample.py
│  │     │  │  ├─ series.py
│  │     │  │  ├─ shared_docs.py
│  │     │  │  └─ sorting.py
│  │     │  ├─ errors/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ io/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _util.cpython-312.pyc
│  │     │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  ├─ clipboards.cpython-312.pyc
│  │     │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  ├─ feather_format.cpython-312.pyc
│  │     │  │  │  ├─ gbq.cpython-312.pyc
│  │     │  │  │  ├─ html.cpython-312.pyc
│  │     │  │  │  ├─ orc.cpython-312.pyc
│  │     │  │  │  ├─ parquet.cpython-312.pyc
│  │     │  │  │  ├─ pickle.cpython-312.pyc
│  │     │  │  │  ├─ pytables.cpython-312.pyc
│  │     │  │  │  ├─ spss.cpython-312.pyc
│  │     │  │  │  ├─ sql.cpython-312.pyc
│  │     │  │  │  ├─ stata.cpython-312.pyc
│  │     │  │  │  └─ xml.cpython-312.pyc
│  │     │  │  ├─ clipboard/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ excel/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _base.cpython-312.pyc
│  │     │  │  │  │  ├─ _calamine.cpython-312.pyc
│  │     │  │  │  │  ├─ _odfreader.cpython-312.pyc
│  │     │  │  │  │  ├─ _odswriter.cpython-312.pyc
│  │     │  │  │  │  ├─ _openpyxl.cpython-312.pyc
│  │     │  │  │  │  ├─ _pyxlsb.cpython-312.pyc
│  │     │  │  │  │  ├─ _util.cpython-312.pyc
│  │     │  │  │  │  ├─ _xlrd.cpython-312.pyc
│  │     │  │  │  │  └─ _xlsxwriter.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _base.py
│  │     │  │  │  ├─ _calamine.py
│  │     │  │  │  ├─ _odfreader.py
│  │     │  │  │  ├─ _odswriter.py
│  │     │  │  │  ├─ _openpyxl.py
│  │     │  │  │  ├─ _pyxlsb.py
│  │     │  │  │  ├─ _util.py
│  │     │  │  │  ├─ _xlrd.py
│  │     │  │  │  └─ _xlsxwriter.py
│  │     │  │  ├─ formats/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _color_data.cpython-312.pyc
│  │     │  │  │  │  ├─ console.cpython-312.pyc
│  │     │  │  │  │  ├─ css.cpython-312.pyc
│  │     │  │  │  │  ├─ csvs.cpython-312.pyc
│  │     │  │  │  │  ├─ excel.cpython-312.pyc
│  │     │  │  │  │  ├─ format.cpython-312.pyc
│  │     │  │  │  │  ├─ html.cpython-312.pyc
│  │     │  │  │  │  ├─ info.cpython-312.pyc
│  │     │  │  │  │  ├─ printing.cpython-312.pyc
│  │     │  │  │  │  ├─ string.cpython-312.pyc
│  │     │  │  │  │  ├─ style_render.cpython-312.pyc
│  │     │  │  │  │  ├─ style.cpython-312.pyc
│  │     │  │  │  │  └─ xml.cpython-312.pyc
│  │     │  │  │  ├─ templates/
│  │     │  │  │  │  ├─ html_style.tpl
│  │     │  │  │  │  ├─ html_table.tpl
│  │     │  │  │  │  ├─ html.tpl
│  │     │  │  │  │  ├─ latex_longtable.tpl
│  │     │  │  │  │  ├─ latex_table.tpl
│  │     │  │  │  │  ├─ latex.tpl
│  │     │  │  │  │  └─ string.tpl
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _color_data.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ css.py
│  │     │  │  │  ├─ csvs.py
│  │     │  │  │  ├─ excel.py
│  │     │  │  │  ├─ format.py
│  │     │  │  │  ├─ html.py
│  │     │  │  │  ├─ info.py
│  │     │  │  │  ├─ printing.py
│  │     │  │  │  ├─ string.py
│  │     │  │  │  ├─ style_render.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  └─ xml.py
│  │     │  │  ├─ json/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _json.cpython-312.pyc
│  │     │  │  │  │  ├─ _normalize.cpython-312.pyc
│  │     │  │  │  │  └─ _table_schema.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  ├─ _normalize.py
│  │     │  │  │  └─ _table_schema.py
│  │     │  │  ├─ parsers/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ arrow_parser_wrapper.cpython-312.pyc
│  │     │  │  │  │  ├─ base_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ c_parser_wrapper.cpython-312.pyc
│  │     │  │  │  │  ├─ python_parser.cpython-312.pyc
│  │     │  │  │  │  └─ readers.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ arrow_parser_wrapper.py
│  │     │  │  │  ├─ base_parser.py
│  │     │  │  │  ├─ c_parser_wrapper.py
│  │     │  │  │  ├─ python_parser.py
│  │     │  │  │  └─ readers.py
│  │     │  │  ├─ sas/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ sas_constants.cpython-312.pyc
│  │     │  │  │  │  ├─ sas_xport.cpython-312.pyc
│  │     │  │  │  │  ├─ sas7bdat.cpython-312.pyc
│  │     │  │  │  │  └─ sasreader.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ sas_constants.py
│  │     │  │  │  ├─ sas_xport.py
│  │     │  │  │  ├─ sas7bdat.py
│  │     │  │  │  └─ sasreader.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _util.py
│  │     │  │  ├─ api.py
│  │     │  │  ├─ clipboards.py
│  │     │  │  ├─ common.py
│  │     │  │  ├─ feather_format.py
│  │     │  │  ├─ gbq.py
│  │     │  │  ├─ html.py
│  │     │  │  ├─ orc.py
│  │     │  │  ├─ parquet.py
│  │     │  │  ├─ pickle.py
│  │     │  │  ├─ pytables.py
│  │     │  │  ├─ spss.py
│  │     │  │  ├─ sql.py
│  │     │  │  ├─ stata.py
│  │     │  │  └─ xml.py
│  │     │  ├─ plotting/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _core.cpython-312.pyc
│  │     │  │  │  └─ _misc.cpython-312.pyc
│  │     │  │  ├─ _matplotlib/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ boxplot.cpython-312.pyc
│  │     │  │  │  │  ├─ converter.cpython-312.pyc
│  │     │  │  │  │  ├─ core.cpython-312.pyc
│  │     │  │  │  │  ├─ groupby.cpython-312.pyc
│  │     │  │  │  │  ├─ hist.cpython-312.pyc
│  │     │  │  │  │  ├─ misc.cpython-312.pyc
│  │     │  │  │  │  ├─ style.cpython-312.pyc
│  │     │  │  │  │  ├─ timeseries.cpython-312.pyc
│  │     │  │  │  │  └─ tools.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ boxplot.py
│  │     │  │  │  ├─ converter.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ groupby.py
│  │     │  │  │  ├─ hist.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ timeseries.py
│  │     │  │  │  └─ tools.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _core.py
│  │     │  │  └─ _misc.py
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ test_aggregation.cpython-312.pyc
│  │     │  │  │  ├─ test_algos.cpython-312.pyc
│  │     │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  ├─ test_downstream.cpython-312.pyc
│  │     │  │  │  ├─ test_errors.cpython-312.pyc
│  │     │  │  │  ├─ test_expressions.cpython-312.pyc
│  │     │  │  │  ├─ test_flags.cpython-312.pyc
│  │     │  │  │  ├─ test_multilevel.cpython-312.pyc
│  │     │  │  │  ├─ test_nanops.cpython-312.pyc
│  │     │  │  │  ├─ test_optional_dependency.cpython-312.pyc
│  │     │  │  │  ├─ test_register_accessor.cpython-312.pyc
│  │     │  │  │  ├─ test_sorting.cpython-312.pyc
│  │     │  │  │  └─ test_take.cpython-312.pyc
│  │     │  │  ├─ api/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  └─ test_types.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  └─ test_types.py
│  │     │  │  ├─ apply/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_frame_apply_relabeling.cpython-312.pyc
│  │     │  │  │  │  ├─ test_frame_apply.cpython-312.pyc
│  │     │  │  │  │  ├─ test_frame_transform.cpython-312.pyc
│  │     │  │  │  │  ├─ test_invalid_arg.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numba.cpython-312.pyc
│  │     │  │  │  │  ├─ test_series_apply_relabeling.cpython-312.pyc
│  │     │  │  │  │  ├─ test_series_apply.cpython-312.pyc
│  │     │  │  │  │  ├─ test_series_transform.cpython-312.pyc
│  │     │  │  │  │  └─ test_str.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ test_frame_apply_relabeling.py
│  │     │  │  │  ├─ test_frame_apply.py
│  │     │  │  │  ├─ test_frame_transform.py
│  │     │  │  │  ├─ test_invalid_arg.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_series_apply_relabeling.py
│  │     │  │  │  ├─ test_series_apply.py
│  │     │  │  │  ├─ test_series_transform.py
│  │     │  │  │  └─ test_str.py
│  │     │  │  ├─ arithmetic/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array_ops.cpython-312.pyc
│  │     │  │  │  │  ├─ test_categorical.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetime64.cpython-312.pyc
│  │     │  │  │  │  ├─ test_interval.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numeric.cpython-312.pyc
│  │     │  │  │  │  ├─ test_object.cpython-312.pyc
│  │     │  │  │  │  ├─ test_period.cpython-312.pyc
│  │     │  │  │  │  └─ test_timedelta64.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_array_ops.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_datetime64.py
│  │     │  │  │  ├─ test_interval.py
│  │     │  │  │  ├─ test_numeric.py
│  │     │  │  │  ├─ test_object.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  └─ test_timedelta64.py
│  │     │  │  ├─ arrays/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ masked_shared.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetimelike.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetimes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ndarray_backed.cpython-312.pyc
│  │     │  │  │  │  ├─ test_period.cpython-312.pyc
│  │     │  │  │  │  └─ test_timedeltas.cpython-312.pyc
│  │     │  │  │  ├─ boolean/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_comparison.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_construction.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_function.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_logical.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_ops.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reduction.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_repr.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_logical.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_reduction.py
│  │     │  │  │  │  └─ test_repr.py
│  │     │  │  │  ├─ categorical/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_algos.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_analytics.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_map.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_missing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_operators.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_replace.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_repr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sorting.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_subclass.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_take.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_warnings.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_algos.py
│  │     │  │  │  │  ├─ test_analytics.py
│  │     │  │  │  │  ├─ test_api.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_missing.py
│  │     │  │  │  │  ├─ test_operators.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  ├─ test_sorting.py
│  │     │  │  │  │  ├─ test_subclass.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  └─ test_warnings.py
│  │     │  │  │  ├─ datetimes/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_cumulative.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_cumulative.py
│  │     │  │  │  │  └─ test_reductions.py
│  │     │  │  │  ├─ floating/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_comparison.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_concat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_construction.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_contains.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_function.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_repr.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_to_numpy.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_contains.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_repr.py
│  │     │  │  │  │  └─ test_to_numpy.py
│  │     │  │  │  ├─ integer/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_comparison.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_concat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_construction.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_function.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reduction.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_repr.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_comparison.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_construction.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_reduction.py
│  │     │  │  │  │  └─ test_repr.py
│  │     │  │  │  ├─ interval/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interval_pyarrow.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interval.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_overlaps.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_interval_pyarrow.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  └─ test_overlaps.py
│  │     │  │  │  ├─ masked/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arrow_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_function.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_arrow_compat.py
│  │     │  │  │  │  ├─ test_function.py
│  │     │  │  │  │  └─ test_indexing.py
│  │     │  │  │  ├─ numpy_/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_numpy.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  └─ test_numpy.py
│  │     │  │  │  ├─ period/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arrow_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arrow_compat.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  └─ test_reductions.py
│  │     │  │  │  ├─ sparse/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_accessor.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetics.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_array.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_combine_concat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dtype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_libsparse.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_unary.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_accessor.py
│  │     │  │  │  │  ├─ test_arithmetics.py
│  │     │  │  │  │  ├─ test_array.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_combine_concat.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_dtype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_libsparse.py
│  │     │  │  │  │  ├─ test_reductions.py
│  │     │  │  │  │  └─ test_unary.py
│  │     │  │  │  ├─ string_/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_concat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_string_arrow.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_string.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_string_arrow.py
│  │     │  │  │  │  └─ test_string.py
│  │     │  │  │  ├─ timedeltas/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_cumulative.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_cumulative.py
│  │     │  │  │  │  └─ test_reductions.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ masked_shared.py
│  │     │  │  │  ├─ test_array.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_datetimes.py
│  │     │  │  │  ├─ test_ndarray_backed.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  └─ test_timedeltas.py
│  │     │  │  ├─ base/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  ├─ test_conversion.cpython-312.pyc
│  │     │  │  │  │  ├─ test_fillna.cpython-312.pyc
│  │     │  │  │  │  ├─ test_misc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_transpose.cpython-312.pyc
│  │     │  │  │  │  ├─ test_unique.cpython-312.pyc
│  │     │  │  │  │  └─ test_value_counts.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_conversion.py
│  │     │  │  │  ├─ test_fillna.py
│  │     │  │  │  ├─ test_misc.py
│  │     │  │  │  ├─ test_transpose.py
│  │     │  │  │  ├─ test_unique.py
│  │     │  │  │  └─ test_value_counts.py
│  │     │  │  ├─ computation/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_compat.cpython-312.pyc
│  │     │  │  │  │  └─ test_eval.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_compat.py
│  │     │  │  │  └─ test_eval.py
│  │     │  │  ├─ config/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_config.cpython-312.pyc
│  │     │  │  │  │  └─ test_localization.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_config.py
│  │     │  │  │  └─ test_localization.py
│  │     │  │  ├─ construction/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ test_extract_array.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ test_extract_array.py
│  │     │  │  ├─ copy_view/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array.cpython-312.pyc
│  │     │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  ├─ test_chained_assignment_deprecation.cpython-312.pyc
│  │     │  │  │  │  ├─ test_clip.cpython-312.pyc
│  │     │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  ├─ test_core_functionalities.cpython-312.pyc
│  │     │  │  │  │  ├─ test_functions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_internals.cpython-312.pyc
│  │     │  │  │  │  ├─ test_interp_fillna.cpython-312.pyc
│  │     │  │  │  │  ├─ test_methods.cpython-312.pyc
│  │     │  │  │  │  ├─ test_replace.cpython-312.pyc
│  │     │  │  │  │  ├─ test_setitem.cpython-312.pyc
│  │     │  │  │  │  ├─ test_util.cpython-312.pyc
│  │     │  │  │  │  └─ util.cpython-312.pyc
│  │     │  │  │  ├─ index/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_datetimeindex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_periodindex.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_timedeltaindex.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_datetimeindex.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_periodindex.py
│  │     │  │  │  │  └─ test_timedeltaindex.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_array.py
│  │     │  │  │  ├─ test_astype.py
│  │     │  │  │  ├─ test_chained_assignment_deprecation.py
│  │     │  │  │  ├─ test_clip.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_core_functionalities.py
│  │     │  │  │  ├─ test_functions.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_internals.py
│  │     │  │  │  ├─ test_interp_fillna.py
│  │     │  │  │  ├─ test_methods.py
│  │     │  │  │  ├─ test_replace.py
│  │     │  │  │  ├─ test_setitem.py
│  │     │  │  │  ├─ test_util.py
│  │     │  │  │  └─ util.py
│  │     │  │  ├─ dtypes/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_concat.cpython-312.pyc
│  │     │  │  │  │  ├─ test_dtypes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_generic.cpython-312.pyc
│  │     │  │  │  │  ├─ test_inference.cpython-312.pyc
│  │     │  │  │  │  └─ test_missing.cpython-312.pyc
│  │     │  │  │  ├─ cast/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_can_hold_element.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_construct_from_scalar.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_construct_ndarray.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_construct_object_arr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dict_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_downcast.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_find_common_type.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_infer_datetimelike.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_infer_dtype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_maybe_box_native.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_promote.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_can_hold_element.py
│  │     │  │  │  │  ├─ test_construct_from_scalar.py
│  │     │  │  │  │  ├─ test_construct_ndarray.py
│  │     │  │  │  │  ├─ test_construct_object_arr.py
│  │     │  │  │  │  ├─ test_dict_compat.py
│  │     │  │  │  │  ├─ test_downcast.py
│  │     │  │  │  │  ├─ test_find_common_type.py
│  │     │  │  │  │  ├─ test_infer_datetimelike.py
│  │     │  │  │  │  ├─ test_infer_dtype.py
│  │     │  │  │  │  ├─ test_maybe_box_native.py
│  │     │  │  │  │  └─ test_promote.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_concat.py
│  │     │  │  │  ├─ test_dtypes.py
│  │     │  │  │  ├─ test_generic.py
│  │     │  │  │  ├─ test_inference.py
│  │     │  │  │  └─ test_missing.py
│  │     │  │  ├─ extension/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arrow.cpython-312.pyc
│  │     │  │  │  │  ├─ test_categorical.cpython-312.pyc
│  │     │  │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_extension.cpython-312.pyc
│  │     │  │  │  │  ├─ test_interval.cpython-312.pyc
│  │     │  │  │  │  ├─ test_masked.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numpy.cpython-312.pyc
│  │     │  │  │  │  ├─ test_period.cpython-312.pyc
│  │     │  │  │  │  ├─ test_sparse.cpython-312.pyc
│  │     │  │  │  │  └─ test_string.cpython-312.pyc
│  │     │  │  │  ├─ array_with_attr/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ array.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_array_with_attr.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  └─ test_array_with_attr.py
│  │     │  │  │  ├─ base/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ accumulate.cpython-312.pyc
│  │     │  │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  │  ├─ casting.cpython-312.pyc
│  │     │  │  │  │  │  ├─ constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ dim2.cpython-312.pyc
│  │     │  │  │  │  │  ├─ dtype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ getitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ groupby.cpython-312.pyc
│  │     │  │  │  │  │  ├─ index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ interface.cpython-312.pyc
│  │     │  │  │  │  │  ├─ io.cpython-312.pyc
│  │     │  │  │  │  │  ├─ methods.cpython-312.pyc
│  │     │  │  │  │  │  ├─ missing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ ops.cpython-312.pyc
│  │     │  │  │  │  │  ├─ printing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ reduce.cpython-312.pyc
│  │     │  │  │  │  │  ├─ reshaping.cpython-312.pyc
│  │     │  │  │  │  │  └─ setitem.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ accumulate.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ casting.py
│  │     │  │  │  │  ├─ constructors.py
│  │     │  │  │  │  ├─ dim2.py
│  │     │  │  │  │  ├─ dtype.py
│  │     │  │  │  │  ├─ getitem.py
│  │     │  │  │  │  ├─ groupby.py
│  │     │  │  │  │  ├─ index.py
│  │     │  │  │  │  ├─ interface.py
│  │     │  │  │  │  ├─ io.py
│  │     │  │  │  │  ├─ methods.py
│  │     │  │  │  │  ├─ missing.py
│  │     │  │  │  │  ├─ ops.py
│  │     │  │  │  │  ├─ printing.py
│  │     │  │  │  │  ├─ reduce.py
│  │     │  │  │  │  ├─ reshaping.py
│  │     │  │  │  │  └─ setitem.py
│  │     │  │  │  ├─ date/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ array.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ array.py
│  │     │  │  │  ├─ decimal/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ array.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_decimal.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  └─ test_decimal.py
│  │     │  │  │  ├─ json/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ array.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_json.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  └─ test_json.py
│  │     │  │  │  ├─ list/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ array.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_list.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ array.py
│  │     │  │  │  │  └─ test_list.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_arrow.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_extension.py
│  │     │  │  │  ├─ test_interval.py
│  │     │  │  │  ├─ test_masked.py
│  │     │  │  │  ├─ test_numpy.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_sparse.py
│  │     │  │  │  └─ test_string.py
│  │     │  │  ├─ frame/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_alter_axes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arrow_interface.cpython-312.pyc
│  │     │  │  │  │  ├─ test_block_internals.cpython-312.pyc
│  │     │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cumulative.cpython-312.pyc
│  │     │  │  │  │  ├─ test_iteration.cpython-312.pyc
│  │     │  │  │  │  ├─ test_logical_ops.cpython-312.pyc
│  │     │  │  │  │  ├─ test_nonunique_indexes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_npfuncs.cpython-312.pyc
│  │     │  │  │  │  ├─ test_query_eval.cpython-312.pyc
│  │     │  │  │  │  ├─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_repr.cpython-312.pyc
│  │     │  │  │  │  ├─ test_stack_unstack.cpython-312.pyc
│  │     │  │  │  │  ├─ test_subclass.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ufunc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_unary.cpython-312.pyc
│  │     │  │  │  │  └─ test_validate.cpython-312.pyc
│  │     │  │  │  ├─ constructors/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_from_dict.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_from_records.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_from_dict.py
│  │     │  │  │  │  └─ test_from_records.py
│  │     │  │  │  ├─ indexing/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_coercion.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_delitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_get_value.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_get.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_getitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_insert.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_mask.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_set_value.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_take.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_where.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_xs.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_coercion.py
│  │     │  │  │  │  ├─ test_delitem.py
│  │     │  │  │  │  ├─ test_get_value.py
│  │     │  │  │  │  ├─ test_get.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  ├─ test_mask.py
│  │     │  │  │  │  ├─ test_set_value.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  └─ test_xs.py
│  │     │  │  │  ├─ methods/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_add_prefix_suffix.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_align.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_asfreq.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_asof.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_assign.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_at_time.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_between_time.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_clip.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_combine_first.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_combine.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_compare.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_convert_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_copy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_count.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_cov_corr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_describe.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_diff.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dot.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_drop_duplicates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_drop.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_droplevel.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dropna.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_duplicated.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_equals.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_explode.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_fillna.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_filter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_first_and_last.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_first_valid_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_get_numeric_data.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_head_tail.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_infer_objects.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_info.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interpolate.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_is_homogeneous_dtype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_isetitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_isin.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_iterrows.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_map.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_matmul.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_nlargest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pct_change.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pipe.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pop.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_quantile.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_rank.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reindex_like.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reindex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_rename_axis.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_rename.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reorder_levels.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_replace.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reset_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_round.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sample.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_select_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_set_axis.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_set_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_shift.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_size.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sort_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sort_values.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_swapaxes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_swaplevel.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_csv.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_dict_of_blocks.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_dict.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_numpy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_period.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_records.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_timestamp.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_transpose.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_truncate.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_tz_convert.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_tz_localize.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_update.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_value_counts.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_values.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_add_prefix_suffix.py
│  │     │  │  │  │  ├─ test_align.py
│  │     │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  ├─ test_assign.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_at_time.py
│  │     │  │  │  │  ├─ test_between_time.py
│  │     │  │  │  │  ├─ test_clip.py
│  │     │  │  │  │  ├─ test_combine_first.py
│  │     │  │  │  │  ├─ test_combine.py
│  │     │  │  │  │  ├─ test_compare.py
│  │     │  │  │  │  ├─ test_convert_dtypes.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_count.py
│  │     │  │  │  │  ├─ test_cov_corr.py
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_diff.py
│  │     │  │  │  │  ├─ test_dot.py
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_droplevel.py
│  │     │  │  │  │  ├─ test_dropna.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_duplicated.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_explode.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_filter.py
│  │     │  │  │  │  ├─ test_first_and_last.py
│  │     │  │  │  │  ├─ test_first_valid_index.py
│  │     │  │  │  │  ├─ test_get_numeric_data.py
│  │     │  │  │  │  ├─ test_head_tail.py
│  │     │  │  │  │  ├─ test_infer_objects.py
│  │     │  │  │  │  ├─ test_info.py
│  │     │  │  │  │  ├─ test_interpolate.py
│  │     │  │  │  │  ├─ test_is_homogeneous_dtype.py
│  │     │  │  │  │  ├─ test_isetitem.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_iterrows.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_matmul.py
│  │     │  │  │  │  ├─ test_nlargest.py
│  │     │  │  │  │  ├─ test_pct_change.py
│  │     │  │  │  │  ├─ test_pipe.py
│  │     │  │  │  │  ├─ test_pop.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_reindex_like.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_rename_axis.py
│  │     │  │  │  │  ├─ test_rename.py
│  │     │  │  │  │  ├─ test_reorder_levels.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_reset_index.py
│  │     │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  ├─ test_sample.py
│  │     │  │  │  │  ├─ test_select_dtypes.py
│  │     │  │  │  │  ├─ test_set_axis.py
│  │     │  │  │  │  ├─ test_set_index.py
│  │     │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  ├─ test_size.py
│  │     │  │  │  │  ├─ test_sort_index.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_swapaxes.py
│  │     │  │  │  │  ├─ test_swaplevel.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_dict_of_blocks.py
│  │     │  │  │  │  ├─ test_to_dict.py
│  │     │  │  │  │  ├─ test_to_numpy.py
│  │     │  │  │  │  ├─ test_to_period.py
│  │     │  │  │  │  ├─ test_to_records.py
│  │     │  │  │  │  ├─ test_to_timestamp.py
│  │     │  │  │  │  ├─ test_transpose.py
│  │     │  │  │  │  ├─ test_truncate.py
│  │     │  │  │  │  ├─ test_tz_convert.py
│  │     │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  ├─ test_update.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  └─ test_values.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_alter_axes.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  ├─ test_arrow_interface.py
│  │     │  │  │  ├─ test_block_internals.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_iteration.py
│  │     │  │  │  ├─ test_logical_ops.py
│  │     │  │  │  ├─ test_nonunique_indexes.py
│  │     │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  ├─ test_query_eval.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_repr.py
│  │     │  │  │  ├─ test_stack_unstack.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_unary.py
│  │     │  │  │  └─ test_validate.py
│  │     │  │  ├─ generic/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_duplicate_labels.cpython-312.pyc
│  │     │  │  │  │  ├─ test_finalize.cpython-312.pyc
│  │     │  │  │  │  ├─ test_frame.cpython-312.pyc
│  │     │  │  │  │  ├─ test_generic.cpython-312.pyc
│  │     │  │  │  │  ├─ test_label_or_level_utils.cpython-312.pyc
│  │     │  │  │  │  ├─ test_series.cpython-312.pyc
│  │     │  │  │  │  └─ test_to_xarray.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_duplicate_labels.py
│  │     │  │  │  ├─ test_finalize.py
│  │     │  │  │  ├─ test_frame.py
│  │     │  │  │  ├─ test_generic.py
│  │     │  │  │  ├─ test_label_or_level_utils.py
│  │     │  │  │  ├─ test_series.py
│  │     │  │  │  └─ test_to_xarray.py
│  │     │  │  ├─ groupby/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_all_methods.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_apply_mutate.cpython-312.pyc
│  │     │  │  │  │  ├─ test_apply.cpython-312.pyc
│  │     │  │  │  │  ├─ test_bin_groupby.cpython-312.pyc
│  │     │  │  │  │  ├─ test_categorical.cpython-312.pyc
│  │     │  │  │  │  ├─ test_counting.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cumulative.cpython-312.pyc
│  │     │  │  │  │  ├─ test_filters.cpython-312.pyc
│  │     │  │  │  │  ├─ test_groupby_dropna.cpython-312.pyc
│  │     │  │  │  │  ├─ test_groupby_subclass.cpython-312.pyc
│  │     │  │  │  │  ├─ test_groupby.cpython-312.pyc
│  │     │  │  │  │  ├─ test_grouping.cpython-312.pyc
│  │     │  │  │  │  ├─ test_index_as_string.cpython-312.pyc
│  │     │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_libgroupby.cpython-312.pyc
│  │     │  │  │  │  ├─ test_missing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numba.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numeric_only.cpython-312.pyc
│  │     │  │  │  │  ├─ test_pipe.cpython-312.pyc
│  │     │  │  │  │  ├─ test_raises.cpython-312.pyc
│  │     │  │  │  │  ├─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  └─ test_timegrouper.cpython-312.pyc
│  │     │  │  │  ├─ aggregate/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_aggregate.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_cython.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_numba.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_other.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_aggregate.py
│  │     │  │  │  │  ├─ test_cython.py
│  │     │  │  │  │  ├─ test_numba.py
│  │     │  │  │  │  └─ test_other.py
│  │     │  │  │  ├─ methods/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_corrwith.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_describe.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_groupby_shift_diff.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_is_monotonic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_nlargest_nsmallest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_nth.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_quantile.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_rank.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sample.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_size.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_skew.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_value_counts.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_corrwith.py
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_groupby_shift_diff.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_nlargest_nsmallest.py
│  │     │  │  │  │  ├─ test_nth.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_sample.py
│  │     │  │  │  │  ├─ test_size.py
│  │     │  │  │  │  ├─ test_skew.py
│  │     │  │  │  │  └─ test_value_counts.py
│  │     │  │  │  ├─ transform/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_numba.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_transform.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_numba.py
│  │     │  │  │  │  └─ test_transform.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_all_methods.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_apply_mutate.py
│  │     │  │  │  ├─ test_apply.py
│  │     │  │  │  ├─ test_bin_groupby.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_counting.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_filters.py
│  │     │  │  │  ├─ test_groupby_dropna.py
│  │     │  │  │  ├─ test_groupby_subclass.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_grouping.py
│  │     │  │  │  ├─ test_index_as_string.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_libgroupby.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_numeric_only.py
│  │     │  │  │  ├─ test_pipe.py
│  │     │  │  │  ├─ test_raises.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  └─ test_timegrouper.py
│  │     │  │  ├─ indexes/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_any_index.cpython-312.pyc
│  │     │  │  │  │  ├─ test_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetimelike.cpython-312.pyc
│  │     │  │  │  │  ├─ test_engines.cpython-312.pyc
│  │     │  │  │  │  ├─ test_frozen.cpython-312.pyc
│  │     │  │  │  │  ├─ test_index_new.cpython-312.pyc
│  │     │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numpy_compat.cpython-312.pyc
│  │     │  │  │  │  ├─ test_old_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_setops.cpython-312.pyc
│  │     │  │  │  │  └─ test_subclass.cpython-312.pyc
│  │     │  │  │  ├─ base_class/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reshape.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setops.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_where.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reshape.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  └─ test_where.py
│  │     │  │  │  ├─ categorical/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_append.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_category.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_equals.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_fillna.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_map.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reindex.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_setops.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_category.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  └─ test_setops.py
│  │     │  │  │  ├─ datetimelike_/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_drop_duplicates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_equals.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_is_monotonic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_nat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sort_values.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_value_counts.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_nat.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  └─ test_value_counts.py
│  │     │  │  │  ├─ datetimes/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_date_range.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_datetime.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_freq_attr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_iter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_npfuncs.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_ops.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_partial_slicing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reindex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_scalar_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setops.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_timezones.cpython-312.pyc
│  │     │  │  │  │  ├─ methods/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_asof.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_delete.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_factorize.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_fillna.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_insert.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_isocalendar.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_map.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_normalize.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_repeat.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_resolution.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_round.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_shift.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_snap.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_frame.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_julian_date.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_period.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_pydatetime.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_series.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_tz_convert.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_tz_localize.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_unique.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_delete.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_isocalendar.py
│  │     │  │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  │  ├─ test_normalize.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_resolution.py
│  │     │  │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  ├─ test_snap.py
│  │     │  │  │  │  │  ├─ test_to_frame.py
│  │     │  │  │  │  │  ├─ test_to_julian_date.py
│  │     │  │  │  │  │  ├─ test_to_period.py
│  │     │  │  │  │  │  ├─ test_to_pydatetime.py
│  │     │  │  │  │  │  ├─ test_to_series.py
│  │     │  │  │  │  │  ├─ test_tz_convert.py
│  │     │  │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  │  └─ test_unique.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_date_range.py
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_iter.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_partial_slicing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  └─ test_timezones.py
│  │     │  │  │  ├─ interval/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_equals.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interval_range.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interval_tree.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interval.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_setops.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_interval_range.py
│  │     │  │  │  │  ├─ test_interval_tree.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  └─ test_setops.py
│  │     │  │  │  ├─ multi/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_analytics.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_conversion.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_copy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_drop.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_duplicates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_equivalence.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_get_level_values.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_get_set.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_integrity.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_isin.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_lexsort.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_missing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_monotonic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_names.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_partial_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reindex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reshape.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setops.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sorting.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_take.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_analytics.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_compat.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_conversion.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_duplicates.py
│  │     │  │  │  │  ├─ test_equivalence.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_get_level_values.py
│  │     │  │  │  │  ├─ test_get_set.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_integrity.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_lexsort.py
│  │     │  │  │  │  ├─ test_missing.py
│  │     │  │  │  │  ├─ test_monotonic.py
│  │     │  │  │  │  ├─ test_names.py
│  │     │  │  │  │  ├─ test_partial_indexing.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_reshape.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_sorting.py
│  │     │  │  │  │  └─ test_take.py
│  │     │  │  │  ├─ numeric/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_numeric.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_setops.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_numeric.py
│  │     │  │  │  │  └─ test_setops.py
│  │     │  │  │  ├─ object/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  └─ test_indexing.py
│  │     │  │  │  ├─ period/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_freq_attr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_monotonic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_partial_slicing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_period_range.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_period.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_resolution.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_scalar_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_searchsorted.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setops.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_tools.cpython-312.pyc
│  │     │  │  │  │  ├─ methods/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_asfreq.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_factorize.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_fillna.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_insert.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_is_full.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_repeat.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_shift.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_to_timestamp.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_is_full.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  ├─ test_shift.py
│  │     │  │  │  │  │  └─ test_to_timestamp.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_monotonic.py
│  │     │  │  │  │  ├─ test_partial_slicing.py
│  │     │  │  │  │  ├─ test_period_range.py
│  │     │  │  │  │  ├─ test_period.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_resolution.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  └─ test_tools.py
│  │     │  │  │  ├─ ranges/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_range.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_setops.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_range.py
│  │     │  │  │  │  └─ test_setops.py
│  │     │  │  │  ├─ string/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  └─ test_indexing.py
│  │     │  │  │  ├─ timedeltas/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_delete.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_freq_attr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_ops.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_scalar_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_searchsorted.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setops.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_timedelta_range.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_timedelta.cpython-312.pyc
│  │     │  │  │  │  ├─ methods/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_factorize.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_fillna.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_insert.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_repeat.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_shift.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  │  ├─ test_factorize.py
│  │     │  │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  │  ├─ test_insert.py
│  │     │  │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  │  └─ test_shift.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_delete.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_freq_attr.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_ops.py
│  │     │  │  │  │  ├─ test_pickle.py
│  │     │  │  │  │  ├─ test_scalar_compat.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_setops.py
│  │     │  │  │  │  ├─ test_timedelta_range.py
│  │     │  │  │  │  └─ test_timedelta.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_any_index.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_engines.py
│  │     │  │  │  ├─ test_frozen.py
│  │     │  │  │  ├─ test_index_new.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_numpy_compat.py
│  │     │  │  │  ├─ test_old_base.py
│  │     │  │  │  ├─ test_setops.py
│  │     │  │  │  └─ test_subclass.py
│  │     │  │  ├─ indexing/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_at.cpython-312.pyc
│  │     │  │  │  │  ├─ test_categorical.cpython-312.pyc
│  │     │  │  │  │  ├─ test_chaining_and_caching.cpython-312.pyc
│  │     │  │  │  │  ├─ test_check_indexer.cpython-312.pyc
│  │     │  │  │  │  ├─ test_coercion.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_floats.cpython-312.pyc
│  │     │  │  │  │  ├─ test_iat.cpython-312.pyc
│  │     │  │  │  │  ├─ test_iloc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_indexers.cpython-312.pyc
│  │     │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_loc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_na_indexing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_partial.cpython-312.pyc
│  │     │  │  │  │  └─ test_scalar.cpython-312.pyc
│  │     │  │  │  ├─ interval/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interval_new.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_interval.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_interval_new.py
│  │     │  │  │  │  └─ test_interval.py
│  │     │  │  │  ├─ multiindex/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_chaining_and_caching.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_datetime.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_getitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_iloc.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing_slow.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_loc.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_multiindex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_partial.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_slice.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_sorted.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_chaining_and_caching.py
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_iloc.py
│  │     │  │  │  │  ├─ test_indexing_slow.py
│  │     │  │  │  │  ├─ test_loc.py
│  │     │  │  │  │  ├─ test_multiindex.py
│  │     │  │  │  │  ├─ test_partial.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_slice.py
│  │     │  │  │  │  └─ test_sorted.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_at.py
│  │     │  │  │  ├─ test_categorical.py
│  │     │  │  │  ├─ test_chaining_and_caching.py
│  │     │  │  │  ├─ test_check_indexer.py
│  │     │  │  │  ├─ test_coercion.py
│  │     │  │  │  ├─ test_datetime.py
│  │     │  │  │  ├─ test_floats.py
│  │     │  │  │  ├─ test_iat.py
│  │     │  │  │  ├─ test_iloc.py
│  │     │  │  │  ├─ test_indexers.py
│  │     │  │  │  ├─ test_indexing.py
│  │     │  │  │  ├─ test_loc.py
│  │     │  │  │  ├─ test_na_indexing.py
│  │     │  │  │  ├─ test_partial.py
│  │     │  │  │  └─ test_scalar.py
│  │     │  │  ├─ interchange/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_impl.cpython-312.pyc
│  │     │  │  │  │  ├─ test_spec_conformance.cpython-312.pyc
│  │     │  │  │  │  └─ test_utils.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_impl.py
│  │     │  │  │  ├─ test_spec_conformance.py
│  │     │  │  │  └─ test_utils.py
│  │     │  │  ├─ internals/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_internals.cpython-312.pyc
│  │     │  │  │  │  └─ test_managers.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_internals.py
│  │     │  │  │  └─ test_managers.py
│  │     │  │  ├─ io/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ generate_legacy_storage_files.cpython-312.pyc
│  │     │  │  │  │  ├─ test_clipboard.cpython-312.pyc
│  │     │  │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_compression.cpython-312.pyc
│  │     │  │  │  │  ├─ test_feather.cpython-312.pyc
│  │     │  │  │  │  ├─ test_fsspec.cpython-312.pyc
│  │     │  │  │  │  ├─ test_gbq.cpython-312.pyc
│  │     │  │  │  │  ├─ test_gcs.cpython-312.pyc
│  │     │  │  │  │  ├─ test_html.cpython-312.pyc
│  │     │  │  │  │  ├─ test_http_headers.cpython-312.pyc
│  │     │  │  │  │  ├─ test_orc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_parquet.cpython-312.pyc
│  │     │  │  │  │  ├─ test_pickle.cpython-312.pyc
│  │     │  │  │  │  ├─ test_s3.cpython-312.pyc
│  │     │  │  │  │  ├─ test_spss.cpython-312.pyc
│  │     │  │  │  │  ├─ test_sql.cpython-312.pyc
│  │     │  │  │  │  └─ test_stata.cpython-312.pyc
│  │     │  │  │  ├─ excel/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_odf.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_odswriter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_openpyxl.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_readers.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_style.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_writers.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_xlrd.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_xlsxwriter.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_odf.py
│  │     │  │  │  │  ├─ test_odswriter.py
│  │     │  │  │  │  ├─ test_openpyxl.py
│  │     │  │  │  │  ├─ test_readers.py
│  │     │  │  │  │  ├─ test_style.py
│  │     │  │  │  │  ├─ test_writers.py
│  │     │  │  │  │  ├─ test_xlrd.py
│  │     │  │  │  │  └─ test_xlsxwriter.py
│  │     │  │  │  ├─ formats/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_console.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_css.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_eng_formatting.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_format.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_ipython_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_printing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_csv.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_excel.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_html.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_latex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_markdown.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_to_string.cpython-312.pyc
│  │     │  │  │  │  ├─ style/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_bar.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_exceptions.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_format.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_highlight.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_html.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_matplotlib.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_non_unique.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_style.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_latex.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_string.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_tooltip.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_bar.py
│  │     │  │  │  │  │  ├─ test_exceptions.py
│  │     │  │  │  │  │  ├─ test_format.py
│  │     │  │  │  │  │  ├─ test_highlight.py
│  │     │  │  │  │  │  ├─ test_html.py
│  │     │  │  │  │  │  ├─ test_matplotlib.py
│  │     │  │  │  │  │  ├─ test_non_unique.py
│  │     │  │  │  │  │  ├─ test_style.py
│  │     │  │  │  │  │  ├─ test_to_latex.py
│  │     │  │  │  │  │  ├─ test_to_string.py
│  │     │  │  │  │  │  └─ test_tooltip.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_console.py
│  │     │  │  │  │  ├─ test_css.py
│  │     │  │  │  │  ├─ test_eng_formatting.py
│  │     │  │  │  │  ├─ test_format.py
│  │     │  │  │  │  ├─ test_ipython_compat.py
│  │     │  │  │  │  ├─ test_printing.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_excel.py
│  │     │  │  │  │  ├─ test_to_html.py
│  │     │  │  │  │  ├─ test_to_latex.py
│  │     │  │  │  │  ├─ test_to_markdown.py
│  │     │  │  │  │  └─ test_to_string.py
│  │     │  │  │  ├─ json/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_compression.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_deprecated_kwargs.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_json_table_schema_ext_dtype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_json_table_schema.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_normalize.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pandas.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_readlines.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_ujson.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_compression.py
│  │     │  │  │  │  ├─ test_deprecated_kwargs.py
│  │     │  │  │  │  ├─ test_json_table_schema_ext_dtype.py
│  │     │  │  │  │  ├─ test_json_table_schema.py
│  │     │  │  │  │  ├─ test_normalize.py
│  │     │  │  │  │  ├─ test_pandas.py
│  │     │  │  │  │  ├─ test_readlines.py
│  │     │  │  │  │  └─ test_ujson.py
│  │     │  │  │  ├─ parser/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_c_parser_only.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_comment.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_compression.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_concatenate_chunks.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_converters.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dialect.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_encoding.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_header.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_index_col.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_mangle_dupes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_multi_thread.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_na_values.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_network.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_parse_dates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_python_parser_only.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_quoting.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_read_fwf.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_skiprows.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_textreader.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_unsupported.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_upcast.cpython-312.pyc
│  │     │  │  │  │  ├─ common/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_chunksize.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_common_basic.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_data_list.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_decimal.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_file_buffer_url.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_float.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_index.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_inf.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_ints.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_iterator.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_read_errors.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_verbose.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_chunksize.py
│  │     │  │  │  │  │  ├─ test_common_basic.py
│  │     │  │  │  │  │  ├─ test_data_list.py
│  │     │  │  │  │  │  ├─ test_decimal.py
│  │     │  │  │  │  │  ├─ test_file_buffer_url.py
│  │     │  │  │  │  │  ├─ test_float.py
│  │     │  │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  │  ├─ test_inf.py
│  │     │  │  │  │  │  ├─ test_ints.py
│  │     │  │  │  │  │  ├─ test_iterator.py
│  │     │  │  │  │  │  ├─ test_read_errors.py
│  │     │  │  │  │  │  └─ test_verbose.py
│  │     │  │  │  │  ├─ dtypes/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_categorical.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_dtypes_basic.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_empty.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  │  ├─ test_dtypes_basic.py
│  │     │  │  │  │  │  └─ test_empty.py
│  │     │  │  │  │  ├─ usecols/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_parse_dates.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_strings.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_usecols_basic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_parse_dates.py
│  │     │  │  │  │  │  ├─ test_strings.py
│  │     │  │  │  │  │  └─ test_usecols_basic.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_c_parser_only.py
│  │     │  │  │  │  ├─ test_comment.py
│  │     │  │  │  │  ├─ test_compression.py
│  │     │  │  │  │  ├─ test_concatenate_chunks.py
│  │     │  │  │  │  ├─ test_converters.py
│  │     │  │  │  │  ├─ test_dialect.py
│  │     │  │  │  │  ├─ test_encoding.py
│  │     │  │  │  │  ├─ test_header.py
│  │     │  │  │  │  ├─ test_index_col.py
│  │     │  │  │  │  ├─ test_mangle_dupes.py
│  │     │  │  │  │  ├─ test_multi_thread.py
│  │     │  │  │  │  ├─ test_na_values.py
│  │     │  │  │  │  ├─ test_network.py
│  │     │  │  │  │  ├─ test_parse_dates.py
│  │     │  │  │  │  ├─ test_python_parser_only.py
│  │     │  │  │  │  ├─ test_quoting.py
│  │     │  │  │  │  ├─ test_read_fwf.py
│  │     │  │  │  │  ├─ test_skiprows.py
│  │     │  │  │  │  ├─ test_textreader.py
│  │     │  │  │  │  ├─ test_unsupported.py
│  │     │  │  │  │  └─ test_upcast.py
│  │     │  │  │  ├─ pytables/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_append.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_categorical.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_complex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_errors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_file_handling.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_keys.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_put.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pytables_missing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_read.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_retain_attributes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_round_trip.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_select.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_store.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_subclass.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_time_series.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_timezones.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ common.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  ├─ test_compat.py
│  │     │  │  │  │  ├─ test_complex.py
│  │     │  │  │  │  ├─ test_errors.py
│  │     │  │  │  │  ├─ test_file_handling.py
│  │     │  │  │  │  ├─ test_keys.py
│  │     │  │  │  │  ├─ test_put.py
│  │     │  │  │  │  ├─ test_pytables_missing.py
│  │     │  │  │  │  ├─ test_read.py
│  │     │  │  │  │  ├─ test_retain_attributes.py
│  │     │  │  │  │  ├─ test_round_trip.py
│  │     │  │  │  │  ├─ test_select.py
│  │     │  │  │  │  ├─ test_store.py
│  │     │  │  │  │  ├─ test_subclass.py
│  │     │  │  │  │  ├─ test_time_series.py
│  │     │  │  │  │  └─ test_timezones.py
│  │     │  │  │  ├─ sas/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_byteswap.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sas.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sas7bdat.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_xport.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_byteswap.py
│  │     │  │  │  │  ├─ test_sas.py
│  │     │  │  │  │  ├─ test_sas7bdat.py
│  │     │  │  │  │  └─ test_xport.py
│  │     │  │  │  ├─ xml/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_xml.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_xml_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_xml.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_to_xml.py
│  │     │  │  │  │  ├─ test_xml_dtypes.py
│  │     │  │  │  │  └─ test_xml.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ generate_legacy_storage_files.py
│  │     │  │  │  ├─ test_clipboard.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_compression.py
│  │     │  │  │  ├─ test_feather.py
│  │     │  │  │  ├─ test_fsspec.py
│  │     │  │  │  ├─ test_gbq.py
│  │     │  │  │  ├─ test_gcs.py
│  │     │  │  │  ├─ test_html.py
│  │     │  │  │  ├─ test_http_headers.py
│  │     │  │  │  ├─ test_orc.py
│  │     │  │  │  ├─ test_parquet.py
│  │     │  │  │  ├─ test_pickle.py
│  │     │  │  │  ├─ test_s3.py
│  │     │  │  │  ├─ test_spss.py
│  │     │  │  │  ├─ test_sql.py
│  │     │  │  │  └─ test_stata.py
│  │     │  │  ├─ libs/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_hashtable.cpython-312.pyc
│  │     │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  ├─ test_lib.cpython-312.pyc
│  │     │  │  │  │  └─ test_libalgos.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_hashtable.py
│  │     │  │  │  ├─ test_join.py
│  │     │  │  │  ├─ test_lib.py
│  │     │  │  │  └─ test_libalgos.py
│  │     │  │  ├─ plotting/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_backend.cpython-312.pyc
│  │     │  │  │  │  ├─ test_boxplot_method.cpython-312.pyc
│  │     │  │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  │  ├─ test_converter.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetimelike.cpython-312.pyc
│  │     │  │  │  │  ├─ test_groupby.cpython-312.pyc
│  │     │  │  │  │  ├─ test_hist_method.cpython-312.pyc
│  │     │  │  │  │  ├─ test_misc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_series.cpython-312.pyc
│  │     │  │  │  │  └─ test_style.cpython-312.pyc
│  │     │  │  │  ├─ frame/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_frame_color.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_frame_groupby.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_frame_legend.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_frame_subplots.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_frame.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_hist_box_by.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_frame_color.py
│  │     │  │  │  │  ├─ test_frame_groupby.py
│  │     │  │  │  │  ├─ test_frame_legend.py
│  │     │  │  │  │  ├─ test_frame_subplots.py
│  │     │  │  │  │  ├─ test_frame.py
│  │     │  │  │  │  └─ test_hist_box_by.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ common.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_backend.py
│  │     │  │  │  ├─ test_boxplot_method.py
│  │     │  │  │  ├─ test_common.py
│  │     │  │  │  ├─ test_converter.py
│  │     │  │  │  ├─ test_datetimelike.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_hist_method.py
│  │     │  │  │  ├─ test_misc.py
│  │     │  │  │  ├─ test_series.py
│  │     │  │  │  └─ test_style.py
│  │     │  │  ├─ reductions/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  └─ test_stat_reductions.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  └─ test_stat_reductions.py
│  │     │  │  ├─ resample/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_base.cpython-312.pyc
│  │     │  │  │  │  ├─ test_datetime_index.cpython-312.pyc
│  │     │  │  │  │  ├─ test_period_index.cpython-312.pyc
│  │     │  │  │  │  ├─ test_resample_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_resampler_grouper.cpython-312.pyc
│  │     │  │  │  │  ├─ test_time_grouper.cpython-312.pyc
│  │     │  │  │  │  └─ test_timedelta.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_base.py
│  │     │  │  │  ├─ test_datetime_index.py
│  │     │  │  │  ├─ test_period_index.py
│  │     │  │  │  ├─ test_resample_api.py
│  │     │  │  │  ├─ test_resampler_grouper.py
│  │     │  │  │  ├─ test_time_grouper.py
│  │     │  │  │  └─ test_timedelta.py
│  │     │  │  ├─ reshape/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_crosstab.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cut.cpython-312.pyc
│  │     │  │  │  │  ├─ test_from_dummies.cpython-312.pyc
│  │     │  │  │  │  ├─ test_get_dummies.cpython-312.pyc
│  │     │  │  │  │  ├─ test_melt.cpython-312.pyc
│  │     │  │  │  │  ├─ test_pivot_multilevel.cpython-312.pyc
│  │     │  │  │  │  ├─ test_pivot.cpython-312.pyc
│  │     │  │  │  │  ├─ test_qcut.cpython-312.pyc
│  │     │  │  │  │  ├─ test_union_categoricals.cpython-312.pyc
│  │     │  │  │  │  └─ test_util.cpython-312.pyc
│  │     │  │  │  ├─ concat/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_append_common.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_append.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_categorical.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_concat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dataframe.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_datetimes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_empty.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_invalid.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_series.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_sort.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_append_common.py
│  │     │  │  │  │  ├─ test_append.py
│  │     │  │  │  │  ├─ test_categorical.py
│  │     │  │  │  │  ├─ test_concat.py
│  │     │  │  │  │  ├─ test_dataframe.py
│  │     │  │  │  │  ├─ test_datetimes.py
│  │     │  │  │  │  ├─ test_empty.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_invalid.py
│  │     │  │  │  │  ├─ test_series.py
│  │     │  │  │  │  └─ test_sort.py
│  │     │  │  │  ├─ merge/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_join.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_merge_asof.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_merge_cross.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_merge_index_as_string.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_merge_ordered.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_merge.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_multi.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_join.py
│  │     │  │  │  │  ├─ test_merge_asof.py
│  │     │  │  │  │  ├─ test_merge_cross.py
│  │     │  │  │  │  ├─ test_merge_index_as_string.py
│  │     │  │  │  │  ├─ test_merge_ordered.py
│  │     │  │  │  │  ├─ test_merge.py
│  │     │  │  │  │  └─ test_multi.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_crosstab.py
│  │     │  │  │  ├─ test_cut.py
│  │     │  │  │  ├─ test_from_dummies.py
│  │     │  │  │  ├─ test_get_dummies.py
│  │     │  │  │  ├─ test_melt.py
│  │     │  │  │  ├─ test_pivot_multilevel.py
│  │     │  │  │  ├─ test_pivot.py
│  │     │  │  │  ├─ test_qcut.py
│  │     │  │  │  ├─ test_union_categoricals.py
│  │     │  │  │  └─ test_util.py
│  │     │  │  ├─ scalar/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_na_scalar.cpython-312.pyc
│  │     │  │  │  │  └─ test_nat.cpython-312.pyc
│  │     │  │  │  ├─ interval/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_contains.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interval.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_overlaps.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_contains.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_interval.py
│  │     │  │  │  │  └─ test_overlaps.py
│  │     │  │  │  ├─ period/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_asfreq.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_period.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_asfreq.py
│  │     │  │  │  │  └─ test_period.py
│  │     │  │  │  ├─ timedelta/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_timedelta.cpython-312.pyc
│  │     │  │  │  │  ├─ methods/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_as_unit.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_round.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_as_unit.py
│  │     │  │  │  │  │  └─ test_round.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  └─ test_timedelta.py
│  │     │  │  │  ├─ timestamp/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_comparisons.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_timestamp.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_timezones.cpython-312.pyc
│  │     │  │  │  │  ├─ methods/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_as_unit.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_normalize.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_replace.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_round.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_timestamp_method.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_julian_date.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_to_pydatetime.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ test_tz_convert.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ test_tz_localize.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ test_as_unit.py
│  │     │  │  │  │  │  ├─ test_normalize.py
│  │     │  │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  │  ├─ test_timestamp_method.py
│  │     │  │  │  │  │  ├─ test_to_julian_date.py
│  │     │  │  │  │  │  ├─ test_to_pydatetime.py
│  │     │  │  │  │  │  ├─ test_tz_convert.py
│  │     │  │  │  │  │  └─ test_tz_localize.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  │  ├─ test_comparisons.py
│  │     │  │  │  │  ├─ test_constructors.py
│  │     │  │  │  │  ├─ test_formats.py
│  │     │  │  │  │  ├─ test_timestamp.py
│  │     │  │  │  │  └─ test_timezones.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_na_scalar.py
│  │     │  │  │  └─ test_nat.py
│  │     │  │  ├─ series/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_arithmetic.cpython-312.pyc
│  │     │  │  │  │  ├─ test_constructors.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cumulative.cpython-312.pyc
│  │     │  │  │  │  ├─ test_formats.cpython-312.pyc
│  │     │  │  │  │  ├─ test_iteration.cpython-312.pyc
│  │     │  │  │  │  ├─ test_logical_ops.cpython-312.pyc
│  │     │  │  │  │  ├─ test_missing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_npfuncs.cpython-312.pyc
│  │     │  │  │  │  ├─ test_reductions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_subclass.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ufunc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_unary.cpython-312.pyc
│  │     │  │  │  │  └─ test_validate.cpython-312.pyc
│  │     │  │  │  ├─ accessors/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_cat_accessor.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dt_accessor.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_list_accessor.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sparse_accessor.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_str_accessor.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_struct_accessor.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_cat_accessor.py
│  │     │  │  │  │  ├─ test_dt_accessor.py
│  │     │  │  │  │  ├─ test_list_accessor.py
│  │     │  │  │  │  ├─ test_sparse_accessor.py
│  │     │  │  │  │  ├─ test_str_accessor.py
│  │     │  │  │  │  └─ test_struct_accessor.py
│  │     │  │  │  ├─ indexing/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_datetime.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_delitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_get.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_getitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_indexing.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_mask.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_set_value.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_setitem.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_take.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_where.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_xs.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_datetime.py
│  │     │  │  │  │  ├─ test_delitem.py
│  │     │  │  │  │  ├─ test_get.py
│  │     │  │  │  │  ├─ test_getitem.py
│  │     │  │  │  │  ├─ test_indexing.py
│  │     │  │  │  │  ├─ test_mask.py
│  │     │  │  │  │  ├─ test_set_value.py
│  │     │  │  │  │  ├─ test_setitem.py
│  │     │  │  │  │  ├─ test_take.py
│  │     │  │  │  │  ├─ test_where.py
│  │     │  │  │  │  └─ test_xs.py
│  │     │  │  │  ├─ methods/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_add_prefix_suffix.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_align.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_argsort.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_asof.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_astype.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_autocorr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_between.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_case_when.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_clip.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_combine_first.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_combine.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_compare.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_convert_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_copy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_count.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_cov_corr.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_describe.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_diff.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_drop_duplicates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_drop.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dropna.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dtypes.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_duplicated.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_equals.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_explode.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_fillna.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_get_numeric_data.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_head_tail.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_infer_objects.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_info.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_interpolate.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_is_monotonic.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_is_unique.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_isin.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_isna.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_item.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_map.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_matmul.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_nlargest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_nunique.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pct_change.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_pop.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_quantile.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_rank.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reindex_like.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reindex.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_rename_axis.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_rename.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_repeat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_replace.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_reset_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_round.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_searchsorted.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_set_name.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_size.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sort_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_sort_values.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_csv.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_dict.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_frame.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_to_numpy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_tolist.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_truncate.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_tz_localize.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_unique.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_unstack.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_update.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_value_counts.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_values.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_view.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_add_prefix_suffix.py
│  │     │  │  │  │  ├─ test_align.py
│  │     │  │  │  │  ├─ test_argsort.py
│  │     │  │  │  │  ├─ test_asof.py
│  │     │  │  │  │  ├─ test_astype.py
│  │     │  │  │  │  ├─ test_autocorr.py
│  │     │  │  │  │  ├─ test_between.py
│  │     │  │  │  │  ├─ test_case_when.py
│  │     │  │  │  │  ├─ test_clip.py
│  │     │  │  │  │  ├─ test_combine_first.py
│  │     │  │  │  │  ├─ test_combine.py
│  │     │  │  │  │  ├─ test_compare.py
│  │     │  │  │  │  ├─ test_convert_dtypes.py
│  │     │  │  │  │  ├─ test_copy.py
│  │     │  │  │  │  ├─ test_count.py
│  │     │  │  │  │  ├─ test_cov_corr.py
│  │     │  │  │  │  ├─ test_describe.py
│  │     │  │  │  │  ├─ test_diff.py
│  │     │  │  │  │  ├─ test_drop_duplicates.py
│  │     │  │  │  │  ├─ test_drop.py
│  │     │  │  │  │  ├─ test_dropna.py
│  │     │  │  │  │  ├─ test_dtypes.py
│  │     │  │  │  │  ├─ test_duplicated.py
│  │     │  │  │  │  ├─ test_equals.py
│  │     │  │  │  │  ├─ test_explode.py
│  │     │  │  │  │  ├─ test_fillna.py
│  │     │  │  │  │  ├─ test_get_numeric_data.py
│  │     │  │  │  │  ├─ test_head_tail.py
│  │     │  │  │  │  ├─ test_infer_objects.py
│  │     │  │  │  │  ├─ test_info.py
│  │     │  │  │  │  ├─ test_interpolate.py
│  │     │  │  │  │  ├─ test_is_monotonic.py
│  │     │  │  │  │  ├─ test_is_unique.py
│  │     │  │  │  │  ├─ test_isin.py
│  │     │  │  │  │  ├─ test_isna.py
│  │     │  │  │  │  ├─ test_item.py
│  │     │  │  │  │  ├─ test_map.py
│  │     │  │  │  │  ├─ test_matmul.py
│  │     │  │  │  │  ├─ test_nlargest.py
│  │     │  │  │  │  ├─ test_nunique.py
│  │     │  │  │  │  ├─ test_pct_change.py
│  │     │  │  │  │  ├─ test_pop.py
│  │     │  │  │  │  ├─ test_quantile.py
│  │     │  │  │  │  ├─ test_rank.py
│  │     │  │  │  │  ├─ test_reindex_like.py
│  │     │  │  │  │  ├─ test_reindex.py
│  │     │  │  │  │  ├─ test_rename_axis.py
│  │     │  │  │  │  ├─ test_rename.py
│  │     │  │  │  │  ├─ test_repeat.py
│  │     │  │  │  │  ├─ test_replace.py
│  │     │  │  │  │  ├─ test_reset_index.py
│  │     │  │  │  │  ├─ test_round.py
│  │     │  │  │  │  ├─ test_searchsorted.py
│  │     │  │  │  │  ├─ test_set_name.py
│  │     │  │  │  │  ├─ test_size.py
│  │     │  │  │  │  ├─ test_sort_index.py
│  │     │  │  │  │  ├─ test_sort_values.py
│  │     │  │  │  │  ├─ test_to_csv.py
│  │     │  │  │  │  ├─ test_to_dict.py
│  │     │  │  │  │  ├─ test_to_frame.py
│  │     │  │  │  │  ├─ test_to_numpy.py
│  │     │  │  │  │  ├─ test_tolist.py
│  │     │  │  │  │  ├─ test_truncate.py
│  │     │  │  │  │  ├─ test_tz_localize.py
│  │     │  │  │  │  ├─ test_unique.py
│  │     │  │  │  │  ├─ test_unstack.py
│  │     │  │  │  │  ├─ test_update.py
│  │     │  │  │  │  ├─ test_value_counts.py
│  │     │  │  │  │  ├─ test_values.py
│  │     │  │  │  │  └─ test_view.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_arithmetic.py
│  │     │  │  │  ├─ test_constructors.py
│  │     │  │  │  ├─ test_cumulative.py
│  │     │  │  │  ├─ test_formats.py
│  │     │  │  │  ├─ test_iteration.py
│  │     │  │  │  ├─ test_logical_ops.py
│  │     │  │  │  ├─ test_missing.py
│  │     │  │  │  ├─ test_npfuncs.py
│  │     │  │  │  ├─ test_reductions.py
│  │     │  │  │  ├─ test_subclass.py
│  │     │  │  │  ├─ test_ufunc.py
│  │     │  │  │  ├─ test_unary.py
│  │     │  │  │  └─ test_validate.py
│  │     │  │  ├─ strings/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_case_justify.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cat.cpython-312.pyc
│  │     │  │  │  │  ├─ test_extract.cpython-312.pyc
│  │     │  │  │  │  ├─ test_find_replace.cpython-312.pyc
│  │     │  │  │  │  ├─ test_get_dummies.cpython-312.pyc
│  │     │  │  │  │  ├─ test_split_partition.cpython-312.pyc
│  │     │  │  │  │  ├─ test_string_array.cpython-312.pyc
│  │     │  │  │  │  └─ test_strings.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_case_justify.py
│  │     │  │  │  ├─ test_cat.py
│  │     │  │  │  ├─ test_extract.py
│  │     │  │  │  ├─ test_find_replace.py
│  │     │  │  │  ├─ test_get_dummies.py
│  │     │  │  │  ├─ test_split_partition.py
│  │     │  │  │  ├─ test_string_array.py
│  │     │  │  │  └─ test_strings.py
│  │     │  │  ├─ tools/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_to_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_to_numeric.cpython-312.pyc
│  │     │  │  │  │  ├─ test_to_time.cpython-312.pyc
│  │     │  │  │  │  └─ test_to_timedelta.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_to_datetime.py
│  │     │  │  │  ├─ test_to_numeric.py
│  │     │  │  │  ├─ test_to_time.py
│  │     │  │  │  └─ test_to_timedelta.py
│  │     │  │  ├─ tseries/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ frequencies/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_freq_code.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_frequencies.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_inference.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_freq_code.py
│  │     │  │  │  │  ├─ test_frequencies.py
│  │     │  │  │  │  └─ test_inference.py
│  │     │  │  │  ├─ holiday/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_calendar.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_federal.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_holiday.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_observance.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ test_calendar.py
│  │     │  │  │  │  ├─ test_federal.py
│  │     │  │  │  │  ├─ test_holiday.py
│  │     │  │  │  │  └─ test_observance.py
│  │     │  │  │  ├─ offsets/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ common.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_business_day.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_business_hour.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_business_month.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_business_quarter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_business_year.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_common.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_custom_business_day.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_custom_business_hour.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_custom_business_month.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_dst.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_easter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_fiscal.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_index.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_month.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_offsets_properties.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_offsets.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_quarter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_ticks.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_week.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_year.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ common.py
│  │     │  │  │  │  ├─ test_business_day.py
│  │     │  │  │  │  ├─ test_business_hour.py
│  │     │  │  │  │  ├─ test_business_month.py
│  │     │  │  │  │  ├─ test_business_quarter.py
│  │     │  │  │  │  ├─ test_business_year.py
│  │     │  │  │  │  ├─ test_common.py
│  │     │  │  │  │  ├─ test_custom_business_day.py
│  │     │  │  │  │  ├─ test_custom_business_hour.py
│  │     │  │  │  │  ├─ test_custom_business_month.py
│  │     │  │  │  │  ├─ test_dst.py
│  │     │  │  │  │  ├─ test_easter.py
│  │     │  │  │  │  ├─ test_fiscal.py
│  │     │  │  │  │  ├─ test_index.py
│  │     │  │  │  │  ├─ test_month.py
│  │     │  │  │  │  ├─ test_offsets_properties.py
│  │     │  │  │  │  ├─ test_offsets.py
│  │     │  │  │  │  ├─ test_quarter.py
│  │     │  │  │  │  ├─ test_ticks.py
│  │     │  │  │  │  ├─ test_week.py
│  │     │  │  │  │  └─ test_year.py
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ tslibs/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_array_to_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ccalendar.cpython-312.pyc
│  │     │  │  │  │  ├─ test_conversion.cpython-312.pyc
│  │     │  │  │  │  ├─ test_fields.cpython-312.pyc
│  │     │  │  │  │  ├─ test_libfrequencies.cpython-312.pyc
│  │     │  │  │  │  ├─ test_liboffsets.cpython-312.pyc
│  │     │  │  │  │  ├─ test_np_datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_npy_units.cpython-312.pyc
│  │     │  │  │  │  ├─ test_parse_iso8601.cpython-312.pyc
│  │     │  │  │  │  ├─ test_parsing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_period.cpython-312.pyc
│  │     │  │  │  │  ├─ test_resolution.cpython-312.pyc
│  │     │  │  │  │  ├─ test_strptime.cpython-312.pyc
│  │     │  │  │  │  ├─ test_timedeltas.cpython-312.pyc
│  │     │  │  │  │  ├─ test_timezones.cpython-312.pyc
│  │     │  │  │  │  ├─ test_to_offset.cpython-312.pyc
│  │     │  │  │  │  └─ test_tzconversion.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_array_to_datetime.py
│  │     │  │  │  ├─ test_ccalendar.py
│  │     │  │  │  ├─ test_conversion.py
│  │     │  │  │  ├─ test_fields.py
│  │     │  │  │  ├─ test_libfrequencies.py
│  │     │  │  │  ├─ test_liboffsets.py
│  │     │  │  │  ├─ test_np_datetime.py
│  │     │  │  │  ├─ test_npy_units.py
│  │     │  │  │  ├─ test_parse_iso8601.py
│  │     │  │  │  ├─ test_parsing.py
│  │     │  │  │  ├─ test_period.py
│  │     │  │  │  ├─ test_resolution.py
│  │     │  │  │  ├─ test_strptime.py
│  │     │  │  │  ├─ test_timedeltas.py
│  │     │  │  │  ├─ test_timezones.py
│  │     │  │  │  ├─ test_to_offset.py
│  │     │  │  │  └─ test_tzconversion.py
│  │     │  │  ├─ util/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_almost_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_attr_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_categorical_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_extension_array_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_frame_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_index_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_interval_array_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_numpy_array_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_produces_warning.cpython-312.pyc
│  │     │  │  │  │  ├─ test_assert_series_equal.cpython-312.pyc
│  │     │  │  │  │  ├─ test_deprecate_kwarg.cpython-312.pyc
│  │     │  │  │  │  ├─ test_deprecate_nonkeyword_arguments.cpython-312.pyc
│  │     │  │  │  │  ├─ test_deprecate.cpython-312.pyc
│  │     │  │  │  │  ├─ test_doc.cpython-312.pyc
│  │     │  │  │  │  ├─ test_hashing.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numba.cpython-312.pyc
│  │     │  │  │  │  ├─ test_rewrite_warning.cpython-312.pyc
│  │     │  │  │  │  ├─ test_shares_memory.cpython-312.pyc
│  │     │  │  │  │  ├─ test_show_versions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_util.cpython-312.pyc
│  │     │  │  │  │  ├─ test_validate_args_and_kwargs.cpython-312.pyc
│  │     │  │  │  │  ├─ test_validate_args.cpython-312.pyc
│  │     │  │  │  │  ├─ test_validate_inclusive.cpython-312.pyc
│  │     │  │  │  │  └─ test_validate_kwargs.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_assert_almost_equal.py
│  │     │  │  │  ├─ test_assert_attr_equal.py
│  │     │  │  │  ├─ test_assert_categorical_equal.py
│  │     │  │  │  ├─ test_assert_extension_array_equal.py
│  │     │  │  │  ├─ test_assert_frame_equal.py
│  │     │  │  │  ├─ test_assert_index_equal.py
│  │     │  │  │  ├─ test_assert_interval_array_equal.py
│  │     │  │  │  ├─ test_assert_numpy_array_equal.py
│  │     │  │  │  ├─ test_assert_produces_warning.py
│  │     │  │  │  ├─ test_assert_series_equal.py
│  │     │  │  │  ├─ test_deprecate_kwarg.py
│  │     │  │  │  ├─ test_deprecate_nonkeyword_arguments.py
│  │     │  │  │  ├─ test_deprecate.py
│  │     │  │  │  ├─ test_doc.py
│  │     │  │  │  ├─ test_hashing.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_rewrite_warning.py
│  │     │  │  │  ├─ test_shares_memory.py
│  │     │  │  │  ├─ test_show_versions.py
│  │     │  │  │  ├─ test_util.py
│  │     │  │  │  ├─ test_validate_args_and_kwargs.py
│  │     │  │  │  ├─ test_validate_args.py
│  │     │  │  │  ├─ test_validate_inclusive.py
│  │     │  │  │  └─ test_validate_kwargs.py
│  │     │  │  ├─ window/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  ├─ test_api.cpython-312.pyc
│  │     │  │  │  │  ├─ test_apply.cpython-312.pyc
│  │     │  │  │  │  ├─ test_base_indexer.cpython-312.pyc
│  │     │  │  │  │  ├─ test_cython_aggregations.cpython-312.pyc
│  │     │  │  │  │  ├─ test_dtypes.cpython-312.pyc
│  │     │  │  │  │  ├─ test_ewm.cpython-312.pyc
│  │     │  │  │  │  ├─ test_expanding.cpython-312.pyc
│  │     │  │  │  │  ├─ test_groupby.cpython-312.pyc
│  │     │  │  │  │  ├─ test_numba.cpython-312.pyc
│  │     │  │  │  │  ├─ test_online.cpython-312.pyc
│  │     │  │  │  │  ├─ test_pairwise.cpython-312.pyc
│  │     │  │  │  │  ├─ test_rolling_functions.cpython-312.pyc
│  │     │  │  │  │  ├─ test_rolling_quantile.cpython-312.pyc
│  │     │  │  │  │  ├─ test_rolling_skew_kurt.cpython-312.pyc
│  │     │  │  │  │  ├─ test_rolling.cpython-312.pyc
│  │     │  │  │  │  ├─ test_timeseries_window.cpython-312.pyc
│  │     │  │  │  │  └─ test_win_type.cpython-312.pyc
│  │     │  │  │  ├─ moments/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_moments_consistency_ewm.cpython-312.pyc
│  │     │  │  │  │  │  ├─ test_moments_consistency_expanding.cpython-312.pyc
│  │     │  │  │  │  │  └─ test_moments_consistency_rolling.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ conftest.py
│  │     │  │  │  │  ├─ test_moments_consistency_ewm.py
│  │     │  │  │  │  ├─ test_moments_consistency_expanding.py
│  │     │  │  │  │  └─ test_moments_consistency_rolling.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ conftest.py
│  │     │  │  │  ├─ test_api.py
│  │     │  │  │  ├─ test_apply.py
│  │     │  │  │  ├─ test_base_indexer.py
│  │     │  │  │  ├─ test_cython_aggregations.py
│  │     │  │  │  ├─ test_dtypes.py
│  │     │  │  │  ├─ test_ewm.py
│  │     │  │  │  ├─ test_expanding.py
│  │     │  │  │  ├─ test_groupby.py
│  │     │  │  │  ├─ test_numba.py
│  │     │  │  │  ├─ test_online.py
│  │     │  │  │  ├─ test_pairwise.py
│  │     │  │  │  ├─ test_rolling_functions.py
│  │     │  │  │  ├─ test_rolling_quantile.py
│  │     │  │  │  ├─ test_rolling_skew_kurt.py
│  │     │  │  │  ├─ test_rolling.py
│  │     │  │  │  ├─ test_timeseries_window.py
│  │     │  │  │  └─ test_win_type.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ test_aggregation.py
│  │     │  │  ├─ test_algos.py
│  │     │  │  ├─ test_common.py
│  │     │  │  ├─ test_downstream.py
│  │     │  │  ├─ test_errors.py
│  │     │  │  ├─ test_expressions.py
│  │     │  │  ├─ test_flags.py
│  │     │  │  ├─ test_multilevel.py
│  │     │  │  ├─ test_nanops.py
│  │     │  │  ├─ test_optional_dependency.py
│  │     │  │  ├─ test_register_accessor.py
│  │     │  │  ├─ test_sorting.py
│  │     │  │  └─ test_take.py
│  │     │  ├─ tseries/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  ├─ frequencies.cpython-312.pyc
│  │     │  │  │  ├─ holiday.cpython-312.pyc
│  │     │  │  │  └─ offsets.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ api.py
│  │     │  │  ├─ frequencies.py
│  │     │  │  ├─ holiday.py
│  │     │  │  └─ offsets.py
│  │     │  ├─ util/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _decorators.cpython-312.pyc
│  │     │  │  │  ├─ _doctools.cpython-312.pyc
│  │     │  │  │  ├─ _exceptions.cpython-312.pyc
│  │     │  │  │  ├─ _print_versions.cpython-312.pyc
│  │     │  │  │  ├─ _test_decorators.cpython-312.pyc
│  │     │  │  │  ├─ _tester.cpython-312.pyc
│  │     │  │  │  └─ _validators.cpython-312.pyc
│  │     │  │  ├─ version/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _decorators.py
│  │     │  │  ├─ _doctools.py
│  │     │  │  ├─ _exceptions.py
│  │     │  │  ├─ _print_versions.py
│  │     │  │  ├─ _test_decorators.py
│  │     │  │  ├─ _tester.py
│  │     │  │  └─ _validators.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _version_meson.py
│  │     │  ├─ _version.py
│  │     │  ├─ conftest.py
│  │     │  ├─ pyproject.toml
│  │     │  └─ testing.py
│  │     ├─ pandas-2.3.1.dist-info/
│  │     │  ├─ DELVEWHEEL
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  └─ WHEEL
│  │     ├─ pandas.libs/
│  │     │  └─ msvcp140-1a0962f2a91a74c6d7136a768987a591.dll
│  │     ├─ parso/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _compatibility.cpython-312.pyc
│  │     │  │  ├─ cache.cpython-312.pyc
│  │     │  │  ├─ file_io.cpython-312.pyc
│  │     │  │  ├─ grammar.cpython-312.pyc
│  │     │  │  ├─ normalizer.cpython-312.pyc
│  │     │  │  ├─ parser.cpython-312.pyc
│  │     │  │  ├─ tree.cpython-312.pyc
│  │     │  │  └─ utils.cpython-312.pyc
│  │     │  ├─ pgen2/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ generator.cpython-312.pyc
│  │     │  │  │  └─ grammar_parser.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ generator.py
│  │     │  │  └─ grammar_parser.py
│  │     │  ├─ python/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ diff.cpython-312.pyc
│  │     │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  ├─ parser.cpython-312.pyc
│  │     │  │  │  ├─ pep8.cpython-312.pyc
│  │     │  │  │  ├─ prefix.cpython-312.pyc
│  │     │  │  │  ├─ token.cpython-312.pyc
│  │     │  │  │  ├─ tokenize.cpython-312.pyc
│  │     │  │  │  └─ tree.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ diff.py
│  │     │  │  ├─ errors.py
│  │     │  │  ├─ grammar310.txt
│  │     │  │  ├─ grammar311.txt
│  │     │  │  ├─ grammar312.txt
│  │     │  │  ├─ grammar313.txt
│  │     │  │  ├─ grammar36.txt
│  │     │  │  ├─ grammar37.txt
│  │     │  │  ├─ grammar38.txt
│  │     │  │  ├─ grammar39.txt
│  │     │  │  ├─ parser.py
│  │     │  │  ├─ pep8.py
│  │     │  │  ├─ prefix.py
│  │     │  │  ├─ token.py
│  │     │  │  ├─ tokenize.py
│  │     │  │  └─ tree.py
│  │     │  ├─ __init__.py
│  │     │  ├─ _compatibility.py
│  │     │  ├─ cache.py
│  │     │  ├─ file_io.py
│  │     │  ├─ grammar.py
│  │     │  ├─ normalizer.py
│  │     │  ├─ parser.py
│  │     │  ├─ py.typed
│  │     │  ├─ tree.py
│  │     │  └─ utils.py
│  │     ├─ parso-0.8.4.dist-info/
│  │     │  ├─ AUTHORS.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ LICENSE.txt
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ past/
│  │     │  ├─ __pycache__/
│  │     │  │  └─ __init__.cpython-312.pyc
│  │     │  ├─ builtins/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ misc.cpython-312.pyc
│  │     │  │  │  └─ noniterators.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ misc.py
│  │     │  │  └─ noniterators.py
│  │     │  ├─ translation/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ types/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ basestring.cpython-312.pyc
│  │     │  │  │  ├─ olddict.cpython-312.pyc
│  │     │  │  │  └─ oldstr.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ basestring.py
│  │     │  │  ├─ olddict.py
│  │     │  │  └─ oldstr.py
│  │     │  ├─ utils/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  └─ __init__.py
│  │     ├─ PIL/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ _binary.cpython-312.pyc
│  │     │  │  ├─ _deprecate.cpython-312.pyc
│  │     │  │  ├─ _tkinter_finder.cpython-312.pyc
│  │     │  │  ├─ _typing.cpython-312.pyc
│  │     │  │  ├─ _util.cpython-312.pyc
│  │     │  │  ├─ _version.cpython-312.pyc
│  │     │  │  ├─ AvifImagePlugin.cpython-312.pyc
│  │     │  │  ├─ BdfFontFile.cpython-312.pyc
│  │     │  │  ├─ BlpImagePlugin.cpython-312.pyc
│  │     │  │  ├─ BmpImagePlugin.cpython-312.pyc
│  │     │  │  ├─ BufrStubImagePlugin.cpython-312.pyc
│  │     │  │  ├─ ContainerIO.cpython-312.pyc
│  │     │  │  ├─ CurImagePlugin.cpython-312.pyc
│  │     │  │  ├─ DcxImagePlugin.cpython-312.pyc
│  │     │  │  ├─ DdsImagePlugin.cpython-312.pyc
│  │     │  │  ├─ EpsImagePlugin.cpython-312.pyc
│  │     │  │  ├─ ExifTags.cpython-312.pyc
│  │     │  │  ├─ features.cpython-312.pyc
│  │     │  │  ├─ FitsImagePlugin.cpython-312.pyc
│  │     │  │  ├─ FliImagePlugin.cpython-312.pyc
│  │     │  │  ├─ FontFile.cpython-312.pyc
│  │     │  │  ├─ FpxImagePlugin.cpython-312.pyc
│  │     │  │  ├─ FtexImagePlugin.cpython-312.pyc
│  │     │  │  ├─ GbrImagePlugin.cpython-312.pyc
│  │     │  │  ├─ GdImageFile.cpython-312.pyc
│  │     │  │  ├─ GifImagePlugin.cpython-312.pyc
│  │     │  │  ├─ GimpGradientFile.cpython-312.pyc
│  │     │  │  ├─ GimpPaletteFile.cpython-312.pyc
│  │     │  │  ├─ GribStubImagePlugin.cpython-312.pyc
│  │     │  │  ├─ Hdf5StubImagePlugin.cpython-312.pyc
│  │     │  │  ├─ IcnsImagePlugin.cpython-312.pyc
│  │     │  │  ├─ IcoImagePlugin.cpython-312.pyc
│  │     │  │  ├─ Image.cpython-312.pyc
│  │     │  │  ├─ ImageChops.cpython-312.pyc
│  │     │  │  ├─ ImageCms.cpython-312.pyc
│  │     │  │  ├─ ImageColor.cpython-312.pyc
│  │     │  │  ├─ ImageDraw.cpython-312.pyc
│  │     │  │  ├─ ImageDraw2.cpython-312.pyc
│  │     │  │  ├─ ImageEnhance.cpython-312.pyc
│  │     │  │  ├─ ImageFile.cpython-312.pyc
│  │     │  │  ├─ ImageFilter.cpython-312.pyc
│  │     │  │  ├─ ImageFont.cpython-312.pyc
│  │     │  │  ├─ ImageGrab.cpython-312.pyc
│  │     │  │  ├─ ImageMath.cpython-312.pyc
│  │     │  │  ├─ ImageMode.cpython-312.pyc
│  │     │  │  ├─ ImageMorph.cpython-312.pyc
│  │     │  │  ├─ ImageOps.cpython-312.pyc
│  │     │  │  ├─ ImagePalette.cpython-312.pyc
│  │     │  │  ├─ ImagePath.cpython-312.pyc
│  │     │  │  ├─ ImageQt.cpython-312.pyc
│  │     │  │  ├─ ImageSequence.cpython-312.pyc
│  │     │  │  ├─ ImageShow.cpython-312.pyc
│  │     │  │  ├─ ImageStat.cpython-312.pyc
│  │     │  │  ├─ ImageTk.cpython-312.pyc
│  │     │  │  ├─ ImageTransform.cpython-312.pyc
│  │     │  │  ├─ ImageWin.cpython-312.pyc
│  │     │  │  ├─ ImImagePlugin.cpython-312.pyc
│  │     │  │  ├─ ImtImagePlugin.cpython-312.pyc
│  │     │  │  ├─ IptcImagePlugin.cpython-312.pyc
│  │     │  │  ├─ Jpeg2KImagePlugin.cpython-312.pyc
│  │     │  │  ├─ JpegImagePlugin.cpython-312.pyc
│  │     │  │  ├─ JpegPresets.cpython-312.pyc
│  │     │  │  ├─ McIdasImagePlugin.cpython-312.pyc
│  │     │  │  ├─ MicImagePlugin.cpython-312.pyc
│  │     │  │  ├─ MpegImagePlugin.cpython-312.pyc
│  │     │  │  ├─ MpoImagePlugin.cpython-312.pyc
│  │     │  │  ├─ MspImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PaletteFile.cpython-312.pyc
│  │     │  │  ├─ PalmImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PcdImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PcfFontFile.cpython-312.pyc
│  │     │  │  ├─ PcxImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PdfImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PdfParser.cpython-312.pyc
│  │     │  │  ├─ PixarImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PngImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PpmImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PsdImagePlugin.cpython-312.pyc
│  │     │  │  ├─ PSDraw.cpython-312.pyc
│  │     │  │  ├─ QoiImagePlugin.cpython-312.pyc
│  │     │  │  ├─ report.cpython-312.pyc
│  │     │  │  ├─ SgiImagePlugin.cpython-312.pyc
│  │     │  │  ├─ SpiderImagePlugin.cpython-312.pyc
│  │     │  │  ├─ SunImagePlugin.cpython-312.pyc
│  │     │  │  ├─ TarIO.cpython-312.pyc
│  │     │  │  ├─ TgaImagePlugin.cpython-312.pyc
│  │     │  │  ├─ TiffImagePlugin.cpython-312.pyc
│  │     │  │  ├─ TiffTags.cpython-312.pyc
│  │     │  │  ├─ WalImageFile.cpython-312.pyc
│  │     │  │  ├─ WebPImagePlugin.cpython-312.pyc
│  │     │  │  ├─ WmfImagePlugin.cpython-312.pyc
│  │     │  │  ├─ XbmImagePlugin.cpython-312.pyc
│  │     │  │  ├─ XpmImagePlugin.cpython-312.pyc
│  │     │  │  └─ XVThumbImagePlugin.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ _avif.cp312-win_amd64.pyd
│  │     │  ├─ _avif.pyi
│  │     │  ├─ _binary.py
│  │     │  ├─ _deprecate.py
│  │     │  ├─ _imaging.cp312-win_amd64.pyd
│  │     │  ├─ _imaging.pyi
│  │     │  ├─ _imagingcms.cp312-win_amd64.pyd
│  │     │  ├─ _imagingcms.pyi
│  │     │  ├─ _imagingft.cp312-win_amd64.pyd
│  │     │  ├─ _imagingft.pyi
│  │     │  ├─ _imagingmath.cp312-win_amd64.pyd
│  │     │  ├─ _imagingmath.pyi
│  │     │  ├─ _imagingmorph.cp312-win_amd64.pyd
│  │     │  ├─ _imagingmorph.pyi
│  │     │  ├─ _imagingtk.cp312-win_amd64.pyd
│  │     │  ├─ _imagingtk.pyi
│  │     │  ├─ _tkinter_finder.py
│  │     │  ├─ _typing.py
│  │     │  ├─ _util.py
│  │     │  ├─ _version.py
│  │     │  ├─ _webp.cp312-win_amd64.pyd
│  │     │  ├─ _webp.pyi
│  │     │  ├─ AvifImagePlugin.py
│  │     │  ├─ BdfFontFile.py
│  │     │  ├─ BlpImagePlugin.py
│  │     │  ├─ BmpImagePlugin.py
│  │     │  ├─ BufrStubImagePlugin.py
│  │     │  ├─ ContainerIO.py
│  │     │  ├─ CurImagePlugin.py
│  │     │  ├─ DcxImagePlugin.py
│  │     │  ├─ DdsImagePlugin.py
│  │     │  ├─ EpsImagePlugin.py
│  │     │  ├─ ExifTags.py
│  │     │  ├─ features.py
│  │     │  ├─ FitsImagePlugin.py
│  │     │  ├─ FliImagePlugin.py
│  │     │  ├─ FontFile.py
│  │     │  ├─ FpxImagePlugin.py
│  │     │  ├─ FtexImagePlugin.py
│  │     │  ├─ GbrImagePlugin.py
│  │     │  ├─ GdImageFile.py
│  │     │  ├─ GifImagePlugin.py
│  │     │  ├─ GimpGradientFile.py
│  │     │  ├─ GimpPaletteFile.py
│  │     │  ├─ GribStubImagePlugin.py
│  │     │  ├─ Hdf5StubImagePlugin.py
│  │     │  ├─ IcnsImagePlugin.py
│  │     │  ├─ IcoImagePlugin.py
│  │     │  ├─ Image.py
│  │     │  ├─ ImageChops.py
│  │     │  ├─ ImageCms.py
│  │     │  ├─ ImageColor.py
│  │     │  ├─ ImageDraw.py
│  │     │  ├─ ImageDraw2.py
│  │     │  ├─ ImageEnhance.py
│  │     │  ├─ ImageFile.py
│  │     │  ├─ ImageFilter.py
│  │     │  ├─ ImageFont.py
│  │     │  ├─ ImageGrab.py
│  │     │  ├─ ImageMath.py
│  │     │  ├─ ImageMode.py
│  │     │  ├─ ImageMorph.py
│  │     │  ├─ ImageOps.py
│  │     │  ├─ ImagePalette.py
│  │     │  ├─ ImagePath.py
│  │     │  ├─ ImageQt.py
│  │     │  ├─ ImageSequence.py
│  │     │  ├─ ImageShow.py
│  │     │  ├─ ImageStat.py
│  │     │  ├─ ImageTk.py
│  │     │  ├─ ImageTransform.py
│  │     │  ├─ ImageWin.py
│  │     │  ├─ ImImagePlugin.py
│  │     │  ├─ ImtImagePlugin.py
│  │     │  ├─ IptcImagePlugin.py
│  │     │  ├─ Jpeg2KImagePlugin.py
│  │     │  ├─ JpegImagePlugin.py
│  │     │  ├─ JpegPresets.py
│  │     │  ├─ McIdasImagePlugin.py
│  │     │  ├─ MicImagePlugin.py
│  │     │  ├─ MpegImagePlugin.py
│  │     │  ├─ MpoImagePlugin.py
│  │     │  ├─ MspImagePlugin.py
│  │     │  ├─ PaletteFile.py
│  │     │  ├─ PalmImagePlugin.py
│  │     │  ├─ PcdImagePlugin.py
│  │     │  ├─ PcfFontFile.py
│  │     │  ├─ PcxImagePlugin.py
│  │     │  ├─ PdfImagePlugin.py
│  │     │  ├─ PdfParser.py
│  │     │  ├─ PixarImagePlugin.py
│  │     │  ├─ PngImagePlugin.py
│  │     │  ├─ PpmImagePlugin.py
│  │     │  ├─ PsdImagePlugin.py
│  │     │  ├─ PSDraw.py
│  │     │  ├─ py.typed
│  │     │  ├─ QoiImagePlugin.py
│  │     │  ├─ report.py
│  │     │  ├─ SgiImagePlugin.py
│  │     │  ├─ SpiderImagePlugin.py
│  │     │  ├─ SunImagePlugin.py
│  │     │  ├─ TarIO.py
│  │     │  ├─ TgaImagePlugin.py
│  │     │  ├─ TiffImagePlugin.py
│  │     │  ├─ TiffTags.py
│  │     │  ├─ WalImageFile.py
│  │     │  ├─ WebPImagePlugin.py
│  │     │  ├─ WmfImagePlugin.py
│  │     │  ├─ XbmImagePlugin.py
│  │     │  ├─ XpmImagePlugin.py
│  │     │  └─ XVThumbImagePlugin.py
│  │     ├─ pillow-11.3.0.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ top_level.txt
│  │     │  ├─ WHEEL
│  │     │  └─ zip-safe
│  │     ├─ pip/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  └─ __pip-runner__.cpython-312.pyc
│  │     │  ├─ _internal/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ build_env.cpython-312.pyc
│  │     │  │  │  ├─ cache.cpython-312.pyc
│  │     │  │  │  ├─ configuration.cpython-312.pyc
│  │     │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  ├─ main.cpython-312.pyc
│  │     │  │  │  ├─ pyproject.cpython-312.pyc
│  │     │  │  │  ├─ self_outdated_check.cpython-312.pyc
│  │     │  │  │  └─ wheel_builder.cpython-312.pyc
│  │     │  │  ├─ cli/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ autocompletion.cpython-312.pyc
│  │     │  │  │  │  ├─ base_command.cpython-312.pyc
│  │     │  │  │  │  ├─ cmdoptions.cpython-312.pyc
│  │     │  │  │  │  ├─ command_context.cpython-312.pyc
│  │     │  │  │  │  ├─ index_command.cpython-312.pyc
│  │     │  │  │  │  ├─ main_parser.cpython-312.pyc
│  │     │  │  │  │  ├─ main.cpython-312.pyc
│  │     │  │  │  │  ├─ parser.cpython-312.pyc
│  │     │  │  │  │  ├─ progress_bars.cpython-312.pyc
│  │     │  │  │  │  ├─ req_command.cpython-312.pyc
│  │     │  │  │  │  ├─ spinners.cpython-312.pyc
│  │     │  │  │  │  └─ status_codes.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ autocompletion.py
│  │     │  │  │  ├─ base_command.py
│  │     │  │  │  ├─ cmdoptions.py
│  │     │  │  │  ├─ command_context.py
│  │     │  │  │  ├─ index_command.py
│  │     │  │  │  ├─ main_parser.py
│  │     │  │  │  ├─ main.py
│  │     │  │  │  ├─ parser.py
│  │     │  │  │  ├─ progress_bars.py
│  │     │  │  │  ├─ req_command.py
│  │     │  │  │  ├─ spinners.py
│  │     │  │  │  └─ status_codes.py
│  │     │  │  ├─ commands/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ cache.cpython-312.pyc
│  │     │  │  │  │  ├─ check.cpython-312.pyc
│  │     │  │  │  │  ├─ completion.cpython-312.pyc
│  │     │  │  │  │  ├─ configuration.cpython-312.pyc
│  │     │  │  │  │  ├─ debug.cpython-312.pyc
│  │     │  │  │  │  ├─ download.cpython-312.pyc
│  │     │  │  │  │  ├─ freeze.cpython-312.pyc
│  │     │  │  │  │  ├─ hash.cpython-312.pyc
│  │     │  │  │  │  ├─ help.cpython-312.pyc
│  │     │  │  │  │  ├─ index.cpython-312.pyc
│  │     │  │  │  │  ├─ inspect.cpython-312.pyc
│  │     │  │  │  │  ├─ install.cpython-312.pyc
│  │     │  │  │  │  ├─ list.cpython-312.pyc
│  │     │  │  │  │  ├─ lock.cpython-312.pyc
│  │     │  │  │  │  ├─ search.cpython-312.pyc
│  │     │  │  │  │  ├─ show.cpython-312.pyc
│  │     │  │  │  │  ├─ uninstall.cpython-312.pyc
│  │     │  │  │  │  └─ wheel.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ completion.py
│  │     │  │  │  ├─ configuration.py
│  │     │  │  │  ├─ debug.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  ├─ hash.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ inspect.py
│  │     │  │  │  ├─ install.py
│  │     │  │  │  ├─ list.py
│  │     │  │  │  ├─ lock.py
│  │     │  │  │  ├─ search.py
│  │     │  │  │  ├─ show.py
│  │     │  │  │  ├─ uninstall.py
│  │     │  │  │  └─ wheel.py
│  │     │  │  ├─ distributions/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  ├─ installed.cpython-312.pyc
│  │     │  │  │  │  ├─ sdist.cpython-312.pyc
│  │     │  │  │  │  └─ wheel.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  ├─ installed.py
│  │     │  │  │  ├─ sdist.py
│  │     │  │  │  └─ wheel.py
│  │     │  │  ├─ index/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ collector.cpython-312.pyc
│  │     │  │  │  │  ├─ package_finder.cpython-312.pyc
│  │     │  │  │  │  └─ sources.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ collector.py
│  │     │  │  │  ├─ package_finder.py
│  │     │  │  │  └─ sources.py
│  │     │  │  ├─ locations/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _distutils.cpython-312.pyc
│  │     │  │  │  │  ├─ _sysconfig.cpython-312.pyc
│  │     │  │  │  │  └─ base.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _distutils.py
│  │     │  │  │  ├─ _sysconfig.py
│  │     │  │  │  └─ base.py
│  │     │  │  ├─ metadata/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _json.cpython-312.pyc
│  │     │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  └─ pkg_resources.cpython-312.pyc
│  │     │  │  │  ├─ importlib/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _compat.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _dists.cpython-312.pyc
│  │     │  │  │  │  │  └─ _envs.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _compat.py
│  │     │  │  │  │  ├─ _dists.py
│  │     │  │  │  │  └─ _envs.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _json.py
│  │     │  │  │  ├─ base.py
│  │     │  │  │  └─ pkg_resources.py
│  │     │  │  ├─ models/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ candidate.cpython-312.pyc
│  │     │  │  │  │  ├─ direct_url.cpython-312.pyc
│  │     │  │  │  │  ├─ format_control.cpython-312.pyc
│  │     │  │  │  │  ├─ index.cpython-312.pyc
│  │     │  │  │  │  ├─ installation_report.cpython-312.pyc
│  │     │  │  │  │  ├─ link.cpython-312.pyc
│  │     │  │  │  │  ├─ pylock.cpython-312.pyc
│  │     │  │  │  │  ├─ scheme.cpython-312.pyc
│  │     │  │  │  │  ├─ search_scope.cpython-312.pyc
│  │     │  │  │  │  ├─ selection_prefs.cpython-312.pyc
│  │     │  │  │  │  ├─ target_python.cpython-312.pyc
│  │     │  │  │  │  └─ wheel.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ candidate.py
│  │     │  │  │  ├─ direct_url.py
│  │     │  │  │  ├─ format_control.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ installation_report.py
│  │     │  │  │  ├─ link.py
│  │     │  │  │  ├─ pylock.py
│  │     │  │  │  ├─ scheme.py
│  │     │  │  │  ├─ search_scope.py
│  │     │  │  │  ├─ selection_prefs.py
│  │     │  │  │  ├─ target_python.py
│  │     │  │  │  └─ wheel.py
│  │     │  │  ├─ network/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ auth.cpython-312.pyc
│  │     │  │  │  │  ├─ cache.cpython-312.pyc
│  │     │  │  │  │  ├─ download.cpython-312.pyc
│  │     │  │  │  │  ├─ lazy_wheel.cpython-312.pyc
│  │     │  │  │  │  ├─ session.cpython-312.pyc
│  │     │  │  │  │  ├─ utils.cpython-312.pyc
│  │     │  │  │  │  └─ xmlrpc.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ download.py
│  │     │  │  │  ├─ lazy_wheel.py
│  │     │  │  │  ├─ session.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ xmlrpc.py
│  │     │  │  ├─ operations/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ check.cpython-312.pyc
│  │     │  │  │  │  ├─ freeze.cpython-312.pyc
│  │     │  │  │  │  └─ prepare.cpython-312.pyc
│  │     │  │  │  ├─ build/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ build_tracker.cpython-312.pyc
│  │     │  │  │  │  │  ├─ metadata_editable.cpython-312.pyc
│  │     │  │  │  │  │  ├─ metadata_legacy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ metadata.cpython-312.pyc
│  │     │  │  │  │  │  ├─ wheel_editable.cpython-312.pyc
│  │     │  │  │  │  │  ├─ wheel_legacy.cpython-312.pyc
│  │     │  │  │  │  │  └─ wheel.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ build_tracker.py
│  │     │  │  │  │  ├─ metadata_editable.py
│  │     │  │  │  │  ├─ metadata_legacy.py
│  │     │  │  │  │  ├─ metadata.py
│  │     │  │  │  │  ├─ wheel_editable.py
│  │     │  │  │  │  ├─ wheel_legacy.py
│  │     │  │  │  │  └─ wheel.py
│  │     │  │  │  ├─ install/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ editable_legacy.cpython-312.pyc
│  │     │  │  │  │  │  └─ wheel.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ editable_legacy.py
│  │     │  │  │  │  └─ wheel.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ check.py
│  │     │  │  │  ├─ freeze.py
│  │     │  │  │  └─ prepare.py
│  │     │  │  ├─ req/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ constructors.cpython-312.pyc
│  │     │  │  │  │  ├─ req_dependency_group.cpython-312.pyc
│  │     │  │  │  │  ├─ req_file.cpython-312.pyc
│  │     │  │  │  │  ├─ req_install.cpython-312.pyc
│  │     │  │  │  │  ├─ req_set.cpython-312.pyc
│  │     │  │  │  │  └─ req_uninstall.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ constructors.py
│  │     │  │  │  ├─ req_dependency_group.py
│  │     │  │  │  ├─ req_file.py
│  │     │  │  │  ├─ req_install.py
│  │     │  │  │  ├─ req_set.py
│  │     │  │  │  └─ req_uninstall.py
│  │     │  │  ├─ resolution/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ base.cpython-312.pyc
│  │     │  │  │  ├─ legacy/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ resolver.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ resolver.py
│  │     │  │  │  ├─ resolvelib/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ base.cpython-312.pyc
│  │     │  │  │  │  │  ├─ candidates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ factory.cpython-312.pyc
│  │     │  │  │  │  │  ├─ found_candidates.cpython-312.pyc
│  │     │  │  │  │  │  ├─ provider.cpython-312.pyc
│  │     │  │  │  │  │  ├─ reporter.cpython-312.pyc
│  │     │  │  │  │  │  ├─ requirements.cpython-312.pyc
│  │     │  │  │  │  │  └─ resolver.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ base.py
│  │     │  │  │  │  ├─ candidates.py
│  │     │  │  │  │  ├─ factory.py
│  │     │  │  │  │  ├─ found_candidates.py
│  │     │  │  │  │  ├─ provider.py
│  │     │  │  │  │  ├─ reporter.py
│  │     │  │  │  │  ├─ requirements.py
│  │     │  │  │  │  └─ resolver.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  └─ base.py
│  │     │  │  ├─ utils/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _jaraco_text.cpython-312.pyc
│  │     │  │  │  │  ├─ _log.cpython-312.pyc
│  │     │  │  │  │  ├─ appdirs.cpython-312.pyc
│  │     │  │  │  │  ├─ compat.cpython-312.pyc
│  │     │  │  │  │  ├─ compatibility_tags.cpython-312.pyc
│  │     │  │  │  │  ├─ datetime.cpython-312.pyc
│  │     │  │  │  │  ├─ deprecation.cpython-312.pyc
│  │     │  │  │  │  ├─ direct_url_helpers.cpython-312.pyc
│  │     │  │  │  │  ├─ egg_link.cpython-312.pyc
│  │     │  │  │  │  ├─ entrypoints.cpython-312.pyc
│  │     │  │  │  │  ├─ filesystem.cpython-312.pyc
│  │     │  │  │  │  ├─ filetypes.cpython-312.pyc
│  │     │  │  │  │  ├─ glibc.cpython-312.pyc
│  │     │  │  │  │  ├─ hashes.cpython-312.pyc
│  │     │  │  │  │  ├─ logging.cpython-312.pyc
│  │     │  │  │  │  ├─ misc.cpython-312.pyc
│  │     │  │  │  │  ├─ packaging.cpython-312.pyc
│  │     │  │  │  │  ├─ retry.cpython-312.pyc
│  │     │  │  │  │  ├─ setuptools_build.cpython-312.pyc
│  │     │  │  │  │  ├─ subprocess.cpython-312.pyc
│  │     │  │  │  │  ├─ temp_dir.cpython-312.pyc
│  │     │  │  │  │  ├─ unpacking.cpython-312.pyc
│  │     │  │  │  │  ├─ urls.cpython-312.pyc
│  │     │  │  │  │  ├─ virtualenv.cpython-312.pyc
│  │     │  │  │  │  └─ wheel.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _jaraco_text.py
│  │     │  │  │  ├─ _log.py
│  │     │  │  │  ├─ appdirs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ compatibility_tags.py
│  │     │  │  │  ├─ datetime.py
│  │     │  │  │  ├─ deprecation.py
│  │     │  │  │  ├─ direct_url_helpers.py
│  │     │  │  │  ├─ egg_link.py
│  │     │  │  │  ├─ entrypoints.py
│  │     │  │  │  ├─ filesystem.py
│  │     │  │  │  ├─ filetypes.py
│  │     │  │  │  ├─ glibc.py
│  │     │  │  │  ├─ hashes.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ misc.py
│  │     │  │  │  ├─ packaging.py
│  │     │  │  │  ├─ retry.py
│  │     │  │  │  ├─ setuptools_build.py
│  │     │  │  │  ├─ subprocess.py
│  │     │  │  │  ├─ temp_dir.py
│  │     │  │  │  ├─ unpacking.py
│  │     │  │  │  ├─ urls.py
│  │     │  │  │  ├─ virtualenv.py
│  │     │  │  │  └─ wheel.py
│  │     │  │  ├─ vcs/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ bazaar.cpython-312.pyc
│  │     │  │  │  │  ├─ git.cpython-312.pyc
│  │     │  │  │  │  ├─ mercurial.cpython-312.pyc
│  │     │  │  │  │  ├─ subversion.cpython-312.pyc
│  │     │  │  │  │  └─ versioncontrol.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ bazaar.py
│  │     │  │  │  ├─ git.py
│  │     │  │  │  ├─ mercurial.py
│  │     │  │  │  ├─ subversion.py
│  │     │  │  │  └─ versioncontrol.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ build_env.py
│  │     │  │  ├─ cache.py
│  │     │  │  ├─ configuration.py
│  │     │  │  ├─ exceptions.py
│  │     │  │  ├─ main.py
│  │     │  │  ├─ pyproject.py
│  │     │  │  ├─ self_outdated_check.py
│  │     │  │  └─ wheel_builder.py
│  │     │  ├─ _vendor/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  └─ typing_extensions.cpython-312.pyc
│  │     │  │  ├─ cachecontrol/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _cmd.cpython-312.pyc
│  │     │  │  │  │  ├─ adapter.cpython-312.pyc
│  │     │  │  │  │  ├─ cache.cpython-312.pyc
│  │     │  │  │  │  ├─ controller.cpython-312.pyc
│  │     │  │  │  │  ├─ filewrapper.cpython-312.pyc
│  │     │  │  │  │  ├─ heuristics.cpython-312.pyc
│  │     │  │  │  │  ├─ serialize.cpython-312.pyc
│  │     │  │  │  │  └─ wrapper.cpython-312.pyc
│  │     │  │  │  ├─ caches/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ file_cache.cpython-312.pyc
│  │     │  │  │  │  │  └─ redis_cache.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ file_cache.py
│  │     │  │  │  │  └─ redis_cache.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _cmd.py
│  │     │  │  │  ├─ adapter.py
│  │     │  │  │  ├─ cache.py
│  │     │  │  │  ├─ controller.py
│  │     │  │  │  ├─ filewrapper.py
│  │     │  │  │  ├─ heuristics.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ serialize.py
│  │     │  │  │  └─ wrapper.py
│  │     │  │  ├─ certifi/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  └─ core.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  ├─ cacert.pem
│  │     │  │  │  ├─ core.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ dependency_groups/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  ├─ _implementation.cpython-312.pyc
│  │     │  │  │  │  ├─ _lint_dependency_groups.cpython-312.pyc
│  │     │  │  │  │  ├─ _pip_wrapper.cpython-312.pyc
│  │     │  │  │  │  └─ _toml_compat.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  ├─ _implementation.py
│  │     │  │  │  ├─ _lint_dependency_groups.py
│  │     │  │  │  ├─ _pip_wrapper.py
│  │     │  │  │  ├─ _toml_compat.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ distlib/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ compat.cpython-312.pyc
│  │     │  │  │  │  ├─ database.cpython-312.pyc
│  │     │  │  │  │  ├─ index.cpython-312.pyc
│  │     │  │  │  │  ├─ locators.cpython-312.pyc
│  │     │  │  │  │  ├─ manifest.cpython-312.pyc
│  │     │  │  │  │  ├─ markers.cpython-312.pyc
│  │     │  │  │  │  ├─ metadata.cpython-312.pyc
│  │     │  │  │  │  ├─ resources.cpython-312.pyc
│  │     │  │  │  │  ├─ scripts.cpython-312.pyc
│  │     │  │  │  │  ├─ util.cpython-312.pyc
│  │     │  │  │  │  ├─ version.cpython-312.pyc
│  │     │  │  │  │  └─ wheel.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ database.py
│  │     │  │  │  ├─ index.py
│  │     │  │  │  ├─ locators.py
│  │     │  │  │  ├─ manifest.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ resources.py
│  │     │  │  │  ├─ scripts.py
│  │     │  │  │  ├─ t32.exe
│  │     │  │  │  ├─ t64-arm.exe
│  │     │  │  │  ├─ t64.exe
│  │     │  │  │  ├─ util.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  ├─ w32.exe
│  │     │  │  │  ├─ w64-arm.exe
│  │     │  │  │  ├─ w64.exe
│  │     │  │  │  └─ wheel.py
│  │     │  │  ├─ distro/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  └─ distro.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  ├─ distro.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ idna/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ codec.cpython-312.pyc
│  │     │  │  │  │  ├─ compat.cpython-312.pyc
│  │     │  │  │  │  ├─ core.cpython-312.pyc
│  │     │  │  │  │  ├─ idnadata.cpython-312.pyc
│  │     │  │  │  │  ├─ intranges.cpython-312.pyc
│  │     │  │  │  │  ├─ package_data.cpython-312.pyc
│  │     │  │  │  │  └─ uts46data.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ codec.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ core.py
│  │     │  │  │  ├─ idnadata.py
│  │     │  │  │  ├─ intranges.py
│  │     │  │  │  ├─ package_data.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  └─ uts46data.py
│  │     │  │  ├─ msgpack/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ ext.cpython-312.pyc
│  │     │  │  │  │  └─ fallback.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ ext.py
│  │     │  │  │  └─ fallback.py
│  │     │  │  ├─ packaging/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _elffile.cpython-312.pyc
│  │     │  │  │  │  ├─ _manylinux.cpython-312.pyc
│  │     │  │  │  │  ├─ _musllinux.cpython-312.pyc
│  │     │  │  │  │  ├─ _parser.cpython-312.pyc
│  │     │  │  │  │  ├─ _structures.cpython-312.pyc
│  │     │  │  │  │  ├─ _tokenizer.cpython-312.pyc
│  │     │  │  │  │  ├─ markers.cpython-312.pyc
│  │     │  │  │  │  ├─ metadata.cpython-312.pyc
│  │     │  │  │  │  ├─ requirements.cpython-312.pyc
│  │     │  │  │  │  ├─ specifiers.cpython-312.pyc
│  │     │  │  │  │  ├─ tags.cpython-312.pyc
│  │     │  │  │  │  ├─ utils.cpython-312.pyc
│  │     │  │  │  │  └─ version.cpython-312.pyc
│  │     │  │  │  ├─ licenses/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _spdx.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _spdx.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _elffile.py
│  │     │  │  │  ├─ _manylinux.py
│  │     │  │  │  ├─ _musllinux.py
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _structures.py
│  │     │  │  │  ├─ _tokenizer.py
│  │     │  │  │  ├─ markers.py
│  │     │  │  │  ├─ metadata.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ requirements.py
│  │     │  │  │  ├─ specifiers.py
│  │     │  │  │  ├─ tags.py
│  │     │  │  │  ├─ utils.py
│  │     │  │  │  └─ version.py
│  │     │  │  ├─ pkg_resources/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ platformdirs/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  ├─ android.cpython-312.pyc
│  │     │  │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  │  ├─ macos.cpython-312.pyc
│  │     │  │  │  │  ├─ unix.cpython-312.pyc
│  │     │  │  │  │  ├─ version.cpython-312.pyc
│  │     │  │  │  │  └─ windows.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  ├─ android.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ macos.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ unix.py
│  │     │  │  │  ├─ version.py
│  │     │  │  │  └─ windows.py
│  │     │  │  ├─ pygments/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  ├─ console.cpython-312.pyc
│  │     │  │  │  │  ├─ filter.cpython-312.pyc
│  │     │  │  │  │  ├─ formatter.cpython-312.pyc
│  │     │  │  │  │  ├─ lexer.cpython-312.pyc
│  │     │  │  │  │  ├─ modeline.cpython-312.pyc
│  │     │  │  │  │  ├─ plugin.cpython-312.pyc
│  │     │  │  │  │  ├─ regexopt.cpython-312.pyc
│  │     │  │  │  │  ├─ scanner.cpython-312.pyc
│  │     │  │  │  │  ├─ sphinxext.cpython-312.pyc
│  │     │  │  │  │  ├─ style.cpython-312.pyc
│  │     │  │  │  │  ├─ token.cpython-312.pyc
│  │     │  │  │  │  ├─ unistring.cpython-312.pyc
│  │     │  │  │  │  └─ util.cpython-312.pyc
│  │     │  │  │  ├─ filters/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ __init__.py
│  │     │  │  │  ├─ formatters/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _mapping.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _mapping.py
│  │     │  │  │  ├─ lexers/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _mapping.cpython-312.pyc
│  │     │  │  │  │  │  └─ python.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _mapping.py
│  │     │  │  │  │  └─ python.py
│  │     │  │  │  ├─ styles/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _mapping.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _mapping.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ filter.py
│  │     │  │  │  ├─ formatter.py
│  │     │  │  │  ├─ lexer.py
│  │     │  │  │  ├─ modeline.py
│  │     │  │  │  ├─ plugin.py
│  │     │  │  │  ├─ regexopt.py
│  │     │  │  │  ├─ scanner.py
│  │     │  │  │  ├─ sphinxext.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ token.py
│  │     │  │  │  ├─ unistring.py
│  │     │  │  │  └─ util.py
│  │     │  │  ├─ pyproject_hooks/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ _impl.cpython-312.pyc
│  │     │  │  │  ├─ _in_process/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _in_process.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _in_process.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _impl.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ requests/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __version__.cpython-312.pyc
│  │     │  │  │  │  ├─ _internal_utils.cpython-312.pyc
│  │     │  │  │  │  ├─ adapters.cpython-312.pyc
│  │     │  │  │  │  ├─ api.cpython-312.pyc
│  │     │  │  │  │  ├─ auth.cpython-312.pyc
│  │     │  │  │  │  ├─ certs.cpython-312.pyc
│  │     │  │  │  │  ├─ compat.cpython-312.pyc
│  │     │  │  │  │  ├─ cookies.cpython-312.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ help.cpython-312.pyc
│  │     │  │  │  │  ├─ hooks.cpython-312.pyc
│  │     │  │  │  │  ├─ models.cpython-312.pyc
│  │     │  │  │  │  ├─ packages.cpython-312.pyc
│  │     │  │  │  │  ├─ sessions.cpython-312.pyc
│  │     │  │  │  │  ├─ status_codes.cpython-312.pyc
│  │     │  │  │  │  ├─ structures.cpython-312.pyc
│  │     │  │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __version__.py
│  │     │  │  │  ├─ _internal_utils.py
│  │     │  │  │  ├─ adapters.py
│  │     │  │  │  ├─ api.py
│  │     │  │  │  ├─ auth.py
│  │     │  │  │  ├─ certs.py
│  │     │  │  │  ├─ compat.py
│  │     │  │  │  ├─ cookies.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ help.py
│  │     │  │  │  ├─ hooks.py
│  │     │  │  │  ├─ models.py
│  │     │  │  │  ├─ packages.py
│  │     │  │  │  ├─ sessions.py
│  │     │  │  │  ├─ status_codes.py
│  │     │  │  │  ├─ structures.py
│  │     │  │  │  └─ utils.py
│  │     │  │  ├─ resolvelib/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ providers.cpython-312.pyc
│  │     │  │  │  │  ├─ reporters.cpython-312.pyc
│  │     │  │  │  │  └─ structs.cpython-312.pyc
│  │     │  │  │  ├─ resolvers/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ abstract.cpython-312.pyc
│  │     │  │  │  │  │  ├─ criterion.cpython-312.pyc
│  │     │  │  │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  │  │  └─ resolution.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ abstract.py
│  │     │  │  │  │  ├─ criterion.py
│  │     │  │  │  │  ├─ exceptions.py
│  │     │  │  │  │  └─ resolution.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ providers.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ reporters.py
│  │     │  │  │  └─ structs.py
│  │     │  │  ├─ rich/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  │  │  ├─ _cell_widths.cpython-312.pyc
│  │     │  │  │  │  ├─ _emoji_codes.cpython-312.pyc
│  │     │  │  │  │  ├─ _emoji_replace.cpython-312.pyc
│  │     │  │  │  │  ├─ _export_format.cpython-312.pyc
│  │     │  │  │  │  ├─ _extension.cpython-312.pyc
│  │     │  │  │  │  ├─ _fileno.cpython-312.pyc
│  │     │  │  │  │  ├─ _inspect.cpython-312.pyc
│  │     │  │  │  │  ├─ _log_render.cpython-312.pyc
│  │     │  │  │  │  ├─ _loop.cpython-312.pyc
│  │     │  │  │  │  ├─ _null_file.cpython-312.pyc
│  │     │  │  │  │  ├─ _palettes.cpython-312.pyc
│  │     │  │  │  │  ├─ _pick.cpython-312.pyc
│  │     │  │  │  │  ├─ _ratio.cpython-312.pyc
│  │     │  │  │  │  ├─ _spinners.cpython-312.pyc
│  │     │  │  │  │  ├─ _stack.cpython-312.pyc
│  │     │  │  │  │  ├─ _timer.cpython-312.pyc
│  │     │  │  │  │  ├─ _win32_console.cpython-312.pyc
│  │     │  │  │  │  ├─ _windows_renderer.cpython-312.pyc
│  │     │  │  │  │  ├─ _windows.cpython-312.pyc
│  │     │  │  │  │  ├─ _wrap.cpython-312.pyc
│  │     │  │  │  │  ├─ abc.cpython-312.pyc
│  │     │  │  │  │  ├─ align.cpython-312.pyc
│  │     │  │  │  │  ├─ ansi.cpython-312.pyc
│  │     │  │  │  │  ├─ bar.cpython-312.pyc
│  │     │  │  │  │  ├─ box.cpython-312.pyc
│  │     │  │  │  │  ├─ cells.cpython-312.pyc
│  │     │  │  │  │  ├─ color_triplet.cpython-312.pyc
│  │     │  │  │  │  ├─ color.cpython-312.pyc
│  │     │  │  │  │  ├─ columns.cpython-312.pyc
│  │     │  │  │  │  ├─ console.cpython-312.pyc
│  │     │  │  │  │  ├─ constrain.cpython-312.pyc
│  │     │  │  │  │  ├─ containers.cpython-312.pyc
│  │     │  │  │  │  ├─ control.cpython-312.pyc
│  │     │  │  │  │  ├─ default_styles.cpython-312.pyc
│  │     │  │  │  │  ├─ diagnose.cpython-312.pyc
│  │     │  │  │  │  ├─ emoji.cpython-312.pyc
│  │     │  │  │  │  ├─ errors.cpython-312.pyc
│  │     │  │  │  │  ├─ file_proxy.cpython-312.pyc
│  │     │  │  │  │  ├─ filesize.cpython-312.pyc
│  │     │  │  │  │  ├─ highlighter.cpython-312.pyc
│  │     │  │  │  │  ├─ json.cpython-312.pyc
│  │     │  │  │  │  ├─ jupyter.cpython-312.pyc
│  │     │  │  │  │  ├─ layout.cpython-312.pyc
│  │     │  │  │  │  ├─ live_render.cpython-312.pyc
│  │     │  │  │  │  ├─ live.cpython-312.pyc
│  │     │  │  │  │  ├─ logging.cpython-312.pyc
│  │     │  │  │  │  ├─ markup.cpython-312.pyc
│  │     │  │  │  │  ├─ measure.cpython-312.pyc
│  │     │  │  │  │  ├─ padding.cpython-312.pyc
│  │     │  │  │  │  ├─ pager.cpython-312.pyc
│  │     │  │  │  │  ├─ palette.cpython-312.pyc
│  │     │  │  │  │  ├─ panel.cpython-312.pyc
│  │     │  │  │  │  ├─ pretty.cpython-312.pyc
│  │     │  │  │  │  ├─ progress_bar.cpython-312.pyc
│  │     │  │  │  │  ├─ progress.cpython-312.pyc
│  │     │  │  │  │  ├─ prompt.cpython-312.pyc
│  │     │  │  │  │  ├─ protocol.cpython-312.pyc
│  │     │  │  │  │  ├─ region.cpython-312.pyc
│  │     │  │  │  │  ├─ repr.cpython-312.pyc
│  │     │  │  │  │  ├─ rule.cpython-312.pyc
│  │     │  │  │  │  ├─ scope.cpython-312.pyc
│  │     │  │  │  │  ├─ screen.cpython-312.pyc
│  │     │  │  │  │  ├─ segment.cpython-312.pyc
│  │     │  │  │  │  ├─ spinner.cpython-312.pyc
│  │     │  │  │  │  ├─ status.cpython-312.pyc
│  │     │  │  │  │  ├─ style.cpython-312.pyc
│  │     │  │  │  │  ├─ styled.cpython-312.pyc
│  │     │  │  │  │  ├─ syntax.cpython-312.pyc
│  │     │  │  │  │  ├─ table.cpython-312.pyc
│  │     │  │  │  │  ├─ terminal_theme.cpython-312.pyc
│  │     │  │  │  │  ├─ text.cpython-312.pyc
│  │     │  │  │  │  ├─ theme.cpython-312.pyc
│  │     │  │  │  │  ├─ themes.cpython-312.pyc
│  │     │  │  │  │  ├─ traceback.cpython-312.pyc
│  │     │  │  │  │  └─ tree.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ __main__.py
│  │     │  │  │  ├─ _cell_widths.py
│  │     │  │  │  ├─ _emoji_codes.py
│  │     │  │  │  ├─ _emoji_replace.py
│  │     │  │  │  ├─ _export_format.py
│  │     │  │  │  ├─ _extension.py
│  │     │  │  │  ├─ _fileno.py
│  │     │  │  │  ├─ _inspect.py
│  │     │  │  │  ├─ _log_render.py
│  │     │  │  │  ├─ _loop.py
│  │     │  │  │  ├─ _null_file.py
│  │     │  │  │  ├─ _palettes.py
│  │     │  │  │  ├─ _pick.py
│  │     │  │  │  ├─ _ratio.py
│  │     │  │  │  ├─ _spinners.py
│  │     │  │  │  ├─ _stack.py
│  │     │  │  │  ├─ _timer.py
│  │     │  │  │  ├─ _win32_console.py
│  │     │  │  │  ├─ _windows_renderer.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  ├─ _wrap.py
│  │     │  │  │  ├─ abc.py
│  │     │  │  │  ├─ align.py
│  │     │  │  │  ├─ ansi.py
│  │     │  │  │  ├─ bar.py
│  │     │  │  │  ├─ box.py
│  │     │  │  │  ├─ cells.py
│  │     │  │  │  ├─ color_triplet.py
│  │     │  │  │  ├─ color.py
│  │     │  │  │  ├─ columns.py
│  │     │  │  │  ├─ console.py
│  │     │  │  │  ├─ constrain.py
│  │     │  │  │  ├─ containers.py
│  │     │  │  │  ├─ control.py
│  │     │  │  │  ├─ default_styles.py
│  │     │  │  │  ├─ diagnose.py
│  │     │  │  │  ├─ emoji.py
│  │     │  │  │  ├─ errors.py
│  │     │  │  │  ├─ file_proxy.py
│  │     │  │  │  ├─ filesize.py
│  │     │  │  │  ├─ highlighter.py
│  │     │  │  │  ├─ json.py
│  │     │  │  │  ├─ jupyter.py
│  │     │  │  │  ├─ layout.py
│  │     │  │  │  ├─ live_render.py
│  │     │  │  │  ├─ live.py
│  │     │  │  │  ├─ logging.py
│  │     │  │  │  ├─ markup.py
│  │     │  │  │  ├─ measure.py
│  │     │  │  │  ├─ padding.py
│  │     │  │  │  ├─ pager.py
│  │     │  │  │  ├─ palette.py
│  │     │  │  │  ├─ panel.py
│  │     │  │  │  ├─ pretty.py
│  │     │  │  │  ├─ progress_bar.py
│  │     │  │  │  ├─ progress.py
│  │     │  │  │  ├─ prompt.py
│  │     │  │  │  ├─ protocol.py
│  │     │  │  │  ├─ py.typed
│  │     │  │  │  ├─ region.py
│  │     │  │  │  ├─ repr.py
│  │     │  │  │  ├─ rule.py
│  │     │  │  │  ├─ scope.py
│  │     │  │  │  ├─ screen.py
│  │     │  │  │  ├─ segment.py
│  │     │  │  │  ├─ spinner.py
│  │     │  │  │  ├─ status.py
│  │     │  │  │  ├─ style.py
│  │     │  │  │  ├─ styled.py
│  │     │  │  │  ├─ syntax.py
│  │     │  │  │  ├─ table.py
│  │     │  │  │  ├─ terminal_theme.py
│  │     │  │  │  ├─ text.py
│  │     │  │  │  ├─ theme.py
│  │     │  │  │  ├─ themes.py
│  │     │  │  │  ├─ traceback.py
│  │     │  │  │  └─ tree.py
│  │     │  │  ├─ tomli/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _parser.cpython-312.pyc
│  │     │  │  │  │  ├─ _re.cpython-312.pyc
│  │     │  │  │  │  └─ _types.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _parser.py
│  │     │  │  │  ├─ _re.py
│  │     │  │  │  ├─ _types.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ tomli_w/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  └─ _writer.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _writer.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ truststore/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _api.cpython-312.pyc
│  │     │  │  │  │  ├─ _macos.cpython-312.pyc
│  │     │  │  │  │  ├─ _openssl.cpython-312.pyc
│  │     │  │  │  │  ├─ _ssl_constants.cpython-312.pyc
│  │     │  │  │  │  └─ _windows.cpython-312.pyc
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _api.py
│  │     │  │  │  ├─ _macos.py
│  │     │  │  │  ├─ _openssl.py
│  │     │  │  │  ├─ _ssl_constants.py
│  │     │  │  │  ├─ _windows.py
│  │     │  │  │  └─ py.typed
│  │     │  │  ├─ urllib3/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _collections.cpython-312.pyc
│  │     │  │  │  │  ├─ _version.cpython-312.pyc
│  │     │  │  │  │  ├─ connection.cpython-312.pyc
│  │     │  │  │  │  ├─ connectionpool.cpython-312.pyc
│  │     │  │  │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  │  │  ├─ fields.cpython-312.pyc
│  │     │  │  │  │  ├─ filepost.cpython-312.pyc
│  │     │  │  │  │  ├─ poolmanager.cpython-312.pyc
│  │     │  │  │  │  ├─ request.cpython-312.pyc
│  │     │  │  │  │  └─ response.cpython-312.pyc
│  │     │  │  │  ├─ contrib/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _appengine_environ.cpython-312.pyc
│  │     │  │  │  │  │  ├─ appengine.cpython-312.pyc
│  │     │  │  │  │  │  ├─ ntlmpool.cpython-312.pyc
│  │     │  │  │  │  │  ├─ pyopenssl.cpython-312.pyc
│  │     │  │  │  │  │  ├─ securetransport.cpython-312.pyc
│  │     │  │  │  │  │  └─ socks.cpython-312.pyc
│  │     │  │  │  │  ├─ _securetransport/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ bindings.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ low_level.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ bindings.py
│  │     │  │  │  │  │  └─ low_level.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _appengine_environ.py
│  │     │  │  │  │  ├─ appengine.py
│  │     │  │  │  │  ├─ ntlmpool.py
│  │     │  │  │  │  ├─ pyopenssl.py
│  │     │  │  │  │  ├─ securetransport.py
│  │     │  │  │  │  └─ socks.py
│  │     │  │  │  ├─ packages/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ six.cpython-312.pyc
│  │     │  │  │  │  ├─ backports/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ makefile.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ weakref_finalize.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ makefile.py
│  │     │  │  │  │  │  └─ weakref_finalize.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ six.py
│  │     │  │  │  ├─ util/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ connection.cpython-312.pyc
│  │     │  │  │  │  │  ├─ proxy.cpython-312.pyc
│  │     │  │  │  │  │  ├─ queue.cpython-312.pyc
│  │     │  │  │  │  │  ├─ request.cpython-312.pyc
│  │     │  │  │  │  │  ├─ response.cpython-312.pyc
│  │     │  │  │  │  │  ├─ retry.cpython-312.pyc
│  │     │  │  │  │  │  ├─ ssl_.cpython-312.pyc
│  │     │  │  │  │  │  ├─ ssl_match_hostname.cpython-312.pyc
│  │     │  │  │  │  │  ├─ ssltransport.cpython-312.pyc
│  │     │  │  │  │  │  ├─ timeout.cpython-312.pyc
│  │     │  │  │  │  │  ├─ url.cpython-312.pyc
│  │     │  │  │  │  │  └─ wait.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ connection.py
│  │     │  │  │  │  ├─ proxy.py
│  │     │  │  │  │  ├─ queue.py
│  │     │  │  │  │  ├─ request.py
│  │     │  │  │  │  ├─ response.py
│  │     │  │  │  │  ├─ retry.py
│  │     │  │  │  │  ├─ ssl_.py
│  │     │  │  │  │  ├─ ssl_match_hostname.py
│  │     │  │  │  │  ├─ ssltransport.py
│  │     │  │  │  │  ├─ timeout.py
│  │     │  │  │  │  ├─ url.py
│  │     │  │  │  │  └─ wait.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _collections.py
│  │     │  │  │  ├─ _version.py
│  │     │  │  │  ├─ connection.py
│  │     │  │  │  ├─ connectionpool.py
│  │     │  │  │  ├─ exceptions.py
│  │     │  │  │  ├─ fields.py
│  │     │  │  │  ├─ filepost.py
│  │     │  │  │  ├─ poolmanager.py
│  │     │  │  │  ├─ request.py
│  │     │  │  │  └─ response.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ typing_extensions.py
│  │     │  │  └─ vendor.txt
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ __pip-runner__.py
│  │     │  └─ py.typed
│  │     ├─ pip-25.1.1.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  ├─ AUTHORS.txt
│  │     │  │  └─ LICENSE.txt
│  │     │  ├─ entry_points.txt
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  ├─ REQUESTED
│  │     │  ├─ top_level.txt
│  │     │  └─ WHEEL
│  │     ├─ pkg_resources/
│  │     │  ├─ __pycache__/
│  │     │  │  └─ __init__.cpython-312.pyc
│  │     │  ├─ tests/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ test_find_distributions.cpython-312.pyc
│  │     │  │  │  ├─ test_integration_zope_interface.cpython-312.pyc
│  │     │  │  │  ├─ test_markers.cpython-312.pyc
│  │     │  │  │  ├─ test_pkg_resources.cpython-312.pyc
│  │     │  │  │  ├─ test_resources.cpython-312.pyc
│  │     │  │  │  └─ test_working_set.cpython-312.pyc
│  │     │  │  ├─ data/
│  │     │  │  │  ├─ my-test-package_unpacked-egg/
│  │     │  │  │  │  └─ my_test_package-1.0-py3.7.egg/
│  │     │  │  │  │     └─ EGG-INFO/
│  │     │  │  │  │        ├─ dependency_links.txt
│  │     │  │  │  │        ├─ PKG-INFO
│  │     │  │  │  │        ├─ SOURCES.txt
│  │     │  │  │  │        ├─ top_level.txt
│  │     │  │  │  │        └─ zip-safe
│  │     │  │  │  ├─ my-test-package_zipped-egg/
│  │     │  │  │  │  └─ my_test_package-1.0-py3.7.egg
│  │     │  │  │  ├─ my-test-package-source/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  └─ setup.cpython-312.pyc
│  │     │  │  │  │  ├─ setup.cfg
│  │     │  │  │  │  └─ setup.py
│  │     │  │  │  └─ my-test-package-zip/
│  │     │  │  │     └─ my-test-package.zip
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ test_find_distributions.py
│  │     │  │  ├─ test_integration_zope_interface.py
│  │     │  │  ├─ test_markers.py
│  │     │  │  ├─ test_pkg_resources.py
│  │     │  │  ├─ test_resources.py
│  │     │  │  └─ test_working_set.py
│  │     │  ├─ __init__.py
│  │     │  ├─ api_tests.txt
│  │     │  └─ py.typed
│  │     ├─ platformdirs/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ __main__.cpython-312.pyc
│  │     │  │  ├─ android.cpython-312.pyc
│  │     │  │  ├─ api.cpython-312.pyc
│  │     │  │  ├─ macos.cpython-312.pyc
│  │     │  │  ├─ unix.cpython-312.pyc
│  │     │  │  ├─ version.cpython-312.pyc
│  │     │  │  └─ windows.cpython-312.pyc
│  │     │  ├─ __init__.py
│  │     │  ├─ __main__.py
│  │     │  ├─ android.py
│  │     │  ├─ api.py
│  │     │  ├─ macos.py
│  │     │  ├─ py.typed
│  │     │  ├─ unix.py
│  │     │  ├─ version.py
│  │     │  └─ windows.py
│  │     ├─ platformdirs-4.3.8.dist-info/
│  │     │  ├─ licenses/
│  │     │  │  └─ LICENSE
│  │     │  ├─ INSTALLER
│  │     │  ├─ METADATA
│  │     │  ├─ RECORD
│  │     │  └─ WHEEL
│  │     ├─ plotly/
│  │     │  ├─ __pycache__/
│  │     │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  ├─ _subplots.cpython-312.pyc
│  │     │  │  ├─ animation.cpython-312.pyc
│  │     │  │  ├─ basedatatypes.cpython-312.pyc
│  │     │  │  ├─ basewidget.cpython-312.pyc
│  │     │  │  ├─ callbacks.cpython-312.pyc
│  │     │  │  ├─ conftest.cpython-312.pyc
│  │     │  │  ├─ exceptions.cpython-312.pyc
│  │     │  │  ├─ files.cpython-312.pyc
│  │     │  │  ├─ missing_anywidget.cpython-312.pyc
│  │     │  │  ├─ optional_imports.cpython-312.pyc
│  │     │  │  ├─ serializers.cpython-312.pyc
│  │     │  │  ├─ shapeannotation.cpython-312.pyc
│  │     │  │  ├─ subplots.cpython-312.pyc
│  │     │  │  ├─ tools.cpython-312.pyc
│  │     │  │  ├─ utils.cpython-312.pyc
│  │     │  │  └─ validator_cache.cpython-312.pyc
│  │     │  ├─ api/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ colors/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ data/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ express/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _chart_types.cpython-312.pyc
│  │     │  │  │  ├─ _core.cpython-312.pyc
│  │     │  │  │  ├─ _doc.cpython-312.pyc
│  │     │  │  │  ├─ _imshow.cpython-312.pyc
│  │     │  │  │  ├─ _special_inputs.cpython-312.pyc
│  │     │  │  │  └─ imshow_utils.cpython-312.pyc
│  │     │  │  ├─ colors/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ data/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ trendline_functions/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  │  └─ __init__.py
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _chart_types.py
│  │     │  │  ├─ _core.py
│  │     │  │  ├─ _doc.py
│  │     │  │  ├─ _imshow.py
│  │     │  │  ├─ _special_inputs.py
│  │     │  │  └─ imshow_utils.py
│  │     │  ├─ figure_factory/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _2d_density.cpython-312.pyc
│  │     │  │  │  ├─ _annotated_heatmap.cpython-312.pyc
│  │     │  │  │  ├─ _bullet.cpython-312.pyc
│  │     │  │  │  ├─ _candlestick.cpython-312.pyc
│  │     │  │  │  ├─ _county_choropleth.cpython-312.pyc
│  │     │  │  │  ├─ _dendrogram.cpython-312.pyc
│  │     │  │  │  ├─ _distplot.cpython-312.pyc
│  │     │  │  │  ├─ _facet_grid.cpython-312.pyc
│  │     │  │  │  ├─ _gantt.cpython-312.pyc
│  │     │  │  │  ├─ _hexbin_mapbox.cpython-312.pyc
│  │     │  │  │  ├─ _ohlc.cpython-312.pyc
│  │     │  │  │  ├─ _quiver.cpython-312.pyc
│  │     │  │  │  ├─ _scatterplot.cpython-312.pyc
│  │     │  │  │  ├─ _streamline.cpython-312.pyc
│  │     │  │  │  ├─ _table.cpython-312.pyc
│  │     │  │  │  ├─ _ternary_contour.cpython-312.pyc
│  │     │  │  │  ├─ _trisurf.cpython-312.pyc
│  │     │  │  │  ├─ _violin.cpython-312.pyc
│  │     │  │  │  └─ utils.cpython-312.pyc
│  │     │  │  ├─ __init__.py
│  │     │  │  ├─ _2d_density.py
│  │     │  │  ├─ _annotated_heatmap.py
│  │     │  │  ├─ _bullet.py
│  │     │  │  ├─ _candlestick.py
│  │     │  │  ├─ _county_choropleth.py
│  │     │  │  ├─ _dendrogram.py
│  │     │  │  ├─ _distplot.py
│  │     │  │  ├─ _facet_grid.py
│  │     │  │  ├─ _gantt.py
│  │     │  │  ├─ _hexbin_mapbox.py
│  │     │  │  ├─ _ohlc.py
│  │     │  │  ├─ _quiver.py
│  │     │  │  ├─ _scatterplot.py
│  │     │  │  ├─ _streamline.py
│  │     │  │  ├─ _table.py
│  │     │  │  ├─ _ternary_contour.py
│  │     │  │  ├─ _trisurf.py
│  │     │  │  ├─ _violin.py
│  │     │  │  └─ utils.py
│  │     │  ├─ graph_objects/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  └─ __init__.cpython-312.pyc
│  │     │  │  └─ __init__.py
│  │     │  ├─ graph_objs/
│  │     │  │  ├─ __pycache__/
│  │     │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  ├─ _bar.cpython-312.pyc
│  │     │  │  │  ├─ _barpolar.cpython-312.pyc
│  │     │  │  │  ├─ _box.cpython-312.pyc
│  │     │  │  │  ├─ _candlestick.cpython-312.pyc
│  │     │  │  │  ├─ _carpet.cpython-312.pyc
│  │     │  │  │  ├─ _choropleth.cpython-312.pyc
│  │     │  │  │  ├─ _choroplethmap.cpython-312.pyc
│  │     │  │  │  ├─ _choroplethmapbox.cpython-312.pyc
│  │     │  │  │  ├─ _cone.cpython-312.pyc
│  │     │  │  │  ├─ _contour.cpython-312.pyc
│  │     │  │  │  ├─ _contourcarpet.cpython-312.pyc
│  │     │  │  │  ├─ _densitymap.cpython-312.pyc
│  │     │  │  │  ├─ _densitymapbox.cpython-312.pyc
│  │     │  │  │  ├─ _deprecations.cpython-312.pyc
│  │     │  │  │  ├─ _figure.cpython-312.pyc
│  │     │  │  │  ├─ _figurewidget.cpython-312.pyc
│  │     │  │  │  ├─ _frame.cpython-312.pyc
│  │     │  │  │  ├─ _funnel.cpython-312.pyc
│  │     │  │  │  ├─ _funnelarea.cpython-312.pyc
│  │     │  │  │  ├─ _heatmap.cpython-312.pyc
│  │     │  │  │  ├─ _histogram.cpython-312.pyc
│  │     │  │  │  ├─ _histogram2d.cpython-312.pyc
│  │     │  │  │  ├─ _histogram2dcontour.cpython-312.pyc
│  │     │  │  │  ├─ _icicle.cpython-312.pyc
│  │     │  │  │  ├─ _image.cpython-312.pyc
│  │     │  │  │  ├─ _indicator.cpython-312.pyc
│  │     │  │  │  ├─ _isosurface.cpython-312.pyc
│  │     │  │  │  ├─ _layout.cpython-312.pyc
│  │     │  │  │  ├─ _mesh3d.cpython-312.pyc
│  │     │  │  │  ├─ _ohlc.cpython-312.pyc
│  │     │  │  │  ├─ _parcats.cpython-312.pyc
│  │     │  │  │  ├─ _parcoords.cpython-312.pyc
│  │     │  │  │  ├─ _pie.cpython-312.pyc
│  │     │  │  │  ├─ _sankey.cpython-312.pyc
│  │     │  │  │  ├─ _scatter.cpython-312.pyc
│  │     │  │  │  ├─ _scatter3d.cpython-312.pyc
│  │     │  │  │  ├─ _scattercarpet.cpython-312.pyc
│  │     │  │  │  ├─ _scattergeo.cpython-312.pyc
│  │     │  │  │  ├─ _scattergl.cpython-312.pyc
│  │     │  │  │  ├─ _scattermap.cpython-312.pyc
│  │     │  │  │  ├─ _scattermapbox.cpython-312.pyc
│  │     │  │  │  ├─ _scatterpolar.cpython-312.pyc
│  │     │  │  │  ├─ _scatterpolargl.cpython-312.pyc
│  │     │  │  │  ├─ _scattersmith.cpython-312.pyc
│  │     │  │  │  ├─ _scatterternary.cpython-312.pyc
│  │     │  │  │  ├─ _splom.cpython-312.pyc
│  │     │  │  │  ├─ _streamtube.cpython-312.pyc
│  │     │  │  │  ├─ _sunburst.cpython-312.pyc
│  │     │  │  │  ├─ _surface.cpython-312.pyc
│  │     │  │  │  ├─ _table.cpython-312.pyc
│  │     │  │  │  ├─ _treemap.cpython-312.pyc
│  │     │  │  │  ├─ _violin.cpython-312.pyc
│  │     │  │  │  ├─ _volume.cpython-312.pyc
│  │     │  │  │  ├─ _waterfall.cpython-312.pyc
│  │     │  │  │  └─ graph_objs.cpython-312.pyc
│  │     │  │  ├─ bar/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _error_x.cpython-312.pyc
│  │     │  │  │  │  ├─ _error_y.cpython-312.pyc
│  │     │  │  │  │  ├─ _hoverlabel.cpython-312.pyc
│  │     │  │  │  │  ├─ _insidetextfont.cpython-312.pyc
│  │     │  │  │  │  ├─ _legendgrouptitle.cpython-312.pyc
│  │     │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ _outsidetextfont.cpython-312.pyc
│  │     │  │  │  │  ├─ _selected.cpython-312.pyc
│  │     │  │  │  │  ├─ _stream.cpython-312.pyc
│  │     │  │  │  │  ├─ _textfont.cpython-312.pyc
│  │     │  │  │  │  └─ _unselected.cpython-312.pyc
│  │     │  │  │  ├─ hoverlabel/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ legendgrouptitle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ marker/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _colorbar.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _line.cpython-312.pyc
│  │     │  │  │  │  │  └─ _pattern.cpython-312.pyc
│  │     │  │  │  │  ├─ colorbar/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ _tickfont.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ _tickformatstop.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ _title.cpython-312.pyc
│  │     │  │  │  │  │  ├─ title/
│  │     │  │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ _font.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  └─ _title.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ _pattern.py
│  │     │  │  │  ├─ selected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  │  └─ _textfont.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ _textfont.py
│  │     │  │  │  ├─ unselected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  │  └─ _textfont.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ _textfont.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _error_x.py
│  │     │  │  │  ├─ _error_y.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _insidetextfont.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _outsidetextfont.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  ├─ _textfont.py
│  │     │  │  │  └─ _unselected.py
│  │     │  │  ├─ barpolar/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _hoverlabel.cpython-312.pyc
│  │     │  │  │  │  ├─ _legendgrouptitle.cpython-312.pyc
│  │     │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ _selected.cpython-312.pyc
│  │     │  │  │  │  ├─ _stream.cpython-312.pyc
│  │     │  │  │  │  └─ _unselected.cpython-312.pyc
│  │     │  │  │  ├─ hoverlabel/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ legendgrouptitle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ marker/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _colorbar.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _line.cpython-312.pyc
│  │     │  │  │  │  │  └─ _pattern.cpython-312.pyc
│  │     │  │  │  │  ├─ colorbar/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ _tickfont.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ _tickformatstop.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ _title.cpython-312.pyc
│  │     │  │  │  │  │  ├─ title/
│  │     │  │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  │  └─ _font.py
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  │  └─ _title.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _colorbar.py
│  │     │  │  │  │  ├─ _line.py
│  │     │  │  │  │  └─ _pattern.py
│  │     │  │  │  ├─ selected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  │  └─ _textfont.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ _textfont.py
│  │     │  │  │  ├─ unselected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  │  └─ _textfont.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _marker.py
│  │     │  │  │  │  └─ _textfont.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ _unselected.py
│  │     │  │  ├─ box/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _hoverlabel.cpython-312.pyc
│  │     │  │  │  │  ├─ _legendgrouptitle.cpython-312.pyc
│  │     │  │  │  │  ├─ _line.cpython-312.pyc
│  │     │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ _selected.cpython-312.pyc
│  │     │  │  │  │  ├─ _stream.cpython-312.pyc
│  │     │  │  │  │  └─ _unselected.cpython-312.pyc
│  │     │  │  │  ├─ hoverlabel/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ legendgrouptitle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ marker/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _line.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _line.py
│  │     │  │  │  ├─ selected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _marker.py
│  │     │  │  │  ├─ unselected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _marker.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ _unselected.py
│  │     │  │  ├─ candlestick/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _decreasing.cpython-312.pyc
│  │     │  │  │  │  ├─ _hoverlabel.cpython-312.pyc
│  │     │  │  │  │  ├─ _increasing.cpython-312.pyc
│  │     │  │  │  │  ├─ _legendgrouptitle.cpython-312.pyc
│  │     │  │  │  │  ├─ _line.cpython-312.pyc
│  │     │  │  │  │  └─ _stream.cpython-312.pyc
│  │     │  │  │  ├─ decreasing/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _line.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _line.py
│  │     │  │  │  ├─ hoverlabel/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ increasing/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _line.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _line.py
│  │     │  │  │  ├─ legendgrouptitle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _decreasing.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _increasing.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _line.py
│  │     │  │  │  └─ _stream.py
│  │     │  │  ├─ carpet/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _aaxis.cpython-312.pyc
│  │     │  │  │  │  ├─ _baxis.cpython-312.pyc
│  │     │  │  │  │  ├─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ _legendgrouptitle.cpython-312.pyc
│  │     │  │  │  │  └─ _stream.cpython-312.pyc
│  │     │  │  │  ├─ aaxis/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickfont.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickformatstop.cpython-312.pyc
│  │     │  │  │  │  │  └─ _title.cpython-312.pyc
│  │     │  │  │  │  ├─ title/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ _font.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  └─ _title.py
│  │     │  │  │  ├─ baxis/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickfont.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickformatstop.cpython-312.pyc
│  │     │  │  │  │  │  └─ _title.cpython-312.pyc
│  │     │  │  │  │  ├─ title/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ _font.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  └─ _title.py
│  │     │  │  │  ├─ legendgrouptitle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _aaxis.py
│  │     │  │  │  ├─ _baxis.py
│  │     │  │  │  ├─ _font.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  └─ _stream.py
│  │     │  │  ├─ choropleth/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _colorbar.cpython-312.pyc
│  │     │  │  │  │  ├─ _hoverlabel.cpython-312.pyc
│  │     │  │  │  │  ├─ _legendgrouptitle.cpython-312.pyc
│  │     │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ _selected.cpython-312.pyc
│  │     │  │  │  │  ├─ _stream.cpython-312.pyc
│  │     │  │  │  │  └─ _unselected.cpython-312.pyc
│  │     │  │  │  ├─ colorbar/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickfont.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickformatstop.cpython-312.pyc
│  │     │  │  │  │  │  └─ _title.cpython-312.pyc
│  │     │  │  │  │  ├─ title/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ _font.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  └─ _title.py
│  │     │  │  │  ├─ hoverlabel/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ legendgrouptitle/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _font.py
│  │     │  │  │  ├─ marker/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _line.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _line.py
│  │     │  │  │  ├─ selected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _marker.py
│  │     │  │  │  ├─ unselected/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  └─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  └─ _marker.py
│  │     │  │  │  ├─ __init__.py
│  │     │  │  │  ├─ _colorbar.py
│  │     │  │  │  ├─ _hoverlabel.py
│  │     │  │  │  ├─ _legendgrouptitle.py
│  │     │  │  │  ├─ _marker.py
│  │     │  │  │  ├─ _selected.py
│  │     │  │  │  ├─ _stream.py
│  │     │  │  │  └─ _unselected.py
│  │     │  │  ├─ choroplethmap/
│  │     │  │  │  ├─ __pycache__/
│  │     │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  ├─ _colorbar.cpython-312.pyc
│  │     │  │  │  │  ├─ _hoverlabel.cpython-312.pyc
│  │     │  │  │  │  ├─ _legendgrouptitle.cpython-312.pyc
│  │     │  │  │  │  ├─ _marker.cpython-312.pyc
│  │     │  │  │  │  ├─ _selected.cpython-312.pyc
│  │     │  │  │  │  ├─ _stream.cpython-312.pyc
│  │     │  │  │  │  └─ _unselected.cpython-312.pyc
│  │     │  │  │  ├─ colorbar/
│  │     │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickfont.cpython-312.pyc
│  │     │  │  │  │  │  ├─ _tickformatstop.cpython-312.pyc
│  │     │  │  │  │  │  └─ _title.cpython-312.pyc
│  │     │  │  │  │  ├─ title/
│  │     │  │  │  │  │  ├─ __pycache__/
│  │     │  │  │  │  │  │  ├─ __init__.cpython-312.pyc
│  │     │  │  │  │  │  │  └─ _font.cpython-312.pyc
│  │     │  │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  │  └─ _font.py
│  │     │  │  │  │  ├─ __init__.py
│  │     │  │  │  │  ├─ _tickfont.py
│  │     │  │  │  │  ├─ _tickformatstop.py
│  │     │  │  │  │  └─ _title.py
│  │     │  │  │  ├─ hoverlabel/
│  │     │  │  │  │  ├─ __pycache__/



├─ .gitignore
├─ README.md
└─ requirements.txt


```bash
SAR/
│
├── .gitignore
├── requirements.txt
├── README.md
│
├── venv/                      ← .gitignore
├── data/                      ← shapefile, CSV...
├── output/                    ← GeoTIFF, report...
├── notebook/
│   └── 1_s1_moisture.ipynb
├── scripts/
│
└── utils/
    └── config.py              ← common parameters (date, AOI, ecc.)
```

# 2. Reference Documentation

doc path: SAR\doc\sar_moisture\remotesensing-17-00542.pdf
**Reference**: Stanyer et al. (2025), *Remote Sensing*, 17(542), https://doi.org/10.3390/rs17030542  

## Summary

### Title  
**Soil Texture, Soil Moisture, and Sentinel-1 Backscattering: Towards the Retrieval of Field-Scale Soil Hydrological Properties**  
*Stanyer et al., Remote Sens. 2025, 17, 542*

### 1. Introduction

Soil moisture is a key variable for agriculture, climate regulation, and hydrology.  
Radar satellites (such as Sentinel-1) can monitor soil moisture regardless of cloud cover, but their accuracy is limited when **soil texture**—a key factor influencing the radar signal—is not considered.

This study investigates how **Sentinel-1 VV radar backscatter** varies in relation to both **soil moisture (SM)** and **soil texture**, using data from the **COSMOS-UK** monitoring network.

### 2. Materials and Methods

#### 2.1 Study Sites
- 17 agricultural sites in the UK, part of the **COSMOS-UK** network.
- Each site includes a sensor that measures soil moisture using **cosmic-ray neutron probes**.

#### 2.2 Data Sources
- **Soil Moisture (SM)** from COSMOS (0–20 cm depth, ~200 m footprint).
- **VV Backscatter** from Sentinel-1 (C-band, GRD IW mode, 10 m resolution).
- **NDVI** from Sentinel-2, used to detect low-vegetation periods.
- **Soil Texture** from the UK Soil Observatory (UKSO).

#### 2.3 Methodology
- Agricultural **Field Sectors** were defined around each COSMOS sensor.
- **Low Vegetation Periods (L-periods)** were selected where **NDVI < 0.35**.
- Sentinel-1 data were **corrected for orbit-related biases**.
- For each sector and L-period:
  - A **linear regression** was performed between VV and SM.
  - The **slope** (sensitivity: %VWC per dB) was calculated.
- The slopes were then compared with the corresponding **soil texture classes**.

### 3. Results and Discussion

- A **significant linear relationship** was found between SM and VV backscatter under bare-soil conditions.
- The **slope of the regression** varied depending on soil texture:
  - **Sandy soils** showed higher sensitivity (e.g., 1.69% VWC/dB).
  - **Clay soils** showed lower sensitivity (e.g., 4.81% VWC/dB).
- Slopes remained **stable over time** for each site, indicating their dependence on texture.

The results suggest that **VV backscatter can serve as a proxy for soil texture**, especially when combined with rainfall data and hydrological models.

### 4. Conclusions

- The influence of **soil texture** on the Sentinel-1 VV radar response to soil moisture has been confirmed.
- This paves the way for retrieving **soil hydrological properties** (e.g., infiltration potential) **using satellite data alone**.
- The approach can support:
  - Precision agriculture,
  - Field-scale water balance modelling,
  - Irrigation decision support systems.

### Citation

> Stanyer, C., Seco-Rizo, I., Atzberger, C., Marti-Cardona, B.  
> *Soil Texture, Soil Moisture, and Sentinel-1 Backscattering: Towards the Retrieval of Field-Scale Soil Hydrological Properties*.  
> Remote Sens. 2025, 17, 542. https://doi.org/10.3390/rs17030542

---

## Using Sentinel-1 SAR for Soil Moisture and Crop Irrigation Needs

When using **Sentinel-1 SAR imagery** for agricultural applications—especially to estimate **soil moisture (SM)** and calculate **crop irrigation requirements** — you must always **convert the backscatter values (VV in dB) into actual soil moisture (%)**.

### Why?

Sentinel-1 does **not measure soil moisture directly**.  
It returns a **backscatter coefficient** (in dB), which reflects how much of the radar signal bounces off the Earth’s surface.

Backscatter is influenced by:
- Soil moisture
- Soil texture (sand, loam, clay)
- Vegetation cover (NDVI)
- Surface roughness (ploughing, tillage)

Therefore, you need an **empirical formula** to **translate radar signal into real soil moisture**.

---

### Typical Conversion Formula

You can use a **linear regression model** like:

```python
SM (%) = a × VV_dB + b
```

- The **slope `a`** reflects how sensitive backscatter is to moisture.
- The **intercept `b`** varies based on local soil and calibration.

These values depend on the **soil type**:
- **Sandy soil** → lower slope (e.g., −1.7 %/dB)
- **Clay soil** → higher slope (e.g., −4.8 %/dB)

This is exactly what was demonstrated in the paper:  
**"Soil Texture, Soil Moisture, and Sentinel-1 Backscattering" (Stanyer et al., 2025)**

---

### From Soil Moisture to Irrigation Need

Once you have `SM (%)`, you can estimate irrigation requirements:

```python
water_deficit = ideal_SM - actual_SM
mm_water = (water_deficit / 100) * root_zone_depth_mm
```

Where:
- `ideal_SM` = target soil moisture for the crop (e.g., 30% for maize)
- `root_zone_depth_mm` = depth of active root zone (e.g., 300 mm)

---

- Estimate soil moisture from Sentinel-1 | Convert VV ➜ SM |
- Calculate irrigation demand | Compare SM to crop target |
- Determine water amount | Convert deficit to mm or liters/m² |

---

### What is **VV** in Sentinel-1 SAR?

**VV** stands for **Vertical transmit – Vertical receive** polarization.

#### In more detail:

Sentinel-1 is a **Synthetic Aperture Radar (SAR)** satellite that emits microwave pulses toward the Earth's surface and measures the reflected signal (backscatter).

SAR can transmit and receive radar waves in different **polarizations**:

* **V = Vertical** (the electric field is oriented vertically)
* **H = Horizontal**

So:

* **VV** = Radar signal **transmitted vertically** and **received vertically**
* **VH** = Transmitted vertically, received horizontally

---

### Why is **VV used for soil moisture estimation**?

* **VV backscatter** is more **sensitive to surface moisture** than VH in many bare-soil or low-vegetation conditions.
* It responds strongly to **changes in dielectric properties** of the soil, which are influenced by **water content**.
* VV also has **higher signal-to-noise ratio** over smooth, flat surfaces (e.g., agricultural fields).

> In most studies (including Stanyer et al., 2025), **VV backscatter** is used as the main input to estimate **surface soil moisture** from Sentinel-1.

---

### Units and Usage

* VV backscatter is given in **decibels (dB)**.
* It is a **negative number** (e.g., −5 to −20 dB).
* Lower dB → less reflection (dry soil)
  Higher dB → more reflection (wet soil)

You can convert it to **soil moisture (%)** using empirical formulas like:

```python
soil_moisture = a * vv_dB + b
```

---

